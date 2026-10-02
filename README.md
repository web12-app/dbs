# dbs (private)

Private database repository — schemas, migrations and seed data.

> ⚠️ **No application code lives here.**
> The full-stack app (Vite + React frontend, FastAPI + Python backend) is in the
> **public** repo: [web12-app/apds](https://github.com/web12-app/apds) — deployed on Render.

## Files

- `schema.sql` — SQLite schema used by the apds app (source of truth)

## Apply schema manually

```bash
sqlite3 dbs.db < schema.sql
```

The app creates the same tables automatically on startup (`init_db()` in
`apds/backend/main.py`).
