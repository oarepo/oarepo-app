# OAREPO-APP Changelog

## Contents

- [7.0.0rc1](#700rc1)
- [6.2.0rc1](#620rc1)
- [6.1.0](#610)
- [6.0.0](#600)
- [5.0.0](#500)

---

## 7.0.0rc1

Released: **June 6, 2026 at 18:55 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `ccmm-invenio` 1.1.12
[1.1.10 → 1.1.12](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.10...v1.1.12)

- [`9be50034`](https://github.com/nrp-cz/ccmm-invenio/commit/9be50034bf9dce2e5e581b8f7e93e4a45d996735) Major version bump due to major bump in packages: invenio-rdm-records, oarepo-model, oarepo-rdm (#41)
- [`b2e66d42`](https://github.com/nrp-cz/ccmm-invenio/commit/b2e66d4211b6dd3c283a58ebb6ee4df6bbae7122) [skip ci] Bump version to v1.1.11
- [`e31bf7da`](https://github.com/nrp-cz/ccmm-invenio/commit/e31bf7dad88b8407742637382fa30cb593b050ca) feat: related resources ui serializer
- [`97535019`](https://github.com/nrp-cz/ccmm-invenio/commit/97535019ed4eb50c4015895598dcf212a6c0191a) fix: wrong file name
- [`ba428b26`](https://github.com/nrp-cz/ccmm-invenio/commit/ba428b26c36532cafc0ee218ee7f3614b91a9dc8) feat: add schema validation for related resources identifiers
- [`aef2dc70`](https://github.com/nrp-cz/ccmm-invenio/commit/aef2dc7051e4f6de77db0a1cbbdf6052491347a8) fix: change identifiers to related identifiers
- [`88fd5515`](https://github.com/nrp-cz/ccmm-invenio/commit/88fd55159ff30e706900dd6ea6f295b53022894c) fix: lint

#### `invenio-accounts` 8.1.0
[8.0.0 → 8.1.0](https://github.com/inveniosoftware/invenio-accounts/compare/v8.0.0...v8.1.0)

- [`1457083a`](https://github.com/inveniosoftware/invenio-accounts/commit/1457083a4451878971985c6da0508125171d79b4) release: v8.1.0
- [`edc5caa9`](https://github.com/inveniosoftware/invenio-accounts/commit/edc5caa9f351285afda11ab777888499adf5785a) feat: adapt for pluggable password validation

#### `invenio-app-rdm` 14.0.0b11.dev4+oarepo.2.ovgwkwrw5wjd4zb6
[14.0.0b11.dev1+oarepo.1.ktbsmr472rj2vn37 → 14.0.0b11.dev4+oarepo.2.ovgwkwrw5wjd4zb6](https://github.com/inveniosoftware/invenio-app-rdm/compare/v14.0.0b11.dev1...v14.0.0b11.dev4)

- [`992fbaf2`](https://github.com/inveniosoftware/invenio-app-rdm/commit/992fbaf242df22028f9364dd1a6e3315658b0855) chore(setup): bump dependencies
- [`ccdc5e68`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ccdc5e681ad876bbede75f6a12cfb83cc0ff2958) release: v14.0.0b11.dev4
- [`40b950ea`](https://github.com/inveniosoftware/invenio-app-rdm/commit/40b950eaf9f3654406980e9d6fc47a74fae6b0b1) feat(records): deposit form compatibility with per-record-version review requests
- [`2ef77ebc`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2ef77ebcd52c4e747faa9d3e8532478b67a1c78f) chore(setup): bump dependencies
- [`7fdc11a5`](https://github.com/inveniosoftware/invenio-app-rdm/commit/7fdc11a54357a68a6079e09cfb22b940c1d4df17) release: v14.0.0b11.dev3
- [`c991610a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c991610ab4a1d8aa6119b01bc0ec490594d98b77) fix: corrected config variable name
- [`df059a2b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/df059a2b653c120805ae5354853758f956697454) fix: prevent overflow of long values and links in details and sidebar
- [`f0c404b0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f0c404b093c8b8376d760538b330d57c4cd5001c) chore: fix __all__ tuple in audit_logs
- [`bc6f2e2d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/bc6f2e2da1656c3c0ca77f41f9f9f78f203e1dd9) chore: replace `type(...) == str` with `type(...) is str`
- [`55e9cce3`](https://github.com/inveniosoftware/invenio-app-rdm/commit/55e9cce321b014ce52cf12a4b0f4a29a9ef08b10) chore: apply some linter fixes
- [`cd23c779`](https://github.com/inveniosoftware/invenio-app-rdm/commit/cd23c77927737e3cb66963183e57568bcbb2d4c7) chore: remove duplicate function definition in tests
- [`a8e80750`](https://github.com/inveniosoftware/invenio-app-rdm/commit/a8e807501d417cd30dba06d9310654aab2628d97) feat(users): add last login details to admin ui
- [`e3171ad9`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e3171ad9b63942c9ab4b1c4970e70ea8abcc1263) i18n: v14 wrap missing strings
- [`aab76c27`](https://github.com/inveniosoftware/invenio-app-rdm/commit/aab76c27a4f2d01d28545576f9904c99289976fb) feat(mshp-req): integrate membership request notifications
- [`caaa0ce5`](https://github.com/inveniosoftware/invenio-app-rdm/commit/caaa0ce544aa4a276b4946a6396541110a976c5b) 📦 release: v14.0.0b11.dev2
- [`27a08d7f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/27a08d7faf64799ea680bee525fb888ea7fc7b29) files: hide archive button over the size cap
- [`504d054e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/504d054ef60aa6ab2ef3cb21b9969f9bb01c0fd0) fix: enable community owner to remove it from record
- [`51bdcf65`](https://github.com/inveniosoftware/invenio-app-rdm/commit/51bdcf65fda6f50a8bbe4dd6fb200814c00dd2fc) refactor: add comment to permissions' extra params

#### `invenio-checks` 10.0.0 💥
[9.0.0 → 10.0.0](https://github.com/inveniosoftware/invenio-checks/compare/v9.0.0...v10.0.0)

- [`840907d9`](https://github.com/inveniosoftware/invenio-checks/commit/840907d9aca11970c5b5bf781b789fbb46f8d4b8) chore(setup): bump dependencies
- [`2b4c47a4`](https://github.com/inveniosoftware/invenio-checks/commit/2b4c47a476ccb4b5cab3b7e0ad1886e8d8ca3a42) release: v10.0.0

#### `invenio-communities` 28.0.0+oarepo.1.q2q5mh3b6ck6ne4w 💥
[27.0.0+oarepo.1.qy2oeqcxp5b43swa → 28.0.0+oarepo.1.q2q5mh3b6ck6ne4w](https://github.com/inveniosoftware/invenio-communities/compare/v27.0.0...v28.0.0)

- [`d0184334`](https://github.com/inveniosoftware/invenio-communities/commit/d01843345f7d21e0e3d98a0e8b847b80cb597bb3) chore(setup): bump dependencies
- [`ded08b56`](https://github.com/inveniosoftware/invenio-communities/commit/ded08b560fea85cdccad634617ba341655b41698) release: v28.0.0
- [`22a21561`](https://github.com/inveniosoftware/invenio-communities/commit/22a2156126e32d739163f456b0f14544ba8582b1) feat: add member name to kommunity member removal modal
- [`aa74db95`](https://github.com/inveniosoftware/invenio-communities/commit/aa74db959d6f3fdb0c569daab72d6d389990ebbb) feat: added blocks to communities templates
- [`f2254a0b`](https://github.com/inveniosoftware/invenio-communities/commit/f2254a0b3fa540be210ad65a80f081f0eb64e273) fix(ui): new community form typo

#### `invenio-db` 2.5.1
[2.5.0 → 2.5.1](https://github.com/inveniosoftware/invenio-db/compare/v2.5.0...v2.5.1)

- [`b5290708`](https://github.com/inveniosoftware/invenio-db/commit/b5290708be5f1e29d04fbbe0c685f91281863750) release: v2.5.1
- [`af2a329d`](https://github.com/inveniosoftware/invenio-db/commit/af2a329df1accb3d73c1a348e366ff6dd9abac90) fix(options): empty string is valid
- [`1c4c1455`](https://github.com/inveniosoftware/invenio-db/commit/1c4c14557003c8e4624efa02386b53fc932ad662) fix(timezone): the implementation now converts all timezones different from UTC to UTC as we cannot expect every PostgreSQL instance can be configured to UTC.
- [`11633f53`](https://github.com/inveniosoftware/invenio-db/commit/11633f531371d724df3e9508aba6fe23c41eb806) fix(timezone): undo the changes for writing datetimes to the database.

#### `invenio-jobs` 10.0.0 💥
[9.0.0 → 10.0.0](https://github.com/inveniosoftware/invenio-jobs/compare/v9.0.0...v10.0.0)

- [`435375c3`](https://github.com/inveniosoftware/invenio-jobs/commit/435375c3aeb5640394b615989ca95fd993b86f30) chore(setup): bump dependencies
- [`6beffd41`](https://github.com/inveniosoftware/invenio-jobs/commit/6beffd410b3c28a84ec51842db98e08d9c6f4f58) release: v10.0.0
- [`b6befca0`](https://github.com/inveniosoftware/invenio-jobs/commit/b6befca040c8a85cbbf088de5dbc980a84dbbd3a) ui: add delete button
- [`c62d505c`](https://github.com/inveniosoftware/invenio-jobs/commit/c62d505cc150ddf4d249a390e6d105ae21ae036c) i18n: update format strings for error messages

#### `invenio-rdm-records` 31.0.0+oarepo.1.4hk6xwmk2fco7q2v 💥
[29.0.0+oarepo.1.nfqjwnb5odweitxq → 31.0.0+oarepo.1.4hk6xwmk2fco7q2v](https://github.com/inveniosoftware/invenio-rdm-records/compare/v29.0.0...v31.0.0)

- [`21c9d3c0`](https://github.com/inveniosoftware/invenio-rdm-records/commit/21c9d3c01dc2ba815f05fe224735996e3bb07368) release: v31.0.0
- [`93cabdea`](https://github.com/inveniosoftware/invenio-rdm-records/commit/93cabdea25b6882570e138803b1c7651e0e28070) feat(reviews): add config for record version review policy
- [`c58c86d2`](https://github.com/inveniosoftware/invenio-rdm-records/commit/c58c86d2fe8e87ac519bcd1dcdc151a0706c29cc) feat(reviews): per-record-version data model changes
- [`bf24dad0`](https://github.com/inveniosoftware/invenio-rdm-records/commit/bf24dad0116015e58f8c2cd8e4c7fbff32e1fc29) feat(reviews): per-record-version service/api changes
- [`9752e82f`](https://github.com/inveniosoftware/invenio-rdm-records/commit/9752e82fe405bbb728c4f0b740c3a78676d5594f) feat(reviews): per-record-version unit tests
- [`1a7b59eb`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1a7b59eb00af399c9b7b62b2942e790b36033ce8) chore(setup): bump dependencies
- [`0fba06de`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0fba06de9a57a703b212fa75b0bd379cfa08fb95) release: v30.0.0
- [`ca716000`](https://github.com/inveniosoftware/invenio-rdm-records/commit/ca716000c821c7d041bf2515553d354037483350) chore: update commonmeta-py dependency
- [`49288449`](https://github.com/inveniosoftware/invenio-rdm-records/commit/492884490d68e9b0e72225efb77aad189d0fc61a) feat: more flexible prefix handling in DataCite PID Provider
- [`e66b71a3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e66b71a3267741b223f4939e539555a23e49620f) feat: add Crossref PID provider
- [`2394b53a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/2394b53aff6733d62f337cb540b159393a55d057) fix: parent PID registration fragility
- [`a331a35d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a331a35d73d06bc7e3620f865a25004ed2d9f85a) fix: crossref_xml test
- [`1ad89061`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1ad89061b69a70755ed6b72306acad1d5976cbb8) fix: update test_crossref_serializer.py
- [`c3ac9884`](https://github.com/inveniosoftware/invenio-rdm-records/commit/c3ac9884afa611b55d6ea6610c7d04cbe2a0f9dd) fix(schema): use SanitizedUnicode for date description
- [`c19558c7`](https://github.com/inveniosoftware/invenio-rdm-records/commit/c19558c71b1c4ac755bc4e8057a464631f949500) fix: make community header accept apiConfigs prop
- [`60d53cdd`](https://github.com/inveniosoftware/invenio-rdm-records/commit/60d53cdd10db985e8ba9221148f633cabe93dc50) feat: added overridable blocks to community search header
- [`5d081bc3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/5d081bc3ad17c623319d09d63f5459da29b6f621) i18n: update string formater
- [`05376f99`](https://github.com/inveniosoftware/invenio-rdm-records/commit/05376f99a343b4a76a4974e33310f8f4cef4fb1e) tests: fix failing tests
- [`f0b93253`](https://github.com/inveniosoftware/invenio-rdm-records/commit/f0b932534f7b34277d3e03b7779c85389aa02bec) fix: fixed confusing feedback message when preview fails due to validation errors
- [`e4d874de`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e4d874de3c19af93ff8c768823ff655694081c57) fix: file not possible to delete if it fails between operations

#### `invenio-records-resources` 10.1.0+oarepo.1.trnrudg2qsn3n65k
[10.0.0+oarepo.1.rfxn2zcltovd2ihy → 10.1.0+oarepo.1.trnrudg2qsn3n65k](https://github.com/inveniosoftware/invenio-records-resources/compare/v10.0.0...v10.1.0)

- [`840da769`](https://github.com/inveniosoftware/invenio-records-resources/commit/840da769e7b5ccab64b39479ac518b8934a4cd87) 📦 release: v10.1.0
- [`63e8a345`](https://github.com/inveniosoftware/invenio-records-resources/commit/63e8a34545c34d9d31aebf7cef9e29670b3b0c7d) files: limit archive download by total file size

#### `invenio-requests` 14.0.0+oarepo.1.2lmx3k7srcawdrgk 💥
[13.0.0+oarepo.1.s7hlgt7fdpiqngoq → 14.0.0+oarepo.1.2lmx3k7srcawdrgk](https://github.com/inveniosoftware/invenio-requests/compare/v13.0.0...v14.0.0)

- [`18046d14`](https://github.com/inveniosoftware/invenio-requests/commit/18046d149c78e346009b6a22f64262e3f8e3b2c2) chore(setup): bump dependencies
- [`f089e483`](https://github.com/inveniosoftware/invenio-requests/commit/f089e483a8a073abb8dbc715f321fb50524bcf8b) release: v14.0.0
- [`5b2dd9fe`](https://github.com/inveniosoftware/invenio-requests/commit/5b2dd9fe81cdc0e07fdd56adc3fe12064f2b38af) fix(tests): passing expires_at as datetime, not as string
- [`d5c2b8e5`](https://github.com/inveniosoftware/invenio-requests/commit/d5c2b8e5730dd4c3cbb27c5e53418e1612222d3c) fix: preserve redirect responses for S3 downloads
- [`7bc3ff71`](https://github.com/inveniosoftware/invenio-requests/commit/7bc3ff71796f40a8c91258f70b19dac2020f6c6a) i18n: update string formatting

#### `invenio-rest` 3.0.2
[3.0.1 → 3.0.2](https://github.com/inveniosoftware/invenio-rest/compare/v3.0.1...v3.0.2)

- [`0240b00d`](https://github.com/inveniosoftware/invenio-rest/commit/0240b00d9b72dc5994d8f953382aa732c6d86d64) release: v3.0.2
- [`e1a8b5fd`](https://github.com/inveniosoftware/invenio-rest/commit/e1a8b5fdf9a5264f2337f6e40ce4f7370410d446) fix(context): wrong default value
- [`aed531a0`](https://github.com/inveniosoftware/invenio-rest/commit/aed531a079e9c037eb94e6c3d9ce000f197f152d) fix(serializer): inherit context_schema in nested BaseSchema calls

#### `invenio-theme` 4.8.0
[4.7.0 → 4.8.0](https://github.com/inveniosoftware/invenio-theme/compare/v4.7.0...v4.8.0)

- [`031ca2a8`](https://github.com/inveniosoftware/invenio-theme/commit/031ca2a84ee843ee40da0fda1a48ba9f1d193943) release: v4.8.0
- [`6adf6acd`](https://github.com/inveniosoftware/invenio-theme/commit/6adf6acd4534157e79793e9f8c5415c420d6bd30) UX: Add THEME_SITENAME as a suffix in <head>
- [`176659d0`](https://github.com/inveniosoftware/invenio-theme/commit/176659d0a0e98abe00186b3da750444757433e18) bug: prevent title | title
- [`334a7698`](https://github.com/inveniosoftware/invenio-theme/commit/334a76985c2d9349482924165f0b5898f832f24f) refactor: shorten logic

#### `invenio-users-resources` 12.0.0 💥
[11.0.0 → 12.0.0](https://github.com/inveniosoftware/invenio-users-resources/compare/v11.0.0...v12.0.0)

- [`19ac2b40`](https://github.com/inveniosoftware/invenio-users-resources/commit/19ac2b40200e0039af01adb0b0c3aa7d63534a0f) release: v12.0.0
- [`f4576815`](https://github.com/inveniosoftware/invenio-users-resources/commit/f457681535c5572e9095f5f364049a94fd687dbf) fix: increase groups search max result window
- [`08eb90df`](https://github.com/inveniosoftware/invenio-users-resources/commit/08eb90df4cb337844095ae77ee3d542a2b2e389a) fix(groups): keep group ids aligned
- [`327cf0c5`](https://github.com/inveniosoftware/invenio-users-resources/commit/327cf0c51a4c83be95452f78617aaf53609d6e08) feat(users): expose login metadata

#### `invenio-vocabularies` 13.0.0+oarepo.1.jaaeqz7sxjzde5rc 💥
[12.0.0+oarepo.1.ibw3s6nmg4uy4kdr → 13.0.0+oarepo.1.jaaeqz7sxjzde5rc](https://github.com/inveniosoftware/invenio-vocabularies/compare/v12.0.0...v13.0.0)

- [`4fa8ce37`](https://github.com/inveniosoftware/invenio-vocabularies/commit/4fa8ce3775592f1c3b64822a6af2b05a239b9286) chore(setup): bump dependencies
- [`f45fad66`](https://github.com/inveniosoftware/invenio-vocabularies/commit/f45fad6651838c3745ca07dbb9fb3f86c67dc4f3) release: v13.0.0
- [`d9188156`](https://github.com/inveniosoftware/invenio-vocabularies/commit/d9188156d7733f2a676eead66334ccc64b9cdb70) fix(schema): use SanitizedUnicode for i18n_strings values

#### `oarepo-app` 7.0.0rc1
[6.2.0rc1 → 7.0.0rc1](https://github.com/oarepo/oarepo-app/compare/v6.2.0rc1...v7.0.0rc1)

- [`9073e8fa`](https://github.com/oarepo/oarepo-app/commit/9073e8fa14c3ed06416073c2e41cae84182c8c52) fix: strip local version of oarepo package
- [`7c7a061c`](https://github.com/oarepo/oarepo-app/commit/7c7a061c50f7721bbe0e37fec7e4345c68280652) pytest-oarepo was missing from major bumps - fixed.
- [`cb86ebf9`](https://github.com/oarepo/oarepo-app/commit/cb86ebf970ed4e035530729d3505ec9fcaddd9b1) Adding a debug message
- [`3546a401`](https://github.com/oarepo/oarepo-app/commit/3546a4018c2e82ce3feb8147d837bdb6e08fe158) Merge pull request #48 from oarepo/miroslavsimek/be-1111-communities-permissions
- [`87391ed6`](https://github.com/oarepo/oarepo-app/commit/87391ed6f56d0e675379b3440dbdacf409294ee5) fix: test
- [`fc00b69d`](https://github.com/oarepo/oarepo-app/commit/fc00b69dc22b12085f2364b8a85d5ebc5d0fd4b0) lint
- [`f559d91e`](https://github.com/oarepo/oarepo-app/commit/f559d91e101d9480bdef00acf8e84da869c47b26) linting
- [`84ca124f`](https://github.com/oarepo/oarepo-app/commit/84ca124f42a83bd220626a6426bad4fdb591344b) Merge pull request #46 from oarepo/miroslavsimek/be-1111-communities-permissions
- [`205f432e`](https://github.com/oarepo/oarepo-app/commit/205f432e39a4f93efc0f19f4be3e401280deef12) fix: Added check for a new record for submission into a community

#### `oarepo-communities` 10.0.0 💥
[9.0.0 → 10.0.0](https://github.com/oarepo/oarepo-communities/compare/v9.0.0...v10.0.0)

- [`db20c552`](https://github.com/oarepo/oarepo-communities/commit/db20c5520c29324b35ac590fa76024d88af9c439) Major version bump due to major bump in packages: invenio-rdm-records, pytest-oarepo, oarepo-runtime, oarepo-rdm, oarepo-workflows, oarepo-requests
- [`2bc1d300`](https://github.com/oarepo/oarepo-communities/commit/2bc1d30049cf0b7675298e7fab52795ac4331b11) [skip ci] Bump version to v9.0.2
- [`78909dad`](https://github.com/oarepo/oarepo-communities/commit/78909dad9e17d9adad485534750571f673cb98d4) passing explicit community instead of record to the permission policy
- [`c39128ad`](https://github.com/oarepo/oarepo-communities/commit/c39128ad12fe57d6f6aeb87a3a0b5035e56fa166) [skip ci] Bump version to v9.0.1
- [`01d885c6`](https://github.com/oarepo/oarepo-communities/commit/01d885c613669bff3f06ca60cf17bd70c9712dfa) fix: add/remove user from community requires string id

#### `oarepo-dashboard` 7.0.0 💥
[6.0.0 → 7.0.0](https://github.com/oarepo/oarepo-dashboard/compare/v6.0.0...v7.0.0)

- [`79a7dae3`](https://github.com/oarepo/oarepo-dashboard/commit/79a7dae3928bd52b5bfd2a943870339253b203fa) Major version bump due to major bump in invenio packages

#### `oarepo-doi` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-doi/compare/v5.0.0...v6.0.0)

- [`ad63a262`](https://github.com/oarepo/oarepo-doi/commit/ad63a262d225d250f3f89213328eb16a970fe3ef) Merge pull request #48 from oarepo/release-6.0.0
- [`4c42b38e`](https://github.com/oarepo/oarepo-doi/commit/4c42b38e1c524b32379083fbde0f98e141a95a49) Major version bump due to major bump in packages: oarepo-runtime
- [`3693bffb`](https://github.com/oarepo/oarepo-doi/commit/3693bffbc3685df7ac401355361d1829ba6e70ab) Merge pull request #47 from oarepo/chore-tools
- [`96eda735`](https://github.com/oarepo/oarepo-doi/commit/96eda735b33df1bd7f44f751cb6976e0d8c5375e) chore: removed oarepo-tools from dev dependencies

#### `oarepo-invenio-typing-stubs` 0.1.32
0.1.31 → 0.1.32


#### `oarepo-model` 4.0.0 💥
[3.0.0 → 4.0.0](https://github.com/oarepo/oarepo-model/compare/v3.0.0...v4.0.0)

- [`85d1b383`](https://github.com/oarepo/oarepo-model/commit/85d1b3833bb2af401af3a1e48a1fe1cd28674bb5) Major version bump due to major bump in packages: invenio-rdm-records, oarepo-runtime (#124)

#### `oarepo-oidc-einfra` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-oidc-einfra/compare/v5.0.0...v6.0.0)

- [`e3aaafb6`](https://github.com/oarepo/oarepo-oidc-einfra/commit/e3aaafb6c12512416346a03180c58405361b685b) Major version bump due to major bump in packages: invenio-communities, oarepo-runtime, oarepo-requests (#43)

#### `oarepo-rdm` 7.0.0 💥
[6.0.0 → 7.0.0](https://github.com/oarepo/oarepo-rdm/compare/v6.0.0...v7.0.0)

- [`50ce5bb1`](https://github.com/oarepo/oarepo-rdm/commit/50ce5bb1fb6fa9de72054509db0b8d8191a2c6ce) Major version bump due to major bump in packages: invenio-rdm-records, invenio-communities (#96)

#### `oarepo-related-resources` 3.0.0 💥
[2.0.0 → 3.0.0](https://github.com/oarepo/oarepo-related-resources/compare/v2.0.0...v3.0.0)

- [`9278f200`](https://github.com/oarepo/oarepo-related-resources/commit/9278f200d903de9ee336698fc89d177e11e497fd) Major version bump due to major bump in packages: invenio-rdm-records, invenio-vocabularies (#4)

#### `oarepo-requests` 8.0.0 💥
[7.0.0 → 8.0.0](https://github.com/oarepo/oarepo-requests/compare/v7.0.0...v8.0.0)

- [`9d4e7390`](https://github.com/oarepo/oarepo-requests/commit/9d4e73905a27155a8b4886543af023c6192d5d83) Major version bump due to major bump in invenio packages (#190)

#### `oarepo-runtime` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-runtime/compare/v5.0.0...v6.0.0)

- [`76a9dd8f`](https://github.com/oarepo/oarepo-runtime/commit/76a9dd8f07641b30ae31d72bf8f6fa01ff11dba2) Major version bump due to major bump in packages: invenio-rdm-records
- [`ed53cb41`](https://github.com/oarepo/oarepo-runtime/commit/ed53cb415990d7c941489cf8a8b79f54089affd9) [skip ci] Bump version to v5.1.1
- [`dac08dc0`](https://github.com/oarepo/oarepo-runtime/commit/dac08dc0326b5c2751fbae49bd3fdf62d233e40c) chore: deprecating our Generator class (used for typing purposes) in favour of invenio typing stubs.
- [`af79f5ad`](https://github.com/oarepo/oarepo-runtime/commit/af79f5ada2f06f69d7938fc961310b9557bded0a) fix: better mechanism of deprecation
- [`2a725606`](https://github.com/oarepo/oarepo-runtime/commit/2a72560698c0e7b1d676cfd94fcb4c9d1675014e) [skip ci] Bump version to v5.1.0
- [`f2a6056e`](https://github.com/oarepo/oarepo-runtime/commit/f2a6056edec1715e91d9e07da4de955455583126) feat: using invenio CompositeGenerator, deprecating AggregateGenerator
- [`d3463dde`](https://github.com/oarepo/oarepo-runtime/commit/d3463dde4689667f18874e20adeb1f962758bffa) chore: lint
- [`1892de90`](https://github.com/oarepo/oarepo-runtime/commit/1892de9049c8c118ce8a2ca6cd747a1624675c50) fix: test for deprecation warning

#### `oarepo-theme` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/oarepo/oarepo-theme/compare/v4.0.0...v5.0.0)

- [`f9f62e5e`](https://github.com/oarepo/oarepo-theme/commit/f9f62e5e03cc10cf937a9d8ea97ff25a90e019ca) Major version bump due to major bump in packages: invenio-rdm-records

#### `oarepo-ui` 12.0.0 💥
[11.0.0 → 12.0.0](https://github.com/oarepo/oarepo-ui/compare/v11.0.0...v12.0.0)

- [`9df64ec1`](https://github.com/oarepo/oarepo-ui/commit/9df64ec1b5877051d634652eca1263d99a5df08b) Major version bump due to major bump in packages: invenio-communities (#468)

#### `oarepo-vocabularies` 8.0.0 💥
[7.0.0 → 8.0.0](https://github.com/oarepo/oarepo-vocabularies/compare/v7.0.0...v8.0.0)

- [`f834b507`](https://github.com/oarepo/oarepo-vocabularies/commit/f834b507908741cd870f59de16954647850c638d) Major version bump due to major bump in packages: invenio-vocabularies (#259)

#### `oarepo-workflows` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-workflows/compare/v5.0.0...v6.0.0)

- [`66b2055f`](https://github.com/oarepo/oarepo-workflows/commit/66b2055f200fd804a1577c86ed605c51743d3aa3) Major version bump due to major bump in invenio packages (#58)
- [`92b863b4`](https://github.com/oarepo/oarepo-workflows/commit/92b863b45679d579818b772293a9372753d0ff99) fix: renamed composite generators to better names (#59)
- [`c9c6abe6`](https://github.com/oarepo/oarepo-workflows/commit/c9c6abe6d682c666eb0f840fc6bdc9d6d2653291) [skip ci] Bump version to v5.0.1
- [`a3e49264`](https://github.com/oarepo/oarepo-workflows/commit/a3e49264b8ffbc014991e065c96a9619661fbb40) Fix: user quota management permissions (#57)

---

## 6.2.0rc1

Released: **June 4, 2026 at 19:08 UTC**

### Updated packages

#### `oarepo-app` 6.2.0rc1
[6.1.0 → 6.2.0rc1](https://github.com/oarepo/oarepo-app/compare/v6.1.0...v6.2.0rc1)

- [`1139af9d`](https://github.com/oarepo/oarepo-app/commit/1139af9d0307e0fd5027cb953952b4bd2241490a) fix: logging oarepo-app commits in changelog
- [`09f55951`](https://github.com/oarepo/oarepo-app/commit/09f559516348a2a16f11a4777be9ddd5fcc7e64b) fix: changelog extra entries
- [`993863bc`](https://github.com/oarepo/oarepo-app/commit/993863bc75ec91961f8bd8d893a5b3f13806d13c) feat: overwritable vocabularies, pipeline for release candidates

---

## 6.1.0

Released: **June 4, 2026 at 06:30 UTC**

### Updated packages

#### `oarepo-app` 6.0.0 💥
5.0.0 → 6.0.0


#### `oarepo-oai-pmh-harvester` 8.0.0 💥
[7.0.0 → 8.0.0](https://github.com/oarepo/oarepo-oai-pmh-harvester/compare/v7.0.0...v8.0.0)

- [`795f5783`](https://github.com/oarepo/oarepo-oai-pmh-harvester/commit/795f57836cc92d76c795eb9ad802c838b2394be2) Version bump & pyproject cleanup (#119)
- [`4ea3fed6`](https://github.com/oarepo/oarepo-oai-pmh-harvester/commit/4ea3fed6cd4184ba519c5bfd88b65526d6081104) Put version to pyproject.toml (#118)
- [`de63d6b8`](https://github.com/oarepo/oarepo-oai-pmh-harvester/commit/de63d6b8c3b36c382493199d037b52f8254bd659) [skip ci] Bump version to v7.0.0

---

## 6.0.0

Released: **May 31, 2026 at 17:53 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `ccmm-invenio` 1.1.10
[1.1.9 → 1.1.10](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.9...v1.1.10)

- [`9fb29c16`](https://github.com/nrp-cz/ccmm-invenio/commit/9fb29c167c5b6add90277206c96222fdafcd7362) Chore: Major version bump due to invenio bump
- [`3a9214f2`](https://github.com/nrp-cz/ccmm-invenio/commit/3a9214f201c575dd0b63d7627261b5baa8281f6e) [skip ci] Bump version to v1.1.9

#### `invenio-access` 6.0.0 💥
[5.1.0 → 6.0.0](https://github.com/inveniosoftware/invenio-access/compare/v5.1.0...v6.0.0)

- [`953cb047`](https://github.com/inveniosoftware/invenio-access/commit/953cb047ef6c3f69a8268a594e85e0c744a1147f) fix: better dependencies after communities tests
- [`de53a418`](https://github.com/inveniosoftware/invenio-access/commit/de53a418c81d4c24ab1c8d412188774abe098f3e) chore(setup): bump dependencies
- [`2827ee1a`](https://github.com/inveniosoftware/invenio-access/commit/2827ee1a02691fb2b9a28a6e010483a5010bd525) release: v6.0.0

#### `invenio-accounts` 8.0.0 💥
[7.2.1 → 8.0.0](https://github.com/inveniosoftware/invenio-accounts/compare/v7.2.1...v8.0.0)

- [`86d8f17f`](https://github.com/inveniosoftware/invenio-accounts/commit/86d8f17fadf404bbb62b95709b6805263ffebc00) release: v8.0.0
- [`14acceae`](https://github.com/inveniosoftware/invenio-accounts/commit/14acceaedc9ee889ee15548b115acb3544cb3ab4) fix: update password generation and remove passlib dependency
- [`df38c16d`](https://github.com/inveniosoftware/invenio-accounts/commit/df38c16da193bf02601c473fdac05b3e65940600) fix(ui): reorder menu in user settings
- [`f6d93285`](https://github.com/inveniosoftware/invenio-accounts/commit/f6d93285646598d61987ffa01d9c0ec22794751b) feat(users): add username option to create user
- [`d9c20b5a`](https://github.com/inveniosoftware/invenio-accounts/commit/d9c20b5a2df725976b5cc0bc3717209ce263f3a1) fix: handle Alembic dependency on invenio-access
- [`eaece162`](https://github.com/inveniosoftware/invenio-accounts/commit/eaece16209bddc29115cd3dbab67798f3d5046ec) fix: unskipping alembic test
- [`48646548`](https://github.com/inveniosoftware/invenio-accounts/commit/4864654855a321f6c74c152fbb4c09550cf633e1) fix: Added a comment to the alembic file
- [`a6c735c7`](https://github.com/inveniosoftware/invenio-accounts/commit/a6c735c783049a87668e7bd9e40a674283e1a548) fix: conditional dependency to invenio-communities
- [`53aa61a5`](https://github.com/inveniosoftware/invenio-accounts/commit/53aa61a574173b4a7abba3b8f9e84f173a708ca0) fix: better dependencies after communities tests
- [`a2e98d0d`](https://github.com/inveniosoftware/invenio-accounts/commit/a2e98d0d14df598ffa18a00e5f01c07d10cf75d3) fix: not adding user_id if configuration prevents it

#### `invenio-administration` 6.0.0+oarepo.1.vrkijc6bgf4hnbd6 💥
[5.2.0+oarepo.2.zuwubmhg2iyj3cll → 6.0.0+oarepo.1.vrkijc6bgf4hnbd6](https://github.com/inveniosoftware/invenio-administration/compare/v5.2.0...v6.0.0)

- [`aa0a09e6`](https://github.com/inveniosoftware/invenio-administration/commit/aa0a09e63effb06c595a12bf0b4b7f2a830c4412) chore(setup): bump dependencies
- [`fef1337f`](https://github.com/inveniosoftware/invenio-administration/commit/fef1337f7fe26abb80896883c52f8034224d7a3f) release: v6.0.0

#### `invenio-app-rdm` 14.0.0b11.dev1+oarepo.1.ktbsmr472rj2vn37
[14.0.0b10.dev7+oarepo.4.ygkzv7ea34y6xlcc → 14.0.0b11.dev1+oarepo.1.ktbsmr472rj2vn37](https://github.com/inveniosoftware/invenio-app-rdm/compare/v14.0.0b10.dev7...v14.0.0b11.dev1)

- [`ac985d3b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ac985d3b9cb31df1777bad5af9e17eb0d94b8ffe) chore(setup): bump dependencies
- [`63fe8fc5`](https://github.com/inveniosoftware/invenio-app-rdm/commit/63fe8fc5805e3a37cce5c925fa5b159cfcaf9991) release: v14.0.0b11.dev1
- [`fe020162`](https://github.com/inveniosoftware/invenio-app-rdm/commit/fe02016209b9ab95d697fd1f36bb30451c35f479) feat: UI support for zip content previewing
- [`ce43f302`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ce43f3021d17b1fb87ed2a575cc7527068c4997b) chore(setup): bump dependencies
- [`55a60527`](https://github.com/inveniosoftware/invenio-app-rdm/commit/55a605279c4141643a13517119bde371c0e9eea7) release: v14.0.0b11.dev0
- [`61003945`](https://github.com/inveniosoftware/invenio-app-rdm/commit/61003945050d8e1e97e47df7a5dcc2e52099ab10) fix(alembic): script for preparing migration from 13 -> 14
- [`1a70d527`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1a70d5273c590ed2b53acd643b46c1a8847c90c8) deposit: add default values for custom fields on deposit form
- [`4b5c56dd`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4b5c56dd1d1d63b7d8c6f1cf67731e34ff7d99fa) deposits: switch to standard get syntax
- [`9f2f403e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9f2f403e2df0fe624744b1948f1b525ddac44a4c) feat(profiler): integrate Flask-MultiProfiler
- [`d0137a74`](https://github.com/inveniosoftware/invenio-app-rdm/commit/d0137a74ef2c72f4b51f10b5a9f158dc83cf858c) fix(profiler): override the MultiProfiler base template
- [`1069cd30`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1069cd301e55cf8f9d608218448dca844f571622) fix(profiler): register menu item for the multi-profiler
- [`e9abda02`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e9abda02da1a06da46ba79491b95347afecaa2d1) fix(profiler): remove CSP headers for profiler result pages
- [`8b158a38`](https://github.com/inveniosoftware/invenio-app-rdm/commit/8b158a387c6bcb3d111d540d123c584962c0ce61) feat(users): implement role management in user details
- [`62aeb51c`](https://github.com/inveniosoftware/invenio-app-rdm/commit/62aeb51cb19c1987939e81e8fa0d2e6d8072442e) fix: linting warning
- [`85290c99`](https://github.com/inveniosoftware/invenio-app-rdm/commit/85290c99be34064d7310c8714ce1160217622fd0) fix(records-ui): namespace url filter
- [`419a8a45`](https://github.com/inveniosoftware/invenio-app-rdm/commit/419a8a45fcdc2cfe283f98fdc1f4c184b4a19f80) feat(mshp-req+inv): show invitation & mshp-req pages from user & community sides [+]
- [`4691f1b0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4691f1b0074220f056d557d7db051e0bbb78a108) chore(url): use invenio_url_for for consistency in mshp-req and inv code
- [`4cf1c437`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4cf1c437ddf3b07d067c31107e33f906f285ba91) fix(urls): use `invenio_url_for()` instead of hard-coded URLs
- [`effecfd4`](https://github.com/inveniosoftware/invenio-app-rdm/commit/effecfd438c4b42e9876b0030ac456a8982812c9) feat: make resouce type badge clickable
- [`96f9d528`](https://github.com/inveniosoftware/invenio-app-rdm/commit/96f9d528742b172194899e09917a113d26ef0e0d) fix(tombstone): return not-found page + log exception for PIDDeletedError
- [`ca469660`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ca46966096475ce6d04775a97c4d60fa3d9d2051) config: remove hardcoded publisher and use THEME_SITENAME
- [`bbe9c7ef`](https://github.com/inveniosoftware/invenio-app-rdm/commit/bbe9c7ef613b91c261f7c510b332003c0b691578) frontpage: Add aria-label to 'More' search button
- [`dff032e0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/dff032e0f53f24cc3d2249c1c915767a075e78a5) fix(upgrade_scripts): use correct indexer for drafts
- [`4f02af2f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4f02af2f1a1387d35cbe94d90f756f5b5b4f7cd1) fix: wrap overflowing MathJax content in rich text
- [`69d0b2c0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/69d0b2c0f0fb9effdb762e17d5008639fa5e5947) users: fix hardcoded deposit URL in uploads dashboard
- [`c930d928`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c930d9280b4960b669edbad8184f780506025c2a) users: use invenio_url_for for deposit URL

#### `invenio-audit-logs` 3.0.0 💥
[2.0.0 → 3.0.0](https://github.com/inveniosoftware/invenio-audit-logs/compare/v2.0.0...v3.0.0)

- [`12dc2478`](https://github.com/inveniosoftware/invenio-audit-logs/commit/12dc24783872fa4ed44d9b5923068f8476f42e97) chore(setup): bump dependencies
- [`2147659d`](https://github.com/inveniosoftware/invenio-audit-logs/commit/2147659d3438cb2e0df4998c718fb2817baa8774) release: v3.0.0

#### `invenio-banners` 7.0.0 💥
[6.0.0 → 7.0.0](https://github.com/inveniosoftware/invenio-banners/compare/v6.0.0...v7.0.0)

- [`1568a282`](https://github.com/inveniosoftware/invenio-banners/commit/1568a282d807de0c863f0dfd421bfc14106d485b) fix(tests): alembic migration test
- [`a64a098b`](https://github.com/inveniosoftware/invenio-banners/commit/a64a098b002b7d3be5c0df82e45e8c880f9bf0a8) chore(setup): bump dependencies
- [`f6e1e5b5`](https://github.com/inveniosoftware/invenio-banners/commit/f6e1e5b585efedf58dce9762c25493125d810273) release: v7.0.0
- [`7c1726cf`](https://github.com/inveniosoftware/invenio-banners/commit/7c1726cf13e20965c3579c8c2478b2bb596a223e) ui(translations): mark string as translatable

#### `invenio-checks` 9.0.0 💥
[8.2.0 → 9.0.0](https://github.com/inveniosoftware/invenio-checks/compare/v8.2.0...v9.0.0)

- [`04939500`](https://github.com/inveniosoftware/invenio-checks/commit/0493950028906a57d42f5d8110fb5dd03b4cbe76) fix: migrations for choices
- [`1001c9c2`](https://github.com/inveniosoftware/invenio-checks/commit/1001c9c265e5e570d97e35b3900c7617f227c696) chore(setup): bump dependencies
- [`e6da2259`](https://github.com/inveniosoftware/invenio-checks/commit/e6da225994c44db9e026f9b8f9983cd9e582cdeb) release: v9.0.0
- [`b441cdb2`](https://github.com/inveniosoftware/invenio-checks/commit/b441cdb2a1bad938b11348906325ca4fbccd0048) feat: allow empty community_id for check config

#### `invenio-collections` 9.0.0 💥
[8.1.1 → 9.0.0](https://github.com/inveniosoftware/invenio-collections/compare/v8.1.1...v9.0.0)

- [`7c96fe37`](https://github.com/inveniosoftware/invenio-collections/commit/7c96fe37548f52a2e83e59ac06f77cca2584345e) fix: alembic migrations
- [`49dc86e1`](https://github.com/inveniosoftware/invenio-collections/commit/49dc86e1ce6b3a665e7a67fa8fa73a92ea2da7f7) chore(setup): bump dependencies
- [`e136a014`](https://github.com/inveniosoftware/invenio-collections/commit/e136a014006fdd0f186157883c419627839354bc) release: v9.0.0

#### `invenio-communities` 27.0.0+oarepo.1.qy2oeqcxp5b43swa 💥
[26.1.1+oarepo.1.ju33cyh3ievitktv → 27.0.0+oarepo.1.qy2oeqcxp5b43swa](https://github.com/inveniosoftware/invenio-communities/compare/v26.1.1...v27.0.0)

- [`5821035e`](https://github.com/inveniosoftware/invenio-communities/commit/5821035e13dc3613a6ecdf82e3fa689c658ab284) fix: tests in subcommunities
- [`df6edab8`](https://github.com/inveniosoftware/invenio-communities/commit/df6edab897de797f09260738ebf691f6de47b1d2) feat: introduced SameAs to make the policy extendable
- [`db4a1058`](https://github.com/inveniosoftware/invenio-communities/commit/db4a10580560b6497617aa62eec3cb9687b044d7) fix: moved dependency to depends_on
- [`d5c6d688`](https://github.com/inveniosoftware/invenio-communities/commit/d5c6d68859f83de0bd4122219ef37c0b75d9b336) chore(setup): bump dependencies
- [`0824825e`](https://github.com/inveniosoftware/invenio-communities/commit/0824825e4e67da7675689dad2f637f5cbd38fc36) release: v27.0.0
- [`40473b20`](https://github.com/inveniosoftware/invenio-communities/commit/40473b205a663120e631f29017b46beca47f7802) feat(mshp-req): notify upon each membership request action
- [`69add959`](https://github.com/inveniosoftware/invenio-communities/commit/69add959092acf641d70854cf5981629fd33357e) fix(inv): use appropriate link in invitation notification
- [`f8032a44`](https://github.com/inveniosoftware/invenio-communities/commit/f8032a4441eac4c9bc37b3cec09f4d1f250c9323) fix(mshp-req): display discussion link on communiy header correctly [+]
- [`62d30894`](https://github.com/inveniosoftware/invenio-communities/commit/62d3089423c1509fc090beafc0a813fada87a534) feat(mshp-req): display membership requests on community dashboard
- [`b9308752`](https://github.com/inveniosoftware/invenio-communities/commit/b930875203e72566eb29e073cd83321a02a3b6cb) feat(inv): cancel invitations from community invitations search
- [`fb1ea985`](https://github.com/inveniosoftware/invenio-communities/commit/fb1ea98503971344097b56d120522d014790efcb) feat: generalize error message for AlreadyMemberError
- [`79d3f47d`](https://github.com/inveniosoftware/invenio-communities/commit/79d3f47dd009eadc6d67d870e097c32f17af4cf8) feat(inv): use backend self_html for frontend invitation link
- [`e166aa29`](https://github.com/inveniosoftware/invenio-communities/commit/e166aa2949a36627f417aa69028edc09a95d90cb) build(deps-dev): bump minimatch
- [`8dd6c907`](https://github.com/inveniosoftware/invenio-communities/commit/8dd6c9075bcb74ac2d7fe6fe2bfb18856cf99fbb) build(deps-dev): bump lodash
- [`3acca976`](https://github.com/inveniosoftware/invenio-communities/commit/3acca976e8dd19357f5774eb82bccb81cf0a5638) feat(mshp-req): accept,decline,cancel,upate role of membership requests [+]
- [`639b5c94`](https://github.com/inveniosoftware/invenio-communities/commit/639b5c9413fbeb30e45922ea8a23b31c25c8c4c8) fix(mshp-req): enforce action permissions
- [`c7bdfb7d`](https://github.com/inveniosoftware/invenio-communities/commit/c7bdfb7d277b048eec2c243b72be85acb0bd6997) refactor: allow overriding members service components
- [`1ee47ecc`](https://github.com/inveniosoftware/invenio-communities/commit/1ee47eccfc45daf0533fd4ffdb0e73979592d043) fix(community-themes): only request theme CSS for themed communities
- [`52e2decc`](https://github.com/inveniosoftware/invenio-communities/commit/52e2decc7826bee58c7d6ab95d06d3ecb8e30b25) feat(mshp-req): don't show community membership request in community requests
- [`9b23ec95`](https://github.com/inveniosoftware/invenio-communities/commit/9b23ec95011f4f650c1783cdb6a46eb7f4574c47) feat(mshp-req): add permission to search membership requests
- [`f3669531`](https://github.com/inveniosoftware/invenio-communities/commit/f36695312b720dd9fc336cd747f2c27f277bc266) fix(deps): bump invenio-requests since tests assume v12.3.x at least
- [`eb9b0164`](https://github.com/inveniosoftware/invenio-communities/commit/eb9b0164489e39f609b522e238080fd83faa2905) feat: add request.type to communitymembers indices + refactor for clarity
- [`674084ba`](https://github.com/inveniosoftware/invenio-communities/commit/674084ba13cd194594607797321fb4a2da6c4846) feat(mshp-req)!: search membership requests - modifies mapping!
- [`757f2fe3`](https://github.com/inveniosoftware/invenio-communities/commit/757f2fe308df7a2ebf87fdf67c59165bcd5080b7) fix(mshp-req): generate proper self_html link for requests JSON API

#### `invenio-drafts-resources` 10.0.0+oarepo.1.aa7esyllsxmsu6a4 💥
[9.0.2+oarepo.1.7ycffxo2j7hqwzgo → 10.0.0+oarepo.1.aa7esyllsxmsu6a4](https://github.com/inveniosoftware/invenio-drafts-resources/compare/v9.0.2...v10.0.0)

- [`242f532f`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/242f532fb78b6ed7b6fbbd6854dad29147aac746) fix(tests): alembic tests
- [`f684d22c`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/f684d22c3585590eada4e0ba4588b0376d60ee39) chore(setup): bump dependencies
- [`67c65846`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/67c65846b04dd3cbbdd5dce7734b4c3a6d149bc2) release: v10.0.0

#### `invenio-files-rest` 5.0.0+oarepo.1.rm6vkq5heonxnonk 💥
[4.1.0+oarepo.2.a3g2ksmeqiqmhy66 → 5.0.0+oarepo.1.rm6vkq5heonxnonk](https://github.com/inveniosoftware/invenio-files-rest/compare/v4.1.0...v5.0.0)

- [`c9d238c7`](https://github.com/inveniosoftware/invenio-files-rest/commit/c9d238c74ed3a81847e9d37f947acbf62b2dfe45) chore(setup): bump dependencies
- [`5a077e60`](https://github.com/inveniosoftware/invenio-files-rest/commit/5a077e609f0bd4b52882a6c5fece00608f55a2b3) release: v5.0.0

#### `invenio-indexer` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/inveniosoftware/invenio-indexer/compare/v4.0.0...v5.0.0)

- [`68a0e760`](https://github.com/inveniosoftware/invenio-indexer/commit/68a0e760b1d53d660f598c46093e460749670c4e) chore(setup): bump dependencies
- [`77657fc7`](https://github.com/inveniosoftware/invenio-indexer/commit/77657fc7c77eff41be5b996dc7fee22603c587d3) release: v5.0.0

#### `invenio-jobs` 9.0.0 💥
[8.0.1 → 9.0.0](https://github.com/inveniosoftware/invenio-jobs/compare/v8.0.1...v9.0.0)

- [`c007827c`](https://github.com/inveniosoftware/invenio-jobs/commit/c007827c2bfa2aa51b9a113150073f78c2ea8b3f) fix: added missing alembic dependency on invenio-accounts
- [`48e9f121`](https://github.com/inveniosoftware/invenio-jobs/commit/48e9f121f4f9cb3fb2853c6f355951c36d69887b) fix: Using server defaults in model
- [`b9292e17`](https://github.com/inveniosoftware/invenio-jobs/commit/b9292e17bb04d2db1c24ed982e7bde3dd0b4d8a3) fix(tests): alembic bug workaround
- [`7774e20c`](https://github.com/inveniosoftware/invenio-jobs/commit/7774e20cabc7c27eb5172064c3b154c601bad81e) chore: switch to opensearch2 in tests
- [`609c863b`](https://github.com/inveniosoftware/invenio-jobs/commit/609c863b1d2f9525148728a4f8625dec6a42f5f2) chore(setup): bump dependencies
- [`8de980b3`](https://github.com/inveniosoftware/invenio-jobs/commit/8de980b3ff17710101b436bb13b4eec6b7974162) release: v9.0.0

#### `invenio-oaiserver` 5.0.0+oarepo.1.fe244nvk3gg6riuz 💥
[4.1.0+oarepo.1.jeizhxspiugts6ow → 5.0.0+oarepo.1.fe244nvk3gg6riuz](https://github.com/inveniosoftware/invenio-oaiserver/compare/v4.1.0...v5.0.0)

- [`c754e37e`](https://github.com/inveniosoftware/invenio-oaiserver/commit/c754e37ef0a0c2c28bacb1b73f20461dfa47fd5c) chore(setup): bump dependencies
- [`e15a8494`](https://github.com/inveniosoftware/invenio-oaiserver/commit/e15a849442807a50fabbbf0aefaf7446ad0839e3) release: v5.0.0
- [`2e25e602`](https://github.com/inveniosoftware/invenio-oaiserver/commit/2e25e6029fab46415ff55a5d6a9842cbf3b3a794) feat(tests): added test for alembic migration
- [`d2faa0d7`](https://github.com/inveniosoftware/invenio-oaiserver/commit/d2faa0d780a6cbcdf1e9fea4375e75176a68863e) fix: adding server-side default for system_created

#### `invenio-oauth2server` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/inveniosoftware/invenio-oauth2server/compare/v4.0.0...v5.0.0)

- [`35ba6d9b`](https://github.com/inveniosoftware/invenio-oauth2server/commit/35ba6d9bf8c3ac5d37616a2556bd113989d3d1ad) fix: moved down_revision to depends_on
- [`5e27ebe7`](https://github.com/inveniosoftware/invenio-oauth2server/commit/5e27ebe705f5b422ccb1df65f32e9615944b1dae) fix: Enabled alembix test
- [`0379d9ed`](https://github.com/inveniosoftware/invenio-oauth2server/commit/0379d9ed4bfedab17f2740cb6aae56c89287637d) chore(setup): bump dependencies
- [`14989338`](https://github.com/inveniosoftware/invenio-oauth2server/commit/149893389a45027f87fa0a6bdfa2bf18030cce61) release: v5.0.0
- [`6f87101e`](https://github.com/inveniosoftware/invenio-oauth2server/commit/6f87101e82b409081ebed73a744af02d8ef6f287) UI: reorder menu in user settings

#### `invenio-oauthclient` 8.0.0 💥
[7.0.0 → 8.0.0](https://github.com/inveniosoftware/invenio-oauthclient/compare/v7.0.0...v8.0.0)

- [`289531a2`](https://github.com/inveniosoftware/invenio-oauthclient/commit/289531a26e00ff64d0287bce56c1a999fd0f5d22) fix: bad downstream dependency in alembic
- [`cadd53ab`](https://github.com/inveniosoftware/invenio-oauthclient/commit/cadd53aba5bf2334c66a829f61ffc5db2e55f175) chore(setup): bump dependencies
- [`ddce5550`](https://github.com/inveniosoftware/invenio-oauthclient/commit/ddce55509f478fa23fe9a74600ccab8781ef3e5e) release: v8.0.0
- [`e6b5074e`](https://github.com/inveniosoftware/invenio-oauthclient/commit/e6b5074e2c508769c5d4df58985f3de3bb0e2cab) fix(ui): reorder menu in user settings
- [`c8162e64`](https://github.com/inveniosoftware/invenio-oauthclient/commit/c8162e645faaf0b59fe68e2456885835e3e2d570) release: v7.0.1
- [`e3722104`](https://github.com/inveniosoftware/invenio-oauthclient/commit/e3722104977a52b01463d6ac2a56e00209d5fd17) fix(logout): remove unmanage_roles from session

#### `invenio-pages` 9.0.0 💥
[8.0.0 → 9.0.0](https://github.com/inveniosoftware/invenio-pages/compare/v8.0.0...v9.0.0)

- [`163deb78`](https://github.com/inveniosoftware/invenio-pages/commit/163deb789d789c5d13f8cba627e93761c42bad0f) chore(setup): bump dependencies
- [`d566c57a`](https://github.com/inveniosoftware/invenio-pages/commit/d566c57ae7907e93eb29b0dcb13c22016a280222) release: v9.0.0

#### `invenio-previewer` 5.0.0 💥
[4.1.1 → 5.0.0](https://github.com/inveniosoftware/invenio-previewer/compare/v4.1.1...v5.0.0)

- [`190eb869`](https://github.com/inveniosoftware/invenio-previewer/commit/190eb869becafb0d351d115a9ef9a560b75d2299) chore(setup): bump dependencies
- [`eec0d182`](https://github.com/inveniosoftware/invenio-previewer/commit/eec0d182a1e61ab8dfac73e4fe94ae363681fd88) release: v5.0.0
- [`da5e0919`](https://github.com/inveniosoftware/invenio-previewer/commit/da5e0919d2a0a8e48dbf4e3b66c2f47c9b84b6d5) feat: Extend support for container item previewers.
- [`304dee01`](https://github.com/inveniosoftware/invenio-previewer/commit/304dee019b41e7b5b735ca60508140f902e0eeef) i18n: correct format string in error message
- [`88fb7e48`](https://github.com/inveniosoftware/invenio-previewer/commit/88fb7e48d8204f2d4a12a7ec0b9e080941cd6224) feat: GeoJSON support

#### `invenio-rdm-records` 29.0.0+oarepo.1.nfqjwnb5odweitxq 💥
[28.5.0+oarepo.1.7kmabv7jmwdd4bgu → 29.0.0+oarepo.1.nfqjwnb5odweitxq](https://github.com/inveniosoftware/invenio-rdm-records/compare/v28.5.0...v29.0.0)

- [`34b629a7`](https://github.com/inveniosoftware/invenio-rdm-records/commit/34b629a7ccaeae48fedd0d9a033cf07a6ba3d6bf) feat: Support for ZIP extraction
- [`7a653cb2`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7a653cb26e05c60efed616b3eef89cd6bc9bd5e7) chore(tests): use db fixture from pytest-invenio
- [`36200fa6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/36200fa670137e4efee19799a52fa35b376d541d) feat: Using SameAs generator for dynamic binding of permissions
- [`3487e2fb`](https://github.com/inveniosoftware/invenio-rdm-records/commit/3487e2fb6502e41d1cb6ac6f59d2b57270a271b2) refactor(policy): apply SameAs
- [`28867d0d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/28867d0ddacb4080dc43e93a99472c30ae21ca81) fix: alembic migrations
- [`cc8e6991`](https://github.com/inveniosoftware/invenio-rdm-records/commit/cc8e6991dc6d4f07e43830c00861481392b4cfc3) feat: passing extra arguments to _get_record
- [`3b82c29c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/3b82c29cd045f43961bd383fbf85defda55ec463) chore(setup): bump dependencies
- [`dbb001d8`](https://github.com/inveniosoftware/invenio-rdm-records/commit/dbb001d86ebf20d35b6be69b0dcb0825761ada65) release: v29.0.0
- [`00d63a09`](https://github.com/inveniosoftware/invenio-rdm-records/commit/00d63a09d1b3f5041b54c00e3d4cd6f3cb2d3b19) UI: reorder menu in user settings
- [`00ece822`](https://github.com/inveniosoftware/invenio-rdm-records/commit/00ece8229ff84f00d69f621106727bc6a04a8040) feat(stats): allow excluding file download stats from previewer
- [`5eb09d81`](https://github.com/inveniosoftware/invenio-rdm-records/commit/5eb09d81440931f7f1e2ab5e41e2a1e1cf8e0c39) fix: make community modal on deposit form close
- [`cc794aca`](https://github.com/inveniosoftware/invenio-rdm-records/commit/cc794acae393f252bec15045f407e01ae3b5c1bb) fix(vcs): extract license ID when returning
- [`3b772d89`](https://github.com/inveniosoftware/invenio-rdm-records/commit/3b772d8910dff34ca30ac9e979eab296513ce64a) fix: add `policy_id` to request metadata of file modification (#2310)
- [`e5e80895`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e5e8089514f47b670854822da5025e40c7d31423) 📦 release: v28.6.1
- [`a4fbd190`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a4fbd1901c1e68f15a5f3cc257a43b2151a14314) fix(metadata): fix `CustomFieldsComponent` subclass overrides
- [`c61c4d49`](https://github.com/inveniosoftware/invenio-rdm-records/commit/c61c4d49ba3e076e2363400ff6cb8a7ace64c0ca) fix(metadata): use UTC date instead of datetime for publication_date
- [`7ce897f7`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7ce897f7fb9e8e71c61b5151dbd1276e28fc6736) 📦 release: v28.6.0
- [`1b68dc94`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1b68dc947d826594d27463b7de69e022fe387167) fix(serializers): avoid request context in access status description
- [`27cd4893`](https://github.com/inveniosoftware/invenio-rdm-records/commit/27cd48931c49ce409b80f93ca75e1900033c4463) vcs: have fallback publisher value be THEME_SITENAME
- [`1b360893`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1b360893dd6cee9eabe4ef2e432e03c257fa39eb) @tmorrell vcs: have fallback publisher value be THEME_SITENAME
- [`690f09b5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/690f09b5336e368e99243164a370617ae7cf4c63) metadata: auto-populate `publication_date` on new versions
- [`f580e0b9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/f580e0b94031943808dfa768133ce8e3323c04a9) fix: Add max lenght to version field to prevent mis-rendering
- [`36b5431a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/36b5431a2723f781158eccd42581d3b65c1ded6e) fix(doi link): show appropriate DOI link in test(any) environment
- [`b7137697`](https://github.com/inveniosoftware/invenio-rdm-records/commit/b713769772b374798c8b5005795e863beb394c8d) fix: add funder ror to datacite serialization
- [`acfe8d3d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/acfe8d3dcb7c8746aab4c9f1c73949e668e18e10) tests: add test for name only funder
- [`7abddfe3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7abddfe3bf2c40bf8d3a2402b0a5bebc352c6526) fix: add funder to marcxml

#### `invenio-records` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/inveniosoftware/invenio-records/compare/v4.0.0...v5.0.0)

- [`8c9d0b9b`](https://github.com/inveniosoftware/invenio-records/commit/8c9d0b9bf4bd9a4b853864c5b933282a2dbc46af) release: v5.0.0
- [`eaadc778`](https://github.com/inveniosoftware/invenio-records/commit/eaadc7787c0cb2549b40b2f9a3172559ae37e59a) fix(tests): enabled alembic tests
- [`72d1f595`](https://github.com/inveniosoftware/invenio-records/commit/72d1f595da6bfbd20583ac32427d9007733d083f) fix: added pre-undelete-post-undelete hooks

#### `invenio-records-files` 3.0.0 💥
[2.0.0 → 3.0.0](https://github.com/inveniosoftware/invenio-records-files/compare/v2.0.0...v3.0.0)

- [`1f58d4ca`](https://github.com/inveniosoftware/invenio-records-files/commit/1f58d4ca5c067ac5d2554398e4174bcc7767bb41) fix: bad downstream dependency in alembic
- [`8331cdb3`](https://github.com/inveniosoftware/invenio-records-files/commit/8331cdb39c711a24e59fdaf43adf6acfbffe928b) chore(setup): bump dependencies
- [`82da4d79`](https://github.com/inveniosoftware/invenio-records-files/commit/82da4d79b31292578579c62dfa80da4547b426bf) release: v3.0.0

#### `invenio-records-permissions` 3.0.0 💥
[2.0.1 → 3.0.0](https://github.com/inveniosoftware/invenio-records-permissions/compare/v2.0.1...v3.0.0)

- [`2687f82f`](https://github.com/inveniosoftware/invenio-records-permissions/commit/2687f82f7a977d23ca2264dcf78d52450878f975) chore(setup): bump dependencies
- [`e3c7e691`](https://github.com/inveniosoftware/invenio-records-permissions/commit/e3c7e6914e4fd3e1e70df809fb0771e34e9ad89b) release: v3.0.0
- [`77647921`](https://github.com/inveniosoftware/invenio-records-permissions/commit/77647921d32a0a19ff7bdc7c0c9d52db46308e03) feat(typing): Returning None instead of [] in Generator
- [`4836682a`](https://github.com/inveniosoftware/invenio-records-permissions/commit/4836682a54f486e3ed25a0cd57940ee33533e226) feat: SameAs generator

#### `invenio-records-resources` 10.0.0+oarepo.1.rfxn2zcltovd2ihy 💥
[9.3.0+oarepo.1.zcunkj5manhukyog → 10.0.0+oarepo.1.rfxn2zcltovd2ihy](https://github.com/inveniosoftware/invenio-records-resources/compare/v9.3.0...v10.0.0)

- [`d2396a9c`](https://github.com/inveniosoftware/invenio-records-resources/commit/d2396a9c446da6c112e17be0041041c26e094829) feat: add suport for listing and extracing items from containers
- [`376ea683`](https://github.com/inveniosoftware/invenio-records-resources/commit/376ea683a2350cdb52a952e2670025a870a8f3ce) chore(setup): bump dependencies
- [`a34216f9`](https://github.com/inveniosoftware/invenio-records-resources/commit/a34216f9ab3ba76a11a07f587d1d5799e1dbd5ab) release: v10.0.0
- [`88930b55`](https://github.com/inveniosoftware/invenio-records-resources/commit/88930b5500e8997c2687c61989ca079f301e767f) fix(tests): Added alembic test
- [`07d211e4`](https://github.com/inveniosoftware/invenio-records-resources/commit/07d211e457d93fd3642d2972b5497ca367a0e6ca) feat: Passing more context to permissions and components

#### `invenio-records-rest` 5.0.0 💥
[4.1.0 → 5.0.0](https://github.com/inveniosoftware/invenio-records-rest/compare/v4.1.0...v5.0.0)

- [`0458efc0`](https://github.com/inveniosoftware/invenio-records-rest/commit/0458efc0058f9843d3c698b351ee353d7e22e920) chore(setup): bump dependencies
- [`13ed9cec`](https://github.com/inveniosoftware/invenio-records-rest/commit/13ed9cec896708508445a049056c4d85a47e8c3c) release: v5.0.0

#### `invenio-records-ui` 4.0.0 💥
[3.0.0 → 4.0.0](https://github.com/inveniosoftware/invenio-records-ui/compare/v3.0.0...v4.0.0)

- [`451fd6f2`](https://github.com/inveniosoftware/invenio-records-ui/commit/451fd6f2454b0715f631804852c5d01da4c0e965) chore(setup): bump dependencies
- [`039e498e`](https://github.com/inveniosoftware/invenio-records-ui/commit/039e498ecc6123dec501708c97a69285fd61ccd8) release: v4.0.0

#### `invenio-requests` 13.0.0+oarepo.1.s7hlgt7fdpiqngoq 💥
[12.6.1+oarepo.1.e3mgu3w367pgarrw → 13.0.0+oarepo.1.s7hlgt7fdpiqngoq](https://github.com/inveniosoftware/invenio-requests/compare/v12.6.1...v13.0.0)

- [`a945cf67`](https://github.com/inveniosoftware/invenio-requests/commit/a945cf676516c8ba5c9a1d8a0651a2de5452fd5a) feat: introduced SameAs to make the policy extendable
- [`115e4d31`](https://github.com/inveniosoftware/invenio-requests/commit/115e4d31666a406c9fad9195b72bedbbe50f6a92) chore(setup): bump dependencies
- [`f6b0c89c`](https://github.com/inveniosoftware/invenio-requests/commit/f6b0c89c04b4e04ec0cd758b2b31697ea8fea019) release: v13.0.0
- [`f02baf1e`](https://github.com/inveniosoftware/invenio-requests/commit/f02baf1e01bebf025c1635a62d1c5fb4a2fb744f) feat: Extra context for permission checks
- [`2813f668`](https://github.com/inveniosoftware/invenio-requests/commit/2813f6686e9cd15cf7b9372eae8d50284951efc3) fix(comments): null ref for deleted comments
- [`3ceaf414`](https://github.com/inveniosoftware/invenio-requests/commit/3ceaf414be0f2310e0c21fe1cbddff9d4988b7fa) release: v12.6.2

#### `invenio-s3` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/inveniosoftware/invenio-s3/compare/v4.0.0...v5.0.0)

- [`0f9166a1`](https://github.com/inveniosoftware/invenio-s3/commit/0f9166a1aa48366273b34846bc1f23319cd752ce) chore(setup): bump dependencies
- [`5541e23a`](https://github.com/inveniosoftware/invenio-s3/commit/5541e23ae6cc0ca7606d05046924d57c893deb3d) release: v5.0.0

#### `invenio-userprofiles` 6.0.0 💥
[5.1.0 → 6.0.0](https://github.com/inveniosoftware/invenio-userprofiles/compare/v5.1.0...v6.0.0)

- [`1f46b4e1`](https://github.com/inveniosoftware/invenio-userprofiles/commit/1f46b4e1e9d62f733e6402c6f6c43ecd8a1917f0) chore(setup): bump dependencies
- [`3637b0e7`](https://github.com/inveniosoftware/invenio-userprofiles/commit/3637b0e725b2d218a831326fdba7d382923e5796) release: v6.0.0

#### `invenio-users-resources` 11.0.0 💥
[10.5.0 → 11.0.0](https://github.com/inveniosoftware/invenio-users-resources/compare/v10.5.0...v11.0.0)

- [`651d87d6`](https://github.com/inveniosoftware/invenio-users-resources/commit/651d87d6e724df40b3a8bed0c87f4b1f72d67ec1) chore(setup): bump dependencies
- [`aabd8955`](https://github.com/inveniosoftware/invenio-users-resources/commit/aabd895570f4da267bcd906c4420ac5436d5e592) release: v11.0.0
- [`0a0574a7`](https://github.com/inveniosoftware/invenio-users-resources/commit/0a0574a7bd8bb1b6e9ff1f6e35304bbc0c7525ed) feat(users)!: add admin role management backend

#### `invenio-vocabularies` 12.0.0+oarepo.1.ibw3s6nmg4uy4kdr 💥
[11.1.2+oarepo.1.26bhh64bjojb73mv → 12.0.0+oarepo.1.ibw3s6nmg4uy4kdr](https://github.com/inveniosoftware/invenio-vocabularies/compare/v11.1.2...v12.0.0)

- [`61fb785a`](https://github.com/inveniosoftware/invenio-vocabularies/commit/61fb785a3f6e4250bbb8394a6f1cae0d6eafc273) chore(setup): bump dependencies
- [`11dc7708`](https://github.com/inveniosoftware/invenio-vocabularies/commit/11dc7708daeeb9ca219418bedcb6b0b9e5de5750) release: v12.0.0

#### `oarepo-app` 5.0.0 💥
4.0.0 → 5.0.0


#### `oarepo-communities` 9.0.0 💥
[8.1.3 → 9.0.0](https://github.com/oarepo/oarepo-communities/compare/v8.1.3...v9.0.0)

- [`194a51c1`](https://github.com/oarepo/oarepo-communities/commit/194a51c10e524a61dd03c3d995b6851a7794c66d) Major bump due to changes in invenio
- [`ce108e8e`](https://github.com/oarepo/oarepo-communities/commit/ce108e8e8409e0ede4c950c651419c19cfc777e5) fixed communities cli
- [`43f0a7aa`](https://github.com/oarepo/oarepo-communities/commit/43f0a7aab5598f45afbf3780377bd38bc58f850c) [skip ci] Bump version to v8.1.4
- [`bd78a606`](https://github.com/oarepo/oarepo-communities/commit/bd78a606b7cd89180382475f9f8d92b3487e9ab7) _get_record_communities and _get_data_communities return empty list instead of raising errors
- [`4bf429e7`](https://github.com/oarepo/oarepo-communities/commit/4bf429e70d509a3732e05e4a4287d91ec9a30689) errors are deprecated instead of removed directly
- [`856f764c`](https://github.com/oarepo/oarepo-communities/commit/856f764cbdfc18b66d4622f8683ddcaf1eed9a77) [skip ci] Bump version to v8.1.3

#### `oarepo-dashboard` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-dashboard/compare/v5.0.0...v6.0.0)

- [`b29a56bd`](https://github.com/oarepo/oarepo-dashboard/commit/b29a56bd366411bb29ccb8d47f4e018abfdd5bf9) Chore: major bump due to changes in invenio
- [`fe098cdb`](https://github.com/oarepo/oarepo-dashboard/commit/fe098cdb82d23861162c15e0791d93a0f0741473) chore: removed oarepo-tools from dev dependencies

#### `oarepo-doi` 5.0.0 💥
[4.0.1 → 5.0.0](https://github.com/oarepo/oarepo-doi/compare/v4.0.1...v5.0.0)

- [`070efe81`](https://github.com/oarepo/oarepo-doi/commit/070efe81b85cb8e5d169398ab2bef4d0b7730173) Merge pull request #46 from oarepo/release-5.0.0
- [`7b6b6da7`](https://github.com/oarepo/oarepo-doi/commit/7b6b6da7cb4d5f64bec603a97a768d09c4534f9c) Chore: Major version bump due to invenio bumps
- [`42804ad7`](https://github.com/oarepo/oarepo-doi/commit/42804ad75f9322ab0c2d57dfcfc0eaf939dd9b99) Merge pull request #45 from oarepo/docs-default-cfg
- [`28df0f71`](https://github.com/oarepo/oarepo-doi/commit/28df0f711aac6423fd2f075af8d47812fd5af16d) docs: add default config to the documentation

#### `oarepo-model` 3.0.0 💥
[2.4.0 → 3.0.0](https://github.com/oarepo/oarepo-model/compare/v2.4.0...v3.0.0)

- [`77b4b3f7`](https://github.com/oarepo/oarepo-model/commit/77b4b3f7b9b02ce01f76d08d209e99fdc01a095e) Major version bump due to major bump in packages: invenio-rdm-records, oarepo-runtime (#123)
- [`4a120fdd`](https://github.com/oarepo/oarepo-model/commit/4a120fdd28f0be7cf27616ef3d02de170dcc35dc) fix: added value labels (#120)
- [`8d521212`](https://github.com/oarepo/oarepo-model/commit/8d521212490a797b80acb844f67a007c2cca491b) [skip ci] Bump version to v2.4.0

#### `oarepo-oidc-einfra` 5.0.0 💥
[4.1.0 → 5.0.0](https://github.com/oarepo/oarepo-oidc-einfra/compare/v4.1.0...v5.0.0)

- [`0efd6a5d`](https://github.com/oarepo/oarepo-oidc-einfra/commit/0efd6a5d6be309713677953c3c947ab470819543) Major version bump due to changes in ivenio (#42)
- [`e82c5aeb`](https://github.com/oarepo/oarepo-oidc-einfra/commit/e82c5aeb9cc708eed04d2bb7f3a9f414011b3c2a) [skip ci] Bump version to v4.2.0
- [`5af94a4c`](https://github.com/oarepo/oarepo-oidc-einfra/commit/5af94a4c0f7e70ad79a4bf88cb2532c3c7166630) Upgrading invenio - request validation changed (#41)

#### `oarepo-rdm` 6.0.0 💥
[4.0.0 → 6.0.0](https://github.com/oarepo/oarepo-rdm/compare/v4.0.0...v6.0.0)

- [`a6dae478`](https://github.com/oarepo/oarepo-rdm/commit/a6dae4781c448b0111992cdf5f460dae15a77741) Major version bump due to major bump in packages: invenio, oarepo-model, oarepo-runtime, pytest-oarepo, oarepo-ui (#94)
- [`04354df6`](https://github.com/oarepo/oarepo-rdm/commit/04354df62c7dd5515e29dd65a0853ef7b2e42c4c) moved rdm related config to oarepo (#93)
- [`b2eddd89`](https://github.com/oarepo/oarepo-rdm/commit/b2eddd896a420594623e6b0602f0fe83a94ebda8) Pytest oarepo (#64)
- [`e33e9832`](https://github.com/oarepo/oarepo-rdm/commit/e33e983269d0c07c23804be928b3844be681ca6b) [skip ci] Bump version to v4.1.0
- [`9a9561bb`](https://github.com/oarepo/oarepo-rdm/commit/9a9561bb14b882fde20068b985f1b5fd2102593d) added personororgschemas to config (#90)
- [`cb7e6cec`](https://github.com/oarepo/oarepo-rdm/commit/cb7e6cec895311ee144b164e34f1222e8ae5e4b4) fix: added new route (#92)

#### `oarepo-requests` 7.0.0 💥
[5.4.0 → 7.0.0](https://github.com/oarepo/oarepo-requests/compare/v5.4.0...v7.0.0)

- [`7519d276`](https://github.com/oarepo/oarepo-requests/commit/7519d276bc4ac2524c9c2b41aa7c704a9862054c) Major bump due to invenio bump (#188)
- [`556d5d6b`](https://github.com/oarepo/oarepo-requests/commit/556d5d6be55787453f73bde798d50ba8564ee326) [breaking] using vnd serialization for dashboard requests (#186)
- [`91e42d59`](https://github.com/oarepo/oarepo-requests/commit/91e42d59bc418756faf6a24bbb2b87fd1cecb5d8) [skip ci] Bump version to v5.5.0
- [`02873240`](https://github.com/oarepo/oarepo-requests/commit/02873240e53e81a2c7a50ac7104c0c742d3ac7d4) Support per-type default request receiver (#187)
- [`fb0667d6`](https://github.com/oarepo/oarepo-requests/commit/fb0667d6405a3e50cb24b3018c6802a85ab46e6e) [skip ci] Bump version to v5.4.0

#### `oarepo-runtime` 5.0.0 💥
[4.5.0 → 5.0.0](https://github.com/oarepo/oarepo-runtime/compare/v4.5.0...v5.0.0)

- [`97bdb183`](https://github.com/oarepo/oarepo-runtime/commit/97bdb1837f41021912bf7f7ed77f9e1c6727083f) Release bump due to invenio major release bump
- [`4958af69`](https://github.com/oarepo/oarepo-runtime/commit/4958af6902e2563eaffe33cea54f4d8b13b04345) major bumping pytest-oarepo
- [`8701de7d`](https://github.com/oarepo/oarepo-runtime/commit/8701de7d3849b1bd03f64bb6f1c5bbbc9eede5d6) [skip ci] Bump version to v4.5.0

#### `oarepo-theme` 4.0.0 💥
[3.0.0 → 4.0.0](https://github.com/oarepo/oarepo-theme/compare/v3.0.0...v4.0.0)

- [`a79b07c9`](https://github.com/oarepo/oarepo-theme/commit/a79b07c98355e83d56fdd191a355fab09251b0eb) Chore: major bump due to invenio bump

#### `oarepo-ui` 11.0.0 💥
[10.2.0 → 11.0.0](https://github.com/oarepo/oarepo-ui/compare/v10.2.0...v11.0.0)

- [`2881d3dd`](https://github.com/oarepo/oarepo-ui/commit/2881d3ddc4a6ab4adadc99e5b1042370abe3f3e0) [breaking] fix: home page URLs, search layout, form feedback and input spacing`; invenio upgrade
- [`a30092f3`](https://github.com/oarepo/oarepo-ui/commit/a30092f36c1c687edbcaf18788355b0b461e64a3) fix: unable to create urls for home page
- [`05a1c8ed`](https://github.com/oarepo/oarepo-ui/commit/05a1c8ed8e6c433974fc60e97e6498a9569137cb) importing view handlers from app rdm
- [`d5113009`](https://github.com/oarepo/oarepo-ui/commit/d5113009ff8905f067d29220bafe0f0551620b0d) Downgrade version from 11.0.0 to 10.2.0
- [`1a699f77`](https://github.com/oarepo/oarepo-ui/commit/1a699f77ae506a21a12b6ba843b74e93571a303a) fixed default search app layout
- [`ef09e9cf`](https://github.com/oarepo/oarepo-ui/commit/ef09e9cf054db9ebc429c851a63db7e19bff98c0) added translations
- [`1830099f`](https://github.com/oarepo/oarepo-ui/commit/1830099fb1486135beebaab4172ed91fde7a3176) copilot suggestions
- [`90e375b0`](https://github.com/oarepo/oarepo-ui/commit/90e375b0f53e15846cd808ce5f4ad6854415afc3) fixes per PR suggestions
- [`3cc70bcb`](https://github.com/oarepo/oarepo-ui/commit/3cc70bcb24bf6fd225862b6a7d7eaf71f43c1dd2) [breaking] prototyping different form feedback (#448)
- [`b8970c21`](https://github.com/oarepo/oarepo-ui/commit/b8970c215402a5d95865868e24c10bcdb23b0004) fix: spacing between inputs
- [`a17f2460`](https://github.com/oarepo/oarepo-ui/commit/a17f2460658480379d81b6d6cccc3b198c952447) fix: nested errors fix
- [`1bf4eacf`](https://github.com/oarepo/oarepo-ui/commit/1bf4eacfc267edde8a2be7132982ac7eda038a0d) [skip ci] Bump version to v10.2.0

#### `oarepo-vocabularies` 7.0.0 💥
[6.0.0 → 7.0.0](https://github.com/oarepo/oarepo-vocabularies/compare/v6.0.0...v7.0.0)

- [`7dc59a41`](https://github.com/oarepo/oarepo-vocabularies/commit/7dc59a4125802f114264df50d97e5fd0acc07608) Major version bump due to major bump in packages: invenio-vocabularies, oarepo-runtime, oarepo-ui (#258)

#### `oarepo-workflows` 5.0.0 💥
[4.1.0 → 5.0.0](https://github.com/oarepo/oarepo-workflows/compare/v4.1.0...v5.0.0)

- [`073461dc`](https://github.com/oarepo/oarepo-workflows/commit/073461dc9abdae447c2cc89a8fd0b4a05bbce75f) Chore: Major version bump due to changes in invenio (#56)
- [`acd0a32b`](https://github.com/oarepo/oarepo-workflows/commit/acd0a32be75bc88ca5b455c880f182823b2f9993) [skip ci] Bump version to v4.2.1
- [`16b03f33`](https://github.com/oarepo/oarepo-workflows/commit/16b03f33b40f2c4d498b5a2cb9e521105ca3f15c) fix(generators): do not raise exception when workflow not found (#55)
- [`3fa4b839`](https://github.com/oarepo/oarepo-workflows/commit/3fa4b839c9e2f8b9d74a31c576012eb2f9337897) [skip ci] Bump version to v4.2.0
- [`a21791d0`](https://github.com/oarepo/oarepo-workflows/commit/a21791d08f3af4091986478e03e44fd267958d41) RecordOwners can become recipients of a request (#54)
- [`1f375f8a`](https://github.com/oarepo/oarepo-workflows/commit/1f375f8ab8a166de83269739664188fb1b0cc392) [skip ci] Bump version to v4.1.0

---

## 5.0.0

Released: **May 23, 2026 at 05:57 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `ccmm-invenio` 1.1.9
[1.1.6 → 1.1.9](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.6...v1.1.9)

- [`2c8061c6`](https://github.com/nrp-cz/ccmm-invenio/commit/2c8061c6ce300796f96c6333d7c8e37b5ac03ceb) major bump due to oarepo-ui major bump
- [`aa6283b5`](https://github.com/nrp-cz/ccmm-invenio/commit/aa6283b5d15e82644c7ac2adb85d9da737c82ca0) [skip ci] Bump version to v1.1.8
- [`e38cf4e0`](https://github.com/nrp-cz/ccmm-invenio/commit/e38cf4e03056feaba12975e9d154721ee7524513) custom fillfactor for files and access
- [`9a19e1b4`](https://github.com/nrp-cz/ccmm-invenio/commit/9a19e1b4510d789fc0656a4a8b9ed17ea41e09ee) changed names for section props
- [`e726005b`](https://github.com/nrp-cz/ccmm-invenio/commit/e726005bc55a5794399ed5f5800858d0c69707a6) [skip ci] Bump version to v1.1.7
- [`0d68d38e`](https://github.com/nrp-cz/ccmm-invenio/commit/0d68d38eeea10787167153853a2d895b87385a59) feat: added doi widget
- [`baa5a62a`](https://github.com/nrp-cz/ccmm-invenio/commit/baa5a62aec41c2d42d3e7836c6d84e69dca26ce3) removed invenio copyright header

#### `oarepo-app` 4.0.0 💥
3.0.0 → 4.0.0


#### `oarepo-communities` 8.1.3
[8.1.0 → 8.1.3](https://github.com/oarepo/oarepo-communities/compare/v8.1.0...v8.1.3)

- [`045f70b0`](https://github.com/oarepo/oarepo-communities/commit/045f70b0632f658eda3a047e0d45989040f3610a) OARepoCommunityRoles generators return empty list on MissingCommunitiesError and MissingDefaultCommunityError
- [`b2c2a192`](https://github.com/oarepo/oarepo-communities/commit/b2c2a192e45035c3808969edc53219927165e01a) [skip ci] Bump version to v8.1.2
- [`f60717a2`](https://github.com/oarepo/oarepo-communities/commit/f60717a2e401d654811ab746dd599d7275e1f244) fix: InAnyCommunities can not be used in can_create - duplicated 'data'
- [`66a10887`](https://github.com/oarepo/oarepo-communities/commit/66a108871bd0784738f627408cf531943458dfa9) [skip ci] Bump version to v8.1.1
- [`b1715957`](https://github.com/oarepo/oarepo-communities/commit/b1715957fa07f4f1dab07c0445b641b6cd6141be) using invenio's subheader
- [`6989463a`](https://github.com/oarepo/oarepo-communities/commit/6989463ab6c2da84f7e21d502b048c32fd5f5b9c) [skip ci] Bump version to v8.1.0

#### `oarepo-dashboard` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/oarepo/oarepo-dashboard/compare/v4.0.0...v5.0.0)

- [`cdd88be9`](https://github.com/oarepo/oarepo-dashboard/commit/cdd88be94e8ce3674b902b1c1ddf9bc81b3f0825) Major version bump

#### `oarepo-rdm` 4.0.0 💥
[3.2.0 → 4.0.0](https://github.com/oarepo/oarepo-rdm/compare/v3.2.0...v4.0.0)

- [`19f181ef`](https://github.com/oarepo/oarepo-rdm/commit/19f181efc84b65ae6d9e68e940e9919d78b282ca) major bump due to oarepo-ui major version bump (#91)
- [`1a5d8a96`](https://github.com/oarepo/oarepo-rdm/commit/1a5d8a960492de221e095756881f9d875c7dcc8d) [skip ci] Bump version to v3.4.0
- [`7c7114bf`](https://github.com/oarepo/oarepo-rdm/commit/7c7114bffe6a35b0df60ab29d7c46f123efc3ae6) added doi field config to formconfig (#89)
- [`1a852774`](https://github.com/oarepo/oarepo-rdm/commit/1a8527749b784ab891117004474ed7199c202899) renamed component from dummy to example (#87)
- [`3ef4dcbb`](https://github.com/oarepo/oarepo-rdm/commit/3ef4dcbb934a81b779a2cf8941005903ca9b63d9) [skip ci] Bump version to v3.3.0
- [`db8fec7b`](https://github.com/oarepo/oarepo-rdm/commit/db8fec7b6c83867a9a9253a8ae585812846c08e8) added uploads new point (moved from oarepo-ui) (#88)
- [`c1c3775a`](https://github.com/oarepo/oarepo-rdm/commit/c1c3775a157aa7d9628af2f03e207d2ed92ce28c) [skip ci] Bump version to v3.2.0

#### `oarepo-requests` 5.4.0
[5.2.0 → 5.4.0](https://github.com/oarepo/oarepo-requests/compare/v5.2.0...v5.4.0)

- [`f5228148`](https://github.com/oarepo/oarepo-requests/commit/f5228148796c4eec259c31a4117af09051f3e24f) Cache default request receiver function (#185)
- [`a1af1d08`](https://github.com/oarepo/oarepo-requests/commit/a1af1d089c7c949464b6be687e13d11c94f20fab) [skip ci] Bump version to v5.3.0
- [`e8b84303`](https://github.com/oarepo/oarepo-requests/commit/e8b84303fce41611479eaacfb1f305c1feb8b988) Feat: group recipient and notification resolver (#184)
- [`e49d97cd`](https://github.com/oarepo/oarepo-requests/commit/e49d97cd7859a442c09488bcd90501bfcd61deb3) [skip ci] Bump version to v5.2.0

#### `oarepo-ui` 10.2.0 💥
[9.2.0 → 10.2.0](https://github.com/oarepo/oarepo-ui/compare/v9.2.0...v10.2.0)

- [`e05d7c45`](https://github.com/oarepo/oarepo-ui/commit/e05d7c4547b6b399d3c2cb4f8e5b783a8e24d7b3) fix: fixes for manage menu on detail
- [`6069999d`](https://github.com/oarepo/oarepo-ui/commit/6069999d50fb94d836f92efa189750d8ee0aa0af) feat: added metadata summary overridable below steps
- [`63949431`](https://github.com/oarepo/oarepo-ui/commit/63949431f35897c6d8f2097005fa1120c1b08a19) [skip ci] Bump version to v10.1.0
- [`918a413b`](https://github.com/oarepo/oarepo-ui/commit/918a413b2a4bad4e0f6f707f0af61fc2e3a67ce4) section fillness indicator (#438)
- [`d0290937`](https://github.com/oarepo/oarepo-ui/commit/d0290937cbeaaffc4e6b86c3738fc1a6b900b8bf) moved uploads new to oarepo-rdm
- [`9ebec6ca`](https://github.com/oarepo/oarepo-ui/commit/9ebec6ca8de0d5ecfd77e6a8bee171337998fa51) major bump
- [`5d8457e9`](https://github.com/oarepo/oarepo-ui/commit/5d8457e92882cccdd7acfd11c89ef96237f53812) [skip ci] Bump version to v9.2.0

#### `oarepo-vocabularies` 6.0.0 💥
[5.0.0 → 6.0.0](https://github.com/oarepo/oarepo-vocabularies/compare/v5.0.0...v6.0.0)

- [`a35b5a21`](https://github.com/oarepo/oarepo-vocabularies/commit/a35b5a21442d6f089944da2f1288f4555d902212) major bump due to oarepo-ui major bump (#257)

#### `oarepo-workflows` 4.1.0
[4.0.2 → 4.1.0](https://github.com/oarepo/oarepo-workflows/compare/v4.0.2...v4.1.0)

- [`5925c481`](https://github.com/oarepo/oarepo-workflows/commit/5925c48112637a139bfef69f148c450875e3ea07) Feat datarepo workflows (#53)
- [`843a73f5`](https://github.com/oarepo/oarepo-workflows/commit/843a73f504dbcf39311997f51f4d9010a70950fd) [skip ci] Bump version to v4.0.2

---

## 4.0.0

Released: **May 15, 2026 at 09:16 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `oarepo-app` 3.0.0 💥
2.3.1 → 3.0.0


#### `oarepo-doi` 4.0.1 💥
[3.0.2 → 4.0.1](https://github.com/oarepo/oarepo-doi/compare/v3.0.2...v4.0.1)

- [`18b477c7`](https://github.com/oarepo/oarepo-doi/commit/18b477c7a81c0b5cd78a8cb2b0779f89f7f36f3c) Merge pull request #44 from oarepo/default-configuration
- [`1723a882`](https://github.com/oarepo/oarepo-doi/commit/1723a882b819f8619b4e737243b314d0a3adaacf) default configuration special fallback
- [`a7f05f5f`](https://github.com/oarepo/oarepo-doi/commit/a7f05f5fbefa28ccfb196df4207c0adf72a32da8) chore: bump version
- [`07edae16`](https://github.com/oarepo/oarepo-doi/commit/07edae16d5194bd2dfd39c7b37da1078a93ac990) feat: add default community fallback for DOI configuration
- [`b6511f77`](https://github.com/oarepo/oarepo-doi/commit/b6511f772acc65d7043ffa74e9506eb0b76c3574) version
- [`ba11529d`](https://github.com/oarepo/oarepo-doi/commit/ba11529d8833fd9361d8404c9c1272fab5cd7c51) add documentation
- [`28e4e292`](https://github.com/oarepo/oarepo-doi/commit/28e4e292233ff1fe44f5ac0d1119b67ade44d97e) fix: test linter
- [`8e125169`](https://github.com/oarepo/oarepo-doi/commit/8e125169c3e04f029f8fd47d04c0cde799fb8ca0) remove unused code
- [`ca08989f`](https://github.com/oarepo/oarepo-doi/commit/ca08989f72ca769ce9a0a5a9165a09893b975696) datacite provider test
- [`71a9c28a`](https://github.com/oarepo/oarepo-doi/commit/71a9c28af8d3764c58228a9a45adc5148d1fe74b) chore: lint
- [`5661dcc6`](https://github.com/oarepo/oarepo-doi/commit/5661dcc61251416d7f2fdac0b35ab8902fa35bec) fix(ci): restore jobs block in test workflow
- [`b2a42e21`](https://github.com/oarepo/oarepo-doi/commit/b2a42e21c31982f4273db6d2b97cdd3f425c7db6) chore: bump Python version
- [`63e374c2`](https://github.com/oarepo/oarepo-doi/commit/63e374c2fdf15573d2544a8b1816b544b22030a4) feat: add record aware provider
- [`7346c6d0`](https://github.com/oarepo/oarepo-doi/commit/7346c6d0d954d77e79cc43f3e6aebac9dacbaaba) format
- [`986eb5f0`](https://github.com/oarepo/oarepo-doi/commit/986eb5f0caca10a218d1f15701f1fd77e39a663e) record aware code
- [`d379a308`](https://github.com/oarepo/oarepo-doi/commit/d379a308a14be6789269f0b6dd99d0cd1a7beb2a) doi config on rdm14
- [`474b18f7`](https://github.com/oarepo/oarepo-doi/commit/474b18f796dbe63aea90d4e13755ffe4efa3fb1d) doi config on rdm13
- [`b82339ad`](https://github.com/oarepo/oarepo-doi/commit/b82339adac20214cda31c3b6642969284ea6dc89) version
- [`251a6636`](https://github.com/oarepo/oarepo-doi/commit/251a6636f2eb0d0e5ef06f73905d274c128d29d9) disable tests
- [`cf881f0f`](https://github.com/oarepo/oarepo-doi/commit/cf881f0f64bd6f349b6a0ac563881da87b82eb9b) rdm13 refactor

---

## 3.0.0

Released: **May 15, 2026 at 07:46 UTC**

### Updated packages

#### `oarepo-app` 2.3.1
2.2.0 → 2.3.1


#### `oarepo-runtime` 4.5.0
[4.3.0 → 4.5.0](https://github.com/oarepo/oarepo-runtime/compare/v4.3.0...v4.5.0)

- [`838e62a1`](https://github.com/oarepo/oarepo-runtime/commit/838e62a1b9308984bcc92a6f93850aeb65271b01) fix: Fix return types of ExportEngine, add option to choose export representation.
- [`6bf6f911`](https://github.com/oarepo/oarepo-runtime/commit/6bf6f911a3b76b1086cccfff077509e398e2329d) fix: Fix return types of ExportEngine, add option to choose export representation.
- [`679c5dd4`](https://github.com/oarepo/oarepo-runtime/commit/679c5dd44cb900a735b9045a2609f923a2db7ad9) [skip ci] Bump version to v4.4.0
- [`1461af57`](https://github.com/oarepo/oarepo-runtime/commit/1461af570fa44ba222155b72a2faa8d0f473c3e8) feat: Introduce ExportEngine class with a caching mechanism to avoid doing the same export multiple times.
- [`4d857740`](https://github.com/oarepo/oarepo-runtime/commit/4d85774068b4874cbd6a359e294dee8810ac51c7) chore: format
- [`db233966`](https://github.com/oarepo/oarepo-runtime/commit/db2339669fc03b2235da99a85042b87c6a573230) [skip ci] Bump version to v4.3.0

#### `oarepo-ui` 9.2.0
[9.1.5 → 9.2.0](https://github.com/oarepo/oarepo-ui/compare/v9.1.5...v9.2.0)

- [`8cf56bc7`](https://github.com/oarepo/oarepo-ui/commit/8cf56bc7d67a556fe5a83de0857fd2219a4c7375) feat: use ExportEngine cache context to optimize export caching in record_detail
- [`db32b181`](https://github.com/oarepo/oarepo-ui/commit/db32b181a725817a7282e8fc585078360b51cf92) [skip ci] Bump version to v9.1.5

---

## 2.3.0

Released: **May 11, 2026 at 11:05 UTC**

### Updated packages

#### `ccmm-invenio` 1.1.6
[1.1.4 → 1.1.6](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.4...v1.1.6)

- [`cdabcabd`](https://github.com/nrp-cz/ccmm-invenio/commit/cdabcabd42dcd8351afc0f9c9064e6817685742b) cc0 title
- [`6f901ade`](https://github.com/nrp-cz/ccmm-invenio/commit/6f901adebfd030d9152657ab4e56fa231636b089) feat(vocabularies): add OpenAIRE mappings via addons and conversion pipeline
- [`85c1a592`](https://github.com/nrp-cz/ccmm-invenio/commit/85c1a5928238d11f4e45eb2bd0e2cf8685732830) adjust OpenAIRE vocabulary mappings to updated CCMM dictionaries
- [`272de801`](https://github.com/nrp-cz/ccmm-invenio/commit/272de801beafb21628b4e7e3fbf9fe4089641a68) add contributor-type mappings
- [`85722260`](https://github.com/nrp-cz/ccmm-invenio/commit/857222604d6751d36b6b550d97c05cc1aa6ff2a9) add vocabularies datacite mapping
- [`0edeafeb`](https://github.com/nrp-cz/ccmm-invenio/commit/0edeafeb1c6c90081e5079b3a15145fbcce6c50f) refactor: lint
- [`6464d940`](https://github.com/nrp-cz/ccmm-invenio/commit/6464d940ef86c296b9eeb0dabc0a065b1508a2ca) feat(vocabularies): add CC0-1.0 license under CC hierarchy
- [`962e4700`](https://github.com/nrp-cz/ccmm-invenio/commit/962e47001a8ab54fd1edbf5251b5952c445cb8e5) chore(vocabularies): add all tag to all license vocabulary entries

#### `invenio-app` 3.1.1
[3.0.0 → 3.1.1](https://github.com/inveniosoftware/invenio-app/compare/v3.0.0...v3.1.1)

- [`ff2ca4c3`](https://github.com/inveniosoftware/invenio-app/commit/ff2ca4c372d5bc2a392a2e0378d34649c66b3bd3) 📦 release: v3.1.1
- [`5022e3dc`](https://github.com/inveniosoftware/invenio-app/commit/5022e3dc7417e450a20cc3699eda947ccdfae274) fix(tests): patch correct module level for limiter
- [`27ab966b`](https://github.com/inveniosoftware/invenio-app/commit/27ab966b174c7463e19fb70402805352dcad0e69) fix(installation): add Python 3.9-compatible Flask-Limiter version
- [`ed25592f`](https://github.com/inveniosoftware/invenio-app/commit/ed25592fc9ce158dfe4e8ec41b1af162c995434c) fix: Limiter cross-test influence
- [`12e3f79f`](https://github.com/inveniosoftware/invenio-app/commit/12e3f79f3a4f9a34823a02879a4b2cfbab49b619) fix(tests): flask-limiter constructor change
- [`4e688d3a`](https://github.com/inveniosoftware/invenio-app/commit/4e688d3a65a5b453e42a3e033fe2f60e419407db) 📦 release: v3.1.0
- [`0d9c958f`](https://github.com/inveniosoftware/invenio-app/commit/0d9c958f4673bbd05a6c44779a30ebaf73e7f6c3) chore: remove unused imports and apply linter fixes
- [`1e5f7678`](https://github.com/inveniosoftware/invenio-app/commit/1e5f76784ab66ed7907be7899121db0e5c070d17) feat(ext): provide easier-to-access Flask-Talisman instance
- [`485ab132`](https://github.com/inveniosoftware/invenio-app/commit/485ab132b995b5099b89a061b73302cfa9f973c5) feat(ext): provide easier-to-access Flask-Limiter instance

#### `invenio-app-rdm` 14.0.0b10.dev7+oarepo.4.ygkzv7ea34y6xlcc
[14.0.0b10.dev6+oarepo.2.ioyk53cm5eo4shpy → 14.0.0b10.dev7+oarepo.4.ygkzv7ea34y6xlcc](https://github.com/inveniosoftware/invenio-app-rdm/compare/v14.0.0b10.dev6...v14.0.0b10.dev7)

- [`743b8a70`](https://github.com/inveniosoftware/invenio-app-rdm/commit/743b8a70759bec6dbe7edfe85ad68423d98332b0) 📦 release: v14.0.0b10.dev7
- [`ffb7a753`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ffb7a7538c62ea4b3803572caa93e69d3be7aea8) feat(administration): allow blocking with removal reason
- [`428388fb`](https://github.com/inveniosoftware/invenio-app-rdm/commit/428388fb621a1cadad50fd0fbe25d3fa1c24ea40) style: fix alignment of sort by on uploads
- [`f1333245`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f133324556b5230deaafe80d4b167da99870ec76) fix: display user dashboard header for community topic requests as before
- [`df1e1b69`](https://github.com/inveniosoftware/invenio-app-rdm/commit/df1e1b69855cdd0f669770769964bc4ceca00398) feat(auditlogs): hide auditlogs button when the feature is disabled

#### `invenio-checks` 8.2.0
[8.1.0 → 8.2.0](https://github.com/inveniosoftware/invenio-checks/compare/v8.1.0...v8.2.0)

- [`d2d8252e`](https://github.com/inveniosoftware/invenio-checks/commit/d2d8252ec15e1128a4a8271b1af7e5ed061e6dbf) release: v8.2.0
- [`1c768641`](https://github.com/inveniosoftware/invenio-checks/commit/1c768641d3fbf5049e3f7fbd84356f1d3aba65b0) feat(rules): add min/max operators

#### `invenio-collections` 8.1.1
[8.1.0 → 8.1.1](https://github.com/inveniosoftware/invenio-collections/compare/v8.1.0...v8.1.1)

- [`188e8468`](https://github.com/inveniosoftware/invenio-collections/commit/188e84688d8b14351e6cb9ebdbf573a4fe7e3f5a) release: v8.1.1
- [`b19d77fd`](https://github.com/inveniosoftware/invenio-collections/commit/b19d77fd30855f9d2a838e4d2e0e060207c655cc) fix: correct URL for collection

#### `invenio-communities` 26.1.1+oarepo.1.ju33cyh3ievitktv
[26.0.0+oarepo.1.qot6rqrpnjb6q5hz → 26.1.1+oarepo.1.ju33cyh3ievitktv](https://github.com/inveniosoftware/invenio-communities/compare/v26.0.0...v26.1.1)

- [`d9eae8fc`](https://github.com/inveniosoftware/invenio-communities/commit/d9eae8fc2a1be929266f3f7e926b1d17cbad9829) :package: release: v26.1.1
- [`1d6b50c1`](https://github.com/inveniosoftware/invenio-communities/commit/1d6b50c116603257651677b1f0e817fecbdd2ab9) fix(inv): show discussion for invitation requests by generating self_html
- [`954ba3f6`](https://github.com/inveniosoftware/invenio-communities/commit/954ba3f6b99b7917963ee1dc631772dc29604dd5) 📦 release: v26.1.0
- [`f0ce5b6e`](https://github.com/inveniosoftware/invenio-communities/commit/f0ce5b6e412dfa2faa700f0283bdfe90b4d98931) fix(components): handle tombstone `removed_by` value
- [`64ec5cd3`](https://github.com/inveniosoftware/invenio-communities/commit/64ec5cd3d0a34a59215a06be7a2c6691bfaacc26) feat(moderation): handle `actor_id` and `note` in user block callback
- [`a24a6758`](https://github.com/inveniosoftware/invenio-communities/commit/a24a6758715aeaf4ab6bd2f36d124896f787c393) i18n: replace .format() with %-style
- [`8dd60aef`](https://github.com/inveniosoftware/invenio-communities/commit/8dd60aeff93f9280e0feec9eec403b8b650d1a6e) 📦 release: v26.0.1

#### `invenio-drafts-resources` 9.0.2+oarepo.1.7ycffxo2j7hqwzgo
[9.0.1+oarepo.1.p7573uc2mq3xg5se → 9.0.2+oarepo.1.7ycffxo2j7hqwzgo](https://github.com/inveniosoftware/invenio-drafts-resources/compare/v9.0.1...v9.0.2)

- [`0bd2cc6d`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/0bd2cc6dd2a333c8a2db39eb6c3e17128ebeeefc) release: v9.0.2
- [`64dbf4ef`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/64dbf4ef07729fe948ec37f5dc55007c2d08dacf) fix(auditlog): don't require session to accomodate API calls

#### `invenio-oaiserver` 4.1.0+oarepo.1.jeizhxspiugts6ow
[4.0.1+oarepo.2.4sorqldmiw776f3g → 4.1.0+oarepo.1.jeizhxspiugts6ow](https://github.com/inveniosoftware/invenio-oaiserver/compare/v4.0.1...v4.1.0)

- [`30072f7d`](https://github.com/inveniosoftware/invenio-oaiserver/commit/30072f7d6d961651d9124af3622e19987494b066) 📦 release: v4.1.0
- [`4931dead`](https://github.com/inveniosoftware/invenio-oaiserver/commit/4931dead28af68dd8659de19ed8e8cbce99357f3) feat: add support for OAI about serializer
- [`fac0312f`](https://github.com/inveniosoftware/invenio-oaiserver/commit/fac0312f96d9b1572149cec787b39dd2305f2e02) tests: clear serializer caches in about serializer test
- [`8adc6293`](https://github.com/inveniosoftware/invenio-oaiserver/commit/8adc6293f4b101b90fabac0dca62fb58b5821532) refactor: address review feedback

#### `invenio-queues` 1.0.3+oarepo.1.mbv3n5punhjld6n3
[1.0.2+oarepo.4.wsyd5f5b5aoeak67 → 1.0.3+oarepo.1.mbv3n5punhjld6n3](https://github.com/inveniosoftware/invenio-queues/compare/v1.0.2...v1.0.3)

- [`e73de14e`](https://github.com/inveniosoftware/invenio-queues/commit/e73de14eb94a31612afeca4c5ffeeb1b3e57ad23) 📦 release: v1.0.3
- [`8e125da2`](https://github.com/inveniosoftware/invenio-queues/commit/8e125da2b7047801264fbb3e4166680da903bb3f) fix(ext): make `current_queues.queues` property thread-safe
- [`7ec1c68c`](https://github.com/inveniosoftware/invenio-queues/commit/7ec1c68c2a3461c4aab71650252b47e86d2cc896) tests: extend support to Python 3.14

#### `invenio-rdm-records` 28.5.0+oarepo.1.7kmabv7jmwdd4bgu
[28.3.1+oarepo.1.mwjq6wsqhds4s5ur → 28.5.0+oarepo.1.7kmabv7jmwdd4bgu](https://github.com/inveniosoftware/invenio-rdm-records/compare/v28.3.1...v28.5.0)

- [`9736326c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/9736326c6c3735973cdaf00c87a7208b16ddd3a0) 📦 release: v28.5.0
- [`7378ec7d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7378ec7d6456db8cb67ef6b9b5e73fcd4a6bc3b7) feat(moderation): handle `actor_id` and `note` in user block callback
- [`d77ea581`](https://github.com/inveniosoftware/invenio-rdm-records/commit/d77ea5810893e32b174e269c7fefe9db125cb3ca) fix(vcs): add license as custom if not matched as a vocabulary
- [`0c7fb7f5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0c7fb7f5813d3e3859009690c1e137582e1cdae9) release: v28.4.0
- [`df7e2b89`](https://github.com/inveniosoftware/invenio-rdm-records/commit/df7e2b89205e5d937e8efaea65ed1709932c91ac) fix(vcs): avoid failing on unrecognised license; include warning messages in notification
- [`bb74b02e`](https://github.com/inveniosoftware/invenio-rdm-records/commit/bb74b02e608bd4220436d064ac61fb96675d4057) feat: add optional record parameter to support per-community PID assignment (#2279)
- [`3b6b9577`](https://github.com/inveniosoftware/invenio-rdm-records/commit/3b6b9577ac6e3bcb7abaa9c290f65c840424e85d) fix(config): reuse community records search params config
- [`7e0bc939`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7e0bc939a7ad75978f0df1b002a4d7465bd31ccd) fix: missing proptype
- [`45095f32`](https://github.com/inveniosoftware/invenio-rdm-records/commit/45095f32ad8f2c3c763fa7c20affdc17b6f3b940) fix: use translation to customise msg instead of config
- [`4f7ed0e4`](https://github.com/inveniosoftware/invenio-rdm-records/commit/4f7ed0e4a02273b68054ff9be0830b9a35f4a979) fix: using only depositable resource type for fake data
- [`0a18fc93`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0a18fc934c33541914193d1b3e748d6ab6bafb9b) fix: add preview button to publish modal

#### `invenio-requests` 12.6.1+oarepo.1.e3mgu3w367pgarrw
[12.6.0+oarepo.1.gof4prsfnzoqgasf → 12.6.1+oarepo.1.e3mgu3w367pgarrw](https://github.com/inveniosoftware/invenio-requests/compare/v12.6.0...v12.6.1)

- [`98f9012f`](https://github.com/inveniosoftware/invenio-requests/commit/98f9012fd1858c68ba4f763ebf0baafe5ab97cc5) fix(comments): ensure "show less" button is hidden for comments <200px height
- [`47064e1f`](https://github.com/inveniosoftware/invenio-requests/commit/47064e1f8dd0063be4ec7816f722065c1bb1b656) release: v12.6.1

#### `invenio-stats` 6.1.3
[6.1.2 → 6.1.3](https://github.com/inveniosoftware/invenio-stats/compare/v6.1.2...v6.1.3)

- [`8cd1d9a2`](https://github.com/inveniosoftware/invenio-stats/commit/8cd1d9a22f3ef890695b61a1f7b3b21138437eee) 📦 release: v6.1.3
- [`b2507f92`](https://github.com/inveniosoftware/invenio-stats/commit/b2507f924e94b3a4821d2612eae4330fed80e667) fix(stats): warm event cache on finalization

#### `invenio-theme` 4.7.0
[4.6.0 → 4.7.0](https://github.com/inveniosoftware/invenio-theme/compare/v4.6.0...v4.7.0)

- [`ee0a35f3`](https://github.com/inveniosoftware/invenio-theme/commit/ee0a35f3035c69d5a47cfea36a166ae504de09ca) release: v4.7.0
- [`71d049e0`](https://github.com/inveniosoftware/invenio-theme/commit/71d049e0312ef0dd94ded3c7235faa63aee64824) site: add collections rules
- [`db0197fc`](https://github.com/inveniosoftware/invenio-theme/commit/db0197fce13358dfc26155d623831b3dde212ecd) collections: adds css required for collection CRUD UI

#### `invenio-users-resources` 10.5.0
[10.4.1 → 10.5.0](https://github.com/inveniosoftware/invenio-users-resources/compare/v10.4.1...v10.5.0)

- [`81f2894b`](https://github.com/inveniosoftware/invenio-users-resources/commit/81f2894b65d0df0be70661254b9127d95b8f7251) 📦 release: v10.5.0
- [`6225d448`](https://github.com/inveniosoftware/invenio-users-resources/commit/6225d44838518c9136e07cce01318eaeb3123e07) feat(moderation): allow passing `data` and `actor_id` to block action

#### `invenio-vocabularies` 11.1.2+oarepo.1.26bhh64bjojb73mv
[11.0.1+oarepo.2.2pto3quqarmp23uj → 11.1.2+oarepo.1.26bhh64bjojb73mv](https://github.com/inveniosoftware/invenio-vocabularies/compare/v11.0.1...v11.1.2)

- [`9ea63283`](https://github.com/inveniosoftware/invenio-vocabularies/commit/9ea632830716ea964a406e9e31754ab818bd662c) release: v11.1.2
- [`8c996591`](https://github.com/inveniosoftware/invenio-vocabularies/commit/8c996591a680842c763c5048e3879dd1b8a3852a) fix(datastreams): Log ORCID read errors as warnings
- [`f3550cd2`](https://github.com/inveniosoftware/invenio-vocabularies/commit/f3550cd29a63f5e2da67eb030029f497536d10f8) fix(datastreams): replace f-strings in logging calls with %s formatting
- [`fc208298`](https://github.com/inveniosoftware/invenio-vocabularies/commit/fc20829803a02565511e07cdd09e9b5ef3de96b8) fix(names): skip invalid ORCID entries
- [`e20793f7`](https://github.com/inveniosoftware/invenio-vocabularies/commit/e20793f77279c1b8f3cc0547e4e00f89f87120a6) 📦 release: v11.1.1
- [`935a99b5`](https://github.com/inveniosoftware/invenio-vocabularies/commit/935a99b5191a0ee369072fa508259895401619cc) 📦 release: v11.1.0
- [`be71648e`](https://github.com/inveniosoftware/invenio-vocabularies/commit/be71648eb42132ee5cd3d22e2e90145f88a6fff8) feat: added run_subtasks flag in datastream writer

#### `oarepo-app` 2.2.0
2.1.0 → 2.2.0


#### `oarepo-ui` 9.1.5
[9.1.3 → 9.1.5](https://github.com/oarepo/oarepo-ui/compare/v9.1.3...v9.1.5)

- [`9cbd3a1f`](https://github.com/oarepo/oarepo-ui/commit/9cbd3a1f6ed407bf8e00d350dd43370ab77ea2df) fix: buttons not wrapping on smaller screens (#446)
- [`2fb36542`](https://github.com/oarepo/oarepo-ui/commit/2fb3654243721f529410254e1bef9bbda707107c) fix error label positioning
- [`bf8b6d7a`](https://github.com/oarepo/oarepo-ui/commit/bf8b6d7a033aee42e0c1fa8b687c6f435e964272) added model type to resource
- [`e0858d32`](https://github.com/oarepo/oarepo-ui/commit/e0858d3289670063b1035769a186ffcbec97bad5) added serializer for empty model
- [`2e973899`](https://github.com/oarepo/oarepo-ui/commit/2e973899b43bfcc6135a7af48d8031f03bc55863) Update oarepo_ui/resources/records/resource.py
- [`92c840b8`](https://github.com/oarepo/oarepo-ui/commit/92c840b877345fb56340b725b49d923ec447a796) Update oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/api/recordSerializer.js
- [`8c70e1dd`](https://github.com/oarepo/oarepo-ui/commit/8c70e1dd5aff64f2f150ebd21d51c80b6e086446) fixed empty serializer
- [`737024d0`](https://github.com/oarepo/oarepo-ui/commit/737024d0f511f7283b30cbca4ff5feecec52831c) [skip ci] Bump version to v9.1.4
- [`8abf108a`](https://github.com/oarepo/oarepo-ui/commit/8abf108ac98bcee4c83b2df4219d195c52b4bb6d) fix: fix facet layout
- [`707b1c7a`](https://github.com/oarepo/oarepo-ui/commit/707b1c7a5edc38df4c1efca93d381e8cd7cb12ab) fix: change order of buttons for wizard
- [`96292f1b`](https://github.com/oarepo/oarepo-ui/commit/96292f1b63d4014f1dd1ad8d7d4227bbff6ad019) fix: fixed field spacing
- [`d896e160`](https://github.com/oarepo/oarepo-ui/commit/d896e1607d9c3702e24f24a1d7b59f45e2fbe115) fixed /search layout
- [`aaef5b91`](https://github.com/oarepo/oarepo-ui/commit/aaef5b91008571f5abd83ce6b86c1b08ee0b0333) passing form title
- [`d8d05caa`](https://github.com/oarepo/oarepo-ui/commit/d8d05caa17fb50069ce3f4b1b52b5d4b9d56ce8a) [skip ci] Bump version to v9.1.3

---

## 2.2.0

Released: **May 6, 2026 at 15:37 UTC**

### Updated packages

#### `oarepo-app` 2.1.0
2.0.1 → 2.1.0


#### `oarepo-model` 2.4.0
[2.2.0 → 2.4.0](https://github.com/oarepo/oarepo-model/compare/v2.2.0...v2.4.0)

- [`49287f16`](https://github.com/oarepo/oarepo-model/commit/49287f161632abcb04e7f734c42ffc59c186ad09) synthetic metadata (#109)
- [`8105483a`](https://github.com/oarepo/oarepo-model/commit/8105483a3fbcf574b25dfa07ed4688f5c03f842d) [skip ci] Bump version to v2.3.0
- [`502bec82`](https://github.com/oarepo/oarepo-model/commit/502bec8228019b1a123c31a88ec63a9792b1f920) feat: add exporter parameter for record about section (#110)
- [`2f97183b`](https://github.com/oarepo/oarepo-model/commit/2f97183b9691b6c738c40fabe0d00ae039d1e32b) [skip ci] Bump version to v2.2.0

#### `oarepo-rdm` 3.2.0
[3.1.4 → 3.2.0](https://github.com/oarepo/oarepo-rdm/compare/v3.1.4...v3.2.0)

- [`10b85fde`](https://github.com/oarepo/oarepo-rdm/commit/10b85fde09d674b145e0eb4ea52674a84e83894d) fix: using proper serializer for each model (#83)
- [`67e20b75`](https://github.com/oarepo/oarepo-rdm/commit/67e20b75b3008fd3c31e5a7888e911b30e313ffd) fixing metadata (#82)
- [`71c9042d`](https://github.com/oarepo/oarepo-rdm/commit/71c9042d66df8bfa7a5158d3a8f3421ccecf9402) added static assets skeleton (#84)
- [`476951f0`](https://github.com/oarepo/oarepo-rdm/commit/476951f0d1fc48317bf3f12a0d2d7b9d196f8ed7) feat: add about serializer to OAI config (#86)
- [`fde9acdd`](https://github.com/oarepo/oarepo-rdm/commit/fde9acdda60561724f3a0c0fa71020f3cee4dfa2) [skip ci] Bump version to v3.1.4

#### `oarepo-runtime` 4.3.0
[4.2.0 → 4.3.0](https://github.com/oarepo/oarepo-runtime/compare/v4.2.0...v4.3.0)

- [`19a374c6`](https://github.com/oarepo/oarepo-runtime/commit/19a374c6dac70efde3281c32bed9fc0879f5a9e4) fix: Limit maximum number of creators to 30 during signposting.
- [`55572f92`](https://github.com/oarepo/oarepo-runtime/commit/55572f9260ff4f5d3e2b582c579a89616e7333e8) fix: babel.getlocale instead of current_i18n
- [`8f64cc83`](https://github.com/oarepo/oarepo-runtime/commit/8f64cc83a71493b2694c1420e21ad06be294d1fc) feat: add exporter parameter for record about section
- [`370aaeb3`](https://github.com/oarepo/oarepo-runtime/commit/370aaeb32d18b12105c0b2889c45faca3b3f9f54) [skip ci] Bump version to v4.2.0

---

## 2.1.0

Released: **May 5, 2026 at 18:51 UTC**

### Updated packages

#### `ccmm-invenio` 1.1.4
[1.1.2 → 1.1.4](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.2...v1.1.4)

- [`c4c8c66c`](https://github.com/nrp-cz/ccmm-invenio/commit/c4c8c66cc3e5d3930e241887ab36394842057e01) Bump version from 1.1.3 to 1.1.4
- [`0f213b69`](https://github.com/nrp-cz/ccmm-invenio/commit/0f213b69ef8e72037890bbe75818a178770b80a5) added export for citations
- [`007ea256`](https://github.com/nrp-cz/ccmm-invenio/commit/007ea256e44f36e0d237017c9061e5df64935fd1) Bump version from 1.1.2 to 1.1.3
- [`eda2fe5f`](https://github.com/nrp-cz/ccmm-invenio/commit/eda2fe5fefacb2da496511066d144f3bd4718640) reordering and section customization
- [`3e1abc2e`](https://github.com/nrp-cz/ccmm-invenio/commit/3e1abc2e812cb278f2dce3603871f91d883b6fae) added translations

#### `oarepo-app` 2.0.1
2.0.0 → 2.0.1


#### `oarepo-communities` 8.1.0
[8.0.0 → 8.1.0](https://github.com/oarepo/oarepo-communities/compare/v8.0.0...v8.1.0)

- [`08554baf`](https://github.com/oarepo/oarepo-communities/commit/08554bafde999857858cf1c81da9bafe3a95ba91) removed ModelRefTypes

#### `oarepo-glitchtip` 1.3.0
[1.1.1 → 1.3.0](https://github.com/oarepo/oarepo-glitchtip/compare/v1.1.1...v1.3.0)

- [`996d4e3c`](https://github.com/oarepo/oarepo-glitchtip/commit/996d4e3c29bb1f8c5cd628616db4096bf57f9407) reverting enabled logs - not available in current sentry-sdk version (#9)
- [`f518289e`](https://github.com/oarepo/oarepo-glitchtip/commit/f518289e63fa96311cdb1c6cc53e9e80b76640bc) Bump version from 1.1.2 to 1.2.0 (#8)
- [`de2e9aca`](https://github.com/oarepo/oarepo-glitchtip/commit/de2e9acab5410c2e02138b43ef39d2b6c6247ff0) Specify Sentry SDK version range in pyproject.toml (#7)
- [`38059614`](https://github.com/oarepo/oarepo-glitchtip/commit/380596149845721d64e853e079152edbf70dabae) chore: migrated to pyproject.toml with hatchling (#6)
- [`b4b6f4a3`](https://github.com/oarepo/oarepo-glitchtip/commit/b4b6f4a36e93579fa331a4ba271a9a37186c1add) Fake test runner (#5)

#### `oarepo-model` 2.2.0
[2.0.0 → 2.2.0](https://github.com/oarepo/oarepo-model/compare/v2.0.0...v2.2.0)

- [`ed6175c9`](https://github.com/oarepo/oarepo-model/commit/ed6175c929583f25fc21e0d8cc360526d7115f2a) feat: get facet label from model (#108)
- [`e5fe78f7`](https://github.com/oarepo/oarepo-model/commit/e5fe78f7ab09290522bed6ab7006bd00cfe1e505) fixed wrong facet path for fields under metadata (#107)
- [`d064a601`](https://github.com/oarepo/oarepo-model/commit/d064a601aeafa7e8fd35429c0d173bab05e6e9fd) [skip ci] Bump version to v2.1.0
- [`63d25858`](https://github.com/oarepo/oarepo-model/commit/63d25858a3c4195d46182bd27cc5af268955fa52) add `override_values` option to `AddToDictionary` customization, enab… (#106)
- [`f89be52b`](https://github.com/oarepo/oarepo-model/commit/f89be52b7b02a793fb4ee17895a39cc6c03616d9) added is_published facet (#96)

#### `oarepo-oidc-einfra` 4.1.0
[4.0.0 → 4.1.0](https://github.com/oarepo/oarepo-oidc-einfra/compare/v4.0.0...v4.1.0)

- [`a2a44024`](https://github.com/oarepo/oarepo-oidc-einfra/commit/a2a440248af2f7854c820217840b3bf3d0edb1fb) Feat OIDC groups roles (#40)

#### `oarepo-rdm` 3.1.4
[3.0.0 → 3.1.4](https://github.com/oarepo/oarepo-rdm/compare/v3.0.0...v3.1.4)

- [`a844bd9f`](https://github.com/oarepo/oarepo-rdm/commit/a844bd9f07fb24a0966a8954fc18176304eb46ad) fix: added is_preview tag and latest version read to redirector (#85)
- [`c5b62edf`](https://github.com/oarepo/oarepo-rdm/commit/c5b62edfe624a84ce3499fed1c04dd659ad9346d) fix: safely check search options
- [`ef0199aa`](https://github.com/oarepo/oarepo-rdm/commit/ef0199aae470870bd7e586a286c093078b9cec0d) [skip ci] Bump version to v3.1.3
- [`6d77d306`](https://github.com/oarepo/oarepo-rdm/commit/6d77d306ca0030da77521870dac2282e31b295ab) added components for RDM related variables
- [`1aa735e1`](https://github.com/oarepo/oarepo-rdm/commit/1aa735e17983d2a5d62df75859749c1d4cb43b02) fixed tests
- [`8d5f5595`](https://github.com/oarepo/oarepo-rdm/commit/8d5f5595051841b3abfe1cfc87b9ddf0cf690d18) [skip ci] Bump version to v3.1.2
- [`75710a9c`](https://github.com/oarepo/oarepo-rdm/commit/75710a9c9a8c0e7074c2dd89c2d6648c8dfcee90) record detail iframe
- [`42dd2a48`](https://github.com/oarepo/oarepo-rdm/commit/42dd2a48ea38778d637a1502cc47fb03fc205c95) passing query params when redirecting from rdm urls
- [`167dbb58`](https://github.com/oarepo/oarepo-rdm/commit/167dbb581f9e5001fbbc57156d3a5ccd5da5e925) account for both draft and published record
- [`2859b450`](https://github.com/oarepo/oarepo-rdm/commit/2859b450d5407657f91c1e5e73db6d2add6c5cd6) [skip ci] Bump version to v3.1.1
- [`af95b0a6`](https://github.com/oarepo/oarepo-rdm/commit/af95b0a676c2a0756e4af292ad1d6b24e667f5ab) inheriting rdm links (#77)
- [`be6a32d0`](https://github.com/oarepo/oarepo-rdm/commit/be6a32d0794cded0b6449f18af8625583c0a52fa) [skip ci] Bump version to v3.1.0
- [`d0ebb94f`](https://github.com/oarepo/oarepo-rdm/commit/d0ebb94f5eb568ccfd1a91dd001262e96b64e8df) error handler for UndefinedModelError (#73)
- [`624f6731`](https://github.com/oarepo/oarepo-rdm/commit/624f6731cf3f01932fc3ea9c47f9baba5a71ef14) RDM_PREFERRED_METADATA_SCHEMA option (#76)

#### `oarepo-requests` 5.2.0
[5.0.0 → 5.2.0](https://github.com/oarepo/oarepo-requests/compare/v5.0.0...v5.2.0)

- [`ae057aea`](https://github.com/oarepo/oarepo-requests/commit/ae057aeacca06056ab359350e43735cfb8717532) Error handlers (#182)
- [`9b3593d2`](https://github.com/oarepo/oarepo-requests/commit/9b3593d2134bdab8df677e53e3d5e93632e60804) [skip ci] Bump version to v5.1.0
- [`1d88d940`](https://github.com/oarepo/oarepo-requests/commit/1d88d9409f59f922062df602dd6dfd62331aac64) ron/be-1070-remove-entity_type-from-model-and-its-uses (#181)

#### `oarepo-runtime` 4.2.0
[4.0.0 → 4.2.0](https://github.com/oarepo/oarepo-runtime/compare/v4.0.0...v4.2.0)

- [`6b74661e`](https://github.com/oarepo/oarepo-runtime/commit/6b74661e4c40023ddea82b35e97081dceda02731) feat: taking labels from model if they exist
- [`e5118727`](https://github.com/oarepo/oarepo-runtime/commit/e51187278b5dc57ca220ba55e250fa05ecbe48ae) [skip ci] Bump version to v4.1.0
- [`53c85395`](https://github.com/oarepo/oarepo-runtime/commit/53c853959f95b56bac78590c727a980780c410c3) entity_type removed from model

#### `oarepo-ui` 9.1.3
[9.0.0 → 9.1.3](https://github.com/oarepo/oarepo-ui/compare/v9.0.0...v9.1.3)

- [`56fe3e81`](https://github.com/oarepo/oarepo-ui/commit/56fe3e815c4308b98076a22654fa69f12b9d89b2) moved rdm related things to components in oarepo-rdm
- [`401c3709`](https://github.com/oarepo/oarepo-ui/commit/401c3709c696d24cbf2f1ae7f0c821f17174fbc7) section config that forces save on leaving tab
- [`54c8c896`](https://github.com/oarepo/oarepo-ui/commit/54c8c896a202573c69d63b5aa153940650b77ca4) [skip ci] Bump version to v9.1.2
- [`752f27cd`](https://github.com/oarepo/oarepo-ui/commit/752f27cdbe98f54b91f91f504ec22eb99ddaf683) fix: pages prefix duplicated
- [`1cecfbd1`](https://github.com/oarepo/oarepo-ui/commit/1cecfbd16edc80c1a6bed199314926eaa6097f4e) chore: format
- [`f47767fa`](https://github.com/oarepo/oarepo-ui/commit/f47767fa165ae9f05c23daf7be00b3c2c6cc5c4e) fix: bad variable name
- [`dd5020bd`](https://github.com/oarepo/oarepo-ui/commit/dd5020bda870bd2fda43f77ae123a210569e2a66) renamed render to component
- [`a0cd537a`](https://github.com/oarepo/oarepo-ui/commit/a0cd537a22b5798de6649c01259b30c1711a69ad) [skip ci] Bump version to v9.1.1
- [`e98f9c8d`](https://github.com/oarepo/oarepo-ui/commit/e98f9c8d920d2398d7dc1eeea3446c49411ca175) override multiple options search bar on /search
- [`dc46c4d4`](https://github.com/oarepo/oarepo-ui/commit/dc46c4d4090047ffa1cd65b180d61229942ea5a9) fix: remove back/forward buttons
- [`91407f5c`](https://github.com/oarepo/oarepo-ui/commit/91407f5ce9e11de95c88ddeb5e06fe2423086206) [skip ci] Bump version to v9.1.0
- [`26f86553`](https://github.com/oarepo/oarepo-ui/commit/26f86553bacdf05cac33c240d3f77740f8dd4069) feat: append query params filter function
- [`4e6b9df3`](https://github.com/oarepo/oarepo-ui/commit/4e6b9df3e40cad7d235f81f0ff3fdbd9b74366de) passing embedded tag to detail page
- [`0597b131`](https://github.com/oarepo/oarepo-ui/commit/0597b131f016b8ee2640562c140f40d692e4aab0) fix: using vnd accept header inside of the form

#### `oarepo-workflows` 4.0.2
[4.0.0 → 4.0.2](https://github.com/oarepo/oarepo-workflows/compare/v4.0.0...v4.0.2)

- [`e0707877`](https://github.com/oarepo/oarepo-workflows/commit/e07078777eea5ff3a7fb0282e0eed974440062fb) fix: SameAs not working in policy (#52)
- [`0cf37c86`](https://github.com/oarepo/oarepo-workflows/commit/0cf37c861d4f48ddd3ace004d760a32a55623eef) [skip ci] Bump version to v4.0.1
- [`f6c27559`](https://github.com/oarepo/oarepo-workflows/commit/f6c2755962e5d490ec84e2deae3767e28828f44a) Fix workflow field to allow null values (#48)
- [`cd4aac0a`](https://github.com/oarepo/oarepo-workflows/commit/cd4aac0a397a3219aad46d32fd0f8a046e3ad4db) using CommentEvent as default for can_create_comment (#49)

---

## 2.0.1

Released: **April 19, 2026 at 11:12 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `ccmm-invenio` 1.1.2
[1.1.0 → 1.1.2](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.0...v1.1.2)

- [`2fdba40a`](https://github.com/nrp-cz/ccmm-invenio/commit/2fdba40adcbd0f9f07818faac65784e5ba876cdb) Version bump
- [`d8023ff0`](https://github.com/nrp-cz/ccmm-invenio/commit/d8023ff0d35a5437580696ed2f4f40f956c14f2a) [skip ci] Bump version to v1.1.1
- [`3c613d3c`](https://github.com/nrp-cz/ccmm-invenio/commit/3c613d3c97454092b1ea5a8d51bab50075e57134) added ui resource and config for ccmm specific repos (#22)

#### `invenio-accounts` 7.2.1
[7.1.0 → 7.2.1](https://github.com/inveniosoftware/invenio-accounts/compare/v7.1.0...v7.2.1)

- [`6e8d571e`](https://github.com/inveniosoftware/invenio-accounts/commit/6e8d571ef662ac3626cadd58eaee38737588384b) 📦 release: v7.2.1
- [`97c188de`](https://github.com/inveniosoftware/invenio-accounts/commit/97c188defa4b8ef33cd2f8867525ae56d238368c) Add missing `limits` dependency
- [`41cbd5ac`](https://github.com/inveniosoftware/invenio-accounts/commit/41cbd5ac972b86b7d77abcb7ed9e4e8de7f6dd2d) 📦 release: v7.2.0
- [`79ed7fc7`](https://github.com/inveniosoftware/invenio-accounts/commit/79ed7fc79c42790c53376fe02ca990c8bccfb3dd) feat(auth): add per-account auth rate limits

#### `invenio-app-rdm` 14.0.0b10.dev6+oarepo.2.ioyk53cm5eo4shpy
[14.0.0b9.dev0+oarepo.4.5zcr44vseq4mtvcx → 14.0.0b10.dev6+oarepo.2.ioyk53cm5eo4shpy](https://github.com/inveniosoftware/invenio-app-rdm/compare/v14.0.0b9.dev0...v14.0.0b10.dev6)

- [`71356bb9`](https://github.com/inveniosoftware/invenio-app-rdm/commit/71356bb95efe741ae5697a60a9fcca6a6d555c05) 📦 release: v14.0.0b10.dev6
- [`0ce4237c`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0ce4237c73da1ce0e7c31ba37d1ee532f3b89928) feat: use new RDMSubCommunity request class
- [`52cb4502`](https://github.com/inveniosoftware/invenio-app-rdm/commit/52cb45023bb6b9e8936e2265702a1f1c527b0aa7) fix(administration): set correct permissions for user dashboard
- [`8492fd1a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/8492fd1a0c6898c972904174e8595b9d22c33d96) 📦 release: v14.0.0b10.dev5
- [`53fe860e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/53fe860e070776ca799dd0607705424b67fc42c6) feat: add template for quota increase requests
- [`60385b4e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/60385b4e11722d014ecf5ed3d0eb3c3925e495bd) chore: deprecate FILES_REST in favour of RDM_FILES
- [`187b7c23`](https://github.com/inveniosoftware/invenio-app-rdm/commit/187b7c23b6b964af46aa37e0c2777a87913e5fd1) deposit: pass more information about quota to deposit form
- [`3ad3b661`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3ad3b66106a927235713a09ffa6362ed0abd27e2) assets: added override for progress bar
- [`a4f45578`](https://github.com/inveniosoftware/invenio-app-rdm/commit/a4f45578f8052ab85974b7b81d9469bc8c928cf5) deposit: calculate additional quota storage for user
- [`2c0d5495`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2c0d5495475f7bb0bef9e3d982b70ed11e6b5ae5) deposit: add evaluate_quota_increase
- [`764fe11b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/764fe11b70fde0389235fa7ee2a318b7e48b1706) fix: display of range input on Chrome
- [`2fde849b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2fde849b8a1a39efb35dad53928f3b272113435c) chore: refactor logic to rdm-records and improve user_quota msg
- [`d96bb730`](https://github.com/inveniosoftware/invenio-app-rdm/commit/d96bb7302beaf978169d76c466ebbbfe9f713b7b) release: v14.0.0b10.dev4
- [`3dd9701a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3dd9701ad1a8c88c8837eca6f0bec3bad99768c2) fix(tasks): correct collection task registration
- [`9cac6850`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9cac68505c0e356516529e889d55c82b72e41c7d) fix: collection logo size
- [`f46029c1`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f46029c1b88a2c319702ea7ed7cec1d701356eae) feat(communities-browse): show subcommunities section only if community allows
- [`58eaca06`](https://github.com/inveniosoftware/invenio-app-rdm/commit/58eaca0685d2cccd00ddf3d7a0d8a5d6a0e636e4) release: v14.0.0b10.dev3
- [`a0f34dba`](https://github.com/inveniosoftware/invenio-app-rdm/commit/a0f34dba7f1d095dc483db2b1e8449784e89d7fb) chore: run isort
- [`37e50bb9`](https://github.com/inveniosoftware/invenio-app-rdm/commit/37e50bb94a8c86ca17026ad2753bfd6b7a8ce490) release: v14.0.0b10.dev2
- [`61d2381b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/61d2381bb2ff6905d06a36f7763965896637c99d) fix(views-ui): fix wrong import for collections service
- [`918c447d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/918c447d051dcc4f178a45455128a502625e56d7) fix(views): set correct collections service reference
- [`4f616c15`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4f616c1596a91a63970dd720e5f8080ce90b0e20) release: v14.0.0b10.dev1
- [`1792a726`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1792a7260ce80e16b538ff94a53ed7f869d41f9b) release: v14.0.0b10.dev0
- [`26d9aa91`](https://github.com/inveniosoftware/invenio-app-rdm/commit/26d9aa91525c2f47eec10ae7073a03cd51e1629e) fix(RevisionsDiffViewer.js): Use better diff algo & diff from metadata
- [`bb6468d0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/bb6468d00da9ad678666f3180927411868fd6524) feat(audit_logs): Allow diff view for access audit logs
- [`6206c06d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/6206c06d0d4382ed2c3ca8c699c685a36c364d76) feat(manage): Add view audit logs option to manage menu
- [`8a66b4ef`](https://github.com/inveniosoftware/invenio-app-rdm/commit/8a66b4ef14af7bec41c0b548ec51f6d7d82b87b8) chore: upgrade major dependencies
- [`68dcde17`](https://github.com/inveniosoftware/invenio-app-rdm/commit/68dcde170dc7dcbb2053d68dbd7d84f716d85fdb) fix: detail url from the dashboard
- [`9d7c2153`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9d7c215325b47cf1846ca3748ba52e9ed58408cc) fix: templates for guest and user access
- [`1bdab2f1`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1bdab2f15b3ce42538165caabb19731e7c7f9712) fix: allow rendering request page without file permissions
- [`74312c0b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/74312c0b279f707e33bc8d3974bb25cd4defba20) ui(translations): addition to fix incorrect pluralization in react-invenio-forms
- [`fcc213f4`](https://github.com/inveniosoftware/invenio-app-rdm/commit/fcc213f44e44561bcc462bec52837504383bb668) feat(mshp-req): create user dashboard membership request discussion page [+]
- [`04a522c2`](https://github.com/inveniosoftware/invenio-app-rdm/commit/04a522c21d1940643ba50ef9c99cdfe341cfc0f2) refactor(invitation-req): user user_dashboard.html common to mbshp req
- [`1042d0a1`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1042d0a105343f6d8a198a4146665055bef84f99) feat(mshp-req): add icon to membership request in listing
- [`bbf0cd46`](https://github.com/inveniosoftware/invenio-app-rdm/commit/bbf0cd4610918a3f9b3f380d3545f40c3955be2b) tests: fixtures: OpenAIRE resource type consistent format
- [`5d152c2f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5d152c2f99f3a98015021846f00b456eafb1ca88) collections: update browse display rule
- [`7ce4da18`](https://github.com/inveniosoftware/invenio-app-rdm/commit/7ce4da18761a8606f720eef10a11fae6b58cbfde) fix(communities): update collections service call to use namespace_id
- [`611ccdf1`](https://github.com/inveniosoftware/invenio-app-rdm/commit/611ccdf1cd7dcbc3c887d222a8cfb4c8b9e3ddb1) collections: update conf variable to use COMMUNITIES_COLLECTIONS_ENABLED
- [`c508e478`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c508e478682a6f4e647356032149f0ad90985a9d) fix: fixed hacky pluralization of contributors
- [`8be8fa5f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/8be8fa5fecbfe8f01bf13cda88f8bcc84d556829) fix: typo in users with access
- [`66c59b27`](https://github.com/inveniosoftware/invenio-app-rdm/commit/66c59b27720e971063562a80cd2247dcbc886a26) AddUserGroupAccessModal: De-emphasize search by email
- [`e55c6b87`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e55c6b8781559c266cc3ef9be46f21ed2b927bf2) feat: compat with new invenio-vcs module
- [`123461c0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/123461c07d8f110234c4862adde67527aae45083) ui(translations): mark string as translatable
- [`0849e850`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0849e8503da02bb92630a76bacde16f867a0858d) refactor(MathJax): Pass elements to typesetPromise to optimize re-render
- [`d93b8e78`](https://github.com/inveniosoftware/invenio-app-rdm/commit/d93b8e7816fb346416b4450973e1fe1b7c2a485d) style: fix wide community logo in community selection and request metadata
- [`c46e4c8d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c46e4c8dd3e9fcec5ce04f7ff9b3f35611a51a41) fix(searchbar): wrap search icon in button element
- [`c02ec2bc`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c02ec2bc70945c19dee3ddec39e60a4f57f8083c) feat: add max-width to tombstone container
- [`72a5aea7`](https://github.com/inveniosoftware/invenio-app-rdm/commit/72a5aea73a26f260859a57481636478777b085cc) fix: using app locale for citations
- [`b6b878eb`](https://github.com/inveniosoftware/invenio-app-rdm/commit/b6b878ebd52ea05886d526e56f33a90458319c5e) Fix to display latex symbols correctly in homepage.
- [`c3b0fb38`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c3b0fb38829f816cc2b41ccb1aa5042af7f676a1) fix(file-preview): focus previewer when Preview button is clicked

#### `invenio-audit-logs` 2.0.0 💥
[1.1.0 → 2.0.0](https://github.com/inveniosoftware/invenio-audit-logs/compare/v1.1.0...v2.0.0)

- [`f6a96d4a`](https://github.com/inveniosoftware/invenio-audit-logs/commit/f6a96d4a2bcdb2f4be90db400117616ad1ab21b9) feat!: Add support for dynamic metadata schema validation per action
- [`e0ef59c9`](https://github.com/inveniosoftware/invenio-audit-logs/commit/e0ef59c9e173c6e0fcfbbf3a6aa820ebe6e760f3) refactor(results): Add global schema caching
- [`54c4ce65`](https://github.com/inveniosoftware/invenio-audit-logs/commit/54c4ce6529b12345ceb5d14d54437c20fde268ff) feat(config): Add config flag to disable actions as required
- [`292a1072`](https://github.com/inveniosoftware/invenio-audit-logs/commit/292a10727b824f9d42a14facbe7994631f708865) fix(mappings)!: define metadata as a flat_object instead of dynamic
- [`b9fb44d2`](https://github.com/inveniosoftware/invenio-audit-logs/commit/b9fb44d27ded5bcf070aaf0360adece63a4980be) refactor(tests): Insert nested metadata fields and test advance querying
- [`1376d8c9`](https://github.com/inveniosoftware/invenio-audit-logs/commit/1376d8c91e90377d0066c5ea193ac92f0331acea) 📦 release: v2.0.0

#### `invenio-checks` 8.1.0 💥
[7.0.0 → 8.1.0](https://github.com/inveniosoftware/invenio-checks/compare/v7.0.0...v8.1.0)

- [`e99b905a`](https://github.com/inveniosoftware/invenio-checks/commit/e99b905ae494532a701ce3d9482c088b74da591c) 📦 release: v8.1.0
- [`9aa76b6a`](https://github.com/inveniosoftware/invenio-checks/commit/9aa76b6a6caa98f05d77d7dad0a3136b6f03391d) feat: support metadata check error paths
- [`4d863311`](https://github.com/inveniosoftware/invenio-checks/commit/4d8633110a36dde2c79a2b67a83ee48ae9a1577e) chore: upgrade depenndencies
- [`f0b389d7`](https://github.com/inveniosoftware/invenio-checks/commit/f0b389d75794bbbd66186e63224fbd7e91f0b74e) release: v8.0.1
- [`0d50c561`](https://github.com/inveniosoftware/invenio-checks/commit/0d50c561c80bf87d8b0fc08ba779a533cf2742c3) chore(setup): bump major version of invenio-drafts-resources
- [`d502e957`](https://github.com/inveniosoftware/invenio-checks/commit/d502e95766d388fbfc886d494e38b3b27fe556d1) 📦 release: v8.0.0

#### `invenio-collections` 8.1.0 💥
[7.0.0 → 8.1.0](https://github.com/inveniosoftware/invenio-collections/compare/v7.0.0...v8.1.0)

- [`3e5f7374`](https://github.com/inveniosoftware/invenio-collections/commit/3e5f7374615f9d2d47671d678d37b48a7da944af) ext: abstract records_service dependency from CollectionsService
- [`05c108ae`](https://github.com/inveniosoftware/invenio-collections/commit/05c108aeed17f084606ebf0d33fe40be4a25160b) release: v8.1.0
- [`2b2db7c5`](https://github.com/inveniosoftware/invenio-collections/commit/2b2db7c50773096ffa9c2afd0b6c1c1f7d161cea) tests: fixtures: OpenAIRE resource type consistent format
- [`5e5b9a6b`](https://github.com/inveniosoftware/invenio-collections/commit/5e5b9a6bef9c76e5d8d9a0cbca8d781769059a1c) release: v8.0.2
- [`0febc494`](https://github.com/inveniosoftware/invenio-collections/commit/0febc4943deb98ea71e3fc8c2adcb3bf14ced4aa) translations: init translation mechanism related boilerplate
- [`9379a1a0`](https://github.com/inveniosoftware/invenio-collections/commit/9379a1a0290b6b3ebf3997739fffd43901b9681a) fix(translations): add package-lock.json
- [`b9ea3f3e`](https://github.com/inveniosoftware/invenio-collections/commit/b9ea3f3ee08717875a31b31c4e73887d804aa8a8) release: v8.0.1
- [`a15b38f7`](https://github.com/inveniosoftware/invenio-collections/commit/a15b38f74ffb5041eb5a8f750ddba10d9262482b) release: v8.0.0
- [`a51147db`](https://github.com/inveniosoftware/invenio-collections/commit/a51147db1bff6b26693adb4b540d4375228dccaa) collections: improve service and resource api
- [`20c66571`](https://github.com/inveniosoftware/invenio-collections/commit/20c66571d99d79ab884c4969c2176be789b795ff) collections: add reorder endpoint
- [`27cd3421`](https://github.com/inveniosoftware/invenio-collections/commit/27cd34216dd053993cea2d65d221d46a82682a10) collections: add limit for category and collections
- [`f84e8e9f`](https://github.com/inveniosoftware/invenio-collections/commit/f84e8e9f018fc998c90a0b3be553cc3edf14de44) feat(collections): add CRUD UI
- [`b30adba6`](https://github.com/inveniosoftware/invenio-collections/commit/b30adba66aa88a10326df4a996d2338f429bb03c) feat(collections): decouple from invenio-communities, rename community_id to namespace_id
- [`8738beb3`](https://github.com/inveniosoftware/invenio-collections/commit/8738beb379b95835be4b0bd291159aa23cff3588) ui: fixes and improvements
- [`aabd6897`](https://github.com/inveniosoftware/invenio-collections/commit/aabd68971f024eb851a2a4a33f3c71bc28e8e514) eslint: add eslint
- [`549f17fc`](https://github.com/inveniosoftware/invenio-collections/commit/549f17fcf0d49c1036b10fd932da6927434b649b) ui: improve CollectionTreeManager

#### `invenio-communities` 26.0.0+oarepo.1.qot6rqrpnjb6q5hz 💥
[25.0.0+oarepo.2.vefo4ebswlgllcyt → 26.0.0+oarepo.1.qot6rqrpnjb6q5hz](https://github.com/inveniosoftware/invenio-communities/compare/v25.0.0...v26.0.0)

- [`c05205b2`](https://github.com/inveniosoftware/invenio-communities/commit/c05205b21f5eba9eae4374774515cb5eaf6ad826) fix(collections): rename endpoint for community collections trees
- [`db9bb4a7`](https://github.com/inveniosoftware/invenio-communities/commit/db9bb4a73bfd13a240c0b823a2a090123555a958) release: v26.0.0
- [`2ddd597b`](https://github.com/inveniosoftware/invenio-communities/commit/2ddd597b52d8fca169b51c5fdd7d27869f7566b8) feat: adds collection CRUD ui
- [`80aebef8`](https://github.com/inveniosoftware/invenio-communities/commit/80aebef894e340302c030586c2291a47c0fec60e) collections: Rework the UI to match the browse page
- [`5d492ed1`](https://github.com/inveniosoftware/invenio-communities/commit/5d492ed123cb4723710249c65dd01ecda0c36961) collections: add limits to categories and collections
- [`2cb75d14`](https://github.com/inveniosoftware/invenio-communities/commit/2cb75d14c3bbc1f52cb04410d8aa303c1fe46306) collections: improve modals
- [`fd561e32`](https://github.com/inveniosoftware/invenio-communities/commit/fd561e320e03b050ca8592088a2538e3f286504d) collections: remove collections CRDU UI
- [`f4f8606e`](https://github.com/inveniosoftware/invenio-communities/commit/f4f8606e385da0a38520f67be2c7882fe78ad448) feat(communities): add CollectionsPermissionPolicy and support namespace_id in generators
- [`2543646d`](https://github.com/inveniosoftware/invenio-communities/commit/2543646dfea4c280a4ba61cf9468c6ad46a7970c) collections: add template for UI
- [`f9ce365c`](https://github.com/inveniosoftware/invenio-communities/commit/f9ce365c70236ffef9e69d30d28167bee78224a9) collections: add feature flag to enable/disable collections
- [`c94adef4`](https://github.com/inveniosoftware/invenio-communities/commit/c94adef44c37516b1211825f49f8e00c69933900) InvitationsModal: De-emphasize search by email
- [`696715d2`](https://github.com/inveniosoftware/invenio-communities/commit/696715d274274e7aa36b53bace77c624251c829f) feat(mshp-req): generate self_html link for MembershipRequest
- [`8af3d94b`](https://github.com/inveniosoftware/invenio-communities/commit/8af3d94b7daae1a4ea9e1ee0b4041607ea8b0fac) feat(mshp-req): extract and redirect to self_html of membership request on frontend
- [`eb5bdbae`](https://github.com/inveniosoftware/invenio-communities/commit/eb5bdbae978be96738dd062dd99ea25dade06574) chore(mshp-req): tweak cancel membership request test

#### `invenio-db` 2.5.0
[2.4.0 → 2.5.0](https://github.com/inveniosoftware/invenio-db/compare/v2.4.0...v2.5.0)

- [`7b5d5bef`](https://github.com/inveniosoftware/invenio-db/commit/7b5d5befe089903b8dac3e00603f8365700b8fd5) release: v2.5.0
- [`5d70596b`](https://github.com/inveniosoftware/invenio-db/commit/5d70596bd452d7fee2cccf66d11ba89595dfb1de) feat(alembic): safely create alembic_version table
- [`0f273f07`](https://github.com/inveniosoftware/invenio-db/commit/0f273f0758e09751b0ac419854a38d3b21ce5441) test: when the database is dropped all open connections in the pool get invalid.

#### `invenio-drafts-resources` 9.0.1+oarepo.1.p7573uc2mq3xg5se 💥
[8.0.1+oarepo.2.uurr6e2zpcxyzqrj → 9.0.1+oarepo.1.p7573uc2mq3xg5se](https://github.com/inveniosoftware/invenio-drafts-resources/compare/v8.0.1...v9.0.1)

- [`f682f49b`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/f682f49bc356f5a967f23325717497efe6ed6462) fix(request-context): provide fallback metadata for non-request ops
- [`d791047e`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/d791047e3cff1cdbc7458d7c4eb549e3ace9069f) release: v9.0.1
- [`1f44e5a7`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/1f44e5a7a1e56161f41317aacb70a9c274854e46) refactor(auditlog): Define metadata schema dynamically
- [`84e76f5a`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/84e76f5af395b3229d999ea9d284819282f73e7f) refactor(auditlog): Add parent_pid to draft actions
- [`ad7614e2`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/ad7614e2085051797be3e306e3460dbc26c0023a) refactor(auditlog): RequestContext using X-Forwarded-for & flask session
- [`37f7c8f9`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/37f7c8f94a8eb01bee33081cdbb5acfe63942b83) 📦 release: v9.0.0

#### `invenio-rdm-records` 28.3.1+oarepo.1.mwjq6wsqhds4s5ur 💥
[27.0.0+oarepo.3.3yojwri2nobgwy5x → 28.3.1+oarepo.1.mwjq6wsqhds4s5ur](https://github.com/inveniosoftware/invenio-rdm-records/compare/v27.0.0...v28.3.1)

- [`d6953573`](https://github.com/inveniosoftware/invenio-rdm-records/commit/d695357388d4bdcac1bdaf5956b4d8c39ea2c638) 📦 release: v28.3.1
- [`7bdb146c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7bdb146cff699a869bd10df32c6202ddb68313ac) fix: display DOI validation errors in deposit form
- [`0d8de532`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0d8de5320193e202a0aba598d7ce30eaef3cffc5) 📦 release: v28.3.0
- [`b03a860d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/b03a860d08cc1ad8d6a05e2433b6d1d9224d1dd2) feat: add new RDMSubCommunity request class
- [`50934b84`](https://github.com/inveniosoftware/invenio-rdm-records/commit/50934b84a213baa0b94c4a0fc8c4fd4be6783a93) fix: remove duplicate definition of collections service proxy
- [`afc9603d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/afc9603d04bf4cd4fceddae5d984e156ccbf3873) 📦 release: v28.2.0
- [`5f89c158`](https://github.com/inveniosoftware/invenio-rdm-records/commit/5f89c158c3a8ee04eb77cdf71e1f411519f816cb) chore: formatting and pydocstyle
- [`92f6275b`](https://github.com/inveniosoftware/invenio-rdm-records/commit/92f6275b88187c275bfa84a8813adf9becf18b0c) fix: quota increase missing values in storage service
- [`f96fdb67`](https://github.com/inveniosoftware/invenio-rdm-records/commit/f96fdb6766191e1707d43e9c5b96f304690b9bf4) fix: verify quota increase in policy
- [`f7581121`](https://github.com/inveniosoftware/invenio-rdm-records/commit/f7581121ddef3539abb642e6cf2984b5665c3a39) chore: deprecate FILES_REST in favour of RDM_FILES
- [`a3a578ec`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a3a578ec80345fcfca8169f635cba387c53c6d4e) fix: use real quota info rather than hardcoded numbers
- [`35e8cbb3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/35e8cbb31459dd0c8d142c5e6d1ab6683964fb29) chore: refactor logic to only be in storage service
- [`75655588`](https://github.com/inveniosoftware/invenio-rdm-records/commit/75655588ab609b7bdd0047c77427534517b552b2) feat(storage-quota): settings integration
- [`ba68279b`](https://github.com/inveniosoftware/invenio-rdm-records/commit/ba68279be1b0c494ca4c0207ad4f72a1954af79b) assets: added template and component for storage settings
- [`e73a890b`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e73a890bc4033c071086759bb6b6d885d8aae238) feat: add deposit form quota manager
- [`a7abee9a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a7abee9a83b3d803b9ef630dc48bab1790311af0) feat(backend): add quota increase request backend
- [`9285c57c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/9285c57c28d2412aa778fe8602825448eb0dca43) fix: switch to accordion data-label
- [`a9d5d39a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a9d5d39aa7636a8496b1efda8a48d2cb8cc9c1a3) release: v28.1.0
- [`153ef385`](https://github.com/inveniosoftware/invenio-rdm-records/commit/153ef38502ab9ba0c5660b5ca8cb85abdbcea0bc) release: v28.0.0
- [`e30022f3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e30022f3961ba9d80b121112d5a4e79860eac3e0) fix: user access request routing
- [`a55e23a9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a55e23a931d3dd1c071cc911b38cb89396444e03) feat(community-records-collections): initialize and wire CollectionsService with community_records_service
- [`83a35857`](https://github.com/inveniosoftware/invenio-rdm-records/commit/83a358571f357b20486a837f92b021e68f479198) chore: upgrade invenio-communities
- [`6e332772`](https://github.com/inveniosoftware/invenio-rdm-records/commit/6e3327720abd271ed4222deea9ebdcb64b2d38d4) fix(tests): enable community collections
- [`77c3517e`](https://github.com/inveniosoftware/invenio-rdm-records/commit/77c3517e84b152c1e5b85d9f6c70227ae3e3689d) fix(file-modification): consider `can_modify_locked_files` permission
- [`2f13cee9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/2f13cee9cc5fb1aec347b42f92a412eb73ace7a3) change(setup): set version of VCS
- [`4d5e116c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/4d5e116c10a80412bb9f7ef8367fb9e18a7a3ee7) feat(auditlog): Add audit logs for share access
- [`974df7e5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/974df7e556492fa846559b3e0da90602f8ab69f3) vocabs: update resource_types to datacite 4.7
- [`13d34650`](https://github.com/inveniosoftware/invenio-rdm-records/commit/13d3465082d832bc7c1c58c05280e5dd16bd7ebd) vocabs: add resource_types for datacite 4.5
- [`66df87d3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/66df87d36e893432ee3cbe6eff29a9ab7c0bbbf8) tests: sync tests resource_types
- [`ab422ea3`](https://github.com/inveniosoftware/invenio-rdm-records/commit/ab422ea38a824e2807aa3f64c920a0ba8757b8a9) resource_types: fix OpenAIRE resource type for computational notebook
- [`90a2be5a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/90a2be5a019e6daaf86d2c0801f9bfab4568b836) tests: fixtures: OpenAIRE resource type consistent format
- [`32dfa41e`](https://github.com/inveniosoftware/invenio-rdm-records/commit/32dfa41e59e7b3d044b01a7838813bca74c207d2) ui(translations): mark strings as translatable
- [`042d10ae`](https://github.com/inveniosoftware/invenio-rdm-records/commit/042d10ae9ee57380e4b4993876b765a973cd6ab6) vocabularies: add datacite 4.6 relation types
- [`6f65df62`](https://github.com/inveniosoftware/invenio-rdm-records/commit/6f65df62f77d35f2296016e739889476418eedea) vocabularies: add datacite 4.6 date types
- [`bd245f38`](https://github.com/inveniosoftware/invenio-rdm-records/commit/bd245f38309c6bd224d24a125b855ca1d67c7d57) vocabularies: add datacite 4.7 relationType
- [`0c38e7bf`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0c38e7bf6a172aa0229ee8777779188ea32aab68) identifiers: add cstr and rrid as supported identitifier types
- [`14a0afc4`](https://github.com/inveniosoftware/invenio-rdm-records/commit/14a0afc405c79777a568532fabdb0d8df703529d) feat(vcs): support for new VCS integration (backend)
- [`33446aac`](https://github.com/inveniosoftware/invenio-rdm-records/commit/33446aac9e483782df73a1870f0470c0f84c1973) feat(vcs): support for new VCS integration (frontend)
- [`685824c5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/685824c59034604b00df3c0416e08efe9713e988) ui(translations): mark message as translatable
- [`65315be7`](https://github.com/inveniosoftware/invenio-rdm-records/commit/65315be7dc092001ce09f08bd2259d3c1f56b858) ui(translations): mark strings as translatable

#### `invenio-records-resources` 9.3.0+oarepo.1.zcunkj5manhukyog
[9.1.0+oarepo.4.ojib3jsuu4wnrkln → 9.3.0+oarepo.1.zcunkj5manhukyog](https://github.com/inveniosoftware/invenio-records-resources/compare/v9.1.0...v9.3.0)

- [`a285b12a`](https://github.com/inveniosoftware/invenio-records-resources/commit/a285b12a199bc96ad60992a7a954993710521ef6) 📦 release: v9.3.0
- [`279dd568`](https://github.com/inveniosoftware/invenio-records-resources/commit/279dd568ce5bc67549f39f75b88a775223cfd673) feat(facets): add hard_bounds and dynamic bounds to DateFacet
- [`e8f2d65c`](https://github.com/inveniosoftware/invenio-records-resources/commit/e8f2d65cbd7afb2d86e2c19d7a3ad3e13c2e2f2d) feat(facets): add Facet base class with post_filter and prepare_aggregation
- [`8b7ad35a`](https://github.com/inveniosoftware/invenio-records-resources/commit/8b7ad35a68b48145ba8059dc0b5c365d59560a01) feat: set anchor for EndpointLink dynamically
- [`fc98a3f7`](https://github.com/inveniosoftware/invenio-records-resources/commit/fc98a3f70dec286675f71c8c94b8496312df39a5) :package: release: v9.2.0
- [`6b6da941`](https://github.com/inveniosoftware/invenio-records-resources/commit/6b6da941702c9072e9e6786768a3582956365595) ui(translations): mark string as translatable
- [`1a772dd1`](https://github.com/inveniosoftware/invenio-records-resources/commit/1a772dd198dcf474948f627613a541f0f3328c38) factories: add "search_alias" for index field

#### `invenio-requests` 12.6.0+oarepo.1.gof4prsfnzoqgasf
[12.3.1+oarepo.2.6uloldct77ahzc5b → 12.6.0+oarepo.1.gof4prsfnzoqgasf](https://github.com/inveniosoftware/invenio-requests/compare/v12.3.1...v12.6.0)

- [`adc4bacb`](https://github.com/inveniosoftware/invenio-requests/commit/adc4bacb3dbfbccc79f0dfbffde67430177f8e7e) 📦 release: v12.6.0
- [`8f8a436c`](https://github.com/inveniosoftware/invenio-requests/commit/8f8a436c6190aaca410d0b29b6ad7a8099cbdcaa) labels: add quota increase label
- [`345fb594`](https://github.com/inveniosoftware/invenio-requests/commit/345fb594303de21efeebbeaa41f8ec60681dacdb) 📦 release: v12.5.2
- [`8c6708a7`](https://github.com/inveniosoftware/invenio-requests/commit/8c6708a78d8e2423a9727a5c538583d077414d12) fix: only render super when using dashboard base template
- [`6ea1ce6f`](https://github.com/inveniosoftware/invenio-requests/commit/6ea1ce6f951a3cba5ea30c554bd576f11241244c) fix(links): set anchor only if Endpointlink supports it
- [`89585f52`](https://github.com/inveniosoftware/invenio-requests/commit/89585f5223810cdd5f32c7f679bf1c26fbb9406e) release: v12.5.1
- [`d4c287dc`](https://github.com/inveniosoftware/invenio-requests/commit/d4c287dc421f316221f06e064b095f7f2357706d) feat: RequestTypeDependentEndpointLink dynamically assigns anchor
- [`392ff501`](https://github.com/inveniosoftware/invenio-requests/commit/392ff50176ca4518deec7f5f3f7d763c0eca3996) :package: release: v12.5.0
- [`fcd2a9f7`](https://github.com/inveniosoftware/invenio-requests/commit/fcd2a9f7e0a4ef9a4e986f7f128aba1715ba9823) fix(docstring): typo
- [`38888f97`](https://github.com/inveniosoftware/invenio-requests/commit/38888f9758d5fcd6867b62c884f0035fa89b39e8) release: v12.4.0
- [`b7de89ab`](https://github.com/inveniosoftware/invenio-requests/commit/b7de89ab2496c357d6645e9705539126f1109c35) ui(translations): mark action values as translatable
- [`b86dac0a`](https://github.com/inveniosoftware/invenio-requests/commit/b86dac0a7186ecf9edc8a3205f68dee567d9bc34) formatting: fix formatting
- [`c96bcbc0`](https://github.com/inveniosoftware/invenio-requests/commit/c96bcbc0a34cd1fdf0f0342e51f75b450b9e0ce2) fix(TimelineEventBody): For each comment, render mathjax only for itself
- [`83bde011`](https://github.com/inveniosoftware/invenio-requests/commit/83bde01133d03d763b2b6a927f54577ed943ca9e) fix: wide community logo in request metadata
- [`fc3739af`](https://github.com/inveniosoftware/invenio-requests/commit/fc3739af9e8a9b62e071055299146619b87117e6) fix: event entrypoint incorrectly pointed to request type registry
- [`d772c9e8`](https://github.com/inveniosoftware/invenio-requests/commit/d772c9e84b7b21f14416f3d623bb889ce2f30a9d) chore: replace usage of Link by EndpointLink
- [`1d8b37bd`](https://github.com/inveniosoftware/invenio-requests/commit/1d8b37bd7326460dbbbd2eb049e7d71b98961617) fix: add missing alembic script

#### `invenio-search-ui` 4.2.1
[4.2.0 → 4.2.1](https://github.com/inveniosoftware/invenio-search-ui/compare/v4.2.0...v4.2.1)

- [`484625c2`](https://github.com/inveniosoftware/invenio-search-ui/commit/484625c218e9627d15aa27276a43a78d8d4635e6) 📦 release: v4.2.1
- [`12560aaf`](https://github.com/inveniosoftware/invenio-search-ui/commit/12560aaf3976174cde63d6fc8692b19cadb8614b) fix(facets): order date facet filter options by duration
- [`2eee606e`](https://github.com/inveniosoftware/invenio-search-ui/commit/2eee606ebd7082266201fd4af24161c6850fb25a) chore(setup): bump dependencies
- [`9732ca3f`](https://github.com/inveniosoftware/invenio-search-ui/commit/9732ca3f7e3e8005ad744f39170143212a752c32) build(deps-dev): bump minimatch

#### `invenio-users-resources` 10.4.1
[10.4.0 → 10.4.1](https://github.com/inveniosoftware/invenio-users-resources/compare/v10.4.0...v10.4.1)

- [`cc81a865`](https://github.com/inveniosoftware/invenio-users-resources/commit/cc81a86567c4efc161b63650a15426180b3ea861) fix(resolve): handle None given as user_id
- [`e6f4ac30`](https://github.com/inveniosoftware/invenio-users-resources/commit/e6f4ac3082b593f7bddbabbc76f2e1298b430acd) release: v10.4.1

#### `oarepo-app` 2.0.0 💥
0.0.1 → 2.0.0


#### `oarepo-communities` 8.0.0 💥
[7.0.1 → 8.0.0](https://github.com/oarepo/oarepo-communities/compare/v7.0.1...v8.0.0)

- [`9ccc6576`](https://github.com/oarepo/oarepo-communities/commit/9ccc657654b31f21adc99453cb47c6236ee06316) chore: release train for new major version of oarepo
- [`b048cc39`](https://github.com/oarepo/oarepo-communities/commit/b048cc39afea7680b4f450f408f3ddc6d7835220) [skip ci] Bump version to v7.0.1

#### `oarepo-dashboard` 4.0.0 💥
[3.0.0 → 4.0.0](https://github.com/oarepo/oarepo-dashboard/compare/v3.0.0...v4.0.0)

- [`ee8d4274`](https://github.com/oarepo/oarepo-dashboard/commit/ee8d42743b50af016d8ed8840b9e89e622942161) Major bump induced by invenio-rdm-records major bump

#### `oarepo-model` 2.0.0 💥
[1.0.1 → 2.0.0](https://github.com/oarepo/oarepo-model/compare/v1.0.1...v2.0.0)

- [`df3f9da1`](https://github.com/oarepo/oarepo-model/commit/df3f9da1e3474c051514a6b2a14b665af8089b77) major bump (#105)
- [`c3f57b0d`](https://github.com/oarepo/oarepo-model/commit/c3f57b0d2632c46a1f6eb2946cd00e8b2321b1d4) [skip ci] Bump version to v1.0.1

#### `oarepo-oidc-einfra` 4.0.0 💥
[3.0.1 → 4.0.0](https://github.com/oarepo/oarepo-oidc-einfra/compare/v3.0.1...v4.0.0)

- [`08220371`](https://github.com/oarepo/oarepo-oidc-einfra/commit/0822037128bde93097f247874826874ee9699a5b) Bump to v4.0.0 - Major release (#39)
- [`f9574b9a`](https://github.com/oarepo/oarepo-oidc-einfra/commit/f9574b9a6da9f788e4572438ab90290ec18532e2) [skip ci] Bump version to v3.0.1

#### `oarepo-rdm` 3.0.0 💥
[2.0.0 → 3.0.0](https://github.com/oarepo/oarepo-rdm/compare/v2.0.0...v3.0.0)

- [`b5cee971`](https://github.com/oarepo/oarepo-rdm/commit/b5cee9717cd33f4f6dd770e91e14ac31c054ce00) chore: bump version to 3.0.0 and update dependencies

#### `oarepo-requests` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/oarepo/oarepo-requests/compare/v4.0.0...v5.0.0)

- [`7ffddf4e`](https://github.com/oarepo/oarepo-requests/commit/7ffddf4ebfd8f6415cebabe9632c1332a666d40e) chore: release train for new major version of oarepo (#183)

#### `oarepo-runtime` 4.0.0 💥
[3.0.1 → 4.0.0](https://github.com/oarepo/oarepo-runtime/compare/v3.0.1...v4.0.0)

- [`9606f66e`](https://github.com/oarepo/oarepo-runtime/commit/9606f66e3f953f6e1c6c7b8eaad4c2f9e9f40085) major version bump
- [`c379235f`](https://github.com/oarepo/oarepo-runtime/commit/c379235f30dcf5a6ffc954f1291f178fc3698ecc) not using external in invenio_url_for
- [`bd3aeb4c`](https://github.com/oarepo/oarepo-runtime/commit/bd3aeb4cba093a93a7f5fcece385d9635cc7f38f) added tests
- [`0237c6a8`](https://github.com/oarepo/oarepo-runtime/commit/0237c6a877fdb25537519ee592e4930165d0f5f5) [skip ci] Bump version to v3.0.1

#### `oarepo-theme` 3.0.0 💥
[2.0.0 → 3.0.0](https://github.com/oarepo/oarepo-theme/compare/v2.0.0...v3.0.0)

- [`fd6e0f85`](https://github.com/oarepo/oarepo-theme/commit/fd6e0f8546eb5c1fa2ba3f798368b0db3df09e6e) major version bump

#### `oarepo-ui` 9.0.0 💥
[8.0.0 → 9.0.0](https://github.com/oarepo/oarepo-ui/compare/v8.0.0...v9.0.0)

- [`26799aa3`](https://github.com/oarepo/oarepo-ui/commit/26799aa3ff935b367bcb21f24dbcd9b605062666) major version bump (#440)
- [`6cb29f2c`](https://github.com/oarepo/oarepo-ui/commit/6cb29f2c079ea37ff1310afadec5b8f132169d0b) [skip ci] Bump version to v8.0.2
- [`1abf1a2e`](https://github.com/oarepo/oarepo-ui/commit/1abf1a2e19ae8314e67135ac5059b06709008aab) Remove unused workflows extra to fix circular dependency
- [`a8ce5762`](https://github.com/oarepo/oarepo-ui/commit/a8ce5762a25c88f910a91cf0f92f0d0708ae70c3) [skip ci] Bump version to v8.0.1
- [`5bbc7a59`](https://github.com/oarepo/oarepo-ui/commit/5bbc7a5975a8c425e87ef5a8413f8d7fb6b4ce2e) skip to main appears sometimes in header when you use tab to navigate
- [`4d879c90`](https://github.com/oarepo/oarepo-ui/commit/4d879c908dbe9f569045e439de3b5827b2a610a6) html5backend
- [`749361d1`](https://github.com/oarepo/oarepo-ui/commit/749361d1f571072c409fcf577f3a4beacf3026b4) fix: added better namespacing for panel extra content

#### `oarepo-vocabularies` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/oarepo/oarepo-vocabularies/compare/v4.0.0...v5.0.0)

- [`8f728620`](https://github.com/oarepo/oarepo-vocabularies/commit/8f7286207d3ad4e77167fb471b5148e9cbaed458) Bump version to 5.0.0 and update dependencies for compatibility

#### `oarepo-workflows` 4.0.0 💥
[3.0.0 → 4.0.0](https://github.com/oarepo/oarepo-workflows/compare/v3.0.0...v4.0.0)

- [`9781836e`](https://github.com/oarepo/oarepo-workflows/commit/9781836e6daba6a3ad62b6658f02cbed35d9d5af) chore: release train for new major version of oarepo

---

## 1.0.0

Released: **April 7, 2026 at 08:32 UTC**

> ⚠️ This release contains **breaking changes** — packages marked with 💥 have had a major version bump.

### Updated packages

#### `ccmm-invenio` 1.1.0
[1.1.0a13 → 1.1.0](https://github.com/nrp-cz/ccmm-invenio/compare/v1.1.0a13...v1.1.0)

- [`b30c2d2e`](https://github.com/nrp-cz/ccmm-invenio/commit/b30c2d2e5727c5274ac6c588fbecae9497981072) Version bump to 1.0.0
- [`6971c392`](https://github.com/nrp-cz/ccmm-invenio/commit/6971c3923b44ae3721aee9b36e628d1c5a4853e7) [skip ci] Bump version to 1.1.0a13

#### `invenio-access` 5.1.0 💥
[4.2.1 → 5.1.0](https://github.com/inveniosoftware/invenio-access/compare/v4.2.1...v5.1.0)

- [`c0ba387e`](https://github.com/inveniosoftware/invenio-access/commit/c0ba387e0b558feacdcd27b80849f1a142e36ceb) release: v5.1.0
- [`0327aecc`](https://github.com/inveniosoftware/invenio-access/commit/0327aeccd356ca1c573bce57653014a976fb404b) fix: change role.name to role.id
- [`d3679f95`](https://github.com/inveniosoftware/invenio-access/commit/d3679f9551f215b0f2cef1267370d4ee2a2c3246) chore(setup): bump dependencies
- [`78a619be`](https://github.com/inveniosoftware/invenio-access/commit/78a619beb6afb4f819634d7dd36532357644ac8a) chore(black): update formatting to >= 26.0
- [`fc81d300`](https://github.com/inveniosoftware/invenio-access/commit/fc81d3005674e59791e7e54598420da752d1e034) release: v5.0.0

#### `invenio-accounts` 7.1.0 💥
[6.2.2 → 7.1.0](https://github.com/inveniosoftware/invenio-accounts/compare/v6.2.2...v7.1.0)

- [`cf24fa04`](https://github.com/inveniosoftware/invenio-accounts/commit/cf24fa04e963566edc8619d22b7e1913ef258b15) chore: remove usage of python2 compat
- [`921a0dd0`](https://github.com/inveniosoftware/invenio-accounts/commit/921a0dd0121f9ac589dab3f11a1ec30d8c349357) chore: compatibility webargs > 6.0.0
- [`9e8fe3a7`](https://github.com/inveniosoftware/invenio-accounts/commit/9e8fe3a73d02e885debdd7e9926c3f5fcc88614b) release: v7.1.0
- [`3c943cad`](https://github.com/inveniosoftware/invenio-accounts/commit/3c943cad1359af797428749c3c2eb01acbfe4773) fix(cli): rollback failed db calls
- [`e2473822`](https://github.com/inveniosoftware/invenio-accounts/commit/e2473822a4e8c356b8cf2a8e20a6f4d28c0e5f0a) fix(chore): DeprecationWarning stdlib
- [`a0fd0211`](https://github.com/inveniosoftware/invenio-accounts/commit/a0fd02114ed5ca5c2712958f1a898aa40f401cac) fix: DeprecationWarning: get_user
- [`c7080d24`](https://github.com/inveniosoftware/invenio-accounts/commit/c7080d246c2a387f46512a1c07ea946282f9ed94) chore(setup): bump dependencies
- [`f97e700f`](https://github.com/inveniosoftware/invenio-accounts/commit/f97e700fe63807906398ca093e4cc497e3134b4d) release: v7.0.0
- [`a683cb39`](https://github.com/inveniosoftware/invenio-accounts/commit/a683cb397b5a6b696c11ce1bef233795a77865d8) chore(setup): pin dependencies
- [`a8cffbcb`](https://github.com/inveniosoftware/invenio-accounts/commit/a8cffbcba790c77e4e15d4e845e22b9854432dee) chore(black): update formatting to >= 26.0
- [`91e749d9`](https://github.com/inveniosoftware/invenio-accounts/commit/91e749d914feec6bb36c7081f99f4c862c83b421) release: v6.2.3

#### `invenio-administration` 5.2.0+oarepo.2.zuwubmhg2iyj3cll 💥
[4.3.2.47635988 → 5.2.0+oarepo.2.zuwubmhg2iyj3cll](https://github.com/inveniosoftware/invenio-administration/compare/v4.3.2...v5.2.0)

- [`58b9d35e`](https://github.com/inveniosoftware/invenio-administration/commit/58b9d35e5647fcf8ea31821d3d3e12128f36f950) release: v5.2.0
- [`7eb5a498`](https://github.com/inveniosoftware/invenio-administration/commit/7eb5a498df23e7f97a6129531de652e2a638f42e) permissions: keep backwards compat for users with administration-access only
- [`e046e4a3`](https://github.com/inveniosoftware/invenio-administration/commit/e046e4a347c2db66847672f79d7a89f3eda96165) feat(menu): add conditional visibility control for menu items
- [`2ebd5ba0`](https://github.com/inveniosoftware/invenio-administration/commit/2ebd5ba01652e7a71859c240558495f00f745dd9) permissions: add new permission to control administration menu
- [`01cc5fe9`](https://github.com/inveniosoftware/invenio-administration/commit/01cc5fe9aed858958d35fd8f395028b3f00cfbec) permissions: add get_permission() for menu visibility control
- [`814cd5dc`](https://github.com/inveniosoftware/invenio-administration/commit/814cd5dc2da2d765e10167f1a80e33373d27c1f6) release: v5.1.1
- [`88ba080b`](https://github.com/inveniosoftware/invenio-administration/commit/88ba080b17ceb0fca19334bc854f9e908607d4a9) fields: allow to pass type in form config
- [`828a73e6`](https://github.com/inveniosoftware/invenio-administration/commit/828a73e61ce1b01e43652a1650316c4a1e6cfa35) feat: add range facets for date aggregations
- [`cd83efb6`](https://github.com/inveniosoftware/invenio-administration/commit/cd83efb6e204453ea62297dd5a7833b11c826940) release: v5.1.0
- [`9d75c900`](https://github.com/inveniosoftware/invenio-administration/commit/9d75c900667fd3db16ee49108cfe293502d852d6) chore(setup): bump dependencies
- [`a06f308e`](https://github.com/inveniosoftware/invenio-administration/commit/a06f308e542c9fa9bdef7ea69a756139a2a44382) chore(black): update formatting to >= 26.0
- [`c938e40a`](https://github.com/inveniosoftware/invenio-administration/commit/c938e40aaed9690200377097c53404b15f104f20) release: v5.0.0
- [`48e36e14`](https://github.com/inveniosoftware/invenio-administration/commit/48e36e142afcc902a0221d03eb1d4b6861ae70ca) feat: integrate administration endpoints to invenio_url_for
- [`50cdd6a7`](https://github.com/inveniosoftware/invenio-administration/commit/50cdd6a77ce14ac254e2f078120eb401bcf76dbc) :package: release: v4.4.0
- [`12d5d650`](https://github.com/inveniosoftware/invenio-administration/commit/12d5d6502602acb020cf2eea5c123a5e362ed1e5) fix(ui): transpile error

#### `invenio-app` 3.0.0 💥
[2.3.0 → 3.0.0](https://github.com/inveniosoftware/invenio-app/compare/v2.3.0...v3.0.0)

- [`8f12b875`](https://github.com/inveniosoftware/invenio-app/commit/8f12b875c30d049972d45bf931434e0b0f738ef4) chore(setup): bump dependencies
- [`153dedab`](https://github.com/inveniosoftware/invenio-app/commit/153dedaba084d8b55ce98dfe5a6f003edd061e90) release: v3.0.0
- [`56246e0c`](https://github.com/inveniosoftware/invenio-app/commit/56246e0c8e3b2a0f7f47c6610ba4a8169834c41a) tests: extend support to Python 3.14

#### `invenio-app-rdm` 14.0.0b9.dev0+oarepo.4.5zcr44vseq4mtvcx
[14.0.0.98925620b3.dev6 → 14.0.0b9.dev0+oarepo.4.5zcr44vseq4mtvcx](https://github.com/inveniosoftware/invenio-app-rdm/compare/v14.0.0b3.dev6...v14.0.0b9.dev0)

- [`747d40a7`](https://github.com/inveniosoftware/invenio-app-rdm/commit/747d40a783f4635c4a844d15078ec8dde6c9b962) change(setup): upgrade collections, rdm-records and checks
- [`9e0b8108`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9e0b81083aa4a166e93843b5b96966e938f78d83) release: v14.0.0b9.dev0
- [`b8d5f016`](https://github.com/inveniosoftware/invenio-app-rdm/commit/b8d5f01679e3ca46bedcc5cc3b6d057b0f55d9c1) release: v14.0.0b8.dev0
- [`26797cb6`](https://github.com/inveniosoftware/invenio-app-rdm/commit/26797cb67f2bda7e38a663a5dcc422a412f27c24) macros: fix vocabulary custom field search value on landing page
- [`655befec`](https://github.com/inveniosoftware/invenio-app-rdm/commit/655befecfc7b808fee016163451a9c36c27ddd5f) release: v14.0.0b7.dev1
- [`53011dfc`](https://github.com/inveniosoftware/invenio-app-rdm/commit/53011dfcadd014844d9e12fb01a60c31224b0384) change(setup): upgrade invenio-dependencies
- [`14adf394`](https://github.com/inveniosoftware/invenio-app-rdm/commit/14adf3944c4c2fbad4c7136cbf4b670112a3f9e8) release: v14.0.0b7.dev0
- [`be2dcb18`](https://github.com/inveniosoftware/invenio-app-rdm/commit/be2dcb18b9e2279f57b1bdb29e27a5b1dac4ce06) fix(ui): group publishing information fields into Journal/Imprint/Thesis sections
- [`b9ef2c98`](https://github.com/inveniosoftware/invenio-app-rdm/commit/b9ef2c98f13fc1c64dc39fae0e8e869ebe26885e) feat: add remove_community_from_record permission check
- [`229c5450`](https://github.com/inveniosoftware/invenio-app-rdm/commit/229c5450504363114450b75b3cf1b2a93b6896c8) docs: fix broken coverage badge in README
- [`7d47b28f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/7d47b28f187ee2e7789ff9a6af667fa82faef294) docs: remove broken coverage badge
- [`5a535525`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5a53552540786fd35d76a523ebeb254d8f8aafb3) change(setup): major upgrade invenio packages
- [`a61f155b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/a61f155b46999f62c324fb0d95cf998c8a2a628a) release: 14.0.0b6.dev0
- [`e68889ac`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e68889ace17ada9844f5a87069bdc06e95222e0f) fix: form accordion label
- [`5e09887d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5e09887d8598450e52df88105fb8a92f7ddae75a) fix(doi link): rely on API links to display correct DOI link per record version
- [`1be91373`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1be91373ce5b403243474ddec0c0e624b1b9c48e) fix(upgrade_scripts): Ignore deleted drafts
- [`f1400981`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f1400981d4048de5a5902b12c6d1b5b77ddf0ef1) 📦 release: v14.0.0b5.dev6
- [`73e6b12b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/73e6b12b4f48683ded0d2d2cab485467db21499e) fix(requests): reload preview iframe when opening record tab
- [`f9d75adc`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f9d75adc444d393f83cf4b5c168cf09890aafd21) fix(ui): use preset variable to set icon height
- [`731e3213`](https://github.com/inveniosoftware/invenio-app-rdm/commit/731e3213b5e2d4649771f3a0dcf95500d2a0a684) fix(ui): change padding for children facets in accordion
- [`14d17a46`](https://github.com/inveniosoftware/invenio-app-rdm/commit/14d17a46242dbfefcaacf6bd8cfb63b75e53580f) chore(deps-dev): bump minimatch
- [`20bb0c96`](https://github.com/inveniosoftware/invenio-app-rdm/commit/20bb0c96a75efad033851a0db66859d006272139) release: v14.0.0b5.dev5
- [`1894b69c`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1894b69c465c8eb9ed796b7fd4eb74de436a5f10) fix(record-detail): render access status as safe HTML
- [`c9f5b253`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c9f5b2538d2db585295cb791bd0b74b0c71c33fe) fix: add record files restriction option to enable cache-control header
- [`f64aefe8`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f64aefe8dfa029329d09258b4948a6da40ee0d62) fix(pending-communities): use self_html link instead of adding /me manually
- [`00770ae9`](https://github.com/inveniosoftware/invenio-app-rdm/commit/00770ae917ff18bc20c11ba011a80961e217ec35) chore(deps-dev): bump lodash
- [`fd0ed3a4`](https://github.com/inveniosoftware/invenio-app-rdm/commit/fd0ed3a473c54ba8e380ddac6f0f2ff8ac899702) fix(config): remove value for the deprecated WSGI_PROXIES variable
- [`e5afec45`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e5afec45c5160d44eb761c695d4b4f939d2d9d4f) release: v14.0.0b5.dev4
- [`359e8b8d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/359e8b8d4ad14be2ce291f41a9e6bf8094c9ba28) fix(db): use UTC for Postgres
- [`9206b5d8`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9206b5d8c821decb33bfd7d87accddbbe569cee5) style: aria-disabled button
- [`7c3ce598`](https://github.com/inveniosoftware/invenio-app-rdm/commit/7c3ce59847d63f7ccf2dfbf1f3536407cb0e75aa) fix: limit max width of community logo
- [`85e48ab9`](https://github.com/inveniosoftware/invenio-app-rdm/commit/85e48ab9a5af26287e71b50fe4df85974009318c) fix(administration-user-access): user permission based ACL
- [`e85a6b22`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e85a6b22475702430910a6a2bee05ec8b5dc37fa) feat(comment-file): limit display width of user uploaded images
- [`c99d6951`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c99d69517f1849df8ca16ff4615ad52b00e8ec11) fix(css): allow horizontal scrolling for request comment body
- [`1e19015a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/1e19015ac15dae33c5cb84d0175d63f9ab0cf525) 📦 release: v14.0.0b5.dev3
- [`50507a8a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/50507a8a1ddfff2e7903e1b4fad9cc8526630f1c) feat(facets): register overriden range facet element as default
- [`24847d1b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/24847d1b5d14070aa8554a2df7646e706acb1fd6) 📦 release: v14.0.0b5.dev2
- [`ee39c88d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ee39c88d0a4a166d12a228f4b9670eeb0b754692) feat(roles): add administration views for role management
- [`3f765b9e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3f765b9e5b10e6b6b27a1faf229990088ad518ff) Improve German translation of search help page
- [`3e0980b6`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3e0980b674592f8880792b31a9ed07d1c7217328) Add German translations for statistics and versioning help pages
- [`8bee47a0`](https://github.com/inveniosoftware/invenio-app-rdm/commit/8bee47a034581fd9005da49d1374dddb6c4f06f2) help pages: Fixed header levels in search guide
- [`5893048f`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5893048f7fad24f30902c70540bd7507767bd136) help pages: Reformatted link tags for better readability
- [`73e5ac57`](https://github.com/inveniosoftware/invenio-app-rdm/commit/73e5ac57bd6af6604ab79d31cea84b55da6a1d5a) help pages: Remove duplicated sentence
- [`58919f38`](https://github.com/inveniosoftware/invenio-app-rdm/commit/58919f38d96168fdbb86c411fa3bfb7e5f5f5843) help pages: Correct HTML tags
- [`2508a090`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2508a0904d765ae5629519d01a2ecd179c7f92e4) help pages: Remove empty paragraph below main header
- [`859bfd6b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/859bfd6bdadb96ddca349cee023b84d4f76ec062) help pages: Fix broken strings
- [`88622007`](https://github.com/inveniosoftware/invenio-app-rdm/commit/88622007f06e957974b16d80657f27f049acaf30) help pages: Add University of Münster copyright to header
- [`0021d1f2`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0021d1f2249f70a4a7b25792036abb33960cd708) help pages: Adjust link description text for regular expression syntax
- [`0e5af31d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0e5af31d153c00bb1a847467d45b932fade18154) help pages: Add missing example links
- [`5356aee8`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5356aee851384a4ea2438e95fa571c260285b729) feat(deposit): add extra and after overridables
- [`f0034f1d`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f0034f1d397773c001ebcb92299a379443783106) feat(deposit): add record to overridable context
- [`4a5b9898`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4a5b98988ce4ce6e8833c2332a8d58f9186172af) feat(administration): add user creation
- [`35b634d7`](https://github.com/inveniosoftware/invenio-app-rdm/commit/35b634d73c4daecda1da3178135b92d6d94b0e4a) feat(deposit): allow overriding deposit serializer
- [`2cb76752`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2cb767523d6e137d02a69649d91b2ea0b3edccaf) fix: show all contributers on dashboard page
- [`5e7d2719`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5e7d27199f82722d9a634a6e9b10f13c639691ad) chore(setup): bump dependencies
- [`2a27af2e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/2a27af2e43ad5b84703900106ad78a08f8be0c99) fix(chore): DeprecationWarning stdlib
- [`443a98a5`](https://github.com/inveniosoftware/invenio-app-rdm/commit/443a98a57990a9929380b0a8e8c6bd0f2bb47f07) release: v14.0.0b5.dev0
- [`46a5b23e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/46a5b23e71967f3c859d62cf297d117e1fbdd98e) fix: manage record link functionality for all versions
- [`da2ac3f6`](https://github.com/inveniosoftware/invenio-app-rdm/commit/da2ac3f65242052ff36e797921fcd1951c167bc8) feat(css): styles for deep-linked request comment replies
- [`34c313a1`](https://github.com/inveniosoftware/invenio-app-rdm/commit/34c313a15678240ea0c417e1c36a3116cfd66e8e) style: collapsible messages style
- [`b92b8456`](https://github.com/inveniosoftware/invenio-app-rdm/commit/b92b8456d4b7b10af06e497adcaa99bf85b50213) search guide: fix regex example
- [`eb114e57`](https://github.com/inveniosoftware/invenio-app-rdm/commit/eb114e5717a71b8afdff38b3b45953362ed4c7c8) search guide: fix regex example in swedish translation
- [`3e6e97ba`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3e6e97ba036a1206c70a1580ea2dd0a6c5f9fb44) Fix regex search example
- [`565cf9ee`](https://github.com/inveniosoftware/invenio-app-rdm/commit/565cf9eede85b906e797143b3e3db76f353bc3aa) Fix regex search example URL
- [`c540fa1c`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c540fa1c0eb74edd1059d13f6c1d64a8c1066e03) release: v14.0.0b4.dev6
- [`9cd14337`](https://github.com/inveniosoftware/invenio-app-rdm/commit/9cd1433707a04e6d17c762e6cc148f084f983195) fix(ExportDropdown): Fix css spacing and responsiveness
- [`901660fd`](https://github.com/inveniosoftware/invenio-app-rdm/commit/901660fd4b98047f8bc6ec375559ff6c998feae0) release: v14.0.0b4.dev5
- [`040d3191`](https://github.com/inveniosoftware/invenio-app-rdm/commit/040d31917ed5b010c95c3cf122debb811ea01432) feat(CopyButton): Pass remaining props to customize UI & functionality
- [`681631eb`](https://github.com/inveniosoftware/invenio-app-rdm/commit/681631ebdecb469b1a4cfeb5ebd558632cc9e8c1) refactor(RecordVersionsList): Make version items overridable
- [`6ef5b318`](https://github.com/inveniosoftware/invenio-app-rdm/commit/6ef5b318217bae1b5093415518d190b397704578) fix: black formatting
- [`cfe09933`](https://github.com/inveniosoftware/invenio-app-rdm/commit/cfe09933ab5ec83768467560c3baab1ec8328637) release: v14.0.0b4.dev4
- [`15d425fa`](https://github.com/inveniosoftware/invenio-app-rdm/commit/15d425faf7b47f581f6be9aa1488ba13755342e5) feat(records_ui): Add preview_file arg to record landing page
- [`6228be3b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/6228be3b1989a743f3575302871322edb1d856ff) fix(landing_page/theme.js): Fix preview iframe navigation and update URL on click
- [`c36d8c73`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c36d8c730efcbf4a6e849b0a6c35b861aa6c6000) fix(landing_page/theme.js): Optmize preview-link click event
- [`419ce354`](https://github.com/inveniosoftware/invenio-app-rdm/commit/419ce3547c06c88edfcdbc5c7d52d3f702c8cdae) feat(previewer): show message for outdated records
- [`b23f943e`](https://github.com/inveniosoftware/invenio-app-rdm/commit/b23f943e53dbd6cd9f0f5b52d8e4735083d0264e) fix(moderation.requests): handle empty payload key not in request
- [`59c87b28`](https://github.com/inveniosoftware/invenio-app-rdm/commit/59c87b288cb08be2127d310d5f695fb20a27da4f) feat(comment-replies): add single threading on comments
- [`e18f3fcb`](https://github.com/inveniosoftware/invenio-app-rdm/commit/e18f3fcbab367e59c6859ae1ed4a6bee0a54d603) fix: use UUID type for request identifiers
- [`5237260a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5237260a2d48603473d4e4e8412a3ac1822faf74) refactor(ui): support custom file display name resolver
- [`77170575`](https://github.com/inveniosoftware/invenio-app-rdm/commit/771705755846d540b055f0ceca26c2ffcbddf687) release: v14.0.0b4.dev3
- [`06cbf6d7`](https://github.com/inveniosoftware/invenio-app-rdm/commit/06cbf6d76831d10ff7e69a26d7137a65001dd8aa) fix(feed): styling for disabled reply input
- [`f5a2047b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/f5a2047b2dc0d972438392f6084c41d94662ed94) release: v14.0.0b4.dev2
- [`ebf4c89b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/ebf4c89b97e58e48db2a793c8aa865e8063a502d) semantic-ui: feed.overrides: Add placeholder css
- [`5b65083a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/5b65083a190d050908aff2be83a7a5751842e8c9) fix: css padding for preview msg
- [`c956e55a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/c956e55a932c49693e92a16a6ebb1876d1122f42) release: v14.0.0b4.dev1
- [`3e68698b`](https://github.com/inveniosoftware/invenio-app-rdm/commit/3e68698bf8a7ed8fad3cf93434336b90d604dbaf) feat(css): styles for threaded replies
- [`0202650a`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0202650a198ef8699577753c5f30adef0e28db73) feat(views-request): include `can_reply_comment` in template permissions dict
- [`cd121e55`](https://github.com/inveniosoftware/invenio-app-rdm/commit/cd121e55535deb90c9172b22a078c88dc9cc9ce5) chore(setup): bump major versions
- [`4c569edb`](https://github.com/inveniosoftware/invenio-app-rdm/commit/4c569edb4672782e6ce85b1670cf25d416e9179e) release: v14.0.0b4.dev0
- [`0ec0c02c`](https://github.com/inveniosoftware/invenio-app-rdm/commit/0ec0c02ce330a2f6a2b34bd913bd297e8fd62b31) feat: add empty Overridable container before and after the files accordion
- [`7443b1b4`](https://github.com/inveniosoftware/invenio-app-rdm/commit/7443b1b471c42c145b89efcbfef7678459097b3b) assets: added css for hidden comment line and last page first comment

#### `invenio-audit-logs` 1.1.0 💥
[0.3.2 → 1.1.0](https://github.com/inveniosoftware/invenio-audit-logs/compare/v0.3.2...v1.1.0)

- [`ca8b537d`](https://github.com/inveniosoftware/invenio-audit-logs/commit/ca8b537da0cedc08eceabd4465777896a244a765) release: v1.1.0
- [`3fea6756`](https://github.com/inveniosoftware/invenio-audit-logs/commit/3fea675610c85cabdeee90380305652230f50237) service: add action param
- [`01e8313c`](https://github.com/inveniosoftware/invenio-audit-logs/commit/01e8313cac60ba3f512d27f500371747036751f2) fix(service): Return empty result when documents are not indexed yet
- [`164142fc`](https://github.com/inveniosoftware/invenio-audit-logs/commit/164142fc9336047f72589327ccf68bed2a631c27) fix(chore): DeprecationWarning stdlib
- [`20506d15`](https://github.com/inveniosoftware/invenio-audit-logs/commit/20506d1587ec99cfdfa9562b12e0c124a1baa24a) chore(black): update formatting to >= 26.0
- [`9ca0df93`](https://github.com/inveniosoftware/invenio-audit-logs/commit/9ca0df930c3ba6ae7ec13c1301f27a6c3b104b7c) chore(setup): bump dependencies
- [`9e2d60fb`](https://github.com/inveniosoftware/invenio-audit-logs/commit/9e2d60fb3168b0c7910faa6fbdf6f4fbe3302cce) release: v1.0.0
- [`38be73c5`](https://github.com/inveniosoftware/invenio-audit-logs/commit/38be73c5305e80b616b63bc7c33904639cd8255c) chore: replaced deprecated Link

#### `invenio-banners` 6.0.0 💥
[5.2.1 → 6.0.0](https://github.com/inveniosoftware/invenio-banners/compare/v5.2.1...v6.0.0)

- [`e2101cc0`](https://github.com/inveniosoftware/invenio-banners/commit/e2101cc02ae325ce41ab213aa2ff85352cc25b2b) refactor: use invenio-db Timestamp
- [`86eb76b3`](https://github.com/inveniosoftware/invenio-banners/commit/86eb76b3b00f706ad4fd4dd65a8e93ba00f13bc1) chore(setup): bump dependencies
- [`eaeef644`](https://github.com/inveniosoftware/invenio-banners/commit/eaeef64455a9946d07222730f5fff4fbe20c88fa) release: v6.0.0
- [`19d97cf8`](https://github.com/inveniosoftware/invenio-banners/commit/19d97cf89a25c088dce810275caf1792929a70d6) validation: ensure `banner_id` is an Integer
- [`5f383c86`](https://github.com/inveniosoftware/invenio-banners/commit/5f383c86f9ebb14af4c83bd6719d4d9479075f22) refactor(links): replace Link usage by EndpointLink
- [`df679aeb`](https://github.com/inveniosoftware/invenio-banners/commit/df679aeb77c1e8e7404dbd6f3461dac4e5ca50e6) fix(black): update style to match Black 26

#### `invenio-cache` 3.0.0 💥
[2.1.0 → 3.0.0](https://github.com/inveniosoftware/invenio-cache/compare/v2.1.0...v3.0.0)

- [`71e1331c`](https://github.com/inveniosoftware/invenio-cache/commit/71e1331c02c4c037552f59b861a2cfa79da7f251) fix(chore): DeprecationWarning stdlib
- [`0e5421fb`](https://github.com/inveniosoftware/invenio-cache/commit/0e5421fbf2d3a705c1a092099c62fc2b0b82a0a8) fix: DeprecationWarning from flask-caching
- [`471759b3`](https://github.com/inveniosoftware/invenio-cache/commit/471759b3bc8394127b6f2c3453540ada31d3d5fb) fix: PytestMockWarning: Mocks
- [`ff3efca7`](https://github.com/inveniosoftware/invenio-cache/commit/ff3efca759d41b26c9179f7355dc20a419de2412) chore(black): update formatting to >= 26.0
- [`ec603ea7`](https://github.com/inveniosoftware/invenio-cache/commit/ec603ea78c37ae4105f5299903e0d378eab613de) chore(setup): bump pytest-invenio dependency
- [`1a9129ab`](https://github.com/inveniosoftware/invenio-cache/commit/1a9129abd25e5d2fd3cf85ad24b0534689aef996) release: v3.0.0

#### `invenio-checks` 7.0.0 💥
[2.0.0 → 7.0.0](https://github.com/inveniosoftware/invenio-checks/compare/v2.0.0...v7.0.0)

- [`52bf8d56`](https://github.com/inveniosoftware/invenio-checks/commit/52bf8d563f8dfd180760ffca978c9c0fd66a4f74) fix(alembic): add missing revision ID
- [`744c4e26`](https://github.com/inveniosoftware/invenio-checks/commit/744c4e26742bfffe7767daafb54663f1e710bc2c) release: v7.0.0
- [`f01b15e2`](https://github.com/inveniosoftware/invenio-checks/commit/f01b15e23d955dfd23031383a908911d72b2a119) change(setup): bump invenio-jobs, communities
- [`df3292c9`](https://github.com/inveniosoftware/invenio-checks/commit/df3292c91a5c1dba281423a5f58cc65e7d2ede1f) release: v6.0.0
- [`8a1fc471`](https://github.com/inveniosoftware/invenio-checks/commit/8a1fc47193b9f8bdab735a16642294cb62246e20) change(installation): upgrade invenio-communities
- [`99d94e83`](https://github.com/inveniosoftware/invenio-checks/commit/99d94e8347eeea8076e669253b158ea7ca6fa733) release: v5.0.0
- [`4a75fd3c`](https://github.com/inveniosoftware/invenio-checks/commit/4a75fd3cf7bbf072402fef5d76d6add33a5c9a80) fix(chore): DeprecationWarning stdlib
- [`494d706d`](https://github.com/inveniosoftware/invenio-checks/commit/494d706d7f3bb1c123b84ea7948d1deef4f9f027) chore(setup): bump dependencies
- [`a48042c0`](https://github.com/inveniosoftware/invenio-checks/commit/a48042c0bf29602bfffc87fcebf7d7f9ae284f68) release: v4.0.0
- [`0e7dd772`](https://github.com/inveniosoftware/invenio-checks/commit/0e7dd772dbc8aadc5aba79ca3eb313195de3ab10) chore(setup): bump major version of invenio-communities
- [`da53af51`](https://github.com/inveniosoftware/invenio-checks/commit/da53af5105d69c3cf559952703f37dee4a032630) release: v3.0.0

#### `invenio-collections` 7.0.0 💥
[2.1.0 → 7.0.0](https://github.com/inveniosoftware/invenio-collections/compare/v2.1.0...v7.0.0)

- [`312b9c8a`](https://github.com/inveniosoftware/invenio-collections/commit/312b9c8a422a78a56d31c1b85c75f87f8d760a70) change(setup): upgrade rdm-records, invenio-checks
- [`ce93c69d`](https://github.com/inveniosoftware/invenio-collections/commit/ce93c69da037abab9d4109bcc7ee209bbb785f19) release: v7.0.0
- [`a3a4cdf0`](https://github.com/inveniosoftware/invenio-collections/commit/a3a4cdf06754024cab54f0d450588cc6c1179c8a) change(setup): upgrade invenio-communities, rdm-records
- [`84f02d8c`](https://github.com/inveniosoftware/invenio-collections/commit/84f02d8ca3172a347a5efdd9c52bc4dbd998c645) release: v6.0.0
- [`1ddabcc6`](https://github.com/inveniosoftware/invenio-collections/commit/1ddabcc6ef02a797c8648d4673875cb3f5bec6ed) change(setup): remove unused invenio-administration dependency
- [`0c5ee03c`](https://github.com/inveniosoftware/invenio-collections/commit/0c5ee03c8edd34928b2a5656e0931b77c8dcbb0e) release: v5.0.1
- [`dfc48a7f`](https://github.com/inveniosoftware/invenio-collections/commit/dfc48a7fc240bc211928c5d4284ee9f36781809a) change(setup): upgrade invenio-communities, invenio-rdm-records
- [`07819fa3`](https://github.com/inveniosoftware/invenio-collections/commit/07819fa331b045b9c5a42bbb8b74fc788d9367e5) release: v5.0.0
- [`a12454bf`](https://github.com/inveniosoftware/invenio-collections/commit/a12454bf4dfd513d003542bab212fcf89efd7bd8) refactor: use Timestamp from db
- [`cc7369c9`](https://github.com/inveniosoftware/invenio-collections/commit/cc7369c96d73b2067aad0d72408f87924240cebb) chore(setup): bump dependencies
- [`64f54954`](https://github.com/inveniosoftware/invenio-collections/commit/64f549540f03244eaa3d7d765f4a8e3b2dde0648) chore(black): update formatting to >= 26.0
- [`c7e2f42f`](https://github.com/inveniosoftware/invenio-collections/commit/c7e2f42fc20b4f376de2127f3a4fe1288452d96b) release: v4.0.0
- [`381106d9`](https://github.com/inveniosoftware/invenio-collections/commit/381106d911d70268bdc80b71c0cf5b68efcd7f3d) refactor!: replace Link usage by EndpointLink
- [`941a22d5`](https://github.com/inveniosoftware/invenio-collections/commit/941a22d51ad3ed3a8f27fc2e452de9e63d16a145) Revert "alembic: depend on communities instead of rdm-records"
- [`406d4730`](https://github.com/inveniosoftware/invenio-collections/commit/406d47308276a66e8352c9ae7a35681348e90689) release: v3.0.1
- [`aff54201`](https://github.com/inveniosoftware/invenio-collections/commit/aff5420103e16867649b1abb64605d4606f07118) chore(pyproject): bump major versions
- [`2724f807`](https://github.com/inveniosoftware/invenio-collections/commit/2724f807e44f415f532a58b41324d3b2c4dcba4d) release: v3.0.0

#### `invenio-communities` 25.0.0+oarepo.2.vefo4ebswlgllcyt 💥
[21.2.0.8902796 → 25.0.0+oarepo.2.vefo4ebswlgllcyt](https://github.com/inveniosoftware/invenio-communities/compare/v21.2.0...v25.0.0)

- [`f6fe44df`](https://github.com/inveniosoftware/invenio-communities/commit/f6fe44dfb8fc33bb47baaf8e8c16f6061a27d67a) change(setup): upgrade invenio-vocabularies
- [`348cb162`](https://github.com/inveniosoftware/invenio-communities/commit/348cb162eced8b60b04e06a55e4d737bd0feec94) release: v25.0.0
- [`f06a26f4`](https://github.com/inveniosoftware/invenio-communities/commit/f06a26f44083769cb4e37fcb5c1487ff1da138ab) release: v24.0.1
- [`73139b23`](https://github.com/inveniosoftware/invenio-communities/commit/73139b2359c46f3c1b02579a6f4907cac611df31) fix(alembic): correct `down_revision` of group notifications migration
- [`3e5c4073`](https://github.com/inveniosoftware/invenio-communities/commit/3e5c40739214aa882ebc12a2967f2d26e790b0fe) feat(mshp-req): default communities to be closed to membership requests
- [`ae4f32a1`](https://github.com/inveniosoftware/invenio-communities/commit/ae4f32a19b2bd10c1c0ee1e527195ce6ac07e0be) feat(mshp-req): update can_request_membership permission
- [`7d4ae17b`](https://github.com/inveniosoftware/invenio-communities/commit/7d4ae17ba19c7b7261f2eebdcb068d343be18fba) feat(mshp-req): show button of membership discussion on header if applicable
- [`a3f67a07`](https://github.com/inveniosoftware/invenio-communities/commit/a3f67a0777d9e58eb62e11b97214063db254a1c2) feat(mshp-req): only show membership request/discussion button if feature enabled [+]
- [`ee404874`](https://github.com/inveniosoftware/invenio-communities/commit/ee4048740a3aba68bc6d0293db459db760e2e21e) release: v24.0.0
- [`d539476a`](https://github.com/inveniosoftware/invenio-communities/commit/d539476a979afa114e165d01ce2cae8f2dc212db) groups: add group notifications
- [`54e15ec5`](https://github.com/inveniosoftware/invenio-communities/commit/54e15ec53d3bb66e0221db9bc2075edccfb64356) release: v23.1.0
- [`494a388b`](https://github.com/inveniosoftware/invenio-communities/commit/494a388b1f3b0faafef52e1f99ba618dbb41bd74) fix(tests): add files.enabled to subcommunity request
- [`50acf710`](https://github.com/inveniosoftware/invenio-communities/commit/50acf710d5c9d4a9d58fb7ef763f6af9c3dc2a99) feat(facets): register overriden range facet element
- [`5cda1f3f`](https://github.com/inveniosoftware/invenio-communities/commit/5cda1f3f96ce4d75ab322e75c838bf6f2a6dc7b4) fix : Size error on community image upload doesn't go away after image
- [`00102b5e`](https://github.com/inveniosoftware/invenio-communities/commit/00102b5e52d05956e881c7d04ccd245440ae5611) build(deps-dev): bump lodash
- [`257a4aed`](https://github.com/inveniosoftware/invenio-communities/commit/257a4aed403f02813b5bb58dbab867387e195fa4) refactor(schema): remove usage of object_key
- [`b27be1d0`](https://github.com/inveniosoftware/invenio-communities/commit/b27be1d0df898fde64806649f12914685f603b3e) refactor: migrate to context_schema
- [`d1fb1887`](https://github.com/inveniosoftware/invenio-communities/commit/d1fb18874826c28a1f51646da10a76f808dfb4a1) fix(chore): DeprecationWarning stdlib
- [`daf22715`](https://github.com/inveniosoftware/invenio-communities/commit/daf227150d9161b1795b0292d3690b3f7d92e9a6) fix: remove RemovedInMarshmallow4Warning
- [`f36a4abc`](https://github.com/inveniosoftware/invenio-communities/commit/f36a4abc0bf448b5742d12514fd532a19d1be3ea) fix: DeprecationWarning
- [`cb1a1fdc`](https://github.com/inveniosoftware/invenio-communities/commit/cb1a1fdcd7b5d4dbfb96a792088b888f4aff4e08) chore(black): update formatting to >= 26.0
- [`25dadad5`](https://github.com/inveniosoftware/invenio-communities/commit/25dadad588e173db873b96ae2af74f13e58a7159) chore(setup): bump dependencies
- [`e028799b`](https://github.com/inveniosoftware/invenio-communities/commit/e028799bf4e2744f19290d09200937ed17096471) fix(tests): add mocks
- [`f993a96d`](https://github.com/inveniosoftware/invenio-communities/commit/f993a96d28997e0d97bfa1fda6b6f0336cc78b41) fix(tests): remove not existing route
- [`c877d827`](https://github.com/inveniosoftware/invenio-communities/commit/c877d8270c5f2b0bae6cb75376b11166a9ee455e) release: v23.0.0
- [`edf05fa1`](https://github.com/inveniosoftware/invenio-communities/commit/edf05fa1d8d2a96751fa8f9b2d4b7f2cbdfe3375) fix(black): fix style to meet Black 26 standard
- [`f1099733`](https://github.com/inveniosoftware/invenio-communities/commit/f1099733008384e90b557e72e0857275e90e19ed) chore(setup): bump major version of invenio-requests
- [`ade033b4`](https://github.com/inveniosoftware/invenio-communities/commit/ade033b4b09667ad46b71ca45bc5bee02cbd2c87) release: v22.0.0

#### `invenio-config` 1.1.0+oarepo.4.uquwys7agp2l27a3
[1.1.0+oarepo.3.uwlnr7jyjt7lt2y7 → 1.1.0+oarepo.4.uquwys7agp2l27a3](https://github.com/inveniosoftware/invenio-config/compare/v1.1.0...v1.1.0)


#### `invenio-db` 2.4.0
[2.1.2 → 2.4.0](https://github.com/inveniosoftware/invenio-db/compare/v2.1.2...v2.4.0)

- [`4e6db7be`](https://github.com/inveniosoftware/invenio-db/commit/4e6db7bebdd669932a8785113fcdb0ffc9a52763) release: v2.4.0
- [`0edf4f8a`](https://github.com/inveniosoftware/invenio-db/commit/0edf4f8a39d989bc69fc948c2ae064545d63ddd5) fix(utc): move DB config override to _apply_driver_defaults
- [`b3a8b265`](https://github.com/inveniosoftware/invenio-db/commit/b3a8b265ecea8457c24ed72a605db52865413c9b) fix(utc): add warning if libpq options are specified without a timezone
- [`523cbb6e`](https://github.com/inveniosoftware/invenio-db/commit/523cbb6ef7391fd93cea9ce46803186f7dcdf9c1) fix(sqlite): avoid running PRAGMA in multi-engine environments
- [`71cafb6f`](https://github.com/inveniosoftware/invenio-db/commit/71cafb6f43eefdf01292aa10fccb7d3e9d66c4d7) fix(db): remove hacks, move PostgreSQL timezone config to ext.py
- [`b96b6019`](https://github.com/inveniosoftware/invenio-db/commit/b96b60197518445452734e66e5b01e06f9af2ccc) tests(utc): add unit tests for UTCDateTime and Postgres configured time zone
- [`23d27aef`](https://github.com/inveniosoftware/invenio-db/commit/23d27aefd20f335906380b05852960b0ccf7a54b) release: v2.3.0
- [`d9278fcf`](https://github.com/inveniosoftware/invenio-db/commit/d9278fcf06e2acee92eda4565cbe50b15c5595ea) feat(alembic): set lock_timeout with retry on migration connections
- [`5cff5b6c`](https://github.com/inveniosoftware/invenio-db/commit/5cff5b6c55652ceeb4ae57b5bb7827ed1fa51d36) docs(sphinx): ignore unresolved Flask-Alembic type refs
- [`55491403`](https://github.com/inveniosoftware/invenio-db/commit/55491403163a82ae02395f1433607911b08ad992) fix(config): use UTC for PostgreSQL
- [`81cb5b75`](https://github.com/inveniosoftware/invenio-db/commit/81cb5b75fb5ebb3295547a8c85018d59ce6c01d4) fix(setup): pin sqlalchemy-continuum
- [`1f845ba2`](https://github.com/inveniosoftware/invenio-db/commit/1f845ba2e4132c018020a90bd8dd704fa8cac3f5) release: v2.2.1
- [`8029a9b5`](https://github.com/inveniosoftware/invenio-db/commit/8029a9b552620c5e8c2da70c071676932ae1aae7) shared: add UTCDateTime column type
- [`8885f7ec`](https://github.com/inveniosoftware/invenio-db/commit/8885f7eccbaf5a46cc50482bb804f4686fe2a028) fix: docs reference target not found
- [`5212d79e`](https://github.com/inveniosoftware/invenio-db/commit/5212d79eb72ec5d19be1a8cefecf196164c06ae2) db: fix warning
- [`91c96855`](https://github.com/inveniosoftware/invenio-db/commit/91c9685569b4ab791676a4e2d3b5ce7769e096e3) UTCDateTime: handle more cases
- [`ef202529`](https://github.com/inveniosoftware/invenio-db/commit/ef2025295a53a037d04b19201962ad0cf9db475e) db: add Timestamp class
- [`891bf450`](https://github.com/inveniosoftware/invenio-db/commit/891bf450c8892890222b5508b5f6c061c728c3f5) fix: docs reference target not found
- [`9a77042f`](https://github.com/inveniosoftware/invenio-db/commit/9a77042faa6a558e7faedff25fb47f2bc0e378b6) change(utc): use always timezone.utc
- [`04c49908`](https://github.com/inveniosoftware/invenio-db/commit/04c49908809cfda1012383afeb6d5b1bb59b570f) fix: str of datetime
- [`b8ce9acb`](https://github.com/inveniosoftware/invenio-db/commit/b8ce9acbb8afd06db239b78d2437a819279b06e4) chore(black): apply changes for black>=26
- [`27e7643f`](https://github.com/inveniosoftware/invenio-db/commit/27e7643ff784f013fb3b112463bd8e70dd7c350a) release: v2.2.0
- [`de17cc50`](https://github.com/inveniosoftware/invenio-db/commit/de17cc5069aeb63e52a99547818dfab9250c4ee7) chore: add nitpick_ignore to fix CI

#### `invenio-drafts-resources` 8.0.1+oarepo.2.uurr6e2zpcxyzqrj 💥
[7.3.1.76831460 → 8.0.1+oarepo.2.uurr6e2zpcxyzqrj](https://github.com/inveniosoftware/invenio-drafts-resources/compare/v7.3.1...v8.0.1)

- [`7d7bfdd6`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/7d7bfdd6edb02356d84a79f54c774c6e0dfea212) release: v8.0.1
- [`6cb339c3`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/6cb339c3d682341fef298794b7fc94a4f2f0a1dc) fix(api): Cleanup next_draft_id in versions state only on latest draft
- [`d31f8dc7`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/d31f8dc7066a96aa6e3f5de4871950050cafa5b8) fix(media-files): Skip sync when draft files doesn't have a bucket
- [`d9ed258a`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/d9ed258a6f6ec403b5c53f4afb5714725adf6ca9) fix(chore): DeprecationWarning stdlib
- [`56a81ee2`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/56a81ee205415214d413ee19e0d86a543253589e) fix: JSONSCHEMAS_HOST warning
- [`275a4ffd`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/275a4ffd55a593095a243234dc7c6286f1b8fd65) fix: RemovedInMarshmallow4Warning
- [`3d19f7de`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/3d19f7de77a91aad1460e650d9ac7808ea640240) fix: DeprecationWarning from invenio-indexer
- [`49736550`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/49736550e6e7f33b7ffa132626f9c4d72749d389) chore(black): update formatting to >= 26.0
- [`dd5c3401`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/dd5c34017f7fa5622a93241e3ad676344feb22f0) chore(setup): bump dependencies
- [`8e8f87d2`](https://github.com/inveniosoftware/invenio-drafts-resources/commit/8e8f87d297973d4154bf8a49bf984a90dda2f6db) release: v8.0.0

#### `invenio-files-rest` 4.1.0+oarepo.2.a3g2ksmeqiqmhy66 💥
[3.4.1 → 4.1.0+oarepo.2.a3g2ksmeqiqmhy66](https://github.com/inveniosoftware/invenio-files-rest/compare/v3.4.1...v4.1.0)

- [`80699fcd`](https://github.com/inveniosoftware/invenio-files-rest/commit/80699fcdd983a583dcb97ce7bd0356afe055e3be) release: v4.1.0
- [`f876ab6e`](https://github.com/inveniosoftware/invenio-files-rest/commit/f876ab6e66dcb4f5cfa986e52d303934887a6e4c) fix(sphinx): Ignoring ErrorHandler to prevent sphinx reference error
- [`b4b04f62`](https://github.com/inveniosoftware/invenio-files-rest/commit/b4b04f62ef8c8f76657ace17134565350660f530) fix(webargs): Made sources compatible with upgraded webargs
- [`616dc34c`](https://github.com/inveniosoftware/invenio-files-rest/commit/616dc34c38006433653211feb5a9e523b0d399e7) fix: connections to postgresql exhausted in python 3.14.2
- [`ca6aa709`](https://github.com/inveniosoftware/invenio-files-rest/commit/ca6aa709b7b4a38a6ce5485f85d94a1ed49d5156) fix(chore): DeprecationWarning stdlib
- [`0bef417e`](https://github.com/inveniosoftware/invenio-files-rest/commit/0bef417ea384b9e270c64e3ba9cf799ce677f851) Removed dependency on PyFilesystem2
- [`60a30e31`](https://github.com/inveniosoftware/invenio-files-rest/commit/60a30e3171c48b6ea1c31936cf4dec141797d0cd) refactor: move to context_schema
- [`c2d7f311`](https://github.com/inveniosoftware/invenio-files-rest/commit/c2d7f311e1e747bef40eb26ec92b0e8929519e64) fix: LegacyAPIWarning SQLAlchemy
- [`8b117993`](https://github.com/inveniosoftware/invenio-files-rest/commit/8b11799367d2ba2a4129830c6d259376a8041614) chore(setup): bump dependencies
- [`d5b5975c`](https://github.com/inveniosoftware/invenio-files-rest/commit/d5b5975ce4a3658b3756bd1425de6cf6354e6b80) chore(black): update formatting to >= 26.0
- [`131594c9`](https://github.com/inveniosoftware/invenio-files-rest/commit/131594c9324dc6cc353d868affd5788509bae45f) release: v4.0.0
- [`5f2c5540`](https://github.com/inveniosoftware/invenio-files-rest/commit/5f2c554049646514bf121ed9721ce2e5595906ae) ci: fix python 3.13+ compatibility and docstrings
- [`3a15df6e`](https://github.com/inveniosoftware/invenio-files-rest/commit/3a15df6ef55c4d435afd7f7292170110e9074312) i18n: pulled translations

#### `invenio-formatter` 4.0.0 💥
[3.3.1 → 4.0.0](https://github.com/inveniosoftware/invenio-formatter/compare/v3.3.1...v4.0.0)

- [`1a5cea97`](https://github.com/inveniosoftware/invenio-formatter/commit/1a5cea97c9221af8eb4e9e342b29b4cd30a2dc76) fix(chore): DeprecationWarning stdlib
- [`bfc87f39`](https://github.com/inveniosoftware/invenio-formatter/commit/bfc87f395e203f6eda22fb02bfb7463c62e2eaea) chore(black): update formatting to >= 26.0
- [`0724be51`](https://github.com/inveniosoftware/invenio-formatter/commit/0724be5156357856072f40c8f4f8cb5a60077efe) chore(setup): bump pytest-invenio dependency
- [`62f837c6`](https://github.com/inveniosoftware/invenio-formatter/commit/62f837c6fdc66f435b2acb2f24109bdca4d999e7) release: v4.0.0

#### `invenio-github` 5.0.0 💥
[4.0.0 → 5.0.0](https://github.com/inveniosoftware/invenio-github/compare/v4.0.0...v5.0.0)

- [`1975f431`](https://github.com/inveniosoftware/invenio-github/commit/1975f431986610adcb484f3c6b6c5909ab8562e4) fix(chore): DeprecationWarning stdlib
- [`01a63f0a`](https://github.com/inveniosoftware/invenio-github/commit/01a63f0a7024fece6322cab4dbecf2668b9d5671) chore(setup): bump dependencies
- [`2e37785b`](https://github.com/inveniosoftware/invenio-github/commit/2e37785bbb3afa3a6e4386bab5044549b10f43c4) chore(black): update formatting to >= 26.0
- [`b140c872`](https://github.com/inveniosoftware/invenio-github/commit/b140c8723e699639f75bf1e89161675de3d26f80) release: v5.0.0
- [`269f5b0d`](https://github.com/inveniosoftware/invenio-github/commit/269f5b0d0dafeba849a86464bd62de5c5f8cd99e) Update release date for version v4.0.0

#### `invenio-i18n` 3.5.0
[3.4.3 → 3.5.0](https://github.com/inveniosoftware/invenio-i18n/compare/v3.4.3...v3.5.0)

- [`7c8cb9a6`](https://github.com/inveniosoftware/invenio-i18n/commit/7c8cb9a631639ffc732426b366c553445415755e) chore(black): update formatting to >= 26.0
- [`87e03814`](https://github.com/inveniosoftware/invenio-i18n/commit/87e03814c41f2f682cf843bcea4e37d5462af339) release: v3.5.0
- [`603d39cb`](https://github.com/inveniosoftware/invenio-i18n/commit/603d39cb7846fb577e0b0f18f4302e07a8b4fe35) feat(i18n): add translation collection/validation service and update CLI
- [`1b9e6cfe`](https://github.com/inveniosoftware/invenio-i18n/commit/1b9e6cfee52ba7bbf4e3ef7f96ba39bf5be3d79a) feat: add cli command to update fuzzy trns and refactor
- [`1e037c1d`](https://github.com/inveniosoftware/invenio-i18n/commit/1e037c1de436897499989e291c84ca9f63805115) feat(i18n): improve type hints, add fuzzy tests and module docs
- [`72fba4a3`](https://github.com/inveniosoftware/invenio-i18n/commit/72fba4a34a24aa37a7cb5c833bdfe7af5d573075) Update README.rst

#### `invenio-indexer` 4.0.0 💥
[3.1.0 → 4.0.0](https://github.com/inveniosoftware/invenio-indexer/compare/v3.1.0...v4.0.0)

- [`bf65df9d`](https://github.com/inveniosoftware/invenio-indexer/commit/bf65df9df26ba4230b67895eaa7575dc594897b0) fix(chore): DeprecationWarning stdlib
- [`6aca67a5`](https://github.com/inveniosoftware/invenio-indexer/commit/6aca67a584db88fc43f8c2162c045ade6378cc47) fix(tests): update due to sqlalchemy>=2.0.0
- [`70823d88`](https://github.com/inveniosoftware/invenio-indexer/commit/70823d88a78b2c66288ff1dfa2296263d0bf3f51) chore(setup): bump dependencies
- [`b3ba2d67`](https://github.com/inveniosoftware/invenio-indexer/commit/b3ba2d6775f41cc4857236bd4ab2307658611b44) release: v4.0.0

#### `invenio-jobs` 8.0.1 💥
[6.1.0.27571599 → 8.0.1](https://github.com/inveniosoftware/invenio-jobs/compare/v6.1.0...v8.0.1)

- [`92153e6e`](https://github.com/inveniosoftware/invenio-jobs/commit/92153e6e7703c17276c9f9fa69d10e1f27dee8de) fix(alembic): recipes down versions and branch merge
- [`3777cd2e`](https://github.com/inveniosoftware/invenio-jobs/commit/3777cd2e05deeea5fc0f7b2f2fcbecee2d95fa51) release: v8.0.1
- [`ad0563aa`](https://github.com/inveniosoftware/invenio-jobs/commit/ad0563aae0ce213bf546d87eb74c8e1818fab5d1) release: v8.0.0
- [`8f23a9ba`](https://github.com/inveniosoftware/invenio-jobs/commit/8f23a9ba726e74256bef3ba92c5581381abe1c43) utils: enable translations in status messages
- [`3a1b43cc`](https://github.com/inveniosoftware/invenio-jobs/commit/3a1b43cca1d95fdd272d75eb8e183f5ea258a308) logs: fix logs ordering, group by subtask
- [`a4025424`](https://github.com/inveniosoftware/invenio-jobs/commit/a4025424cebaf800e8cdc85cd2b9fca6af68737d) release: v7.1.0
- [`07c7fb69`](https://github.com/inveniosoftware/invenio-jobs/commit/07c7fb69502c9b0d98ae836d5022afd41601b7cb) notifications: Enabled email notifications on jobs
- [`0d27164a`](https://github.com/inveniosoftware/invenio-jobs/commit/0d27164ad115e1aba6b0387c0dbc1d6fc7f7088e) 📦 release: v7.0.1
- [`96c36d97`](https://github.com/inveniosoftware/invenio-jobs/commit/96c36d97d221e3a0ce0136b63952366dea6bd86e) jobs: updated last_success condition and update_run
- [`25f2b66b`](https://github.com/inveniosoftware/invenio-jobs/commit/25f2b66b53132034fd3357f64c275e2bc56f8209) fix(chore): DeprecationWarning stdlib
- [`88cd5718`](https://github.com/inveniosoftware/invenio-jobs/commit/88cd57181b333c71be0cb9bdafd1191bad47908e) fix: RemovedInMarshmallow4Warning
- [`daba4215`](https://github.com/inveniosoftware/invenio-jobs/commit/daba421537adb8e4868887df0e6bb64ced244a3c) fix: ChangedInMarshmallow4Warning
- [`faf6c586`](https://github.com/inveniosoftware/invenio-jobs/commit/faf6c58637bcef0d846abbdf5dc7a89967797193) chore(black): update formatting to >= 26.0
- [`5b2fc133`](https://github.com/inveniosoftware/invenio-jobs/commit/5b2fc13340c5cf5016cf5f4e432a811e39ed9f2e) chore(setup): bump dependencies
- [`74388a65`](https://github.com/inveniosoftware/invenio-jobs/commit/74388a65e9c3144a619a8a9a6712e46749d41856) release: v7.0.0
- [`89608715`](https://github.com/inveniosoftware/invenio-jobs/commit/89608715c2ad5db35d6c616b0458bc9509af702e) feat: commandline client for jobs
- [`bb689bd9`](https://github.com/inveniosoftware/invenio-jobs/commit/bb689bd964f2889ecc9a7cd699737392e829f6d0) feat: add delete button to job detail in administration
- [`a11f18b8`](https://github.com/inveniosoftware/invenio-jobs/commit/a11f18b8a39cf963bd1f1440af4d7fd98f35f177) feat: option to edit job args
- [`cf999782`](https://github.com/inveniosoftware/invenio-jobs/commit/cf99978203f0136bc2ec7e06dec2dad35d3a40ea) chore: deprecate Link usage

#### `invenio-jsonschemas` 2.1.0+oarepo.4.ah2r67trm7bozrty
[2.1.0.14108971 → 2.1.0+oarepo.4.ah2r67trm7bozrty](https://github.com/inveniosoftware/invenio-jsonschemas/compare/v2.1.0...v2.1.0)


#### `invenio-mail` 2.3.0+oarepo.4.qsg7jcloi7wbim37
[2.3.0+oarepo.3.gokq6uzzkamywgao → 2.3.0+oarepo.4.qsg7jcloi7wbim37](https://github.com/inveniosoftware/invenio-mail/compare/v2.3.0...v2.3.0)


#### `invenio-notifications` 1.3.0+oarepo.2.6aeoh5zp2umw2kjc
[1.2.3.87836317 → 1.3.0+oarepo.2.6aeoh5zp2umw2kjc](https://github.com/inveniosoftware/invenio-notifications/compare/v1.2.3...v1.3.0)

- [`d633538a`](https://github.com/inveniosoftware/invenio-notifications/commit/d633538a30cd1a84b54681ca77ff479665a16b5f) release: v1.3.0
- [`715b1825`](https://github.com/inveniosoftware/invenio-notifications/commit/715b1825afad8f3d567d71f94b3ddf3d48febb3d) fix: log warning if group has no valid email
- [`3d50095b`](https://github.com/inveniosoftware/invenio-notifications/commit/3d50095b2b925f3a6bdaba3119b2281da7cf2c52) email: use name as email for groups
- [`78d30c7b`](https://github.com/inveniosoftware/invenio-notifications/commit/78d30c7b07f62c50dbd33161ca73f8cbe5fd7b39) chore(setup): bump dependencies
- [`2cfd0f02`](https://github.com/inveniosoftware/invenio-notifications/commit/2cfd0f0270613b9bd6e32550d130f83bfa73dc4a) chore: reformat black

#### `invenio-oaiserver` 4.0.1+oarepo.2.4sorqldmiw776f3g 💥
[3.7.4.34642440 → 4.0.1+oarepo.2.4sorqldmiw776f3g](https://github.com/inveniosoftware/invenio-oaiserver/compare/v3.7.4...v4.0.1)

- [`38b6071a`](https://github.com/inveniosoftware/invenio-oaiserver/commit/38b6071abdf83b044f9f74bfdcbe45f5be71ac18) fix(tests): PendingDeprecationWarning
- [`098e5f04`](https://github.com/inveniosoftware/invenio-oaiserver/commit/098e5f04ebff633cd887dc20ea11b6e93b4901e9) chore: compatibility webargs > 6.0.0
- [`9dbeaa45`](https://github.com/inveniosoftware/invenio-oaiserver/commit/9dbeaa45e26a39096234c0d0376138aa0379e572) release: v4.0.1
- [`d40e105d`](https://github.com/inveniosoftware/invenio-oaiserver/commit/d40e105d8677c0de09938840e6902665731d6e2d) fix(chore): DeprecationWarning stdlib
- [`4b845187`](https://github.com/inveniosoftware/invenio-oaiserver/commit/4b845187b99240e698163166931fcc7e5fe88af7) chore(setup): bump dependencies
- [`543d1a93`](https://github.com/inveniosoftware/invenio-oaiserver/commit/543d1a93416d261753b2099817096c6e672e6029) release: v4.0.0

#### `invenio-oauth2server` 4.0.0 💥
[3.3.2 → 4.0.0](https://github.com/inveniosoftware/invenio-oauth2server/compare/v3.3.2...v4.0.0)

- [`976e7fb7`](https://github.com/inveniosoftware/invenio-oauth2server/commit/976e7fb712ae1ac32ced23b625156550343fb456) fix(chore): DeprecationWarning stdlib
- [`d9708549`](https://github.com/inveniosoftware/invenio-oauth2server/commit/d970854934893ced49126bb4dad46a2a5b3b8274) chore(setup): bump dependencies
- [`548db19c`](https://github.com/inveniosoftware/invenio-oauth2server/commit/548db19cb5f15cb96876301989d30e3cba22434a) release: v4.0.0
- [`7650b08a`](https://github.com/inveniosoftware/invenio-oauth2server/commit/7650b08a861b1c15e560fe909f18ef94032c4d2d) chore(setup): pin dependencies
- [`388f85b6`](https://github.com/inveniosoftware/invenio-oauth2server/commit/388f85b6f35e9823ea6a98c161c346353cce89e7) release: v3.3.3

#### `invenio-oauthclient` 7.0.0 💥
[6.1.1 → 7.0.0](https://github.com/inveniosoftware/invenio-oauthclient/compare/v6.1.1...v7.0.0)

- [`af10d1e0`](https://github.com/inveniosoftware/invenio-oauthclient/commit/af10d1e07e6c2223003b6268e8f257f819206b94) fix(chore): DeprecationWarning stdlib
- [`a1ae9b7c`](https://github.com/inveniosoftware/invenio-oauthclient/commit/a1ae9b7cf60fe29a0f2237391a3164ebce64f139) chore(setup): bump dependencies
- [`6e29fe2f`](https://github.com/inveniosoftware/invenio-oauthclient/commit/6e29fe2f5f9191338a1d36e98971d67749bfa51c) chore(tests): add admin
- [`976a07b4`](https://github.com/inveniosoftware/invenio-oauthclient/commit/976a07b428f0c506a8bfc9f648b98ba15629b598) release: v7.0.0
- [`0fa2efbe`](https://github.com/inveniosoftware/invenio-oauthclient/commit/0fa2efbefe21e699e3d7c1c783eedff6c391a537) chore(setup): pin dependencies
- [`f026b971`](https://github.com/inveniosoftware/invenio-oauthclient/commit/f026b971a4b88d4cdc9fe6b9662fad988bb1345a) chore(black): update formatting to >= 26.0
- [`177c056b`](https://github.com/inveniosoftware/invenio-oauthclient/commit/177c056b0c4ee3abede95d41632d64d9adef35fd) release: v6.1.2

#### `invenio-pages` 8.0.0 💥
[7.2.1 → 8.0.0](https://github.com/inveniosoftware/invenio-pages/compare/v7.2.1...v8.0.0)

- [`2d84e853`](https://github.com/inveniosoftware/invenio-pages/commit/2d84e8533898a8d92fcd1cd4c58b095c6902c11f) fix(chore): DeprecationWarning stdlib
- [`5b2e08e2`](https://github.com/inveniosoftware/invenio-pages/commit/5b2e08e29cefddc7bbd9288414a09d4e5b957207) chore(black): update formatting to >= 26.0
- [`06848f79`](https://github.com/inveniosoftware/invenio-pages/commit/06848f79106dfee010809409ddd66710ce1832ce) chore(setup): bump dependencies
- [`d62ef93d`](https://github.com/inveniosoftware/invenio-pages/commit/d62ef93d87dcd27ce6281aa2a838d42c48c7e461) release: v8.0.0
- [`3c536925`](https://github.com/inveniosoftware/invenio-pages/commit/3c53692591ab0af06d432477ee94b5eb07a1053e) refactor!: replace Link usage by EndpointLink
- [`84f2c134`](https://github.com/inveniosoftware/invenio-pages/commit/84f2c134b2b9d4fa632779fce2495f99f4efe2aa) :package: release: v7.3.0

#### `invenio-pidstore` 3.0.0 💥
[2.2.2 → 3.0.0](https://github.com/inveniosoftware/invenio-pidstore/compare/v2.2.2...v3.0.0)

- [`705d15f6`](https://github.com/inveniosoftware/invenio-pidstore/commit/705d15f609d6cc60fd0d18fe766ec024bdc77fa3) fix(chore): DeprecationWarning stdlib
- [`358d7360`](https://github.com/inveniosoftware/invenio-pidstore/commit/358d73607c14085d4480e809dcbff91c67c5b0ba) chore(setup): bump dependencies
- [`192e1031`](https://github.com/inveniosoftware/invenio-pidstore/commit/192e1031620a3729cfb3e41980620e0e2e85e10b) release: v3.0.0

#### `invenio-previewer` 4.1.1 💥
[3.5.1 → 4.1.1](https://github.com/inveniosoftware/invenio-previewer/compare/v3.5.1...v4.1.1)

- [`276e112e`](https://github.com/inveniosoftware/invenio-previewer/commit/276e112ec5a2026d314da0fcecabe57f172f2a1d) fix(pdfjs): switch to legacy bundle
- [`2ad1d157`](https://github.com/inveniosoftware/invenio-previewer/commit/2ad1d15788073d47cf72dc9be49e2bcab5addb78) release: v4.1.1
- [`12e7e8df`](https://github.com/inveniosoftware/invenio-previewer/commit/12e7e8dfb873d7d19d7947013929bd443d7f9b03) refactor(pdfjs): Display 'Download' text on button
- [`3877f8a2`](https://github.com/inveniosoftware/invenio-previewer/commit/3877f8a2fb783f04568181c8232e3885acd6d493) 📦 release: v4.1.0
- [`c6df80df`](https://github.com/inveniosoftware/invenio-previewer/commit/c6df80dfc092f43f8c8c5f15601b57ca8a9bfb51) feat(pdfjs): open PDF at page from URL hash
- [`73c1590e`](https://github.com/inveniosoftware/invenio-previewer/commit/73c1590e6c90bef06ef7fe5598f01332c8c8994d) chore(setup): bump dependencies
- [`349c8046`](https://github.com/inveniosoftware/invenio-previewer/commit/349c8046bc99d32d15c0b63de14ec65593339bc1) chore(black): update formatting to >= 26.0
- [`a5ebcda4`](https://github.com/inveniosoftware/invenio-previewer/commit/a5ebcda4d7d8f891fdd2fe3d794129e9f342c07d) release: v4.0.0
- [`4e7a1db0`](https://github.com/inveniosoftware/invenio-previewer/commit/4e7a1db059455c07738c0c61d1d7a0a9e86f8295) release: v3.6.0
- [`bc6c4887`](https://github.com/inveniosoftware/invenio-previewer/commit/bc6c488726104cbccde09dacea469b2a8e16eb49) fix(pdfjs): change inherited template for pdfjs
- [`7f247b5c`](https://github.com/inveniosoftware/invenio-previewer/commit/7f247b5c58af4d6c613b7ef28855fa523978c776) release: v3.6.0
- [`ba08164b`](https://github.com/inveniosoftware/invenio-previewer/commit/ba08164bb883ec445b14a3a724d237465c885152) feat(pdfjs): add download button

#### `invenio-queues` 1.0.2+oarepo.4.wsyd5f5b5aoeak67
[1.0.2+oarepo.3.vl7sv3tcr7whk5pw → 1.0.2+oarepo.4.wsyd5f5b5aoeak67](https://github.com/inveniosoftware/invenio-queues/compare/v1.0.2...v1.0.2)


#### `invenio-rdm-records` 27.0.0+oarepo.3.3yojwri2nobgwy5x 💥
[22.7.3.20646835 → 27.0.0+oarepo.3.3yojwri2nobgwy5x](https://github.com/inveniosoftware/invenio-rdm-records/compare/v22.7.3...v27.0.0)

- [`1fe2a207`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1fe2a207e983db8cbbdc1ab93c34a1fe3de0a53f) change(setup): upgrade invenio-checks
- [`997d7487`](https://github.com/inveniosoftware/invenio-rdm-records/commit/997d748788d21979f32d8c83b772b52d74c22736) release: v27.0.0
- [`06559d7b`](https://github.com/inveniosoftware/invenio-rdm-records/commit/06559d7bc2370d2b66c19fadf31164b54ef4d2e8) change(setup): bump invenio-jobs, communities, vocabularies
- [`39eb8d10`](https://github.com/inveniosoftware/invenio-rdm-records/commit/39eb8d1098a4be94f307b30517772da47b3dfbcb) release: v26.0.0
- [`8d556cba`](https://github.com/inveniosoftware/invenio-rdm-records/commit/8d556cbac4eccec61534143266e9635bb5481478) contrib: add thesis template for thesis custom field
- [`1f23a893`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1f23a893c7ff753f019cf00f99b7b579eafaba39) feat(permissions): add `RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD`
- [`1cd121a5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1cd121a5d366616c3824bd490e6dcc27b079a644) Added Arabic translations to vocabularies (thanks to @salaheddine).
- [`5052c102`](https://github.com/inveniosoftware/invenio-rdm-records/commit/5052c102b3acf2cbdcda21f9d15efc89a194ca22) fix: get accordion data-label instead of the label
- [`9451118c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/9451118c1b1f0544bf22c12cec625ef9095ded0d) change(setup): upgrade invenio-communities
- [`a750c4a6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a750c4a6049937ac49426503c3ffa6a56776d5dc) release: v25.0.0
- [`78ebff8c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/78ebff8c0cba4171f6a66cadf916af64d0522092) chore(deps-dev): bump minimatch
- [`53c2ef79`](https://github.com/inveniosoftware/invenio-rdm-records/commit/53c2ef793c7dc0d0f117ef27efbf852342edb63d) release: v24.1.1
- [`8b929f4d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/8b929f4dc178f380c7be2da47e2931d2eec67f97) fix(ui-access-status): show login hint for restricted files
- [`56134646`](https://github.com/inveniosoftware/invenio-rdm-records/commit/56134646cb9fa8dee2bbb7a77ccb658d2e48ff4c) release: v24.1.0
- [`179949e8`](https://github.com/inveniosoftware/invenio-rdm-records/commit/179949e80620fc20d77c729c97aa95035c8c63f5) feat(facets): add publication date facet
- [`b281d8a5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/b281d8a58d19892d15b45133179378df8a30bdd1) fix(request-events): include anchor method in override
- [`f05da56c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/f05da56c676c5768b196da8fbe26bcd0f84179b0) fix: use role IDs instead of names.
- [`7c8ad928`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7c8ad928502a8f7e58d43997df3628a649f0b82f) refactor(schema): remove usage of object_key
- [`eaa4ba42`](https://github.com/inveniosoftware/invenio-rdm-records/commit/eaa4ba426a1a5f9ae192461105fb109183444b2a) refactor: remove usage of is_parent context
- [`cceae746`](https://github.com/inveniosoftware/invenio-rdm-records/commit/cceae746b70f8cf2b4d861e3a5f97cf9d5dfeab1) refactor: remove max_number form context
- [`13beec19`](https://github.com/inveniosoftware/invenio-rdm-records/commit/13beec1948b6c44f36ae428fe26aeba976fdf297) fix:  DeprecationWarning
- [`63cdadb6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/63cdadb69962570af2ed5c57557dcabd4b072ba5) fix(chore): DeprecationWarning stdlib
- [`67f7383a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/67f7383aad45fa99f08056640d88e436dd6cd504) fix(chore): LegacyAPIWarning sqlalchemy
- [`1251445d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1251445dd6cc0d78d696fe914e3561981d09dcc4) fix(chore): DeprecationWarning stdlib
- [`c2162d7a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/c2162d7aade42a4351649be572ae183c4f28baa7) fix(chore): RemovedInMarshmallow4Warning
- [`1106820c`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1106820c01b89e99ed74448337e4164bc5c9722b) fix(chore): RemovedInMarshmallow4Warning
- [`275f67b8`](https://github.com/inveniosoftware/invenio-rdm-records/commit/275f67b8eae825892a8ca7718931b7374d126cb5) fix(js): react warnings
- [`1006ef55`](https://github.com/inveniosoftware/invenio-rdm-records/commit/1006ef557bbe956e0d7777293823d9838a198092) fix(Warning): Received  for a non-boolean attribute .
- [`efd0b9b6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/efd0b9b63aa2c473f7f9680007b4bb615f724aca) fix:  PytestCollectionWarning
- [`a18ed708`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a18ed708e1b55d293cf6e7d1224e3b7be02e8f6c) fix: FutureWarning
- [`57d5ed51`](https://github.com/inveniosoftware/invenio-rdm-records/commit/57d5ed5100f7b48fe33285ffe92cf30af7b67090) fix: ChangedInMarshmallow4Warning
- [`53bcd691`](https://github.com/inveniosoftware/invenio-rdm-records/commit/53bcd691e875ca509dc552a3b5586a4ad97aa6a9) fix: SyntaxWarning: "\d" is invalid
- [`266d7110`](https://github.com/inveniosoftware/invenio-rdm-records/commit/266d7110cdbbc6d6c34be96dcc92d40c433fe9af) revert: part of utcnow fix
- [`a2e1c121`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a2e1c1214a343744a1fa57fc8b4c08028934b329) refactor: replace deprecated Link usage
- [`bead6b34`](https://github.com/inveniosoftware/invenio-rdm-records/commit/bead6b34deb1250d5c802fcb1e8eab7b02c40d90) chore(black): update formatting to >= 26.0
- [`0cda23cf`](https://github.com/inveniosoftware/invenio-rdm-records/commit/0cda23cfea3ed4e2ce3d1ad899a34db21d282c3a) refactor(Link): take into account upstream changes
- [`ccc452b8`](https://github.com/inveniosoftware/invenio-rdm-records/commit/ccc452b8107d0031f0c9355f49db2a964b51cc81) chore(setup): bump dependencies
- [`050d74bb`](https://github.com/inveniosoftware/invenio-rdm-records/commit/050d74bba50bade35db2e92016c15e39810bcb20) release: v24.0.0
- [`2db229bf`](https://github.com/inveniosoftware/invenio-rdm-records/commit/2db229bf0687bc976b250dd38a3991b2ed1bce0f) fix(access_requests_ui): Fix view for guest when receiver isnt community
- [`4672a2e6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/4672a2e6be5b223ffcb6aa7f05a85a776138f88c) fix(deposit): prevent Enter key from removing array field rows
- [`b201ebd5`](https://github.com/inveniosoftware/invenio-rdm-records/commit/b201ebd50b0777c1dc690f8063e0f2b336e76214) release: v23.2.2
- [`55ce95b9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/55ce95b9a5eda75be517c63d35f20bbe4ba6b3ab) release: v23.2.1
- [`a38881fb`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a38881fbdb47f24655440094c8f70c8b1b615a4d) fix(request_policies): allow system user to modify files
- [`00e90ec9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/00e90ec96c2792e3406c6c4502ca6a372e9bbc62) fix(permissions): allow system user to manage files
- [`eb7205f8`](https://github.com/inveniosoftware/invenio-rdm-records/commit/eb7205f833c9313a62e737e085b09e496d3dfb47) chore: black 26.1.0 formatting
- [`6a3e7738`](https://github.com/inveniosoftware/invenio-rdm-records/commit/6a3e7738fbc2aa9b7563c0d31de0a3f314cd3790) chore: black formatting python3.9 compatability
- [`7d8b34b1`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7d8b34b16f5076732355969f15613c01b8b73372) files: fix for pending files with long names
- [`18e26ce9`](https://github.com/inveniosoftware/invenio-rdm-records/commit/18e26ce9cda7211649e29ba0c99670f000caabec) fix(deposit): rename conflicting prop func
- [`958c1bec`](https://github.com/inveniosoftware/invenio-rdm-records/commit/958c1bec64c5fd7debd9a94edf8997790b267fc2) fix(requests): inherit from BaseRequest to fix self_html links
- [`7cc13708`](https://github.com/inveniosoftware/invenio-rdm-records/commit/7cc1370813e85b188f3dd75250c85f92673763fe) release: v23.2.0
- [`dca31207`](https://github.com/inveniosoftware/invenio-rdm-records/commit/dca312077a60c68164ebd76f50344d826601ac2e) fix(tests): update wikidata identifier
- [`6a54bd00`](https://github.com/inveniosoftware/invenio-rdm-records/commit/6a54bd00fd9ad33e38876e9ccb7acb2ac5f24a15) fix: The character 'U+fe0f' is invisible.
- [`af4fb45f`](https://github.com/inveniosoftware/invenio-rdm-records/commit/af4fb45f2d0495f35292a5d327b7def910e57b23) Add Arabic translations for resource types
- [`9b9e0201`](https://github.com/inveniosoftware/invenio-rdm-records/commit/9b9e0201d8968c1c29ece91117ae62411dfeea66) fix(schema): take the list of allowed tags and attrs from the app config
- [`5e2bdec4`](https://github.com/inveniosoftware/invenio-rdm-records/commit/5e2bdec470950924eb1f24ddc7c80c8d20b3c1ca) 📦 release: v23.1.1
- [`4cbe615f`](https://github.com/inveniosoftware/invenio-rdm-records/commit/4cbe615fad3270dac0fd7334b6e923fd95b9e1c8) bibtex: schema: add publication-thesis for compatibility
- [`e5dfe9c6`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e5dfe9c65fbb369349012f14d39a029589ed6854) 📦 release: v23.1.0
- [`a0e62fee`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a0e62fee171bdcc81965fc9aff64dd12f784a4ca) feat(config): validate WikiData IDs for locations
- [`4c0ef91f`](https://github.com/inveniosoftware/invenio-rdm-records/commit/4c0ef91f9eace178749fed5253dcc5870d05f27f) fix(tests): use valid WikiData IDs and Geonames in fixtures
- [`a2580edc`](https://github.com/inveniosoftware/invenio-rdm-records/commit/a2580edc5b0661c9617f05224e6ef0388b659aa8) feat: add wikidata identifier to known identifier schemes
- [`d554b972`](https://github.com/inveniosoftware/invenio-rdm-records/commit/d554b9721ef1593eeef17e9ab269f77db4cb55b4) serializers: use datapackage mediatype
- [`ce4caa49`](https://github.com/inveniosoftware/invenio-rdm-records/commit/ce4caa491d0cd8651ce771d631ff13c22ada7e08) fix(tests): make logic to restore last revision more robust
- [`e2af196b`](https://github.com/inveniosoftware/invenio-rdm-records/commit/e2af196b32a1d09b904898a501a386a12fd62582) feat(permissions): add reply_comment permission
- [`3057378d`](https://github.com/inveniosoftware/invenio-rdm-records/commit/3057378d74b2ab9caa8a9e2054cb584bb52eb983) chore(setup): bump major versions
- [`58562e8a`](https://github.com/inveniosoftware/invenio-rdm-records/commit/58562e8a11058cc8f0edae33d9c01c8d6d9b3a34) release: v23.0.0

#### `invenio-records` 4.0.0 💥
[3.1.1 → 4.0.0](https://github.com/inveniosoftware/invenio-records/compare/v3.1.1...v4.0.0)

- [`13c7fb05`](https://github.com/inveniosoftware/invenio-records/commit/13c7fb05bd4ad039a0c4c549791faeb307adbd6b) fix(chore): DeprecationWarning stdlib
- [`27ba3444`](https://github.com/inveniosoftware/invenio-records/commit/27ba3444217a9e3c350376a61d2fcf0e27a3e4f1) fix: refresolver deprecationwarning
- [`266853a5`](https://github.com/inveniosoftware/invenio-records/commit/266853a551ba152f16dd69e920c01d87373b71cb) chore(tests): get rid of SAWarning
- [`f69bbe4c`](https://github.com/inveniosoftware/invenio-records/commit/f69bbe4c482c56d27fa3864d723e503f5169d804) chore(black): update formatting to >= 26.0
- [`fa998f37`](https://github.com/inveniosoftware/invenio-records/commit/fa998f37e28d8763a0ecb5f62f3b2653b172a0fd) fix(docs): reference target not found
- [`1f4249fb`](https://github.com/inveniosoftware/invenio-records/commit/1f4249fbaf4442ccbdf5870ecb4a0feb2ece5bdc) release: v4.0.0
- [`4c382f6d`](https://github.com/inveniosoftware/invenio-records/commit/4c382f6dc1d5bf78fd5ccd46e197a1d52a4a18eb) fix: extend support to Python 3.14

#### `invenio-records-files` 2.0.0 💥
[1.2.1 → 2.0.0](https://github.com/inveniosoftware/invenio-records-files/compare/v1.2.1...v2.0.0)

- [`ab0bbde8`](https://github.com/inveniosoftware/invenio-records-files/commit/ab0bbde8aa118a687cb80ba390ca864efa10e81b) chore(setup): bump dependencies
- [`fc602df1`](https://github.com/inveniosoftware/invenio-records-files/commit/fc602df171061a0b8adb2dc3a732d7e074d3c35b) fix: PytestDeprecationWarning
- [`36b4bc53`](https://github.com/inveniosoftware/invenio-records-files/commit/36b4bc534cd809f0c248071c4ad48573a6e3d471) chore(context): apply marshmallow context change
- [`1405225e`](https://github.com/inveniosoftware/invenio-records-files/commit/1405225ed3b5a813bbec8a68c81fd106afcee64c) release: v2.0.0
- [`0c75c89b`](https://github.com/inveniosoftware/invenio-records-files/commit/0c75c89ba1889efecf6c43ba9e3aeb129ecc1f2a) migrate setup.py to setup.cfg
- [`030f63c1`](https://github.com/inveniosoftware/invenio-records-files/commit/030f63c1088e814eec8e0961fc3e7cc35199ac72) migrate to use black as opinionated auto formater
- [`ca7bef86`](https://github.com/inveniosoftware/invenio-records-files/commit/ca7bef86dd2302e951f451b40d6c05217041ac2c) add .git-blame-ignore-revs
- [`ed7a49c4`](https://github.com/inveniosoftware/invenio-records-files/commit/ed7a49c40a6524e0252da8bd3dc251a7c22dc3d6) fix docs compatibilty problem with Sphinx>=5.0.0
- [`4bf4401f`](https://github.com/inveniosoftware/invenio-records-files/commit/4bf4401f20046673329ae59402b4e9d63e74c608) move check_manifest configuration to setup.cfg.
- [`596b7e68`](https://github.com/inveniosoftware/invenio-records-files/commit/596b7e68f4d9813585bcd4c92a5f91c74ec23545) increase minimal python version to 3.7
- [`fd687b95`](https://github.com/inveniosoftware/invenio-records-files/commit/fd687b951b19811c84f497925ad50db633c8b3ea) global: clean test infrastructure
- [`ee5ce782`](https://github.com/inveniosoftware/invenio-records-files/commit/ee5ce7821248f48e93f455358a43a83e77160851) fix: setuptools require underscores instead of dashes
- [`74d9a5eb`](https://github.com/inveniosoftware/invenio-records-files/commit/74d9a5eb28d333bb3974281a80d18836d9620c2a) setup: change to reusable workflows
- [`79057ec6`](https://github.com/inveniosoftware/invenio-records-files/commit/79057ec62c363d11ffaeb7fe87ed16abe95385f0) fix: sphinxwarning
- [`667d5271`](https://github.com/inveniosoftware/invenio-records-files/commit/667d527168e476f3bb821eed80f7257e88b1c480) fix: missing module data.v7
- [`5fa90934`](https://github.com/inveniosoftware/invenio-records-files/commit/5fa909340818b29fc61f1c065097959623243d40) fix: no module imp
- [`a128f51b`](https://github.com/inveniosoftware/invenio-records-files/commit/a128f51bc69f8e335cbb63a5205888d02a372a1c) global: add compatibility to sqlalchemy >= 2.0
- [`365235bd`](https://github.com/inveniosoftware/invenio-records-files/commit/365235bd0903245efb453ef253ff3d8c73e7d6fc) fix(tests): skip alembic test
- [`05df4fd8`](https://github.com/inveniosoftware/invenio-records-files/commit/05df4fd85061d211462b4262cd1a097393e5691e) chore(setup): to be backwards compatible
- [`9ff3e34a`](https://github.com/inveniosoftware/invenio-records-files/commit/9ff3e34a51666f003056709d97b8e28480409668) chore(black): update formatting to >= 26.0
- [`8482aa21`](https://github.com/inveniosoftware/invenio-records-files/commit/8482aa21788cd18a7ba16c8985f3cc31093ffb23) fix(docs): not found attr
- [`16724215`](https://github.com/inveniosoftware/invenio-records-files/commit/16724215f277e481a6ce9a2ea29aeac38d3c447d) release: v1.2.2
- [`52f15ae6`](https://github.com/inveniosoftware/invenio-records-files/commit/52f15ae6b2c086d7696422732a91430c8cc6ba78) model: add bucket id index
- [`2bd12eb4`](https://github.com/inveniosoftware/invenio-records-files/commit/2bd12eb4999fafef784226442642f2ed4821c6c2) fix tests
- [`39752eb0`](https://github.com/inveniosoftware/invenio-records-files/commit/39752eb08b5041ab8eeb1a7e37ea23e78158a30f) update copyright
- [`5a2e92b3`](https://github.com/inveniosoftware/invenio-records-files/commit/5a2e92b3b3a3e5c955a7034daca30f5c58608b30) global: migrate CI to gh-actions
- [`1546ef45`](https://github.com/inveniosoftware/invenio-records-files/commit/1546ef4517816f12d3000b7d36c2cf9a422f4541) travis: update python matrix

#### `invenio-records-permissions` 2.0.1 💥
[1.2.1 → 2.0.1](https://github.com/inveniosoftware/invenio-records-permissions/compare/v1.2.1...v2.0.1)

- [`1319da74`](https://github.com/inveniosoftware/invenio-records-permissions/commit/1319da740c347f79700f7268cf0bc0dc3456f93b) release: v2.0.1
- [`26ff4b34`](https://github.com/inveniosoftware/invenio-records-permissions/commit/26ff4b34f129262219033c13a143226ea2eb75c9) fix(tests): check role.id instead of role.name
- [`fb78182c`](https://github.com/inveniosoftware/invenio-records-permissions/commit/fb78182c43776ec264d9b901fce3c5559f6bc8ab) chore(setup): bump dependencies
- [`6f4dde42`](https://github.com/inveniosoftware/invenio-records-permissions/commit/6f4dde42036025277a5ce8c8b4c9989fa04f5091) chore(black): update formatting to >= 26.0
- [`4923cdbc`](https://github.com/inveniosoftware/invenio-records-permissions/commit/4923cdbc7a07b67571a3f22c602d009c167371a3) release: v2.0.0

#### `invenio-records-resources` 9.1.0+oarepo.4.ojib3jsuu4wnrkln 💥
[8.7.1.44682796 → 9.1.0+oarepo.4.ojib3jsuu4wnrkln](https://github.com/inveniosoftware/invenio-records-resources/compare/v8.7.1...v9.1.0)

- [`45611a9a`](https://github.com/inveniosoftware/invenio-records-resources/commit/45611a9a6e8fb34ee64efbd9cfa3851b69622c60) release: v9.1.0
- [`9d25108a`](https://github.com/inveniosoftware/invenio-records-resources/commit/9d25108af145eee8f52c0ed811db762c757ad829) feat(facets): add DateFacet for date histogram ranges
- [`a61383d4`](https://github.com/inveniosoftware/invenio-records-resources/commit/a61383d4f0a36a973e494183519b5e43cf474ac5) tests: add DateFacet tests
- [`48ee7867`](https://github.com/inveniosoftware/invenio-records-resources/commit/48ee7867bc1a9de392b777295fbea19489ff483e) refactor: remove context usage
- [`92bac2e9`](https://github.com/inveniosoftware/invenio-records-resources/commit/92bac2e90a435ca582ff7775ce92291ca21e52cb) fix: removed dependency on PyFilesystem2
- [`ffe861d9`](https://github.com/inveniosoftware/invenio-records-resources/commit/ffe861d941f26f25fe7aac422ec37d93e3f8a7cf) fix(chore): DeprecationWarning stdlib
- [`094714b6`](https://github.com/inveniosoftware/invenio-records-resources/commit/094714b658fb6d935b2b2617055f81f6280fff35) fix: RemovedInMarshmallow4Warning
- [`ce387e0f`](https://github.com/inveniosoftware/invenio-records-resources/commit/ce387e0f6ecb5bb5fd3d1b9efc35389418fce3c5) fix: RemovedInMarshmallow4Warning
- [`b29745ea`](https://github.com/inveniosoftware/invenio-records-resources/commit/b29745ea9c5b3eb86bd4d4eaa43ffd516c6687c7) chore: remove warnings
- [`14c17c96`](https://github.com/inveniosoftware/invenio-records-resources/commit/14c17c96094dd49430108365b373efbc3f8ddf90) fix: DeprecationWarning from invenio-indexer
- [`c0189672`](https://github.com/inveniosoftware/invenio-records-resources/commit/c0189672c34f2cd767a83ee42db0e4fae4c1ffcc) chore(setup): bump dependencies
- [`a8b47a55`](https://github.com/inveniosoftware/invenio-records-resources/commit/a8b47a55c413417fb75c14f302ccce3f9d741908) release: v9.0.0
- [`c12c5740`](https://github.com/inveniosoftware/invenio-records-resources/commit/c12c5740cefdba80282a10088d29cf09f1c9ff7b) fix: avoid deepcopy in EndpointLink bc of possible problematic context content
- [`d511460d`](https://github.com/inveniosoftware/invenio-records-resources/commit/d511460dfa61ccfe6f76774b7c7136d6c4c7d6c5) fix: re-add removed import
- [`19399948`](https://github.com/inveniosoftware/invenio-records-resources/commit/19399948ebbe1ef4858b694fe1ed0d527fdb308b) fix: black formatting
- [`feade7f3`](https://github.com/inveniosoftware/invenio-records-resources/commit/feade7f345b7cadd3e5b10ecd4ccd15424fab7d2) refactor: use EndpointLink in RecordTypeFactory [+]
- [`573de217`](https://github.com/inveniosoftware/invenio-records-resources/commit/573de217337d7f782796dcb44718f50d427df1ad) feat: add support for anchor in EndpointLink
- [`77d064f1`](https://github.com/inveniosoftware/invenio-records-resources/commit/77d064f16569d87e1aeb3baa1003ff694922459c) feat: expose FileEndpointLink at services import level
- [`ee953717`](https://github.com/inveniosoftware/invenio-records-resources/commit/ee95371797c4cf694b1ea8ac45734f3822e746af) release: v8.8.0
- [`32b854c7`](https://github.com/inveniosoftware/invenio-records-resources/commit/32b854c7343d5264d3d1690b0f0e056217a44118) fix(files-mgr): remember file information before write operations
- [`39bcb9bf`](https://github.com/inveniosoftware/invenio-records-resources/commit/39bcb9bf627d678b85a59f7e3c12c33c3eec7ab5) fix(files-svc): clean up broken FileInstances when an upload fails
- [`a5c2ecb7`](https://github.com/inveniosoftware/invenio-records-resources/commit/a5c2ecb7f22b873523277847b82b7330787b00ea) feat(search): allow enforcing a max page size

#### `invenio-records-rest` 4.1.0 💥
[3.2.1 → 4.1.0](https://github.com/inveniosoftware/invenio-records-rest/compare/v3.2.1...v4.1.0)

- [`1c11fbb6`](https://github.com/inveniosoftware/invenio-records-rest/commit/1c11fbb61ea60b87a0120fe43ea3942e84a01260) chore: compatibility webargs > 6.0.0
- [`749ad8f1`](https://github.com/inveniosoftware/invenio-records-rest/commit/749ad8f1114b6ac3a59d1ca08fc151fc9f906fc6) release: v4.1.0
- [`b22507bd`](https://github.com/inveniosoftware/invenio-records-rest/commit/b22507bd39df73816fc2f954f98965f9b5ba5f24) chore(setup): bump dependencies
- [`e5d90b77`](https://github.com/inveniosoftware/invenio-records-rest/commit/e5d90b779a2b1fbda4e82a1d9b3d2b48c5a76987) fix(chore): DeprecationWarning stdlib
- [`91654986`](https://github.com/inveniosoftware/invenio-records-rest/commit/916549868a7ddaaa2ef6005a0b0965da4727b07b) fix: PendingDeprecationWarning
- [`e59fb230`](https://github.com/inveniosoftware/invenio-records-rest/commit/e59fb230e29cbb7b5913a7dfc3185f7509ced571) fix: RemovedInMarshmallow4Warning
- [`3aecaacb`](https://github.com/inveniosoftware/invenio-records-rest/commit/3aecaacb853bf53c99012777c247d1ef607e423b) fix: RemovedInMarshmallow4Warning
- [`51c07c14`](https://github.com/inveniosoftware/invenio-records-rest/commit/51c07c14f20ae78ff1689f63080778d3dd085b5e) fix: RemovedInMarshmallow4Warning
- [`43d91ffc`](https://github.com/inveniosoftware/invenio-records-rest/commit/43d91ffc24afdb05777faa807ed80e1bd58a3931) chore: apply changes for marshmallow context
- [`58cde43e`](https://github.com/inveniosoftware/invenio-records-rest/commit/58cde43e22683988ea56b8fd311f42bba8d2aa04) release: v4.0.0
- [`06db8685`](https://github.com/inveniosoftware/invenio-records-rest/commit/06db8685029823a571542178e322bbe3e6544806) i18n: pulled translations

#### `invenio-records-ui` 3.0.0 💥
[2.1.2 → 3.0.0](https://github.com/inveniosoftware/invenio-records-ui/compare/v2.1.2...v3.0.0)

- [`512383be`](https://github.com/inveniosoftware/invenio-records-ui/commit/512383bedc29bf928667a5f3f9c41613e62bef2e) chore(setup): bump dependencies
- [`b6bb44f4`](https://github.com/inveniosoftware/invenio-records-ui/commit/b6bb44f47970ada86add26b8604b079ae827de4e) release: v3.0.0

#### `invenio-requests` 12.3.1+oarepo.2.6uloldct77ahzc5b 💥
[10.5.0.36628667 → 12.3.1+oarepo.2.6uloldct77ahzc5b](https://github.com/inveniosoftware/invenio-requests/compare/v10.5.0...v12.3.1)

- [`bcbf67fe`](https://github.com/inveniosoftware/invenio-requests/commit/bcbf67fe452c9c2434a934482c36843e1cf69acf) release: v12.3.1
- [`cd7a165c`](https://github.com/inveniosoftware/invenio-requests/commit/cd7a165ca5e9064bb7798d842984bd16ec041bee) fix(RequestMetadata): pass required props to the <Overridable>
- [`4a2192b4`](https://github.com/inveniosoftware/invenio-requests/commit/4a2192b42e612bfc6b90764dd7137ee11aa7ece2) feat: deep link for replies
- [`97e60f2f`](https://github.com/inveniosoftware/invenio-requests/commit/97e60f2f640f1ef3b96af995c152b477dd83465a) feat: make messages collapsible
- [`8e35c64b`](https://github.com/inveniosoftware/invenio-requests/commit/8e35c64bb530a46962e67b579110308d6f42e59f) fix: defer dataset extraction
- [`3eabdd7a`](https://github.com/inveniosoftware/invenio-requests/commit/3eabdd7a383576ad3fb340c71ffc4ae0ed4f933e) refactor: move dataset values to React context
- [`4ba940c3`](https://github.com/inveniosoftware/invenio-requests/commit/4ba940c31ba58d19f9206c4b8f75a2db8754fd78) fix: timeline event body forward ref
- [`079a5ed2`](https://github.com/inveniosoftware/invenio-requests/commit/079a5ed29a7b7580a78f548177ec9468952bdbf7) feature: comments files (#571)
- [`937837c6`](https://github.com/inveniosoftware/invenio-requests/commit/937837c6a6d5124296cdeefb9b968cff4f425446) fix(timeline): resize detection for comment body
- [`55c3b0ab`](https://github.com/inveniosoftware/invenio-requests/commit/55c3b0abf10fd174108aa04ccd8ebe242b876dd0) fix(files): Add 'not found' handler for file UI endpoint
- [`62e54bb5`](https://github.com/inveniosoftware/invenio-requests/commit/62e54bb532b6a2650f342f557d49d70d0fcd2684) fix(timeline): prevent infinite re-rendering of comment editor
- [`01b7f412`](https://github.com/inveniosoftware/invenio-requests/commit/01b7f412e911758aedbc54fe40f75c64420833a7) tests: skip alembic test
- [`547ede92`](https://github.com/inveniosoftware/invenio-requests/commit/547ede92542de0ec4e579dbe462616b29192e9b1) release: v12.3.0
- [`a68d845b`](https://github.com/inveniosoftware/invenio-requests/commit/a68d845bf5b55e1faa117575ebec462bae64ac78) fix(events): add back support for #commentevent anchor
- [`b5221693`](https://github.com/inveniosoftware/invenio-requests/commit/b52216938626d02c2915c1222d6d8234960ba660) release: v12.2.1
- [`6a633dca`](https://github.com/inveniosoftware/invenio-requests/commit/6a633dca063cedfd829bd732f547b967ce76a9d6) release: v12.2.0
- [`643ec6b0`](https://github.com/inveniosoftware/invenio-requests/commit/643ec6b0671562898450c42fc2b3f44f8d90345e) fix: role name to role id in request creation
- [`446689b7`](https://github.com/inveniosoftware/invenio-requests/commit/446689b731d6e5addae7a21cc22d279a78947876) fix: disable comment button when message is empty
- [`19e88deb`](https://github.com/inveniosoftware/invenio-requests/commit/19e88deb2b1611d477d881258ab5efbdcac53c31) feat: enable deepcopy for AttrProxy
- [`c7383b18`](https://github.com/inveniosoftware/invenio-requests/commit/c7383b1805bfbef50a4c1c14a3a2d55eaa78822b) release: v12.1.0
- [`6b16a93f`](https://github.com/inveniosoftware/invenio-requests/commit/6b16a93fcaa75b0b13727d8bf4b39d91fa1e6aee) refactor: move to context_schema
- [`5a355eea`](https://github.com/inveniosoftware/invenio-requests/commit/5a355eea1a34b62bd77fd4df807ae70735de458d) fix(chore): DeprecationWarning stdlib
- [`4bd01915`](https://github.com/inveniosoftware/invenio-requests/commit/4bd01915f31f627b6d8e2482ce1803798d0a75aa) fix: DeprecationWarning pytest-invenio
- [`3134e539`](https://github.com/inveniosoftware/invenio-requests/commit/3134e5393413fb6d8ab82fe69b785d9a583f6b01) fix:  PytestCollectionWarning
- [`1b97f51b`](https://github.com/inveniosoftware/invenio-requests/commit/1b97f51b64f34bf7be3e0025be0ec5a49f774e1b) chore(setup): bump dependencies
- [`961a1911`](https://github.com/inveniosoftware/invenio-requests/commit/961a1911cbb933c8d52ab927f7b9894044bcd5b9) refactor!: replace deprecated Link usage [+]
- [`65757301`](https://github.com/inveniosoftware/invenio-requests/commit/6575730169b393e55c0ce4412fab2392a5dd63fe) chore(tests): replace deprecated es_clear fixture by search_clear
- [`0159ee57`](https://github.com/inveniosoftware/invenio-requests/commit/0159ee5719c0b968b3493d809c2c38a446cfe620) refactor: refine mechanism for EndpointLinks dependent on RequestType
- [`457cc66f`](https://github.com/inveniosoftware/invenio-requests/commit/457cc66f1a495856b2456346a36e4c62bc7d90e9) chore(lint): lint for Black 26
- [`5c546405`](https://github.com/inveniosoftware/invenio-requests/commit/5c54640520e71d45592d3ad1906a4ccbad695130) refactor: rename comment(s) links
- [`6794a4f2`](https://github.com/inveniosoftware/invenio-requests/commit/6794a4f2f975e724f4c27ba1e3817cd482735be1) fix(tests): provide fake administration views for upgraded users-resources
- [`b9247dd7`](https://github.com/inveniosoftware/invenio-requests/commit/b9247dd746dcc737d20a87755ba9f037bfd6c924) fix(compatibility): TypeError
- [`f953d8c1`](https://github.com/inveniosoftware/invenio-requests/commit/f953d8c1bdcf51f751670168f94995e0fb4cfc8e) release: v12.0.0
- [`a607d169`](https://github.com/inveniosoftware/invenio-requests/commit/a607d169019b4f10c886e0222374508cd93cbc9e) chore: black 26.1.0 formatting
- [`fab6ede1`](https://github.com/inveniosoftware/invenio-requests/commit/fab6ede1c2dbdb736adccbca195e80aca5fc89a4) CHANGES: fix typo in year
- [`d2bf9d7d`](https://github.com/inveniosoftware/invenio-requests/commit/d2bf9d7dbbed4d8b45a991ba50e0d9ca08746ff9) release: v11.2.3
- [`c9caa35a`](https://github.com/inveniosoftware/invenio-requests/commit/c9caa35a1d204090075cea6c739dfdeb4b320bae) fix(timeline): support showing replies preview for timeline_focused endpoint
- [`0d4d4e3a`](https://github.com/inveniosoftware/invenio-requests/commit/0d4d4e3a9a9615d1a712c6399dd88404b8d3ce67) release: v11.2.2
- [`3cb56825`](https://github.com/inveniosoftware/invenio-requests/commit/3cb568257d5cd4a305a756aebb88e47184b3f4c6) fix(request-metadata): missing record link
- [`c299bc56`](https://github.com/inveniosoftware/invenio-requests/commit/c299bc566579ee620ad4ce39ec0574fbc444e198) fix(routes): use UUID type for request identifiers
- [`01c6bbf4`](https://github.com/inveniosoftware/invenio-requests/commit/01c6bbf4010da37207d9b695a767c134dc6db68c) release: v11.2.1
- [`baa587fb`](https://github.com/inveniosoftware/invenio-requests/commit/baa587fb3d0f881570577f4f08036889b51106f9) fix(comment-editor): ensure disabled when can_create_comment is false
- [`132c0365`](https://github.com/inveniosoftware/invenio-requests/commit/132c03659d7fb25acc32d576277c1f7396d3bf55) fix(timeline): small typo in state reducer
- [`c22a17aa`](https://github.com/inveniosoftware/invenio-requests/commit/c22a17aa1d38fc853802c48cd11464d8673928d0) fix(timeline): missing `expand` parameter to timeline_focused service handler
- [`90aef2e4`](https://github.com/inveniosoftware/invenio-requests/commit/90aef2e445993ed196dda3da431ab558d68e5a82) fix(timeline): incorrect pagination for deep-linked comments
- [`79f87f87`](https://github.com/inveniosoftware/invenio-requests/commit/79f87f8765463458e770a9241d96439cfcd4f15b) fix(comment-editor): ensure disabled when can_create_comment is false
- [`629de244`](https://github.com/inveniosoftware/invenio-requests/commit/629de2442b8eaf88d549c70800056b653a29a8a0) release: v11.2.0
- [`9c346582`](https://github.com/inveniosoftware/invenio-requests/commit/9c346582da010687c0f4200d07036fcc75f8ffbf) feat(comments): replace pagination with "collapsed" section design
- [`92036c83`](https://github.com/inveniosoftware/invenio-requests/commit/92036c83a4e888f93c254a438e7857c9a4507976) fix(timeline): pass correct props to TimelineEventBody
- [`3790ed5c`](https://github.com/inveniosoftware/invenio-requests/commit/3790ed5c65f98dce708b240e854bc2fa60cc9639) release: v11.1.0
- [`bf3df44b`](https://github.com/inveniosoftware/invenio-requests/commit/bf3df44b8eddcb9a7f6415092ac321fa0ba2a8c7) fix(reducer): remove unused PARENT_APPEND_DRAFT_CONTENT action
- [`090ba17e`](https://github.com/inveniosoftware/invenio-requests/commit/090ba17ea4acacb936040ae6f12a7cc98004c059) feat(comment-replies): implement frontend for threaded replies
- [`baf95530`](https://github.com/inveniosoftware/invenio-requests/commit/baf95530a592f1f3c81890b6b043bee1430a0d8f) fix(comment-replies): minor fixes and refactoring of frontend
- [`6da05c5c`](https://github.com/inveniosoftware/invenio-requests/commit/6da05c5c34db6900203abb4a889ecc5db9b8e0b9) feat(comment-replies): disable input box if user cannot reply
- [`4173b878`](https://github.com/inveniosoftware/invenio-requests/commit/4173b8783e413c473610cf19b3aecc3c504c69ba) fix(errors): Pass default description message
- [`ab6db6dd`](https://github.com/inveniosoftware/invenio-requests/commit/ab6db6dd89338afc0c1376f6509d593d00a29b9f) release: v11.0.0
- [`e62da7f8`](https://github.com/inveniosoftware/invenio-requests/commit/e62da7f899db4ce75f746140b499c63a1f475151) feat(comment-replies): add single threading on comments
- [`beeb9dc3`](https://github.com/inveniosoftware/invenio-requests/commit/beeb9dc3e97d8c7d5a9a5b0eeffe6be81bf850ba) fix(timeline): move mathjax render to TimelineEventBody
- [`0dd42828`](https://github.com/inveniosoftware/invenio-requests/commit/0dd42828ec437ed80109aa9984c0603bf1592430) fix(TimelineCommentEvent): Render LaTeX on save/cancel
- [`3dd87e6c`](https://github.com/inveniosoftware/invenio-requests/commit/3dd87e6c96b4ad3c45f9d1c7dd0e050dd30a9424) fix(LockRequest): Change PopupComponent prop type to func

#### `invenio-rest` 3.0.1 💥
[2.0.5 → 3.0.1](https://github.com/inveniosoftware/invenio-rest/compare/v2.0.5...v3.0.1)

- [`5ef1e7d6`](https://github.com/inveniosoftware/invenio-rest/commit/5ef1e7d6195b2f3f312a136b627fdb0af71d4231) chore(setup): unpin webargs
- [`8bcb0c75`](https://github.com/inveniosoftware/invenio-rest/commit/8bcb0c754d445bcc3554de151ec9a5da18221b85) release: v3.0.1
- [`43cd3279`](https://github.com/inveniosoftware/invenio-rest/commit/43cd32799f094529276522cd41d0bf1138cd4567) refactor: use context_schema
- [`82ef67ea`](https://github.com/inveniosoftware/invenio-rest/commit/82ef67ea9ca03e6eb2a7c1a286e372a8fdfbe045) fix(chore): DeprecationWarning stdlib
- [`7422072f`](https://github.com/inveniosoftware/invenio-rest/commit/7422072f928a2cecfc44ca84ca1f88da8fd16713) fix(tests): PendingDeprecationWarning
- [`dd268e19`](https://github.com/inveniosoftware/invenio-rest/commit/dd268e1911959118826143905f8161450f543a77) chore(setup): bump dependencies
- [`2111adf5`](https://github.com/inveniosoftware/invenio-rest/commit/2111adf5181bcc8475cd3b7ef9c1f7e40c06cea4) release: v3.0.0

#### `invenio-s3` 4.0.0 💥
[3.0.2 → 4.0.0](https://github.com/inveniosoftware/invenio-s3/compare/v3.0.2...v4.0.0)

- [`e768e644`](https://github.com/inveniosoftware/invenio-s3/commit/e768e644dcd814456a028ee341a9743088493540) chore(setup): bump dependencies
- [`115aac1e`](https://github.com/inveniosoftware/invenio-s3/commit/115aac1ebf5586137673623368a0dc31e1515b8b) release: v4.0.0

#### `invenio-search` 3.1.2+oarepo.4.uwz7uudxhtm36x5h
[3.1.2.86707846 → 3.1.2+oarepo.4.uwz7uudxhtm36x5h](https://github.com/inveniosoftware/invenio-search/compare/v3.1.2...v3.1.2)


#### `invenio-search-ui` 4.2.0
[4.1.5 → 4.2.0](https://github.com/inveniosoftware/invenio-search-ui/compare/v4.1.5...v4.2.0)

- [`8d8e376a`](https://github.com/inveniosoftware/invenio-search-ui/commit/8d8e376a4286f979856667d1d08ac2c4c44b7eb9) release: v4.2.0
- [`d994605c`](https://github.com/inveniosoftware/invenio-search-ui/commit/d994605ce6cd6199b1ee573e1f30978aae3f67db) feat: add range facets for date aggregations
- [`7249343c`](https://github.com/inveniosoftware/invenio-search-ui/commit/7249343c49478b878504a34bbfceac5f6b988388) fix: pass agg config to BucketAggregation
- [`7389292c`](https://github.com/inveniosoftware/invenio-search-ui/commit/7389292c1623830029e9c6dacbb00b8d1992e13a) search-ui: correct arrow icon in nested facets

#### `invenio-sitemap` 1.0.0 💥
[0.3.0 → 1.0.0](https://github.com/inveniosoftware/invenio-sitemap/compare/v0.3.0...v1.0.0)

- [`df892bba`](https://github.com/inveniosoftware/invenio-sitemap/commit/df892bbae32fe39f811cb912f2885c03d4597c51) chore(setup): bump dependencies
- [`4c25da72`](https://github.com/inveniosoftware/invenio-sitemap/commit/4c25da729aba40f65a1f391fa9a6c94f4bca5d78) chore(black): update formatting to >= 26.0
- [`682ff557`](https://github.com/inveniosoftware/invenio-sitemap/commit/682ff5570570aca7af43826c8cc31a93c375d3a7) release: v1.0.0

#### `invenio-stats` 6.1.2 💥
[5.1.1 → 6.1.2](https://github.com/inveniosoftware/invenio-stats/compare/v5.1.1...v6.1.2)

- [`13392d06`](https://github.com/inveniosoftware/invenio-stats/commit/13392d068fdfb317b10fe55ed3b16564bc7578ba) fix(aggregations): make queries backwards-compatible with non timezone aware indices
- [`cf92934f`](https://github.com/inveniosoftware/invenio-stats/commit/cf92934f484abbc399dd92b0f51f04402dcce3f2) release: v6.1.2
- [`112d0372`](https://github.com/inveniosoftware/invenio-stats/commit/112d037267e02f94491bfa4924ffedf9644885b6) fix(queries): make queries backwards-compatible with non timezone aware indices
- [`dc58a427`](https://github.com/inveniosoftware/invenio-stats/commit/dc58a4278db93bb96cd480c63cdd072e8ab0e17c) release: v6.1.1
- [`d93b5957`](https://github.com/inveniosoftware/invenio-stats/commit/d93b59579844a4bc16485583007015e1363642b9) feat(config): add STATS_EVENTS_UTC_DATETIME_ENABLED flag
- [`24b1e024`](https://github.com/inveniosoftware/invenio-stats/commit/24b1e024caa5c7aba0d7cb8487dd709e5d4f56e3) release: v6.1.0
- [`331cff19`](https://github.com/inveniosoftware/invenio-stats/commit/331cff19f8461a4660a2f0d1845f6e541cb0a1af) fix(chore): DeprecationWarning stdlib
- [`29c79e6a`](https://github.com/inveniosoftware/invenio-stats/commit/29c79e6ad09852b1cb826487a1fec9fb86522281) chore(black): update formatting to >= 26.0
- [`f89b0dee`](https://github.com/inveniosoftware/invenio-stats/commit/f89b0deeb45e6ab10f0cdc2ea4fcf2aa4ab7ff66) chore(setup): bump dependencies
- [`cea19ce1`](https://github.com/inveniosoftware/invenio-stats/commit/cea19ce1359d436eef8ff744ad9cdf5831a6fd91) release: v6.0.0
- [`e29828ed`](https://github.com/inveniosoftware/invenio-stats/commit/e29828edaae747f1c21499c320ae7d7292f1fb16) fix: DeprecationWarning warn use warning
- [`49cfe085`](https://github.com/inveniosoftware/invenio-stats/commit/49cfe08570e663567a6278a3e081d957e2b1baa6) tests: extend support to Python 3.14
- [`efb858a3`](https://github.com/inveniosoftware/invenio-stats/commit/efb858a3500b4c269b02b09f50de382e0c6700fd) i18n:push translations

#### `invenio-theme` 4.6.0
[4.5.0 → 4.6.0](https://github.com/inveniosoftware/invenio-theme/compare/v4.5.0...v4.6.0)

- [`45a9966a`](https://github.com/inveniosoftware/invenio-theme/commit/45a9966a82e8db881575404044748c341821773f) release: 4.6.0
- [`ae0a9e10`](https://github.com/inveniosoftware/invenio-theme/commit/ae0a9e100e2e031368e13f8c2278a4faa0c2b7c2) site: add logs display rules
- [`a144f00c`](https://github.com/inveniosoftware/invenio-theme/commit/a144f00c2df504171cdf4150c1d2a4a90fbdbf6e) chore: reformat black
- [`74dfa068`](https://github.com/inveniosoftware/invenio-theme/commit/74dfa06815421b8c05fa43a0758ffa1361af3f5e) css: add flex rules

#### `invenio-userprofiles` 5.1.0 💥
[4.1.1 → 5.1.0](https://github.com/inveniosoftware/invenio-userprofiles/compare/v4.1.1...v5.1.0)

- [`730633eb`](https://github.com/inveniosoftware/invenio-userprofiles/commit/730633eb108a71a7810c91d1a1e7b2e7fdaa28ee) fix(validation): use invenio-accounts `validate_username` method
- [`d2971ce4`](https://github.com/inveniosoftware/invenio-userprofiles/commit/d2971ce4399b0a7d62f67b1bdfc566090d0da961) release: v5.1.0
- [`193e0361`](https://github.com/inveniosoftware/invenio-userprofiles/commit/193e036186c2534d8812fb709a2a491b62a5211c) chore(setup): bump dependencies
- [`0f5561c9`](https://github.com/inveniosoftware/invenio-userprofiles/commit/0f5561c99bbe54603789e904318920e68918e5d6) release: v5.0.0

#### `invenio-users-resources` 10.4.0 💥
[9.0.3 → 10.4.0](https://github.com/inveniosoftware/invenio-users-resources/compare/v9.0.3...v10.4.0)

- [`6152b49b`](https://github.com/inveniosoftware/invenio-users-resources/commit/6152b49b58d1f8492a99c668c61659db8283bb26) 📦 release: v10.4.0
- [`671463f0`](https://github.com/inveniosoftware/invenio-users-resources/commit/671463f07e358a91bf3519077ccb7d91b5d82828) tests: precise assertions on user search results
- [`df4297da`](https://github.com/inveniosoftware/invenio-users-resources/commit/df4297da12a0ca5020a774d9e5e3e0302e7acaf5) search: improve with CompositeSuggestQueryParser
- [`e85556f8`](https://github.com/inveniosoftware/invenio-users-resources/commit/e85556f85f7bd7b43e035c4ab009862a64dcb6cb) tests: username with a dash
- [`ff70ea28`](https://github.com/inveniosoftware/invenio-users-resources/commit/ff70ea2891f8834156ffcd990d44d0ea7e62fac7) search: fix finding of usernames with dash
- [`e6af6f57`](https://github.com/inveniosoftware/invenio-users-resources/commit/e6af6f57969efb7c71339033550950b3829e0296) release: v10.3.0
- [`e6fb2c84`](https://github.com/inveniosoftware/invenio-users-resources/commit/e6fb2c84ed370f6749a57f57fd8a1781defc989a) fix(groups): resolve role by id instead of name
- [`7f982dc5`](https://github.com/inveniosoftware/invenio-users-resources/commit/7f982dc5d738f37c7a56b5e5861d0055366e7cf8) 📦 release: v10.2.0
- [`7faff425`](https://github.com/inveniosoftware/invenio-users-resources/commit/7faff425e0cbf38ce5493310cf24fd810b3f5643) feat(admin): add groups CRUD and role-aware views
- [`441d4965`](https://github.com/inveniosoftware/invenio-users-resources/commit/441d4965ea2e84799512490e323e161c38060162) fix(schemas): move description validation to schema
- [`54d0c4cd`](https://github.com/inveniosoftware/invenio-users-resources/commit/54d0c4cdc8ffd1ffcc60c3b6379b0016e57f9918) fix(users): improve role handling and group validation
- [`1f5a0f8b`](https://github.com/inveniosoftware/invenio-users-resources/commit/1f5a0f8bd7671345b0d19f6ab1548c5f40c0300d) fix(groups): clarify usage of group id and name
- [`e4c19b33`](https://github.com/inveniosoftware/invenio-users-resources/commit/e4c19b336d965261432b60fe54c7ba2fc4316c9a) feat(groups): enforce validation and protect group updates
- [`8ceb965d`](https://github.com/inveniosoftware/invenio-users-resources/commit/8ceb965d0d924e181a2115ddb0bd7a1153da0d00) Add proper superadmin permissions checks and protection
- [`85c6766a`](https://github.com/inveniosoftware/invenio-users-resources/commit/85c6766ab2c3a9c84faeee1e91930c95e4044b73) fix(roles): block escalation to protected roles
- [`2b86319f`](https://github.com/inveniosoftware/invenio-users-resources/commit/2b86319fe59beec56d9e431ca4ae4c3571717d5c) refactor: move to context_schema
- [`4d96be79`](https://github.com/inveniosoftware/invenio-users-resources/commit/4d96be792955f2135b3b8d0e5ae55372d41db5fe) fix(chore): DeprecationWarning stdlib
- [`0c1cabc1`](https://github.com/inveniosoftware/invenio-users-resources/commit/0c1cabc14c8619db3edaadfa3f3e996e5a74f906) fix: DeprecationWarning
- [`ef4d3296`](https://github.com/inveniosoftware/invenio-users-resources/commit/ef4d329628d716328d41058714a97a2d2833ea6d) chore(black): update formatting to >= 26.0
- [`92e98bdb`](https://github.com/inveniosoftware/invenio-users-resources/commit/92e98bdb9f29282f7635362b57a18333c1faa22f) chore(setup): bump dependencies
- [`f91f7674`](https://github.com/inveniosoftware/invenio-users-resources/commit/f91f76742aea4818d4a9b09da08711e056b4ddaf) release: v10.0.0
- [`043afacb`](https://github.com/inveniosoftware/invenio-users-resources/commit/043afacb4c539ba71a9edd5b91e423d0811920c8) chore+fix: replace usage of Link by EndpointLink and co. [+]
- [`ed32a58f`](https://github.com/inveniosoftware/invenio-users-resources/commit/ed32a58f04f28f6b84412face183c709c4004098) chore: replace deprecated logger.warn->warning
- [`3178c333`](https://github.com/inveniosoftware/invenio-users-resources/commit/3178c333815a90c95530d84fe2ef788b5fd8db3c) Update release date for version v9.0.3

#### `invenio-vocabularies` 11.0.1+oarepo.2.2pto3quqarmp23uj 💥
[9.1.2.64309979 → 11.0.1+oarepo.2.2pto3quqarmp23uj](https://github.com/inveniosoftware/invenio-vocabularies/compare/v9.1.2...v11.0.1)

- [`427a06e4`](https://github.com/inveniosoftware/invenio-vocabularies/commit/427a06e4db4b9f35e5d57ced934cebc25ca80da5) fix(setup): register orcid names job
- [`8f90b750`](https://github.com/inveniosoftware/invenio-vocabularies/commit/8f90b7504445bbc3b1a1d07d952309e135c7e308) release: v11.0.1
- [`8655ec5c`](https://github.com/inveniosoftware/invenio-vocabularies/commit/8655ec5cd65f152efd20aacad2be253cce98d3d2) service: fix read_all permission from search -> read
- [`0d442d32`](https://github.com/inveniosoftware/invenio-vocabularies/commit/0d442d32307068b2965b494d4e5fd94a635e8687) change(setup): bump invenio-jobs
- [`77db728e`](https://github.com/inveniosoftware/invenio-vocabularies/commit/77db728ef0e16285c7d74f749af87719ae3a887e) release: v11.0.0
- [`cbec9bea`](https://github.com/inveniosoftware/invenio-vocabularies/commit/cbec9bea511e9c6fa7101332a620839306359bd2) jobs: registered job to import euroscivoc subjects
- [`3ea5377b`](https://github.com/inveniosoftware/invenio-vocabularies/commit/3ea5377b5eaf065d4596c48bdc3616302bd10dc6) awards: updated config with openaire funder prefix
- [`08375f42`](https://github.com/inveniosoftware/invenio-vocabularies/commit/08375f42b291086133c81a8eb262056f2b0b7d85) fix(black): for python3.9
- [`ac7ccf24`](https://github.com/inveniosoftware/invenio-vocabularies/commit/ac7ccf2455bb44bb06b55641580fc0eb8cf931d9) 📦 release: v10.1.0
- [`fb68221e`](https://github.com/inveniosoftware/invenio-vocabularies/commit/fb68221e120b9fee12d6b5c38537bff1f4550c4d) orcid: replaced error with warning for missing name
- [`c464fe47`](https://github.com/inveniosoftware/invenio-vocabularies/commit/c464fe47c708c5a1f96603db4c95d9070550e020) datastream: added user agent in reader http request
- [`a24fed43`](https://github.com/inveniosoftware/invenio-vocabularies/commit/a24fed433bbc850446173e0cbe3f987e266381f1) datastream: formatting and refactor updates
- [`3dd3a633`](https://github.com/inveniosoftware/invenio-vocabularies/commit/3dd3a633658cc62145e74c6344a28603a60ba3a8) fix(chore): DeprecationWarning stdlib
- [`8daca984`](https://github.com/inveniosoftware/invenio-vocabularies/commit/8daca984d766d78542e4397c29bb932d37dbae88) chore(setup): bump dependencies
- [`423f8788`](https://github.com/inveniosoftware/invenio-vocabularies/commit/423f8788857ab3cb98476fb2c41d75aef79db140) chore+fix: replace deprecated usage of Link [+]
- [`bb470958`](https://github.com/inveniosoftware/invenio-vocabularies/commit/bb4709588ebe6a2f7006766b1a71bb794fdf583a) refactor: refactor some resource tests for clarity + rm unused imports
- [`13249301`](https://github.com/inveniosoftware/invenio-vocabularies/commit/13249301e756e5990a7698ade27b431bf0090045) chore(black): update formatting to >= 26.0
- [`0aea69f9`](https://github.com/inveniosoftware/invenio-vocabularies/commit/0aea69f9fdf4907efe598ee88674572ea65c68a7) refactor: deduplicate code ModePIDFieldVocabularyMixin
- [`48398c60`](https://github.com/inveniosoftware/invenio-vocabularies/commit/48398c6004b8bc498e6488b08c3abeb776b220af) refactor: context_schema instead of self.context
- [`d56436c9`](https://github.com/inveniosoftware/invenio-vocabularies/commit/d56436c911366c4fa1a9e2933c6ae28b80a88c94) release: v10.0.0

#### `invenio-webhooks` 2.0.0 💥
[1.1.0 → 2.0.0](https://github.com/inveniosoftware/invenio-webhooks/compare/v1.1.0...v2.0.0)

- [`159e7ce2`](https://github.com/inveniosoftware/invenio-webhooks/commit/159e7ce2bdc5ae5075142b4555ba1bb39d474bf6) fix(chore): DeprecationWarning stdlib
- [`284b08cf`](https://github.com/inveniosoftware/invenio-webhooks/commit/284b08cf95d69dd709cf66ced5a6b409d7984f10) chore(setup): bump dependencies
- [`9eda4836`](https://github.com/inveniosoftware/invenio-webhooks/commit/9eda483685fac20d28d0036218aa178ce5bb2879) release: v2.0.0
- [`a4aa4d40`](https://github.com/inveniosoftware/invenio-webhooks/commit/a4aa4d400e5ec53744e47466f3f4322042c8d3a7) chore(setup): pin dependencies
- [`8a138cf0`](https://github.com/inveniosoftware/invenio-webhooks/commit/8a138cf0a56ce8331dce404ab2c28d73c7d275eb) release: v1.1.1

#### `oarepo-app` 0.0.1
0.1.0 → 0.0.1


#### `oarepo-communities` 7.0.1 💥
[6.0.0.dev9 → 7.0.1](https://github.com/oarepo/oarepo-communities/compare/v6.0.0.dev9...v7.0.1)

- [`248b36c4`](https://github.com/oarepo/oarepo-communities/commit/248b36c445733206958083d1240b4c18e39aa128) fix: forgotten bump to python 3.14
- [`8b92596e`](https://github.com/oarepo/oarepo-communities/commit/8b92596e849d6b11e071b47ab3d223d64a707b21) fix: removed communities for the new oarepo package
- [`84a47319`](https://github.com/oarepo/oarepo-communities/commit/84a473194dfb568520ca3af4c2eebf0c32cb4d89) version bump to 6.1.0
- [`301853d1`](https://github.com/oarepo/oarepo-communities/commit/301853d1b21b7034e2556fa90e2b5dd8e06f76a0) Removed fake endpoint
- [`2e5cfb28`](https://github.com/oarepo/oarepo-communities/commit/2e5cfb28ceec1154d57b866cb3eaa384781311ff) chore(lint): removed extra entrypoint, format
- [`89c7a022`](https://github.com/oarepo/oarepo-communities/commit/89c7a022084f4044022d55effba54353deadaa01) fix: tests
- [`4c35b89c`](https://github.com/oarepo/oarepo-communities/commit/4c35b89c913e21c8da62de6bec0efb1caa1c39c2) trying to remove dependency on communities
- [`7d432fc6`](https://github.com/oarepo/oarepo-communities/commit/7d432fc62b76c033f1f70fe90216452d3b7d9d05) using community_get_or_create_in_default_workflow in tests
- [`e85d7032`](https://github.com/oarepo/oarepo-communities/commit/e85d7032c07c391fba46512e89b7c9e062e6b680) using community_get_or_create_in_default_workflow in another tests
- [`f3875746`](https://github.com/oarepo/oarepo-communities/commit/f38757462b1641551525c6d601b03b710156df25) Major version bump
- [`acd376e4`](https://github.com/oarepo/oarepo-communities/commit/acd376e4c2b648335e96a1f04b7e4d2d742ae6ca) UserGenerator moved
- [`5375be5a`](https://github.com/oarepo/oarepo-communities/commit/5375be5af29837cd089eba1f597c881f9add79ca) [skip ci] Bump version to 6.0.0dev9

#### `oarepo-dashboard` 3.0.0 💥
[2.0.0.dev4 → 3.0.0](https://github.com/oarepo/oarepo-dashboard/compare/v2.0.0.dev4...v3.0.0)

- [`07df76b6`](https://github.com/oarepo/oarepo-dashboard/commit/07df76b605edf8c1088c48141b018382d19d4eff) Removed invenio entrypoints
- [`43a94b17`](https://github.com/oarepo/oarepo-dashboard/commit/43a94b17dfa3f6f092f3e1d5b3c5a791433e58bb) Major version bump
- [`7af507f4`](https://github.com/oarepo/oarepo-dashboard/commit/7af507f4e6afde517c6f8ba08601f46119e6dfaf) [skip ci] Bump version to 2.0.0dev4

#### `oarepo-invenio-typing-stubs` 0.1.31
0.1.29 → 0.1.31


#### `oarepo-model` 1.0.1 💥
[0.1.0.dev51 → 1.0.1](https://github.com/oarepo/oarepo-model/compare/v0.1.0.dev51...v1.0.1)

- [`24bdf7f3`](https://github.com/oarepo/oarepo-model/commit/24bdf7f3a470428e141e5139330909020b04c272) chore: Major version bump (#98)
- [`7d6356a7`](https://github.com/oarepo/oarepo-model/commit/7d6356a781521de52fed534ef24089d8be37d324) [skip ci] Bump version to 0.1.0dev53
- [`a61fe3aa`](https://github.com/oarepo/oarepo-model/commit/a61fe3aa87610fdd3168db140a4621d0a3c0b962) removed incorrect oarepo version (#97)
- [`c9f61adc`](https://github.com/oarepo/oarepo-model/commit/c9f61adc0aef0e65262c14e64d5e68fc2d8659a5) [skip ci] Bump version to 0.1.0dev52
- [`027be127`](https://github.com/oarepo/oarepo-model/commit/027be1271dcee4f7ae43e2e51b3a6de3d0b3b87a) model field on record parent (#94)
- [`a54723cd`](https://github.com/oarepo/oarepo-model/commit/a54723cd59a4028ae6bda771d586c970f283e29d) [skip ci] Bump version to 0.1.0dev51

#### `oarepo-oidc-einfra` 3.0.1 💥
[2.0.0.dev4 → 3.0.1](https://github.com/oarepo/oarepo-oidc-einfra/compare/v2.0.0.dev4...v3.0.1)

- [`9f678fbe`](https://github.com/oarepo/oarepo-oidc-einfra/commit/9f678fbe3e18b4903e7b3267bb47bb876276ca50) Switched to python 3.14 (#38)
- [`d625d1ad`](https://github.com/oarepo/oarepo-oidc-einfra/commit/d625d1ad8760b8b44aee2f24ac21c4b3b8c29e30) Major version bump (#37)
- [`d8cbb9bb`](https://github.com/oarepo/oarepo-oidc-einfra/commit/d8cbb9bb0417e1b1352159c4adbc0737a20d3139) [skip ci] Bump version to 2.0.0dev4

#### `oarepo-rdm` 2.0.0 💥
[1.0.0.dev44 → 2.0.0](https://github.com/oarepo/oarepo-rdm/compare/v1.0.0.dev44...v2.0.0)

- [`7b2a08da`](https://github.com/oarepo/oarepo-rdm/commit/7b2a08da8ca01a4eb1863bf7cbddfa0ecbd39127) fix: removing RDM entrypoints (#74)
- [`c4c6a5fd`](https://github.com/oarepo/oarepo-rdm/commit/c4c6a5fda9878fd30d6c3245904c306d0eae3187) using same routes for reqeusts as in invenio
- [`12da5a5b`](https://github.com/oarepo/oarepo-rdm/commit/12da5a5bdf3efda22ac9bca144f3adaeed5e43d2) APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS config variable default
- [`861e9e2e`](https://github.com/oarepo/oarepo-rdm/commit/861e9e2e95c13f2ca5a28df417b7114c2ea94d4c) added ui resource config to hold ui components
- [`cab3cc1d`](https://github.com/oarepo/oarepo-rdm/commit/cab3cc1d0a726f529f0a6635acca5f7594aca3db) added tests
- [`a1df3b9e`](https://github.com/oarepo/oarepo-rdm/commit/a1df3b9e31b18186e5a88b04f58487c2b13ecf9e) [skip ci] Bump version to 1.0.0dev46
- [`6b449f36`](https://github.com/oarepo/oarepo-rdm/commit/6b449f367dab2238263e9697d048436c7eeaa0c2) Config refactor (#56)
- [`e4016e8d`](https://github.com/oarepo/oarepo-rdm/commit/e4016e8dbf7a5e8de53f6aa61d3c7d4b1f0c3724) using rdm resource configs for file resources (#68)
- [`81102097`](https://github.com/oarepo/oarepo-rdm/commit/81102097733d01cca49b9c795c59f427b188ab42) [skip ci] Bump version to 1.0.0dev45
- [`f6b1db67`](https://github.com/oarepo/oarepo-rdm/commit/f6b1db67192230e4493c56711a1aef3b92bcb574) oai properties in exports; oai serializer for single model bug fix (#71)
- [`cf69d692`](https://github.com/oarepo/oarepo-rdm/commit/cf69d692746e68854af464d4e0c5e524ae5240af) corrected tests to run with new invenio dependencies; format (#72)
- [`4fd6a172`](https://github.com/oarepo/oarepo-rdm/commit/4fd6a1721eb9d21441181d98a89806ca064c9fec) [skip ci] Bump version to 1.0.0dev44

#### `oarepo-requests` 4.0.0 💥
[3.0.0.dev5 → 4.0.0](https://github.com/oarepo/oarepo-requests/compare/v3.0.0.dev5...v4.0.0)

- [`fa8b3068`](https://github.com/oarepo/oarepo-requests/commit/fa8b3068d1c36c2540f8d068358ab7eb0bbec057) krist/be-1001-have-a-look-at-pytest-oarepo (#178)
- [`9c2dd3b3`](https://github.com/oarepo/oarepo-requests/commit/9c2dd3b3c8a11299568bd76281efb301fe8fb400) rdm-14 removed code (#170)
- [`42a6a5d8`](https://github.com/oarepo/oarepo-requests/commit/42a6a5d82db8031a8f76d1476561dade8fb5f791) added individual workflow into test workflows (#179)
- [`779becd4`](https://github.com/oarepo/oarepo-requests/commit/779becd4015aafe51d526d2edd3f948efe40be5b) [skip ci] Bump version to 3.0.0dev5

#### `oarepo-runtime` 3.0.1 💥
[2.0.0.dev59 → 3.0.1](https://github.com/oarepo/oarepo-runtime/compare/v2.0.0.dev59...v3.0.1)

- [`7dab5bbf`](https://github.com/oarepo/oarepo-runtime/commit/7dab5bbf3bd0eab3676e656d2f9133cd1ad9bc14) major version bump
- [`5d4b51a1`](https://github.com/oarepo/oarepo-runtime/commit/5d4b51a18a1013365f0d7eaf88eef40224a17ed8) chore: referencing invenio packages in dependencies
- [`39e10596`](https://github.com/oarepo/oarepo-runtime/commit/39e105962fc8088c4e00fde094745022157de4b4) [skip ci] Bump version to 2.0.0dev59

#### `oarepo-theme` 2.0.0 💥
[1.0.0.dev7 → 2.0.0](https://github.com/oarepo/oarepo-theme/compare/v1.0.0.dev7...v2.0.0)

- [`d9f49914`](https://github.com/oarepo/oarepo-theme/commit/d9f49914009abf5844b881148f64a19143d9d3d4) Major version bump
- [`1882d5bc`](https://github.com/oarepo/oarepo-theme/commit/1882d5bce6b414124dc31cbd8321f03c9b6c3857) [skip ci] Bump version to 1.0.0dev7

#### `oarepo-ui` 8.0.0 💥
[7.0.0.dev9 → 8.0.0](https://github.com/oarepo/oarepo-ui/compare/v7.0.0.dev9...v8.0.0)

- [`3bbe8a35`](https://github.com/oarepo/oarepo-ui/commit/3bbe8a35ec29b6cd317741283433da10788fa051) fix: tests
- [`15a3f6dc`](https://github.com/oarepo/oarepo-ui/commit/15a3f6dc6a7c22667b4bf5d31a69939f45add2c9) chore(format): linter upgrade
- [`5875ed45`](https://github.com/oarepo/oarepo-ui/commit/5875ed45380555f7eb5f89bfa62678004a0bdb7c) fix: remove communities circular dependency
- [`4d1cb0c5`](https://github.com/oarepo/oarepo-ui/commit/4d1cb0c53eba7f56aefa1c9a368f12cb637a98a8) Bumping version of pytest-oarepo
- [`bbee2f39`](https://github.com/oarepo/oarepo-ui/commit/bbee2f39bebee5ad1e2c727ae63441ce311f7e8d) removed workflow/requests dependency
- [`a57cdaa3`](https://github.com/oarepo/oarepo-ui/commit/a57cdaa30d652483f5a7daa8a2314c11ff1e2a2b) Freezing python version
- [`15e9b8b8`](https://github.com/oarepo/oarepo-ui/commit/15e9b8b8e3540c68d35b16e776886afa52dca7c6) Removed/skipped RDM stuff
- [`926c3b5b`](https://github.com/oarepo/oarepo-ui/commit/926c3b5b3fc52017bab81a7743bf59a671e3a2a2) Changing the community fixture not to use workflows
- [`55bb4e6c`](https://github.com/oarepo/oarepo-ui/commit/55bb4e6c1eab7cccdc8e43c9fa6c247b3bff8d54) Major version bump
- [`fb4dcc15`](https://github.com/oarepo/oarepo-ui/commit/fb4dcc156683d31bff53f2d9d40a4363d1cd56b7) test invenio dependencies, readme version fix
- [`9dd1f918`](https://github.com/oarepo/oarepo-ui/commit/9dd1f918291c30acb05b842a9eff26399a7187f4) fixed overriding model data with explicit prop passing
- [`3c85fd3a`](https://github.com/oarepo/oarepo-ui/commit/3c85fd3a1ed72bdb91c2ab16842301919698b9bb) fixed more inputs
- [`b373627d`](https://github.com/oarepo/oarepo-ui/commit/b373627d863c00da69c23a320111aa07df6962ac) copilog suggestions
- [`e9fa7d96`](https://github.com/oarepo/oarepo-ui/commit/e9fa7d96c9432c11adfdf446d7f5cf0e2c89e853) communities memberships on detail
- [`79b1a6f4`](https://github.com/oarepo/oarepo-ui/commit/79b1a6f4e84a2afbc39e2ffacf8294da203b03db) Potential fix for pull request finding
- [`3d20e79c`](https://github.com/oarepo/oarepo-ui/commit/3d20e79cff6608346f025ec74b4bb30e4d5e2ab1) [skip ci] Bump version to 7.0.0dev9

#### `oarepo-vocabularies` 4.0.0 💥
[3.0.0.dev9 → 4.0.0](https://github.com/oarepo/oarepo-vocabularies/compare/v3.0.0.dev9...v4.0.0)

- [`f4f9d280`](https://github.com/oarepo/oarepo-vocabularies/commit/f4f9d28081792b269cde6bb893a6619bd229a425) Major version bump (#255)
- [`96f56cab`](https://github.com/oarepo/oarepo-vocabularies/commit/96f56cab8897103e13f04ea0662e7d7a425480a9) Refactor VocabularyResultsListItem component and add custom styles for vocabulary results
- [`6983e052`](https://github.com/oarepo/oarepo-vocabularies/commit/6983e05209faf5ff977d33574eb0015d3a3bbbf4) Enhance vocabulary breadcrumb and title components for better display and usability
- [`023679ed`](https://github.com/oarepo/oarepo-vocabularies/commit/023679ed0ee40a4ab25455266cdf4d3bee9fa77f) Refactor breadcrumb and search components for improved navigation; remove unused vocabulary results list item styles
- [`433f0b6f`](https://github.com/oarepo/oarepo-vocabularies/commit/433f0b6f43f6b6bb9cbe2f955b63a29fb13f8b57) fixed tests
- [`7d5c2df7`](https://github.com/oarepo/oarepo-vocabularies/commit/7d5c2df793fa9ee3bd11d69037ad1a0c990c2848) Add margin to breadcumbs; move from default to rdm theme folder
- [`2565e327`](https://github.com/oarepo/oarepo-vocabularies/commit/2565e32782a21378b76941266b4c0abf6965e395) [skip ci] Bump version to 3.0.0dev9

#### `oarepo-workflows` 3.0.0 💥
[2.0.0.dev10 → 3.0.0](https://github.com/oarepo/oarepo-workflows/compare/v2.0.0.dev10...v3.0.0)

- [`516a385f`](https://github.com/oarepo/oarepo-workflows/commit/516a385ffab9fc3a12bbb118fc6181d362462fb1) Major version bump due to invenio changes (#50)
- [`a169fb37`](https://github.com/oarepo/oarepo-workflows/commit/a169fb375c615f3d3ba75ccc647195edc60e50e2) [skip ci] Bump version to 2.0.0dev10

---

## 0.0.1

Released: **March 22, 2026 at 21:13 UTC**

*No package changes recorded for this release.*
