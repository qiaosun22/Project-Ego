# ProjectEgo Roadmap

ProjectEgo is a living dataset observatory, reproducible quality audit, and downstream utility benchmark for egocentric robot learning. The project is built around one principle: every public claim must be traceable to evidence and every computed score must be reproducible.

## North Star

Help a researcher answer:

> Given my robot-learning task, data budget, compute budget, modality requirements, and legal constraints, which egocentric dataset or dataset portfolio should I use, and why?

## Project Outputs

1. **Living Catalog**: versioned records for public, gated, restricted, unavailable, and publicly documented proprietary datasets.
2. **ProjectEgo Standard**: task-aware quality dimensions, metrics, evidence levels, confidence, and missing-data policy.
3. **Dataset Auditor**: reproducible metadata, file, frame, annotation, and sequence checks.
4. **Utility Benchmark**: fixed-budget training experiments measuring downstream and cross-dataset value.
5. **Survey**: a systematic review connecting human egocentric data to robot learning.
6. **Website and API**: searchable profiles, comparisons, provenance, change history, and machine-readable exports.

## Principles

- **Evidence before score**: preserve sources, timestamps, evaluator versions, and uncertainty.
- **No unverifiable equivalence**: proprietary and inaccessible datasets may be cataloged but cannot receive file-derived scores.
- **No opaque overall rank**: publish dimension and task-specific scores; composite recommendations must expose weights.
- **Facts are immutable inputs**: raw observations are separated from derived metrics and presentation.
- **Version everything**: datasets, schemas, evaluators, score formulas, and benchmark results have independent versions.
- **Reproducibility over coverage theater**: unknown is a valid value; fabricated completeness is not.

## Milestones

### M0 — Research Contract and Data Model

Target: August 2026

- [x] Publish project roadmap.
- [x] Publish systematic review protocol v0.1.
- [x] Publish dataset schema v0.1 and a dependency-free validator.
- [x] Add a schema-conformant example record.
- [ ] Open governance, contribution, correction, and conflict-of-interest policies.
- [ ] Freeze ProjectEgo inclusion criteria v1.0.
- [ ] Define canonical vocabularies for modalities, access, capture platforms, and tasks.

Exit criterion: two maintainers can independently encode the same ten datasets with at least 90% agreement on required fields.

### M1 — Living Catalog

Target: September–October 2026

- [ ] Ingest 100+ candidate datasets across human ego, robot ego, ego–exo, synthetic, and proprietary categories.
- [ ] Deduplicate dataset families and record versions separately.
- [ ] Add automated link, repository, license, and release monitoring.
- [ ] Add evidence-backed dataset pages and change logs.
- [ ] Publish monthly catalog snapshots with stable DOIs when practical.

Exit criterion: at least 90% of included records have two-source identity verification and a last-checked timestamp under 30 days.

### M2 — ProjectEgo Quality Standard

Target: November–December 2026

- [ ] Freeze metric definitions for integrity, perception, semantics, diversity, access, governance, and robot utility.
- [ ] Publish normalization functions and reference fixtures.
- [ ] Define confidence propagation and missing/not-applicable policies.
- [ ] Run inter-rater reliability study for manually audited fields.
- [ ] Release scorecards only after public rubric review.

Exit criterion: all published scores can be regenerated from versioned observations with one command.

### M3 — Dataset Auditor

Target: Q1 2027

- [ ] Release metadata and download-health audit.
- [ ] Release containerized file and sequence inspection.
- [ ] Release stratified frame sampler and perception audit.
- [ ] Add annotation consistency, duplicate, contamination, and leakage checks.
- [ ] Audit an initial cohort of 20 representative datasets.

Exit criterion: independent reruns agree within declared tolerances and produce signed evaluation manifests.

### M4 — Robot Utility Benchmark

Target: Q2–Q3 2027

- [ ] Select reference tasks spanning perception, representation learning, VLA, and policy learning.
- [ ] Publish fixed data/compute budgets and reference model recipes.
- [ ] Measure learning curves, utility per GPU-hour, and cross-dataset transfer.
- [ ] Release the Ego-to-Robot Gap and dataset portfolio baselines.
- [ ] Separate benchmark scores by task instead of declaring a universal winner.

Exit criterion: the first public benchmark release includes at least eight datasets, three tasks, three seeds, confidence intervals, and complete run manifests.

### M5 — Survey and Community Release

Target: Q3–Q4 2027

- [ ] Release the survey preprint and interactive taxonomy.
- [ ] Link every survey table to the living catalog snapshot used in the paper.
- [ ] Launch maintainer correction workflow and community submissions.
- [ ] Establish quarterly releases and an annual state-of-ego-data report.

## Workstreams

| Workstream | Primary artifact | Success measure |
|---|---|---|
| Discovery | Candidate registry and monitoring events | Recall on known benchmark list; time-to-detection |
| Curation | Evidence-backed dataset records | Agreement, freshness, provenance coverage |
| Quality | Versioned observations and scores | Reproducibility and discriminative validity |
| Utility | Training and transfer results | Predictive relationship between quality and utility |
| Survey | Manuscript, taxonomy, bibliography | Coverage, rigor, and linked reproducibility |
| Platform | Website, API, exports | Freshness, accessibility, and citation adoption |

## Immediate Backlog

1. Encode the first 20 anchor datasets and document ambiguous cases.
2. Create controlled vocabularies from those records rather than anticipating every possible modality.
3. Establish automated source monitoring and a candidate triage queue.
4. Draft ProjectEgo Standard v0.1 with metrics but no public rankings.
5. Design the survey extraction form and pilot dual-reviewer screening on 50 records.

## Non-goals

- Hosting or redistributing datasets without explicit authorization.
- Treating paper claims as equivalent to file verification.
- Ranking inaccessible proprietary datasets on unobservable properties.
- Optimizing a single score for publicity at the expense of scientific validity.
- Claiming ISO compliance or legal clearance without an appropriate independent assessment.

