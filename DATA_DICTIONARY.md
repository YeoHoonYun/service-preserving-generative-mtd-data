# Data dictionary and inclusion boundary

Paths below are relative to `evidence/`. JSON files retain the original schema and values; no result was recalculated during staging. `DATA_MANIFEST.json` binds each released file to its original bytes.

| Cohort | Principal records | Unit and interpretation |
| --- | --- | --- |
| Source cost | `paper/service-cost-study/cost_analysis.json` | L0 functional, L1 secured, L2 dynamic maintained source inventories and validation timing. Source tokens are not provider-use tokens. |
| Generation | `artifacts/scale-study-20261009/analysis.json`; `minishop/` and `flaskr/` per-run ledgers and `store/` source | 30 slots per application across three run contexts; 66 total model calls include retries. A slot is not an independent random model sample. Accepted stores preserve code and mapping records; raw model messages are excluded. |
| Matched serving | `artifacts/cost-revision-20261009/matched-runtime/{protocol,runs,summary}.json` | Eight paired randomized blocks of local serving. Workload time, target CPU, and sampled RSS have distinct measurement boundaries. |
| Validation selection and invariance | `artifacts/caiv-study-20261010-r2/`; `artifacts/caiv-extension-20261010/`; `artifacts/invariance-review-20261010/audit.json` | Selection methods, complete-validation comparisons, and source-hash audit. Passing finite tests do not prove full equivalence. |
| Structural replay | `artifacts/intrusion-detection-pilot-20261010/summary.json`; `artifacts/security-invariants-20261012-r3/summary.json` | Fresh-session stale replay, pinned-session continuation, semantic browser use, and selected invariant checks. |
| Three-arm live rotation | `artifacts/matched-rotation-study-20261014-archival-replay/{protocol,results}.json` | Three accepted adjacent pairs; S0 static, S1 generated fixed, S2 generated rotating. The live replay reused archived mappings and made no new model calls. |
| Earlier AI mapping | `artifacts/public-wire-study-20261012/results.json` | Separately hosted, informed fixed and successor mapping phases. Its model time and tokens are contextual, not measurements from the live replay. |
| Flaskr attack and response | `artifacts/blind-matched-attack-20261014/audit.json`; `artifacts/security-phase-response-20261014/summary.json`; `artifacts/final-security-scenarios-20261014/summary.json` | Fixed-target attack cases, pre/during/post response, and detection gaps. Repeated cases share attack classes and targets. |
| Juice Shop benchmark | `artifacts/juice-shop-study-20261014/{audit-final,usage}.json`; `artifacts/juice-shop-adaptive-20261014/audit.json` | Separate deliberately vulnerable benchmark and local proxy response; no generative rotation claim. |
| Manuscript table ledger | `paper/unified-mtd/integrated_table_records.json` | Derived table records retained to compare published values with source cohorts. |

The release excludes raw agent transcripts, browser screenshots, ephemeral session identifiers, full databases, service startup logs, raw incomplete provider-call transcripts (failed-call metadata are retained), and third-party application trees. Exclusion keeps the deposit bounded; it limits reconstruction of every request-level event. The data are sufficient to verify the reported ledgers and inspect the 60 accepted generation source trees, but running fresh generation or full browser/security tests requires the original platform, dependencies, fixtures, and model access. No remote-server test data are included.

## Version 2 additions

| Cohort | Principal records | Unit and interpretation |
| --- | --- | --- |
| Prospective MiniShop | `artifacts/prospective-three-arm-20261020/` | 36 planned target/model/arm/information slots; learn-phase usage separate. Authorized-task rediscovery and harmful authorization outcomes are different. |
| Fixed-public Juice Shop candidates | `artifacts/juice-shop-fixed-public-20261020/` | Four planned generation slots, at most two calls each; only two edge operations vary. |
| Juice Shop three-arm | `artifacts/juice-shop-three-arm-20261020/` | Prospective cold/informed slots; interrupted after a provider safety rejection. Direct upstream remains reachable on loopback. |
| Juice Shop informed replay | `artifacts/juice-shop-informed-replay-20261020/` | Three adjacent pairs, two historical model case sets, three arms, no new model calls. |
| Flaskr response timing | `paper/unified-mtd/research/additional-feedback/B_flaskr_response_timing.ko.md` | Reanalysis of fixed targets, not a live-rotation experiment. |
