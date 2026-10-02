# dbs — APDS marketplace data & storage

Public **data/storage backend** for the [APDS marketplace](https://github.com/web12-app/apds)
(live at https://apds.onrender.com).

> The application presents **Apps, Versions, Downloads** — the git internals
> (tags, releases, commits, actions) behind this repo are implementation
> details and are never exposed to end users. All git authentication happens
> server-side only.

## Structure

```
dbs/
├── data/
│   ├── categories.json      # marketplace categories
│   ├── apps.json            # catalog index (app summaries)
│   ├── apps/{slug}.json     # per-app metadata incl. version history
│   └── reviews/{slug}.json  # user reviews
├── assets/                  # uploaded icons / screenshots
├── scripts/
│   ├── seed_data.py         # regenerates the seed catalog
│   └── publish_version.py   # used by the release workflow
└── .github/workflows/
    └── process-release.yml  # release validation & publishing pipeline
```

## How releases work

1. A developer uploads a package through the marketplace API
   (temporary, authenticated upload session).
2. The server stores the package as a **draft release asset**.
3. The server dispatches the **Process release** workflow.
4. The workflow validates the package (type, magic bytes, SHA-256),
   publishes the release — which creates an **immutable git tag**
   (`apps/{slug}/v{version}`) — and updates the catalog metadata.
5. Users download through the marketplace API, which streams the
   authorized asset and verifies checksums.

## Seeding

```bash
python3 scripts/seed_data.py
```
