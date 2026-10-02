-- dbs — private schema for the apds app (SQLite)
-- Source of truth for the database structure.
-- The app (web12-app/apds) applies this automatically on startup.

CREATE TABLE IF NOT EXISTS records (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_records_created_at ON records (created_at);
