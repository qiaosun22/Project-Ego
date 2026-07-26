# ProjectEgo ICLR Submission Strategy

## Bottom line

ICLR is a plausible target for ProjectEgo as a dataset-and-benchmark paper, but
not as a conventional narrative survey. The ICLR 2026 call explicitly includes
"datasets and benchmarks" and robotics within scope. The current manuscript is
not yet submission-ready because it establishes a taxonomy, protocol, and
metadata-level catalog without file-level audits or controlled downstream
learning results.

The strongest framing is:

> ProjectEgo is an evidence-backed dataset observatory and utility benchmark
> that measures when egocentric human and robot data improve robot learning.

The survey should motivate the benchmark and synthesize evidence. It should not
be presented as the primary novelty.

## Official constraints used for this assessment

- ICLR 2026 accepts work from all areas of machine learning and explicitly lists
  datasets and benchmarks and robotics.
- Initial submissions are limited to 9 main-text pages. References are unlimited;
  appendices are unlimited but reviewers are not required to read them.
- Submissions are double blind. Author identity in the paper or supplement can
  cause desk rejection.
- The official ICLR 2026 LaTeX style is required.
- The 2026 deadlines have passed. This repository uses the latest official
  available template as a formatting baseline; a future submission must migrate
  to that year's official template and policies.

Official sources:

- https://iclr.cc/Conferences/2026/CallForPapers
- https://iclr.cc/Conferences/2026/AuthorGuide
- https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip

## Current readiness assessment

| Area | Current state | ICLR-level target | Priority |
|---|---|---|---|
| Problem importance | Strong and timely | Preserve the human-to-robot decision problem | High |
| Taxonomy | Coherent draft | Validate through dual extraction and ambiguity analysis | High |
| Catalog coverage | 109 candidates, 20 level-2 anchors | Complete systematic search and frozen release | Critical |
| Evidence | Metadata cross-checking | Field-level provenance plus sampled/file audits | Critical |
| Benchmark | Protocol only | Released code, tasks, baselines, and measured results | Critical |
| Robot utility | Proposed | Fixed-budget transfer experiments with uncertainty | Critical |
| Novel ML insight | Hypothesized Ego-to-Robot Gap | Show predictive relationship with transfer outcomes | Critical |
| Reproducibility | JSON/CSV/figures in CI | One-command audit and benchmark reproduction | High |
| Ethics/governance | Conceptual framework | Dataset-specific evidence and risk analysis | High |
| Writing | Long survey draft | 9-page result-led paper plus appendix | High |

## Minimum credible ICLR contribution

Before submission, ProjectEgo should deliver all of the following:

1. A systematic search with deduplication, PRISMA-style counts, frozen query
   strings, two reviewers, and inter-reviewer agreement.
2. At least one public catalog release broad enough to support defensible field
   conclusions, with field-level provenance and versioned corrections.
3. File-level audits on a representative open subset, including decode integrity,
   timestamps, synchronization, calibration, annotations, leakage, and coverage.
4. A released scoring implementation with applicability masks, uncertainty,
   evidence coverage, and sensitivity analysis. No universal opaque score.
5. Controlled robot-learning experiments under equal data and compute budgets.
6. Strong baselines: no pretraining, robot-only data, human-ego data, paired
   ego--exo data, mixtures, and at least one current VLA or policy backbone.
7. Generalization tests across tasks, scenes, viewpoints, and embodiments with
   repeated seeds and confidence intervals.
8. A demonstrated scientific finding, not merely a leaderboard. The strongest
   candidate is whether measured components of the Ego-to-Robot Gap predict
   downstream transfer after controlling for scale and model capacity.

## Recommended experimental design

Use three target families: language-conditioned tabletop manipulation,
dexterous hand-object interaction, and long-horizon mobile manipulation. For
each family, fix policy architecture, optimizer, trainable parameters, total
frames/tokens, compute, adaptation budget, evaluation episodes, and seeds.

Report:

- zero-shot and few-shot target success where meaningful;
- area under the adaptation learning curve;
- final success and failure-mode distribution;
- robustness under viewpoint, object, scene, and embodiment shifts;
- confidence intervals and effect sizes;
- compute, storage, and access costs;
- correlation and ablation analyses for each Ego-to-Robot Gap component.

The central experiment should compare dataset choices under the same budget,
not compare published headline numbers produced by different systems.

## Paper structure for a 9-page submission

1. Introduction and result preview: 1 page.
2. Related work and gap: 0.5 page.
3. ProjectEgo evidence model and catalog protocol: 1.5 pages.
4. Quality and Ego-to-Robot Gap metrics: 1.5 pages.
5. Benchmark setup: 1.5 pages.
6. Main experimental results and ablations: 2 pages.
7. Limitations, ethics, and conclusion: 1 page.

Move the full dataset table, search strings, audit specifications, extended
results, and dataset cards to the appendix and repository.

## Go/no-go criteria

Submit to ICLR only when:

- at least one substantial level-4 audit cohort exists;
- the benchmark code and frozen data manifests are releasable;
- controlled utility experiments produce a defensible cross-dataset finding;
- all main claims are supported in the main 9 pages;
- the anonymous artifact path and manuscript pass an identity audit.

If these criteria cannot be met, release the survey separately and target a
dataset/benchmark track, journal survey venue, or robotics venue after the
empirical benchmark matures.
