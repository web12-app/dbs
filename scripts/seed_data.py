#!/usr/bin/env python3
"""Seed the APDS marketplace catalog (data/*.json) in the dbs repo.

Run from repo root:  python3 scripts/seed_data.py
Idempotent: regenerates the same catalog files.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

CATEGORIES = [
    {"slug": "games", "name": "Games", "emoji": "🎮", "gradient": ["#7c3aed", "#f472b6"]},
    {"slug": "music", "name": "Music", "emoji": "🎵", "gradient": ["#06b6d4", "#3b82f6"]},
    {"slug": "education", "name": "Education", "emoji": "🎓", "gradient": ["#10b981", "#84cc16"]},
    {"slug": "tools", "name": "Tools", "emoji": "🧰", "gradient": ["#0ea5e9", "#6366f1"]},
    {"slug": "productivity", "name": "Productivity", "emoji": "⚡", "gradient": ["#f59e0b", "#ef4444"]},
    {"slug": "social", "name": "Social", "emoji": "💬", "gradient": ["#ec4899", "#f43f5e"]},
    {"slug": "developer-tools", "name": "Developer tools", "emoji": "🧩", "gradient": ["#8b5cf6", "#d946ef"]},
]

# slug, name, developer, dev_id, category, emoji, gradient, tagline, tags,
# featured, trending, downloads, rating, ratings_count, min_os, age, created,
# versions[(ver, date, notes, size_kb, share)], reviews[(user, stars, title, body, date)], shots
APPS = [
    dict(
        slug="lumen-notes", name="Lumen Notes", dev="Northlight Labs", dev_id="northlight-labs",
        category="productivity", emoji="📝", gradient=["#6366f1", "#8b5cf6"],
        tagline="Notes that organize themselves",
        description=("Lumen Notes is a calm, fast home for your ideas. Capture thoughts with instant "
                     "markdown, organize automatically with smart collections, and find anything in "
                     "milliseconds with full-text search. Everything syncs end-to-end encrypted across "
                     "your devices."),
        tags=["notes", "markdown", "sync", "organization"],
        featured=True, trending=True, downloads=284011, rating=4.8, ratings_count=12403,
        min_os="8.0", age="Everyone", created="2026-08-14",
        versions=[
            ("1.2.0", "2026-09-28", "Widgets on the home screen, dark theme polish, and faster offline sync.", 18432, 0.6),
            ("1.1.0", "2026-09-02", "Markdown tables, PDF export, and 40+ fixes.", 17920, 0.4),
        ],
        reviews=[
            ("aarav_dev", 5, "Replaced three apps", "The smart collections alone are worth it. Sync is instant and search is scary fast.", "2026-09-12"),
            ("priya.m", 4, "Almost perfect", "Love the focus mode. Wish widgets came to tablets too.", "2026-09-20"),
        ],
        shots=["Capture instantly", "Smart collections", "Focus mode"],
    ),
    dict(
        slug="pixel-drift", name="Pixel Drift", dev="Frostline Games", dev_id="frostline-games",
        category="games", emoji="🏎️", gradient=["#f97316", "#ef4444"],
        tagline="Retro arcade racing",
        description=("Slide into retro-futuristic arcade racing. Drift through 60 hand-crafted tracks, "
                     "upgrade a garage of 24 hover cars, and climb the global leaderboards. Built for "
                     "quick sessions and long streaks."),
        tags=["racing", "arcade", "retro", "multiplayer"],
        featured=True, trending=True, downloads=1904222, rating=4.6, ratings_count=48211,
        min_os="9.0", age="Teen (fantasy violence)", created="2026-05-30",
        versions=[
            ("2.0.1", "2026-09-30", "Neon Bay circuit and anti-cheat improvements.", 96256, 0.55),
            ("1.9.0", "2026-08-21", "New hover class: Blizzard. Ghost replays.", 91136, 0.45),
        ],
        reviews=[
            ("gamer_raj", 5, "Drift king", "Best arcade racer on here. The hover cars feel great.", "2026-09-18"),
            ("kim_codes", 4, "Great, battery hungry", "Amazing graphics but my phone gets warm after long sessions.", "2026-09-25"),
        ],
        shots=["Garage", "Race day", "Leaderboards"],
    ),
    dict(
        slug="waveform", name="Waveform", dev="Auralis", dev_id="auralis",
        category="music", emoji="🎧", gradient=["#06b6d4", "#3b82f6"],
        tagline="A music player that learns you",
        description=("A music player that learns what you love. Waveform builds adaptive playlists from "
                     "your library, streams losslessly when you're on Wi-Fi, and keeps the beats going "
                     "offline when you're not."),
        tags=["music", "player", "playlists", "offline"],
        featured=False, trending=True, downloads=952301, rating=4.7, ratings_count=30188,
        min_os="8.0", age="Everyone", created="2026-03-12",
        versions=[
            ("3.4.0", "2026-09-25", "Crossfade, gapless everywhere, and a redesigned queue.", 32768, 0.5),
            ("3.3.2", "2026-09-01", "Bug fixes for Bluetooth skip.", 31744, 0.5),
        ],
        reviews=[
            ("nina", 5, "It knows my taste", "The adaptive mix is genuinely magical.", "2026-09-10"),
            ("tone_purist", 4, "Lossless please on 4G", "Excellent player, just let me force lossless everywhere.", "2026-09-22"),
        ],
        shots=["Now playing", "Adaptive mix", "Equalizer"],
    ),
    dict(
        slug="mathlings", name="Mathlings", dev="Tiny Orbit", dev_id="tiny-orbit",
        category="education", emoji="🔢", gradient=["#10b981", "#84cc16"],
        tagline="Math adventures for little minds",
        description=("Meet the Mathlings — tiny creatures that turn arithmetic into adventure. Bite-sized "
                     "puzzles adapt to your child's pace, with gentle streaks and zero ads."),
        tags=["kids", "math", "learning", "puzzles"],
        featured=False, trending=False, downloads=45230, rating=4.9, ratings_count=1877,
        min_os="7.0", age="Everyone", created="2026-09-20",
        versions=[
            ("1.0.2", "2026-09-29", "Gentler difficulty curve and a new counting garden.", 24576, 0.7),
            ("1.0.1", "2026-09-20", "Parental dashboard.", 24064, 0.3),
        ],
        reviews=[
            ("deepa_r", 5, "My kid asks for it", "That never happened with homework before.", "2026-09-27"),
        ],
        shots=["Counting garden", "Puzzle path", "Streak rewards"],
    ),
    dict(
        slug="vaultkey", name="Vaultkey", dev="Ironbark Software", dev_id="ironbark-software",
        category="tools", emoji="🔐", gradient=["#334155", "#0ea5e9"],
        tagline="Passwords, locked tight",
        description=("Your passwords, locked tight. Vaultkey stores secrets in a zero-knowledge vault, "
                     "fills them instantly on every device, and alerts you the moment a breach touches "
                     "your accounts."),
        tags=["security", "passwords", "privacy", "2fa"],
        featured=False, trending=False, downloads=388102, rating=4.5, ratings_count=15504,
        min_os="8.0", age="Everyone", created="2026-02-08",
        versions=[
            ("4.1.0", "2026-09-26", "Passkeys support and emergency kit PDFs.", 12288, 0.5),
            ("4.0.0", "2026-08-30", "Redesigned vault, faster autofill.", 11776, 0.5),
        ],
        reviews=[
            ("sam_the_sec", 5, "Zero knowledge, zero fuss", "Imported 400 logins without a hitch. Breach alerts are quick.", "2026-09-08"),
            ("ola_n", 4, "Good but pricey", "Core features are free; the family plan is worth it though.", "2026-09-19"),
        ],
        shots=["The vault", "Autofill", "Breach radar"],
    ),
    dict(
        slug="chatterbox", name="Chatterbox", dev="Loopside", dev_id="loopside",
        category="social", emoji="💬", gradient=["#ec4899", "#f43f5e"],
        tagline="Talk everywhere, simply",
        description=("Messaging stripped to its essentials — fast, private chats with friends and groups, "
                     "read receipts you control, and no algorithm in sight."),
        tags=["messaging", "chat", "groups", "privacy"],
        featured=False, trending=True, downloads=1204330, rating=4.2, ratings_count=64340,
        min_os="8.0", age="13+", created="2026-01-15",
        versions=[
            ("2.7.3", "2026-09-27", "Voice notes (beta) and push reliability fixes.", 28672, 0.45),
            ("2.6.0", "2026-08-25", "Group invites via link.", 27648, 0.55),
        ],
        reviews=[
            ("mex_", 3, "Fine but basic", "Fast and private, yes. Missing voice notes for now.", "2026-09-14"),
            ("lo_fi", 4, "No algorithm, no drama", "Exactly what group chats should be.", "2026-09-21"),
        ],
        shots=["Chats", "Groups", "Privacy first"],
    ),
    dict(
        slug="snippetly", name="Snippetly", dev="Codecraft", dev_id="codecraft",
        category="developer-tools", emoji="🧩", gradient=["#8b5cf6", "#d946ef"],
        tagline="Your code, one hotkey away",
        description=("Snippetly keeps a searchable library of snippets with syntax highlighting, "
                     "placeholder expansion, and instant sync between your machines."),
        tags=["snippets", "code", "productivity", "sync"],
        featured=False, trending=False, downloads=88420, rating=4.8, ratings_count=3211,
        min_os="8.0", age="Everyone", created="2026-06-10",
        versions=[
            ("1.5.0", "2026-09-19", "Placeholder expansion and team sharing.", 8192, 0.6),
            ("1.4.2", "2026-08-28", "Syntax themes.", 7680, 0.4),
        ],
        reviews=[
            ("byte_wizard", 5, "Hotkey heaven", "Cut my snippet hunt from minutes to seconds.", "2026-09-16"),
        ],
        shots=["Library", "Snippet editor", "Hotkey anywhere"],
    ),
    dict(
        slug="focusflow", name="Focusflow", dev="Northlight Labs", dev_id="northlight-labs",
        category="productivity", emoji="⏱️", gradient=["#f59e0b", "#f97316"],
        tagline="Deep work, made simple",
        description=("Focusflow blends a flexible pomodoro timer with ambient soundscapes and gentle "
                     "analytics that show when you do your best work."),
        tags=["focus", "pomodoro", "timer", "habits"],
        featured=False, trending=False, downloads=210455, rating=4.4, ratings_count=9022,
        min_os="7.0", age="Everyone", created="2026-04-02",
        versions=[
            ("2.2.0", "2026-09-21", "Rhythm insights and 12 new soundscapes.", 15360, 0.5),
            ("2.1.0", "2026-08-11", "Calendar blocking.", 14848, 0.5),
        ],
        reviews=[
            ("anna_k", 4, "Calm and effective", "Soundscapes are lovely. Stats could go deeper.", "2026-09-23"),
        ],
        shots=["Session", "Soundscapes", "Your rhythms"],
    ),
    dict(
        slug="stellar-siege", name="Stellar Siege", dev="Frostline Games", dev_id="frostline-games",
        category="games", emoji="🚀", gradient=["#312e81", "#7c3aed"],
        tagline="Command fleets across the stars",
        description=("A turn-based strategy game of expansion and diplomacy — build stations, forge "
                     "alliances, and out-think opponents in async multiplayer."),
        tags=["strategy", "scifi", "multiplayer", "turn-based"],
        featured=True, trending=False, downloads=604512, rating=4.7, ratings_count=22480,
        min_os="9.0", age="Teen (fantasy violence)", created="2026-06-25",
        versions=[
            ("1.3.0", "2026-09-23", "Alliance treaties and a new sector map.", 71680, 0.5),
            ("1.2.4", "2026-08-19", "Fleet pathfinding fixes.", 69632, 0.5),
        ],
        reviews=[
            ("cmdr_shep", 5, "One more turn...", "Async multiplayer is brilliantly done.", "2026-09-17"),
            ("zoe_q", 4, "Deep strategy", "Steep learning curve but rewarding.", "2026-09-26"),
        ],
        shots=["Star map", "Fleet command", "Diplomacy"],
    ),
    dict(
        slug="tunetrader", name="TuneTrader", dev="Auralis", dev_id="auralis",
        category="music", emoji="🎛️", gradient=["#14b8a6", "#0ea5e9"],
        tagline="Make beats on the move",
        description=("TuneTrader packs a pocket studio — step sequencer, sample pads, and effects — that "
                     "exports studio-quality tracks straight from your phone."),
        tags=["beats", "sequencer", "music", "studio"],
        featured=False, trending=False, downloads=25871, rating=4.3, ratings_count=918,
        min_os="9.0", age="Everyone", created="2026-09-15",
        versions=[
            ("1.1.0", "2026-09-24", "Effects rack and 24-bit export.", 40960, 0.6),
            ("1.0.0", "2026-09-15", "First public release.", 38912, 0.4),
        ],
        reviews=[
            ("beat_mkr", 4, "Studio in a pocket", "Export quality surprised me. UI takes a day to learn.", "2026-09-24"),
        ],
        shots=["Sequencer", "Sample pads", "Export"],
    ),
    dict(
        slug="lingoplay", name="Lingoplay", dev="Tiny Orbit", dev_id="tiny-orbit",
        category="education", emoji="🗣️", gradient=["#22c55e", "#eab308"],
        tagline="Speak a new language in 5 min/day",
        description=("Lingoplay's story-driven micro-lessons adapt to you, with speech practice that "
                     "actually listens. Five minutes a day really adds up."),
        tags=["languages", "learning", "speech", "streaks"],
        featured=True, trending=False, downloads=733940, rating=4.6, ratings_count=40112,
        min_os="8.0", age="Everyone", created="2026-01-20",
        versions=[
            ("2.0.0", "2026-09-17", "New story engine, speech drills v2.", 35840, 0.55),
            ("1.9.1", "2026-08-14", "Streak repair.", 34816, 0.45),
        ],
        reviews=[
            ("yuki_t", 5, "Streak 120 and counting", "Five minutes really works.", "2026-09-11"),
            ("marco_p", 4, "Great stories", "Wish there were more languages.", "2026-09-15"),
        ],
        shots=["Today's story", "Speech practice", "Streak"],
    ),
    dict(
        slug="docudock", name="Docudock", dev="Ironbark Software", dev_id="ironbark-software",
        category="tools", emoji="📄", gradient=["#38bdf8", "#6366f1"],
        tagline="PDFs, tamed",
        description=("Docudock merges, signs, compresses, and converts documents right on your device — "
                     "your files never leave your phone unless you say so."),
        tags=["pdf", "documents", "esign", "files"],
        featured=False, trending=False, downloads=155230, rating=4.4, ratings_count=7044,
        min_os="8.0", age="Everyone", created="2026-02-27",
        versions=[
            ("3.0.1", "2026-09-22", "Faster compression and form detection.", 20480, 0.5),
            ("2.9.0", "2026-08-06", "E-signature overhaul.", 19968, 0.5),
        ],
        reviews=[
            ("form_filler", 5, "Signed and done", "E-signing on my phone just works now.", "2026-09-13"),
        ],
        shots=["Documents", "Sign & fill", "Compress"],
    ),
]

PERMISSIONS = {
    "lumen-notes": ["Internet", "Storage"],
    "pixel-drift": ["Internet", "Storage", "Vibrate"],
    "waveform": ["Internet", "Storage", "Media controls"],
    "mathlings": ["Internet"],
    "vaultkey": ["Internet", "Storage", "Biometrics"],
    "chatterbox": ["Internet", "Storage", "Camera", "Microphone", "Contacts (optional)"],
    "snippetly": ["Internet", "Storage"],
    "focusflow": ["Internet", "Notifications"],
    "stellar-siege": ["Internet", "Storage"],
    "tunetrader": ["Internet", "Storage", "Microphone"],
    "lingoplay": ["Internet", "Microphone", "Storage"],
    "docudock": ["Storage", "Camera", "Internet"],
}

SITES = {
    "northlight-labs": "https://northlightlabs.dev",
    "frostline-games": "https://frostline.games",
    "auralis": "https://auralis.audio",
    "tiny-orbit": "https://tinyorbit.fun",
    "ironbark-software": "https://ironbark.software",
    "loopside": "https://loopside.chat",
    "codecraft": "https://codecraft.tools",
}


def build():
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "apps").mkdir(exist_ok=True)
    (DATA / "reviews").mkdir(exist_ok=True)

    (DATA / "categories.json").write_text(json.dumps(CATEGORIES, indent=2) + "\n")

    summaries = []
    for a in APPS:
        site = SITES[a["dev_id"]]
        latest = a["versions"][0]
        icon = {"type": "gradient", "emoji": a["emoji"], "gradient": a["gradient"]}
        screenshots = [
            {"title": t, "palette": a["gradient"], "emoji": a["emoji"]}
            for t in a["shots"]
        ]
        versions = []
        for ver, date, notes, size_kb, share in a["versions"]:
            versions.append({
                "version": ver,
                "notes": notes,
                "size_kb": size_kb,
                "min_os": a["min_os"],
                "status": "published",
                "created_at": date,
                "published_at": date,
                "downloads": int(a["downloads"] * share),
                "release_tag": f"apps/{a['slug']}/v{ver}",
                "sha256": None,
            })
        full = {
            "slug": a["slug"],
            "name": a["name"],
            "package_id": f"dev.apds.{a['slug'].replace('-', '')}",
            "developer": a["dev"],
            "developer_id": a["dev_id"],
            "category": a["category"],
            "tagline": a["tagline"],
            "description": a["description"],
            "icon": icon,
            "screenshots": screenshots,
            "website": site,
            "privacy_policy": f"{site}/privacy",
            "age_rating": a["age"],
            "permissions": PERMISSIONS[a["slug"]],
            "tags": a["tags"],
            "status": "published",
            "rating": a["rating"],
            "ratings_count": a["ratings_count"],
            "downloads": a["downloads"],
            "created_at": a["created"],
            "updated_at": latest[1],
            "featured": a["featured"],
            "trending": a["trending"],
            "versions": versions,
        }
        (DATA / "apps" / f"{a['slug']}.json").write_text(json.dumps(full, indent=2) + "\n")

        reviews = [
            {"id": f"r{i}", "user": u, "rating": r, "title": t, "body": b, "created_at": d}
            for i, (u, r, t, b, d) in enumerate(a["reviews"])
        ]
        (DATA / "reviews" / f"{a['slug']}.json").write_text(json.dumps(reviews, indent=2) + "\n")

        summaries.append({
            "slug": a["slug"],
            "name": a["name"],
            "developer": a["dev"],
            "developer_id": a["dev_id"],
            "category": a["category"],
            "tagline": a["tagline"],
            "icon": icon,
            "tags": a["tags"],
            "rating": a["rating"],
            "ratings_count": a["ratings_count"],
            "downloads": a["downloads"],
            "version": latest[0],
            "status": "published",
            "featured": a["featured"],
            "trending": a["trending"],
            "created_at": a["created"],
            "updated_at": latest[1],
        })

    (DATA / "apps.json").write_text(json.dumps(summaries, indent=2) + "\n")
    print(f"Seeded {len(summaries)} apps, {len(CATEGORIES)} categories -> {DATA}")


if __name__ == "__main__":
    build()
