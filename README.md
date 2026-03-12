# SkillSync â€” Portfolio & Skill Tracker

SkillSync is a **full-stack Flask web application** that lets developers, students, and professionals manage their skills, showcase projects, and share a live public portfolio â€” all through a clean, modern dashboard.

---

## Overview

SkillSync gives you a personal dashboard to track every skill you've ever learned (rated on a 0â€“10 scale), log every project you've built, and instantly share it all via a unique public portfolio URL (`/portfolio/<your-username>`). It's your living digital profile â€” update it once, and your shareable portfolio updates automatically.

---

## Features

| Area | What It Does |
|---|---|
| **Authentication** | Secure register / login / logout with hashed passwords (Werkzeug) and CSRF-protected forms |
| **Skill Tracking** | Add skills with name, primary category (12 built-in), subcategory, 0â€“10 proficiency level, description, and comma-separated tags |
| **Project Management** | Log projects with title, description, tech stack, GitHub URL, live demo URL, image URL, and status (Completed / In Progress / Planned) |
| **Analytics Dashboard** | Stats cards (total skills, project count, average skill level) plus two Chart.js charts: skills by category and skill level distribution |
| **Profile Editor** | Edit name, bio, GitHub username, LinkedIn URL, personal portfolio URL, and upload a profile picture |
| **Public Portfolio** | Shareable page at `/portfolio/<username>` showing profile, skills with progress bars, and projects |
| **Print / PDF Portfolio** | Browser-printable portfolio view at `/portfolio/print/<username>` with print-optimised CSS â€” save as PDF or paper |
| **API Endpoint** | `/dashboard/api/skills_data` returns JSON for dashboard chart rendering |

---

## Tech Stack

**Backend**
- Python 3 Â· Flask 2.3.3
- Flask-SQLAlchemy 3.0.5 â€” ORM & database management
- Flask-Login 0.6.3 â€” session authentication
- Flask-WTF 1.1.1 / WTForms 3.0.1 â€” forms & CSRF protection
- Werkzeug 2.3.7 â€” WSGI utilities & password hashing
- WeasyPrint 60.1 â€” PDF/print portfolio rendering
- Pillow 10.1.0 â€” profile picture image handling
- python-dotenv 1.0.0 â€” environment variable loading

**Frontend**
- Tailwind CSS (CDN) â€” utility-first styling
- Chart.js (CDN) â€” skills analytics charts
- Font Awesome 6.4 â€” icons
- Google Fonts â€” Poppins (headings) Â· Inter (body)
- Vanilla JavaScript â€” dropdown, tooltip, confirmation, and chart initialisation

**Database**
- SQLite (default, zero-config, file `skillsync.db`)
- Configurable via `DATABASE_URL` environment variable for any SQLAlchemy-supported database

---

## Data Models

### `User`
| Field | Type | Notes |
|---|---|---|
| `username` | String(80) | Unique, indexed |
| `email` | String(120) | Unique, indexed |
| `password_hash` | String(128) | Werkzeug PBKDF2 hash |
| `first_name` / `last_name` | String(50) | Required |
| `bio` | Text | Optional |
| `github_username` | String(100) | Links to GitHub profile on public page |
| `linkedin_url` | String(255) | Optional |
| `portfolio_url` | String(255) | Optional |
| `profile_picture` | String(255) | Stored under `static/uploads/` |
| `created_at` / `last_login` | DateTime | Auto-tracked |

### `Skill`
| Field | Type | Notes |
|---|---|---|
| `name` | String(100) | Required |
| `category` | String(50) | One of 12 preset categories |
| `subcategory` | String(50) | Optional free-text |
| `level` | Integer (0â€“10) | Proficiency score |
| `description` | Text | Optional |
| `tags` | String(200) | Comma-separated |

**Skill Categories:** Programming Languages Â· Web Technologies Â· Frameworks & Libraries Â· Databases & Storage Â· Cloud Services Â· DevOps & Tools Â· Mobile Development Â· Design & Multimedia Â· AI & Machine Learning Â· Security & Authentication Â· Soft Skills Â· Other

### `Project`
| Field | Type | Notes |
|---|---|---|
| `title` | String(150) | Required |
| `description` | Text | Required |
| `tech_stack` | String(255) | Comma-separated technologies |
| `github_url` | String(255) | Optional |
| `demo_url` | String(255) | Optional |
| `image_url` | String(255) | Optional |
| `status` | String(20) | `completed` Â· `in-progress` Â· `planned` |

---

## Route Map

| Method | URL | Description |
|---|---|---|
| GET | `/` | Landing page (redirects to dashboard if logged in) |
| GET/POST | `/auth/register` | New user registration |
| GET/POST | `/auth/login` | Login |
| GET | `/auth/logout` | Logout |
| GET | `/dashboard/` | Main dashboard with stats & charts |
| GET | `/dashboard/skills` | Paginated skills list |
| GET/POST | `/dashboard/add_skill` | Add a new skill |
| GET | `/dashboard/projects` | Paginated projects list |
| GET/POST | `/dashboard/add_project` | Add a new project |
| GET/POST | `/dashboard/profile` | Edit profile & upload picture |
| GET | `/dashboard/api/skills_data` | JSON data for charts |
| GET | `/portfolio/<username>` | Public shareable portfolio |
| GET | `/portfolio/print/<username>` | Printable portfolio (own user only) |

---

## Project Structure

```
SkillSync/
â”œâ”€â”€ run.py                  # App entry point â€” creates DB tables on first run
â”œâ”€â”€ config.py               # Config class (SECRET_KEY, DB URI, pagination)
â”œâ”€â”€ recreate_db.py          # Drop & recreate all tables (dev utility)
â”œâ”€â”€ update_db.py            # Database migration utility
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ .env                    # (you create this) SECRET_KEY, DATABASE_URL
â””â”€â”€ app/
    â”œâ”€â”€ __init__.py         # Application factory (create_app)
    â”œâ”€â”€ extensions.py       # db, login_manager, bootstrap instances
    â”œâ”€â”€ models.py           # User, Skill, Project SQLAlchemy models
    â”œâ”€â”€ forms.py            # WTForms: Login, Register, Profile, Skill, Project
    â”œâ”€â”€ routes/
    â”‚   â”œâ”€â”€ auth.py         # /auth/* â€” register, login, logout
    â”‚   â”œâ”€â”€ dashboard.py    # /dashboard/* â€” skills, projects, profile, charts API
    â”‚   â”œâ”€â”€ main.py         # / and /portfolio/<username> (public view)
    â”‚   â”œâ”€â”€ portfolio.py    # /portfolio/print/<username> (printable view)
    â”‚   â””â”€â”€ api.py          # Reserved for future API endpoints
    â”œâ”€â”€ templates/
    â”‚   â”œâ”€â”€ base.html       # Base layout: Tailwind, Chart.js, FA icons; nav changes based on auth state
    â”‚   â”œâ”€â”€ index.html      # Landing / marketing page
    â”‚   â”œâ”€â”€ portfolio_public.html   # Public portfolio (skills + projects + links)
    â”‚   â”œâ”€â”€ portfolio_print.html    # Print-optimised portfolio with @media print CSS
    â”‚   â”œâ”€â”€ portfolio_pdf.html      # PDF variant
    â”‚   â”œâ”€â”€ resume.html             # Resume view
    â”‚   â”œâ”€â”€ auth/
    â”‚   â”‚   â”œâ”€â”€ login.html
    â”‚   â”‚   â””â”€â”€ register.html
    â”‚   â””â”€â”€ dashboard/
    â”‚       â”œâ”€â”€ dashboard.html   # Stats cards + Chart.js canvases
    â”‚       â”œâ”€â”€ skills.html      # Paginated skill cards
    â”‚       â”œâ”€â”€ add_skill.html   # Skill form
    â”‚       â”œâ”€â”€ projects.html    # Paginated project cards
    â”‚       â”œâ”€â”€ add_project.html # Project form
    â”‚       â””â”€â”€ profile.html     # Profile edit form
    â””â”€â”€ static/
        â”œâ”€â”€ css/main.css
        â”œâ”€â”€ js/
        â”‚   â”œâ”€â”€ main.js       # Dropdowns, tooltips, confirmations, chart init
        â”‚   â”œâ”€â”€ skills.js     # Skills page interactivity
        â”‚   â”œâ”€â”€ projects.js   # Projects page interactivity
        â”‚   â””â”€â”€ search.js     # Client-side search
        â””â”€â”€ uploads/          # User profile pictures
```

---

## UI Design

**Color Palette**

| Role | Hex |
|---|---|
| Primary Blue | `#2563EB` |
| Accent Violet | `#7C3AED` |
| Background | `#F8FAFC` |
| Dark Text | `#0F172A` |

**Typography:** Poppins (headings) Â· Inter (body)

**Layout:** Top navigation bar with user dropdown â†’ full-width content area with responsive card grid.

---

## Setup & Running

### 1. Clone the repo

```bash
git clone https://github.com/Jeremiah-Jefry/SkillSync.git
cd SkillSync
```

### 2. Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///skillsync.db
```

`DATABASE_URL` is optional — SQLite is the default.

### 5. Run the app

```bash
python run.py
```

`run.py` calls `db.create_all()` on startup, so all tables are created automatically on first run.

Visit: **http://127.0.0.1:5000**

---

### Database Utilities

| Script | Purpose |
|---|---|
| `python run.py` | Start the dev server (auto-creates DB if missing) |
| `python recreate_db.py` | Drop all tables and recreate from scratch (dev reset) |
| `python update_db.py` | Apply incremental DB changes |

---

## Architecture

```
Request
  └── Flask App (create_app factory)
        ├── Blueprint: main        → landing page, public portfolio
        ├── Blueprint: auth        → register / login / logout
        ├── Blueprint: dashboard   → skill & project CRUD, profile, chart API
        └── Blueprint: portfolio   → printable portfolio view
              └── SQLAlchemy Models (User → Skills, User → Projects)
```

- Navigation bar auto-switches between a public nav and an authenticated nav via Jinja2 `current_user.is_authenticated` checks.
- Flash messages provide success/danger feedback on all form submissions.
- Skills (20/page) and projects (10/page) are both paginated server-side.
- The login `next` parameter is validated to allow only relative paths (open redirect protection).

---

## Security

- Passwords are hashed with Werkzeug's PBKDF2-SHA256.
- All forms are CSRF-protected by Flask-WTF.
- Profile picture uploads are sanitised with `secure_filename` and restricted to `.jpg`/`.jpeg`/`.png`.
- The print portfolio route enforces owner-only access (403 for other users).
- `SECRET_KEY` and `DATABASE_URL` are loaded from environment variables, never hardcoded.

---

## Roadmap

- [ ] AI-powered resume generator
- [ ] Skill recommendations based on project tech stacks
- [ ] GitHub API integration to auto-import repositories as projects
- [ ] RESTful API layer (`api.py` blueprint — scaffolded, not yet implemented)
- [ ] PWA / mobile-optimised experience
- [ ] Peer portfolio discovery and social features

---

## Author

**Jeremiah Jefry** — Creator & Developer

---

## License

MIT License — open source, free to use and adapt.
