-- dbs — schema reference for the marketplace server-side database (SQLite).
-- The server (apds backend) owns this database; it is NOT stored in this repo.
-- This file documents the structure. Catalog data itself lives in data/*.json.

-- Marketplace accounts (credentials never leave the server)
CREATE TABLE IF NOT EXISTS users (
    id            TEXT PRIMARY KEY,
    username      TEXT NOT NULL UNIQUE COLLATE NOCASE,
    email         TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    created_at    TEXT NOT NULL,
    settings      TEXT NOT NULL DEFAULT '{}'
);

-- Login sessions (server-side tokens, referenced by secure cookies)
CREATE TABLE IF NOT EXISTS sessions (
    token_hash TEXT PRIMARY KEY,
    user_id    TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    user_agent TEXT NOT NULL DEFAULT ''
);

-- Scoped, revocable API keys (only hashes are stored)
CREATE TABLE IF NOT EXISTS api_keys (
    id           TEXT PRIMARY KEY,
    user_id      TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name         TEXT NOT NULL,
    key_hash     TEXT NOT NULL UNIQUE,
    prefix       TEXT NOT NULL,
    scopes       TEXT NOT NULL DEFAULT '[]',   -- JSON array
    created_at   TEXT NOT NULL,
    last_used_at TEXT,
    revoked_at   TEXT
);

-- Developer profiles
CREATE TABLE IF NOT EXISTS developers (
    id         TEXT PRIMARY KEY,
    user_id    TEXT NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    name       TEXT NOT NULL,
    slug       TEXT NOT NULL UNIQUE,
    bio        TEXT NOT NULL DEFAULT '',
    website    TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);

-- Temporary, single-purpose upload sessions (public tunnel auth)
CREATE TABLE IF NOT EXISTS upload_sessions (
    id              TEXT PRIMARY KEY,
    user_id         TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    app_slug        TEXT NOT NULL,
    version         TEXT NOT NULL,
    filename        TEXT NOT NULL,
    declared_size   INTEGER NOT NULL,
    declared_sha256 TEXT NOT NULL,
    token_hash      TEXT NOT NULL UNIQUE,
    state           TEXT NOT NULL DEFAULT 'created', -- created|stored|failed|canceled
    release_id      INTEGER,                          -- internal storage release id
    actual_size     INTEGER,
    actual_sha256   TEXT,
    created_at      TEXT NOT NULL,
    expires_at      TEXT NOT NULL
);

-- Download counters & history
CREATE TABLE IF NOT EXISTS download_stats (
    app_slug TEXT NOT NULL,
    version  TEXT NOT NULL,
    day      TEXT NOT NULL,
    count    INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (app_slug, version, day)
);

CREATE TABLE IF NOT EXISTS download_history (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    TEXT,
    app_slug   TEXT NOT NULL,
    version    TEXT NOT NULL,
    bytes      INTEGER NOT NULL,
    created_at TEXT NOT NULL
);

-- Per-user library (installed / wishlist)
CREATE TABLE IF NOT EXISTS library (
    user_id   TEXT NOT NULL,
    app_slug  TEXT NOT NULL,
    kind      TEXT NOT NULL,        -- installed | wishlist
    added_at  TEXT NOT NULL,
    PRIMARY KEY (user_id, app_slug, kind)
);

-- Notifications
CREATE TABLE IF NOT EXISTS notifications (
    id         TEXT PRIMARY KEY,
    user_id    TEXT NOT NULL,
    kind       TEXT NOT NULL DEFAULT 'info',
    title      TEXT NOT NULL,
    body       TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    read_at    TEXT
);
