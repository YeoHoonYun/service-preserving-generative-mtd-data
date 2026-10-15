# Service-preserving generative MTD: research data and code

This repository is the **data and code companion**, not a second article, to the standalone manuscript *Service-Preserving Generative Moving Target Defense for Web Applications: Generation Costs, Contract-Invariant Validation, and Bounded Security Evidence* by YeoHoon Yoon and Kyung-Sung Kim. The release freezes the evidence available for the 14 October 2026 draft. It does not claim that the manuscript has been posted to SSRN or accepted by a journal.

## Contents

- `evidence.zip` contains `evidence/`, mirroring the relative paths of 1,477 selected local records and source files. The selection includes the 30 files hashed by the manuscript builder, per-run generation ledgers, and accepted MiniShop and Flaskr generation source. It excludes raw model transcripts, screenshots, databases, session traces, complete third-party application trees, and interrupted-call logs. `ARCHIVE_SHA256.txt` verifies the ZIP before extraction.
- `source_evidence_manifest.json` is the manuscript builder's provenance manifest. Its `evidence_sha256` field covers the 30 core records and scripts consumed or cited in the draft.
- `DATA_MANIFEST.json` gives a SHA-256 digest for every staged evidence file.
- `scripts/verify_release.py` checks both hash manifests without installing dependencies.
- `DATA_DICTIONARY.md` maps the experimental cohorts to records, counting units, and known limitations.

Run `python scripts/verify_release.py` from this repository root to verify the ZIP and all deposited files without extraction. Extract `evidence.zip` when you want to inspect or reanalyze records. To reproduce manuscript tables, start with `evidence/paper/unified-mtd/integrated_table_records.json` and the cohort JSON paths listed in `DATA_DICTIONARY.md`. The full local platform and model-provider environment are not archived here; this release supports evidence inspection and selected reanalysis, not bit-for-bit regeneration of new model outputs.

## Interpreting the security evidence

The local generation campaign accepted 60 slots in 66 model calls, using 1,316,878 provider-reported input and output tokens. Selected security-invariant checks passed 5,670/5,670. Exact stale mapping replay failed across 27 fresh-session adjacent-generation pairs, while 27 pinned sessions and 10/10 semantic browser workflows remained usable. A separate three-pair live rotation replay invalidated each prior API mapping, then completed all authorized tasks with archived successor mappings. Its live replay made **no model calls**. The 40,780 tokens reported for informed successor rediscovery came from an earlier, separately hosted AI study and must not be attributed to the live replay. Neither cohort establishes a general reduction in adaptive intrusion success.

The Flaskr and OWASP Juice Shop security cohorts test different targets and attack classes. They must not be pooled into one attack-success denominator. Model-proposed attacks are distinguished from observed harmful state changes. Provider-failed prospective calls have unknown usage and were excluded from completed outcomes.

## Scope and provenance

MiniShop is a research application. Flaskr is adapted from the Flask 3.1.2 tutorial; see `licenses/Flask-LICENSE.txt` and the upstream [Flask repository](https://github.com/pallets/flask/tree/3.1.2/examples/tutorial). OWASP Juice Shop source is not redistributed. All security experiments represented here used local targets. No production service, external account, or third-party application was attacked.

Data and tables are licensed under CC BY 4.0. Research-authored scripts are licensed under MIT. Portions based on Flask retain their upstream BSD-3-Clause terms. The original workspace retains additional excluded material; omissions are intentional and listed in `DATA_DICTIONARY.md`.

## Citation

Use the version-specific Zenodo DOI for a precise snapshot. The concept DOI resolves to the latest version. `CITATION.cff` records the authors and title. Cite the manuscript separately once its public identifier is available.
