# dbs

Private repo — **Vite** frontend + **Python** backend starter.

## Structure

```
dbs/
├── frontend/   # Vite + React
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
└── backend/    # Python — FastAPI + SQLite
    ├── main.py
    └── requirements.txt
```

## Run the backend (Python)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

## Run the frontend (Vite)

```bash
cd frontend
npm install
npm run dev
```

Opens at http://localhost:5173 — the dev server proxies `/api/*` to the backend on port 8000.

## API

| Method | Path | Description |
|---|---|---|
| GET | `/api/health` | Health check |
| GET | `/api/records` | List all records |
| POST | `/api/records` | Create a record `{"name": "...", "value": "..."}` |
| DELETE | `/api/records/{id}` | Delete a record |

SQLite database file is created automatically at `backend/dbs.db`.
