# Discovery snapshots

This directory stores immutable, dated inputs used for high-recall dataset discovery. Inclusion in a snapshot does **not** mean inclusion or verification by ProjectEgo.

## Snapshot inventory

### `open-data-eval-catalog-2026-07-25.csv`

- Source: <https://github.com/Varun-Nair/open-data-eval>
- Upstream file: `data/ego-datasets/ego_dataset_catalog.csv`
- Retrieved: 2026-07-25
- Rows: 109 dataset candidates plus one header row
- License: CC-BY-4.0 per the upstream repository
- Use: candidate discovery and secondary metadata cross-check only

ProjectEgo does not import upstream quality scores. Facts used in ProjectEgo outputs must be independently linked to a primary paper or official release artifact and carry ProjectEgo verification status.

## Search families

The first search snapshot uses the following concept groups across arXiv, GitHub, official dataset ecosystems, prior surveys, and citation chaining:

```text
(egocentric OR first-person OR wearable OR head-mounted OR robot-centric)
AND (dataset OR corpus OR benchmark OR demonstrations OR trajectories)
AND (robot OR embodied OR manipulation OR navigation OR hand-object
     OR vision-language-action OR imitation)
```

Additional exact-name searches are run for each candidate and its known aliases. Robot-native discovery includes Open X-Embodiment/RLDS, LeRobot, DROID, BridgeData, and dataset references from VLA papers. Search results enter a candidate queue before curation.

## Verification rule for quantitative figures

A row may enter a ProjectEgo quantitative figure only when:

1. identity, release year, regime, and at least one quantitative or modality field are supported by a primary paper or official release page;
2. the same facts are checked against a second source, such as an official repository, dataset host, later release documentation, or an attributed secondary audit;
3. discrepancies are recorded rather than averaged or silently resolved;
4. status is `cross_checked_metadata` or higher;
5. the chart caption identifies the cohort and does not imply exhaustive field coverage.

`cross_checked_metadata` corresponds to ProjectEgo evidence level 2. It is not file verification and does not establish downstream utility.

