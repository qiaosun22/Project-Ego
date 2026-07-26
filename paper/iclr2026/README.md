# ProjectEgo ICLR 2026-format draft

This directory vendors the official ICLR 2026 style files downloaded from:

https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip

The source defaults to anonymous submission mode. Do not uncomment
`\iclrfinalcopy` or add author-identifying acknowledgements for review.

Build with a standard TeX Live installation:

```bash
latexmk -pdf main.tex
```

or:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The six PDFs under `figures/` are derived from the repository SVG figures.
Regenerate them after catalog or figure changes rather than editing them by hand.

ICLR 2026 permits at most 9 main-text pages at initial submission; references
and appendices do not count toward that limit. The current source is a research
draft and must be recompiled and page-counted after every substantive edit.
