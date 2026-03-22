from packaging.version import InvalidVersion, Version

CESNET_PYPI_URL = "https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple"
CESNET_PYPI_UPLOAD_URL = "https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi"

OAREPO_INCLUDED_PACKAGES = [
    "oarepo-.*",
    "ccmm-invenio",
]
OAREPO_EXCLUDED_PACKAGES = []


def normalize_package_version(version: str) -> str:
    """Normalize *version* to a canonical form suitable for a git tag.

    Rules:
    - Local identifiers (``+...``) are always stripped.
    - The release is capped at three segments, dropping any extra numeric
      suffix used as a build ID (e.g. ``4.3.2.47635988`` → ``4.3.2``).
    - Pre-release (``a``/``b``/``rc``), ``dev``, and ``post`` markers are
      preserved and emitted in canonical PEP 440 order.
    - Non-PEP-440 strings fall back to stripping the local part and taking
      the first three dot-separated segments.
    """
    try:
        v = Version(version)
    except InvalidVersion:
        base = version.split("+", 1)[0]
        return ".".join(base.split(".")[:3])

    epoch = f"{v.epoch}!" if v.epoch else ""
    release = ".".join(str(x) for x in v.release[:3])
    pre = f"{v.pre[0]}{v.pre[1]}" if v.pre is not None else ""
    post = f".post{v.post}" if v.post is not None else ""
    dev = f".dev{v.dev}" if v.dev is not None else ""

    return f"{epoch}{release}{pre}{post}{dev}"


LOG_PACKAGES = [
    {
        "include": ["invenio-.*"],
        "exclude": [],
        "version_tag": lambda version: f"v{normalize_package_version(version)}",
        "github_organization": "inveniosoftware",
        "github_repo": lambda name: name,
    },
    {
        "include": ["oarepo-.*"],
        "exclude": [],
        "version_tag": normalize_package_version,
        "github_organization": "oarepo",
        "github_repo": lambda name: name,
    },
    {
        "include": ["ccmm-invenio"],
        "exclude": [],
        "version_tag": normalize_package_version,
        "github_organization": "nrp-cz",
        "github_repo": lambda name: name,
    },
]
