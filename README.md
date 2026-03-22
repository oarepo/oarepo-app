# oarepo-app

`oarepo-app` is a base library for repositories based on CESNET extensions to the InvenioRDM ecosystem. This library contains frozen and tested dependencies both to the specific version of InvenioRDM and to the specific version of oarepo libraries (such as oarepo-model, oarepo-runtime, ...)

It's python package is not deployed on PyPI, but rather on [CESNET package registry](https://gitlab.cesnet.cz/703/public/pypi/-/packages) - this allows it to include patched versions of InvenioRDM packages that would be impossible to put on the official PyPI while keeping dependencies intact.

## Versioning policy

The version of this package is always constructed as

```
<major>.<minor>.<patch>.<v-oarepo-app>
```

The first 3 parts of the version always correspond to the `oarepo` package.

The `v-oarepo-app` part is incremented everytime a build is called.

After release of official `invenio-app-rdm`, there will be no backward-incompatible changes nor new features coming into the release oarepo package (neither from invenio nor from oarepo).

In dev/alpha/beta versions, there might be backward incompatible changes, both from InvenioRDM and from oarepo packages. This is detected by checking whether the major version of any included package has changed. When this happens, it is noted in the CHANGELOG file and "+breaking" is appended to the version, for example `14.0.0b5.dev4+breaking`.

## Changelog

The changelog file is automatically generated from the changes to the included packages. There is a regular CHANGELOG.txt file as well as CHANGELOG.json which contains the same information in json format.

## Building the package

Building of a new version of the package has two steps and both must be done using the provided workflows (see `.github/workflows/` in this repository).

1. Create a new branch of oarepo-app
    * Use the **"Create new branch"** workflow to create a new branch
    * This will update all the dependencies to the newest version
    * This will also run tests for all packages with these versions
    * Review the resulting branch and pull request
2. Approve and merge the PR.

### Create a new branch of oarepo-app

This step has a single input parameter - `invenio-app-rdm-version`. The workflow will:

1. Check the newest version of the `oarepo` package that includes the given invenio-app-rdm version and fail if none was found
2. Create a new branch in the form `temporary-<oarepo version>`
3. Replace the base `oarepo` library dependency inside `pyproject.toml`
4. Replace all `oarepo` library dependencies from exact pins (`==`) to minimum-version constraints (`>=`)
5. Run `uv lock` (using the [uv](https://github.com/astral-sh/uv) Python package manager) to resolve and lock library versions

    > **Note:** Steps 4–6 work together: relaxing pins to `>=` allows `uv lock` to resolve the latest compatible versions, after which those resolved versions are pinned back exactly into `pyproject.toml`.

6. Replace the `>=` constraints with the exact versions resolved in the lock file
7. Update `CHANGELOG.json` — the workflow automatically adds a record for this version to the beginning of the array (see [Format of CHANGELOG.json](#format-of-changelogjson) below)
8. Determine whether there was a major version change in any of the libraries — both invenio and oarepo. If so, mark the entry in `CHANGELOG.json` as breaking and append `+breaking` to the version number
9. Generate `CHANGELOG.txt` from `CHANGELOG.json`


### Format of CHANGELOG.json

`CHANGELOG.json` is an array of items, each belonging to a released version, ordered from newest to oldest. Each item has the following structure:

```json5
[
  {
    "version": "14.0.0.15.b1dev4",
    "breaking": false,
    "packages": {
      "invenio-app-rdm": {
        "version": "14.0.0b1dev4",
        "changes": [
          // "commits" contains the commits since the previous version of this package
          // recorded in CHANGELOG.json. If the package has not changed since the
          // previous release, the "commits" field is omitted entirely.
          {
            "commit": "3412341234",
            "message": "short message"
          }
        ]
      }
    }
  }
]
```
