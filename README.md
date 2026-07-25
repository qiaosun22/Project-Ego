# ProjectEgo

**The Awesome Ego-centric Datasets for Robot Learning**

ProjectEgo is a living dataset observatory and reproducible benchmark for understanding which first-person datasets actually help robots learn.

## Foundation

- [Roadmap](ROADMAP.md) — milestones, principles, workstreams, and release criteria.
- [Systematic review protocol](docs/SURVEY_PROTOCOL.md) — scope, search, screening, extraction, and synthesis plan.
- [Survey working paper](docs/SURVEY.md) — narrative draft, taxonomy, benchmark design, and research figures.
- [Dataset schema](schema/dataset.schema.json) — evidence-backed machine-readable record format.
- [Example record](data/datasets/ego4d.json) — provisional schema example, not a completed scorecard.

Validate the catalog without external dependencies:

```bash
python3 scripts/validate_catalog.py
```

## Website

The project homepage is a dependency-free static site. Open `index.html` locally or enable GitHub Pages from the repository root.

> The current catalog values and scores are interface previews, not official benchmark results.
