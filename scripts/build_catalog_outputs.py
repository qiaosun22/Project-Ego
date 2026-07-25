#!/usr/bin/env python3
"""Build ProjectEgo master CSV, statistics, and publication SVGs."""

from __future__ import annotations

import csv
import html
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "catalog" / "anchor_datasets.json"
MASTER = ROOT / "data" / "catalog" / "dataset_master.csv"
STATS = ROOT / "data" / "catalog" / "anchor_statistics.json"
FIGURES = ROOT / "docs" / "figures" / "generated"
MODALITIES = [
    "rgb", "audio", "depth", "gaze", "imu", "hand_pose", "body_pose",
    "language", "calibration", "point_cloud", "motion_capture", "force_torque",
    "mmwave", "robot_state", "robot_action",
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_verified() -> list[dict]:
    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    ids = [record["dataset_id"] for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("dataset_id values must be unique")
    verified = [r for r in records if r["verification_status"] == "cross_checked_metadata"]
    for record in verified:
        if record["evidence_level"] < 2:
            raise ValueError(f"{record['dataset_id']} lacks evidence level 2")
        if not record["primary_source"].startswith("https://"):
            raise ValueError(f"{record['dataset_id']} lacks primary HTTPS source")
        if not record["secondary_source"].startswith("https://"):
            raise ValueError(f"{record['dataset_id']} lacks secondary HTTPS source")
        if not isinstance(record.get("release_year"), int) or not isinstance(record.get("publication_year"), int):
            raise ValueError(f"{record['dataset_id']} requires integer release and publication years")
        unknown_modalities = set(record.get("modalities", [])) - set(MODALITIES)
        if unknown_modalities:
            raise ValueError(f"{record['dataset_id']} has unknown modalities: {sorted(unknown_modalities)}")
    return verified


def write_master(records: list[dict]) -> None:
    fields = [
        "dataset_id", "name", "release_year", "publication_year", "regime", "hours",
        "episodes_or_trajectories", "participants", "environments",
        *[f"has_{m}" for m in MODALITIES],
        "modality_count", "access", "license", "evidence_level",
        "verification_status", "primary_source", "secondary_source",
        "last_checked", "notes",
    ]
    with MASTER.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for record in sorted(records, key=lambda r: (r["publication_year"], r["name"])):
            row = {key: record.get(key) for key in fields}
            for modality in MODALITIES:
                row[f"has_{modality}"] = int(modality in record["modalities"])
            row["modality_count"] = len(record["modalities"])
            writer.writerow({k: "" if v is None else v for k, v in row.items()})


def svg_start(width: int, height: int, title: str, desc: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(title)}</title>',
        f'<desc id="desc">{esc(desc)}</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#18211f;letter-spacing:0}.title{font-size:22px;font-weight:700}.sub{font-size:13px;fill:#5d6965}.lab{font-size:12px;fill:#36413e}.val{font-size:11px;font-weight:700}.grid{stroke:#e2e7e5;stroke-width:1}.axis{stroke:#97a39f;stroke-width:1.2}.human{fill:#1b7f68}.paired{fill:#d8ea55}.robot{fill:#425b66}</style>',
        f'<text x="56" y="44" class="title">{esc(title)}</text>',
        f'<text x="56" y="70" class="sub">{esc(desc)}</text>',
    ]


def write_trend(records: list[dict]) -> None:
    width, height = 1120, 520
    years = list(range(min(r["publication_year"] for r in records), max(r["publication_year"] for r in records) + 1))
    regimes = ["human_ego", "ego_exo", "robot_ego"]
    counts = {(year, regime): 0 for year in years for regime in regimes}
    for record in records:
        counts[(record["publication_year"], record["regime"])] += 1
    lines = svg_start(width, height, "Publication timeline of the verified anchor cohort", f"Reference-paper years for {len(records)} cross-checked anchor datasets; this is not an exhaustive field trend.")
    left, top, plot_w, plot_h = 90, 115, 930, 300
    max_count = max(counts.values())
    for value in range(max_count + 1):
        y = top + plot_h - (value / max_count) * plot_h if max_count else top + plot_h
        lines += [f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" class="grid"/>', f'<text x="{left-18}" y="{y+4:.1f}" text-anchor="end" class="lab">{value}</text>']
    group_w = plot_w / len(years)
    bar_w = min(28, group_w / 4)
    colors = {"human_ego": "human", "ego_exo": "paired", "robot_ego": "robot"}
    for i, year in enumerate(years):
        center = left + group_w * (i + 0.5)
        lines.append(f'<text x="{center:.1f}" y="{top+plot_h+28}" text-anchor="middle" class="lab">{year}</text>')
        for j, regime in enumerate(regimes):
            value = counts[(year, regime)]
            bar_h = (value / max_count) * plot_h if max_count else 0
            x = center + (j - 1) * (bar_w + 5) - bar_w / 2
            y = top + plot_h - bar_h
            lines.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w}" height="{bar_h:.1f}" class="{colors[regime]}"/>')
            if value:
                lines.append(f'<text x="{x+bar_w/2:.1f}" y="{y-7:.1f}" text-anchor="middle" class="val">{value}</text>')
    legend = [("Human ego", "human"), ("Ego–exo", "paired"), ("Robot ego", "robot")]
    for idx, (label, cls) in enumerate(legend):
        x = 680 + idx * 130
        lines += [f'<rect x="{x}" y="465" width="13" height="13" class="{cls}"/>', f'<text x="{x+20}" y="476" class="lab">{label}</text>']
    lines.append('</svg>')
    (FIGURES / "anchor-release-timeline.svg").write_text("\n".join(lines), encoding="utf-8")


def write_modalities(records: list[dict]) -> None:
    width, height = 1120, 130 + 40 * len(MODALITIES)
    counts = Counter(m for record in records for m in record["modalities"])
    ordered = sorted(MODALITIES, key=lambda m: (-counts[m], m))
    lines = svg_start(width, height, "Modality coverage in the verified anchor cohort", f"Percentage of {len(records)} cross-checked datasets reporting each modality; availability and coverage depth are not implied.")
    left, top, plot_w, row_h = 220, 105, 790, 40
    for idx, modality in enumerate(ordered):
        y = top + idx * row_h
        pct = 100 * counts[modality] / len(records)
        lines += [
            f'<text x="{left-18}" y="{y+20}" text-anchor="end" class="lab">{esc(modality.replace("_", " "))}</text>',
            f'<rect x="{left}" y="{y+7}" width="{plot_w}" height="18" fill="#edf1ef"/>',
            f'<rect x="{left}" y="{y+7}" width="{plot_w*pct/100:.1f}" height="18" class="human"/>',
            f'<text x="{left+plot_w+14}" y="{y+21}" class="val">{counts[modality]}/{len(records)} · {pct:.0f}%</text>',
        ]
    lines.append('</svg>')
    (FIGURES / "anchor-modality-coverage.svg").write_text("\n".join(lines), encoding="utf-8")


def write_scale(records: list[dict]) -> None:
    available = sorted((r for r in records if r["hours"] is not None), key=lambda r: r["hours"])
    width, height = 1120, 150 + 48 * len(available)
    max_log = math.log10(max(r["hours"] for r in available))
    lines = svg_start(width, height, "Reported hours across comparable anchor records", "Log scale; missing hours omitted. Ego-Exo4D reports synchronized multi-view hours.")
    left, top, plot_w, row_h = 230, 110, 790, 48
    for power in range(0, math.ceil(max_log) + 1):
        x = left + (power / max_log) * plot_w
        lines += [f'<line x1="{x:.1f}" y1="{top-14}" x2="{x:.1f}" y2="{top+row_h*len(available)-12}" class="grid"/>', f'<text x="{x:.1f}" y="{top-28}" text-anchor="middle" class="lab">10^{power} h</text>']
    classes = {"human_ego": "human", "ego_exo": "paired", "robot_ego": "robot"}
    for idx, record in enumerate(available):
        y = top + idx * row_h
        value = record["hours"]
        bar_w = max(3, math.log10(value) / max_log * plot_w)
        lines += [
            f'<text x="{left-18}" y="{y+18}" text-anchor="end" class="lab">{esc(record["name"])}</text>',
            f'<rect x="{left}" y="{y+5}" width="{bar_w:.1f}" height="19" class="{classes[record["regime"]]}"/>',
            f'<text x="{min(left+bar_w+10, width-65):.1f}" y="{y+19}" class="val">{value:,.1f} h</text>',
        ]
    lines.append('</svg>')
    (FIGURES / "anchor-scale-hours.svg").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records = load_verified()
    FIGURES.mkdir(parents=True, exist_ok=True)
    write_master(records)
    statistics = {
        "cohort_size": len(records),
        "verification_status": "cross_checked_metadata",
        "evidence_level": 2,
        "publication_year_min": min(r["publication_year"] for r in records),
        "publication_year_max": max(r["publication_year"] for r in records),
        "regime_counts": dict(sorted(Counter(r["regime"] for r in records).items())),
        "modality_counts": dict(sorted(Counter(m for r in records for m in r["modalities"]).items())),
        "records_with_hours": sum(r["hours"] is not None for r in records),
    }
    STATS.write_text(json.dumps(statistics, indent=2) + "\n", encoding="utf-8")
    write_trend(records)
    write_modalities(records)
    write_scale(records)
    print(f"Built master table and 3 figures from {len(records)} cross-checked records.")


if __name__ == "__main__":
    main()
