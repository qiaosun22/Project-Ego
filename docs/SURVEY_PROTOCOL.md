# ProjectEgo Systematic Review Protocol

**Working title:** *ProjectEgo: From Human Egocentric Data to Robot Learning — A Systematic Survey, Dataset Audit, and Utility Benchmark*

**Protocol version:** 0.1.0  
**Status:** Pilot protocol  
**Last updated:** 2026-07-25  
**Planned reporting guidance:** PRISMA 2020 where applicable, augmented for datasets, software artifacts, and continuously updated online sources.

## 1. Objectives

The review will characterize the global landscape of egocentric datasets relevant to robot learning and determine which observable dataset properties are associated with downstream utility.

### Research questions

- **RQ1 — Landscape:** What egocentric datasets exist, how were they collected, and how have scale, modality, supervision, access, and intended use evolved?
- **RQ2 — Representation:** Which sensing, annotation, action, embodiment, and environment representations are available?
- **RQ3 — Quality:** How can technical, perceptual, semantic, diversity, governance, and accessibility quality be measured reproducibly?
- **RQ4 — Transfer:** Which properties reduce or increase the gap between human egocentric experience and robot perception or control?
- **RQ5 — Utility:** Under controlled data and compute budgets, which datasets or combinations improve robot-learning outcomes?
- **RQ6 — Gaps:** Which tasks, populations, environments, embodiments, modalities, and governance conditions remain underrepresented?

## 2. Scope and Operational Definitions

An **egocentric observation** is captured from, attached to, or intentionally approximating the situated viewpoint of an acting human, robot, wearable system, or embodied agent. A dataset is relevant when it contains egocentric observations or paired information that materially supports learning from them.

### In-scope dataset classes

- Human-worn first-person video and multimodal sensing.
- Robot-mounted or embodiment-centered observations paired with behavior.
- Paired ego–exo or multi-view datasets containing a valid ego stream.
- Hand–object, gaze, spatial, navigation, and daily-activity datasets with an egocentric viewpoint.
- Synthetic or reconstructed egocentric datasets intended for embodied learning.
- Publicly documented proprietary or closed datasets, cataloged at the evidence level available.
- Dataset mixtures when their constituent datasets or mixture construction can be identified.

### Out of scope

- Third-person-only datasets without an egocentric stream or explicit ego-transfer contribution.
- Papers using an in-scope dataset but contributing neither data, annotations, audit evidence, nor material dataset analysis.
- Private datasets described without enough information to establish identity, provenance, and relevance.
- Pure benchmarks that introduce no dataset, split, annotation, or auditable dataset-level finding.

Robot-centric data will be tagged separately from human egocentric data; inclusion does not imply that the two are interchangeable.

## 3. Information Sources

Searches will cover:

- Scholarly indexes: arXiv, OpenAlex, Crossref, Semantic Scholar, DBLP, IEEE Xplore, ACM Digital Library, and Google Scholar where access permits.
- Publication venues: CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, CoRL, RSS, ICRA, IROS, RA-L, IJRR, CHI, and relevant workshops/challenges.
- Artifact registries: GitHub, Hugging Face, Papers with Code archives, Zenodo, Figshare, OSF, Kaggle, institutional repositories, and project websites.
- Dataset ecosystems: Ego4D, EPIC-KITCHENS, Project Aria, Open X-Embodiment/RLDS, LeRobot, and successor catalogs.
- Secondary discovery: prior reviews, awesome lists, challenge pages, citations, references, author pages, and public company announcements.

Each source will record query, retrieval date, result count, export method, and raw snapshot identifier where licensing permits storage.

## 4. Search Strategy

The base query has four concept groups:

```text
(egocentric OR "first-person" OR wearable OR head-mounted OR robot-centric)
AND
(dataset OR corpus OR benchmark OR demonstrations OR trajectories)
AND
(robot* OR embodied OR manipulation OR navigation OR "vision-language-action"
 OR imitation OR "hand-object" OR activity OR affordance)
AND NOT
(medical-only exclusion terms applied during screening, not retrieval)
```

Queries will be adapted to each source without silently changing the concept groups. Dataset names discovered during screening become additional exact-name searches. Backward and forward citation chaining will be performed for every included anchor dataset.

### Continuous update query

Automated discovery will run at least weekly over sources that expose stable feeds or APIs. New candidates enter a triage queue and do not become included records until screened.

## 5. Selection Process

### Stages

1. **Automated normalization:** canonicalize identifiers and URLs; cluster probable duplicates.
2. **Title/artifact screening:** remove clearly irrelevant records.
3. **Abstract/summary screening:** apply scope criteria and tag uncertain cases.
4. **Full-text/artifact screening:** verify dataset identity, ego relevance, contribution, and available evidence.
5. **Dataset-family resolution:** distinguish dataset, release, extension, annotation layer, benchmark split, and mirror.

Two reviewers should independently screen the pilot sample and all records used in the archival survey. Disagreements are resolved by discussion or a third adjudicator. The living catalog may use single-reviewer additions, but those records remain provisional until independently checked.

### Exclusion reasons

Use exactly one primary reason at full-text stage:

- `not_egocentric`
- `no_dataset_contribution`
- `insufficient_identity`
- `duplicate_or_superseded`
- `no_robot_learning_relevance`
- `unobtainable_full_record`
- `retracted_or_invalidated`

Duplicates are linked, not deleted, when they contain distinct provenance or version information.

## 6. Data Extraction

Extraction uses `schema/dataset.schema.json`. Major groups include:

- identity, aliases, family, release/version, dates, organizations, and canonical links;
- capture agent, viewpoint, devices, sensors, calibration, environments, geography, and participants;
- duration, episodes, frames, trajectories, tasks, objects, actions, and splits;
- modalities, annotations, language, control/action representation, and file formats;
- license, access workflow, commercial terms, privacy, consent, documentation, loaders, and download health;
- known limitations, reported biases, corrections, and dataset relationships;
- provenance, field-level evidence, verification state, and timestamps.

Quantities must preserve units and distinguish reported values from measured values. Conflicting claims are stored as separate evidence records until adjudicated.

## 7. Quality and Risk-of-Bias Assessment

The review will not infer dataset quality from scale alone. Assessments are separated into:

1. Data integrity
2. Perceptual quality
3. Semantic and annotation quality
4. Diversity and coverage
5. Access, governance, privacy, and documentation
6. Robot-learning utility

Every derived metric reports evaluator version, applicable population, sample design, evidence level, uncertainty, and missingness. Dataset creators' claims are treated as evidence level 1 unless independently checked.

### Evidence levels

| Level | Name | Minimum evidence |
|---:|---|---|
| 1 | Claimed | Paper, official page, or maintainer statement |
| 2 | Metadata | Structured metadata or schema independently checked |
| 3 | Sampled | A documented sample of released files inspected |
| 4 | Verified | Full applicable audit executed on accessible release |
| 5 | Validated | Controlled downstream experiment completed |

## 8. Synthesis Plan

### Descriptive synthesis

- Counts and trends by year, dataset class, capture agent, geography, access, license, modality, and task.
- Dataset-family graph showing releases, extensions, annotations, derivatives, and mixtures.
- Coverage matrices for sensors, annotations, actions, embodiments, and environments.
- Evidence completeness and access-health analyses.

### Quantitative synthesis

- Report distributions and uncertainty rather than only means.
- Use saturation-aware scale measures and diversity indices where raw data supports them.
- Analyze correlation between metadata/quality signals and controlled downstream utility.
- Report learning curves and utility per unit of data, compute, storage, and acquisition burden.
- Use cross-dataset transfer matrices to study redundancy and domain gaps.

No universal composite ranking will be reported unless its weights, sensitivity analysis, and intended use case are explicit.

## 9. Reproducibility and Versioning

- The archival survey cites a frozen catalog release and commit.
- Search exports, decisions, extraction records, and analysis code receive checksums and versions.
- Corrections do not overwrite history; they create a new record revision with rationale.
- Dataset records retain `last_verified_at`, while monitoring events retain observation time.
- Closed datasets are evaluated only on observable dimensions and never imputed to match open datasets.

## 10. Ethics and Conflicts

The review will document consent, privacy, geographic and demographic limitations where sources permit, without republishing sensitive samples or personal data. Legal and license fields are factual summaries, not legal advice. Reviewers must declare affiliations, funding, dataset authorship, and commercial conflicts for records they assess.

## 11. Pilot and Amendments

Before protocol v1.0:

1. Run the query on at least two scholarly and two artifact sources.
2. Dual-screen 50 candidate records.
3. Dual-extract 10 diverse datasets.
4. Measure agreement and revise ambiguous definitions.
5. Register all protocol changes in `docs/PROTOCOL_AMENDMENTS.md`.

Substantive changes after screening begins must include date, rationale, affected records, and whether analyses were rerun.

