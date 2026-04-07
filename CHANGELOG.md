# OAREPO-APP Changelog

## Contents

- [1.0.0](#100)
- [0.0.1](#001)

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
