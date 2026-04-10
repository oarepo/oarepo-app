import * as d3 from 'd3';
import ELK from 'elkjs/lib/elk.bundled.js';

const elk = new ELK();

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
    // If there are no bumped packages, default to showing all
    if (nodesBumped.length === 0) currentView = 'all';
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

const nodeWidth  = 160;
const nodeHeight = 60;

async function renderGraph(view, direction) {
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

    // Build ELK graph specification
    const elkGraph = {
        id: 'root',
        layoutOptions: {
            'elk.algorithm': 'layered',
            'elk.direction': direction === 'LR' ? 'RIGHT' : 'DOWN',
            'elk.spacing.nodeNode': '50',
            'elk.layered.spacing.nodeNodeBetweenLayers': '80',
            'elk.edgeRouting': 'SPLINES',
            'elk.layered.crossingMinimization.strategy': 'LAYER_SWEEP',
            'elk.layered.nodePlacement.strategy': 'NETWORK_SIMPLEX',
        },
        children: filteredNodes.map(n => ({
            id: n.id,
            width: nodeWidth,
            height: nodeHeight,
        })),
        edges: filteredEdges.map((e, i) => ({
            id: `e${i}`,
            sources: [e.source],
            targets: [e.target],
        })),
    };

    let elkedGraph;
    try {
        elkedGraph = await elk.layout(elkGraph);
    } catch (err) {
        console.error('ELK layout error:', err);
        svg.append('text')
            .attr('x', containerW / 2).attr('y', containerH / 2)
            .attr('text-anchor', 'middle')
            .style('font-size', '18px').style('fill', '#999')
            .text('Graph layout failed');
        return;
    }

    // Pair each input edge with its ELK-computed layout (matched by index)
    const edgesWithLayout = filteredEdges.map((e, i) => ({
        ...e,
        elkEdge: elkedGraph.edges[i],
    }));

    // Bounding box over laid-out nodes
    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;
    for (const n of elkedGraph.children) {
        minX = Math.min(minX, n.x);
        maxX = Math.max(maxX, n.x + nodeWidth);
        minY = Math.min(minY, n.y);
        maxY = Math.max(maxY, n.y + nodeHeight);
    }

    const padding = 60;
    const graphW = maxX - minX + 2 * padding;
    const graphH = maxY - minY + 2 * padding;

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

    // Arrow markers — refX:10 places the tip (x=10 in the path M0,-5L10,0L0,5)
    // exactly at ELK's endPoint on the node border; the body extends back along the path.
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

    // Smooth Catmull-Rom spline through ELK's route waypoints
    const lineGen = d3.line().curve(d3.curveCatmullRom.alpha(0.5));

    const linkSel = g.selectAll('.link')
        .data(edgesWithLayout)
        .join('path')
        .attr('class', 'link')
        .attr('stroke', e => e.color || '#999')
        .attr('marker-end', e => `url(#arr-${(e.color || '#999').replace('#', '')})`)
        .attr('d', e => {
            const sec = e.elkEdge && e.elkEdge.sections && e.elkEdge.sections[0];
            if (!sec) return '';
            const pts = [
                [sec.startPoint.x, sec.startPoint.y],
                ...(sec.bendPoints || []).map(p => [p.x, p.y]),
                [sec.endPoint.x, sec.endPoint.y],
            ];
            return lineGen(pts);
        });

    // Draw nodes on top of edges
    const nodeSel = g.selectAll('.node')
        .data(elkedGraph.children)
        .join('g')
        .attr('class', 'node')
        .attr('transform', n => `translate(${n.x},${n.y})`);

    nodeSel.each(function(n) {
        const nodeData = nodeMap.get(n.id);
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
            const hoveredId = d.id;
            const connected = new Set([hoveredId]);
            filteredEdges.forEach(e => {
                if (e.source === hoveredId) connected.add(e.target);
                if (e.target === hoveredId) connected.add(e.source);
            });
            nodeSel
                .classed('node-dimmed', n => !connected.has(n.id))
                .classed('node-hovered', n => n.id === hoveredId);
            linkSel
                .classed('link-dimmed',      e => e.source !== hoveredId && e.target !== hoveredId)
                .classed('link-highlighted', e => e.source === hoveredId || e.target === hoveredId);
        })
        .on('mouseleave', function() {
            nodeSel.classed('node-dimmed', false).classed('node-hovered', false);
            linkSel.classed('link-dimmed', false).classed('link-highlighted', false);
        });
}

// Initialize graph when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    renderGraph(currentView, 'LR');

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

