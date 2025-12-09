# Cosilico Law Archive

**Open source US statute text via API.**

US law is public domain, but no open source project provides structured statute text via API with historical versions. This project fills that gap.

## Features

- **Federal statutes** — All 54 titles of the US Code from official USLM XML
- **Historical versions** — Track changes over time
- **REST API** — Query statutes by citation, keyword, or path
- **Structured data** — JSON output with section hierarchy, cross-references, and metadata
- **State codes** — Incremental rollout (starting with CA, NY, TX)

## Quick Start

```bash
# Install
pip install cosilico-lawarchive

# Run the API server
lawarchive serve

# Or use the CLI
lawarchive get "26 USC 32"        # Get IRC § 32 (EITC)
lawarchive search "earned income" # Search across statutes
```

## API Usage

```python
from lawarchive import LawArchive

archive = LawArchive()

# Get a specific section
eitc = archive.get("26 USC 32")
print(eitc.title)        # "Earned income"
print(eitc.text)         # Full section text
print(eitc.subsections)  # Hierarchical structure

# Search
results = archive.search("child tax credit", title=26)
for section in results:
    print(f"{section.citation}: {section.title}")

# Get historical version
eitc_2020 = archive.get("26 USC 32", as_of="2020-01-01")
```

## REST API

```bash
# Get section by citation
curl http://localhost:8000/v1/sections/26/32

# Search
curl "http://localhost:8000/v1/search?q=earned+income&title=26"

# Get specific subsection
curl http://localhost:8000/v1/sections/26/32/a/1

# Historical version
curl "http://localhost:8000/v1/sections/26/32?as_of=2020-01-01"
```

## Data Sources

| Source | Content | Format | Update Frequency |
|--------|---------|--------|------------------|
| [uscode.house.gov](https://uscode.house.gov/download/download.shtml) | US Code | USLM XML | Continuous |
| [eCFR](https://www.ecfr.gov/) | Code of Federal Regulations | XML | Daily |
| State legislatures | State codes | Varies | Varies |

## Architecture

```
cosilico-lawarchive/
├── src/lawarchive/
│   ├── __init__.py
│   ├── archive.py       # Main LawArchive class
│   ├── models.py        # Pydantic models for statutes
│   ├── parsers/
│   │   ├── uslm.py      # USLM XML parser
│   │   ├── ecfr.py      # eCFR XML parser
│   │   └── state/       # State-specific parsers
│   ├── api/
│   │   ├── main.py      # FastAPI app
│   │   └── routes.py    # API routes
│   ├── cli.py           # Command-line interface
│   └── storage/
│       ├── base.py      # Storage interface
│       ├── sqlite.py    # SQLite backend
│       └── postgres.py  # PostgreSQL backend
├── data/
│   └── .gitkeep         # Downloaded/parsed data (gitignored)
├── tests/
└── scripts/
    └── ingest.py        # Data ingestion scripts
```

## Why This Exists

From [DESIGN.md](https://github.com/CosilicoAI/cosilico-engine/blob/main/docs/DESIGN.md#1571-existing-statute-apis-and-why-we-need-our-own):

> No open source project provides structured statute text via API with historical versions.
>
> - OpenLaws.us is closest but proprietary
> - Free Law Project covers case law only
> - Cornell LII prohibits scraping
> - Official sources require self-hosting

We're building this for [Cosilico](https://cosilico.ai)'s rules engine but open-sourcing it as a public good.

## License

Apache 2.0 — Use it for anything.

## Contributing

We welcome contributions! Priority areas:

1. State code parsers (50 states to cover)
2. Historical version tracking
3. Cross-reference resolution
4. Full-text search improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
