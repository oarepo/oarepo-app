import * as d3 from 'd3';
import {
    graphConnect,
    sugiyama,
    layeringSimplex,
    decrossTwoLayer,
    coordCenter,
} from 'd3-dag';

// Global variables for graph data (will be set by the HTML template)
let nodesDataAll = [];
let edgesDataAll = [];
let nodesDataBumped = [];
let edgesDataBumped = [];
let currentView = 'bumped';
let currentDirection = 'LR';

// Initialize the graph data
function initGraphData(nodesAll, edgesAll, nodesBumped, edgesBumped) {
    nodesDataAll = nodesAll;
    edgesDataAll = edgesAll;
    nodesDataBumped = nodesBumped;
    edgesDataBumped = edgesBumped;
}

// Tarjan's algorithm to find strongly connected components (SCCs).
// Returns an array of arrays, each inner array is one SCC (set of node IDs).
function findSCCs(nodeIds, edges) {
    const adj = new Map(nodeIds.map(n => [n, []]));
    for (const e of edges) {
        if (adj.has(e.source)) adj.get(e.source).push(e.target);
    }

    let idx = 0;
    const indices  = new Map();
    const lowlinks = new Map();
    const onStack  = new Map();
    const stack    = [];
    const sccs     = [];

    function strongconnect(v) {
        indices.set(v, idx);
        lowlinks.set(v, idx);
        idx++;
        stack.push(v);
        onStack.set(v, true);

        for (const w of (adj.get(v) || [])) {
            if (!indices.has(w)) {
                strongconnect(w);
                lowlinks.set(v, Math.min(lowlinks.get(v), lowlinks.get(w)));
            } else if (onStack.get(w)) {
                lowlinks.set(v, Math.min(lowlinks.get(v), indices.get(w)));
            }
        }

        if (lowlinks.get(v) === indices.get(v)) {
            const scc = [];
            let w;
            do { w = stack.pop(); onStack.set(w, false); scc.push(w); } while (w !== v);
            sccs.push(scc);
        }
    }

    for (const n of nodeIds) {
        if (!indices.has(n)) strongconnect(n);
    }
    return sccs;
}

// Remove edges that are made redundant by a longer path (transitive reduction).
// Edges within a cycle (intra-SCC) are never removed — the naive BFS approach
// incorrectly flags them because it can reach the target by following the cycle
// itself. Instead we:
//  1. Find SCCs via Tarjan's algorithm.
//  2. Keep all intra-SCC edges unchanged.
//  3. Build a condensation (DAG of SCCs) and apply BFS-based TR only to
//     inter-SCC edges.
function transitiveReduction(edges) {
    const nodeIds = [...new Set(edges.flatMap(e => [e.source, e.target]))];

    const sccs  = findSCCs(nodeIds, edges);
    const sccOf = new Map();
    sccs.forEach((scc, i) => scc.forEach(n => sccOf.set(n, i)));

    // Edges within the same SCC are part of a cycle — always keep them.
    const intraEdges = edges.filter(e => sccOf.get(e.source) === sccOf.get(e.target));
    const interEdges = edges.filter(e => sccOf.get(e.source) !== sccOf.get(e.target));

    // Condensation adjacency: maps sccId → Set<sccId>
    const condAdj = new Map();
    for (const e of interEdges) {
        const s = sccOf.get(e.source), t = sccOf.get(e.target);
        if (!condAdj.has(s)) condAdj.set(s, new Set());
        condAdj.get(s).add(t);
    }

    // BFS on the condensation: is tgtSCC reachable from srcSCC via a path that
    // does NOT use the direct srcSCC→tgtSCC edge?
    function hasAlternatePath(srcSCC, tgtSCC) {
        const visited = new Set();
        const queue   = [];
        for (const n of (condAdj.get(srcSCC) || [])) {
            if (n !== tgtSCC) queue.push(n);
        }
        while (queue.length) {
            const cur = queue.shift();
            if (cur === tgtSCC) return true;
            if (visited.has(cur)) continue;
            visited.add(cur);
            for (const next of (condAdj.get(cur) || [])) queue.push(next);
        }
        return false;
    }

    const reducedInterEdges = interEdges.filter(
        e => !hasAlternatePath(sccOf.get(e.source), sccOf.get(e.target))
    );

    return [...intraEdges, ...reducedInterEdges];
}

// Compute horizontal offsets to fan parallel edges across node entry/exit points
function computeEdgeOffsets(links, nodeWidth, nodeHeight, direction) {
    const bySource = new Map();
    const byTarget = new Map();

    for (const link of links) {
        if (!bySource.has(link.source)) bySource.set(link.source, []);
        if (!byTarget.has(link.target)) byTarget.set(link.target, []);
        bySource.get(link.source).push(link);
        byTarget.get(link.target).push(link);
    }

    const sourceOffsets = new Map();
    const targetOffsets = new Map();
    // In TB: fan horizontally across 40% of nodeWidth; in LR: fan vertically across 40% of nodeHeight
    const maxSpread = (direction === 'LR' ? nodeHeight : nodeWidth) * 0.40;

    for (const ls of bySource.values()) {
        ls.sort((a, b) => a.target.x - b.target.x);
        const step = ls.length > 1 ? maxSpread / (ls.length - 1) : 0;
        ls.forEach((link, i) => {
            sourceOffsets.set(link, ls.length > 1 ? -maxSpread / 2 + i * step : 0);
        });
    }

    for (const ls of byTarget.values()) {
        ls.sort((a, b) => a.source.x - b.source.x);
        const step = ls.length > 1 ? maxSpread / (ls.length - 1) : 0;
        ls.forEach((link, i) => {
            targetOffsets.set(link, ls.length > 1 ? -maxSpread / 2 + i * step : 0);
        });
    }

    return { sourceOffsets, targetOffsets };
}

function renderGraph(view, direction) {
    if (direction === undefined) direction = currentDirection;
    currentDirection = direction;
    currentView = view;

    let filteredNodes = view === 'bumped' ? nodesDataBumped : nodesDataAll;
    let filteredEdges = view === 'bumped' ? edgesDataBumped : edgesDataAll;

    const svg = d3.select('#graph-svg');
    // Remove previous content and detach old zoom listeners
    svg.selectAll('*').remove();
    svg.on('.zoom', null);

    // Size SVG to fill the container exactly
    const container = document.getElementById('graph-container');
    const containerW = container.clientWidth  || 900;
    const containerH = container.clientHeight || 600;
    svg.attr('width', containerW).attr('height', containerH);

    if (filteredNodes.length === 0) {
        svg.append('text')
            .attr('x', containerW / 2).attr('y', containerH / 2)
            .attr('text-anchor', 'middle')
            .style('font-size', '18px').style('fill', '#999')
            .text('No bumped packages to display');
        return;
    }

    const nodeMap = new Map(filteredNodes.map(n => [n.id, n]));

    // Drop edges that are implied by a longer path to reduce visual clutter
    filteredEdges = transitiveReduction(filteredEdges);

    // Build DAG
    let dag;
    try {
        dag = graphConnect()(filteredEdges.map(e => [e.source, e.target]));
    } catch (e) {
        console.error('Error creating DAG:', e);
        svg.append('text')
            .attr('x', containerW / 2).attr('y', containerH / 2)
            .attr('text-anchor', 'middle')
            .style('font-size', '18px').style('fill', '#999')
            .text('Graph contains cycles or cannot be rendered');
        return;
    }

    const nodeWidth = 160;
    const nodeHeight = 60;
    const hGap = 80;
    const vGap = 60;

    const layout = sugiyama()
        // nodeSize is [cross-axis-size, layer-axis-size]:
        //   TB: cross=horizontal (nodeWidth), layer=vertical (nodeHeight)
        //   LR: cross=vertical  (nodeHeight), layer=horizontal (nodeWidth)
        .nodeSize(direction === 'LR'
            ? [nodeHeight + vGap, nodeWidth + hGap]
            : [nodeWidth + hGap, nodeHeight + vGap])
        .layering(layeringSimplex())
        .decross(decrossTwoLayer())
        .coord(coordCenter());

    layout(dag);

    const allLinks = [...dag.links()];
    const { sourceOffsets, targetOffsets } = computeEdgeOffsets(allLinks, nodeWidth, nodeHeight, direction);

    // Map layout coords → screen coords.
    // LR swaps layout.x (cross/vertical) and layout.y (layer/horizontal).
    const screenPos = direction === 'LR'
        ? n => ({ x: n.y, y: n.x })
        : n => ({ x: n.x, y: n.y });

    // Content bounding box (screen coords)
    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;
    for (const node of dag.nodes()) {
        const p = screenPos(node);
        minX = Math.min(minX, p.x);
        maxX = Math.max(maxX, p.x);
        minY = Math.min(minY, p.y);
        maxY = Math.max(maxY, p.y);
    }

    const padding = 60;
    const graphW = maxX - minX + nodeWidth + 2 * padding;
    const graphH = maxY - minY + nodeHeight + 2 * padding;

    // Initial zoom: scale to fit the full graph inside the container (never upscale past 1)
    const initScale = Math.min(containerW / graphW, containerH / graphH, 1) * 0.95;
    const fitTransform = d3.zoomIdentity
        .translate((containerW - graphW * initScale) / 2, (containerH - graphH * initScale) / 2)
        .scale(initScale);

    // Zoom/pan setup — zoomG must exist before we dispatch the initial transform
    const zoomG = svg.append('g');
    const zoomBehavior = d3.zoom()
        .scaleExtent([0.1, 4])
        .on('zoom', (event) => zoomG.attr('transform', event.transform));
    svg.call(zoomBehavior);
    // Double-click resets to fit-to-view
    svg.on('dblclick.zoom', () =>
        svg.transition().duration(400).call(zoomBehavior.transform, fitTransform));
    // Apply initial transform (fires zoom event — zoomG is already defined above)
    svg.call(zoomBehavior.transform, fitTransform);

    // Arrow markers — refX:10 places the arrow tip exactly at the path endpoint
    const defs = svg.append('defs');
    const edgeColors = new Set(filteredEdges.map(e => e.color));
    edgeColors.forEach(color => {
        const id = 'arr-' + color.replace('#', '');
        defs.append('marker')
            .attr('id', id)
            .attr('viewBox', '0 -5 10 10')
            .attr('refX', 10)
            .attr('refY', 0)
            .attr('markerWidth', 6)
            .attr('markerHeight', 6)
            .attr('orient', 'auto')
            .append('path')
            .attr('d', 'M0,-5L10,0L0,5')
            .attr('fill', color);
    });

    const g = zoomG.append('g')
        .attr('transform', `translate(${padding - minX},${padding - minY})`);

    // Edge path helpers
    const arrowClearance = 7;

    // Bump along the main flow axis: curveBumpY (TB) / curveBumpX (LR)
    // Both produce tangent-parallel entries/exits at node borders.
    const lineBump     = d3.line().curve(direction === 'LR' ? d3.curveBumpX     : d3.curveBumpY);
    // Monotone along the main flow axis: never backtracks, keeps paths tight
    const lineMonotone = d3.line().curve(direction === 'LR' ? d3.curveMonotoneX : d3.curveMonotoneY);

    const linkSel = g.selectAll('.link')
        .data(allLinks)
        .join('path')
        .attr('class', 'link')
        .attr('stroke', link => {
            const edgeData = filteredEdges.find(e =>
                e.source === link.source.data && e.target === link.target.data);
            return edgeData ? edgeData.color : '#999';
        })
        .attr('marker-end', link => {
            const sp = screenPos(link.source);
            const tp = screenPos(link.target);
            const backward = direction === 'LR' ? tp.x < sp.x : tp.y < sp.y;
            if (!backward) return null;
            const edgeData = filteredEdges.find(e =>
                e.source === link.source.data && e.target === link.target.data);
            const color = edgeData ? edgeData.color : '#999';
            return `url(#arr-${color.replace('#', '')})`;
        })
        .attr('d', link => {
            const srcDelta = sourceOffsets.get(link) || 0;
            const tgtDelta = targetOffsets.get(link) || 0;
            const sp = screenPos(link.source);
            const tp = screenPos(link.target);
            let sx, sy, tx, ty;
            if (direction === 'LR') {
                // Backward edge: target is to the left of source → exit left, enter right
                const backward = tp.x < sp.x;
                sx = sp.x + (backward ? -nodeWidth / 2 : nodeWidth / 2);
                sy = sp.y + srcDelta;
                tx = tp.x + (backward ? nodeWidth / 2 + arrowClearance : -nodeWidth / 2 - arrowClearance);
                ty = tp.y + tgtDelta;
            } else {
                // Backward edge: target is above source → exit top, enter bottom
                const backward = tp.y < sp.y;
                sx = sp.x + srcDelta;
                sy = sp.y + (backward ? -nodeHeight / 2 : nodeHeight / 2);
                tx = tp.x + tgtDelta;
                ty = tp.y + (backward ? nodeHeight / 2 + arrowClearance : -nodeHeight / 2 - arrowClearance);
            }
            if (link.points.length === 2) {
                return lineBump([[sx, sy], [tx, ty]]);
            }
            // Map layout waypoints to screen coords
            // d3-dag v1.x stores points as [x, y] arrays (not {x,y} objects)
            const mid = link.points.slice(1, -1).map(p =>
                direction === 'LR' ? [p[1], p[0]] : [p[0], p[1]]);
            return lineMonotone([[sx, sy], ...mid, [tx, ty]]);
        });

    // Draw nodes on top of edges
    const nodeSel = g.selectAll('.node')
        .data(dag.nodes())
        .join('g')
        .attr('class', 'node')
        .attr('transform', d => {
            const p = screenPos(d);
            return `translate(${p.x - nodeWidth / 2},${p.y - nodeHeight / 2})`;
        });

    nodeSel.each(function(d) {
        const nodeData = nodeMap.get(d.data);
        if (!nodeData) return;

        const nodeGroup = d3.select(this);

        nodeGroup.append('rect')
            .attr('width', nodeWidth)
            .attr('height', nodeHeight)
            .attr('rx', 6)
            .attr('fill', nodeData.in_cycle ? '#FF6B6B' : nodeData.color)
            .attr('stroke', nodeData.border_color)
            .attr('stroke-width', nodeData.border_width);

        const lines = nodeData.label.split('\n');
        const lineHeight = 14;
        const totalTextHeight = lines.length * lineHeight;
        const startY = (nodeHeight - totalTextHeight) / 2 + lineHeight;

        lines.forEach((line, i) => {
            nodeGroup.append('text')
                .attr('x', nodeWidth / 2)
                .attr('y', startY + i * lineHeight)
                .attr('text-anchor', 'middle')
                .attr('dominant-baseline', 'middle')
                .style('font-size', '12px')
                .style('font-weight', i === 0 ? 'bold' : 'normal')
                .text(line);
        });

    });

    // Hover interactions: dim unrelated nodes/edges, highlight connected ones
    nodeSel
        .on('mouseenter', function(event, d) {
            const hoveredId = d.data;
            const connected = new Set([hoveredId]);
            filteredEdges.forEach(e => {
                if (e.source === hoveredId) connected.add(e.target);
                if (e.target === hoveredId) connected.add(e.source);
            });
            nodeSel
                .classed('node-dimmed', n => !connected.has(n.data))
                .classed('node-hovered', n => n.data === hoveredId);
            linkSel
                .classed('link-dimmed',      lnk => lnk.source.data !== hoveredId && lnk.target.data !== hoveredId)
                .classed('link-highlighted', lnk => lnk.source.data === hoveredId || lnk.target.data === hoveredId);
        })
        .on('mouseleave', function() {
            nodeSel.classed('node-dimmed', false).classed('node-hovered', false);
            linkSel.classed('link-dimmed', false).classed('link-highlighted', false);
        });
}

// Initialize graph when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    renderGraph('bumped', 'LR');

    document.querySelectorAll('input[name="graph-view"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
            renderGraph(e.target.value);
        });
    });

    document.querySelectorAll('input[name="graph-direction"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
            renderGraph(currentView, e.target.value);
        });
    });

    // Re-fit whenever the container changes size (e.g. window resize), debounced
    let resizeTimer;
    new ResizeObserver(() => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => renderGraph(currentView), 120);
    }).observe(document.getElementById('graph-container'));
});

// Expose functions for inline scripts in the HTML template
window.initGraphData = initGraphData;
window.renderGraph = renderGraph;

