# SkillSync - Portfolio & Skill Tracker

SkillSync is a **full-stack Flask web application** that lets developers, students, and professionals manage their skills, showcase projects, and share a live public portfolio -- all through a clean, modern dashboard.

---

## Overview

SkillSync gives you a personal dashboard to track every skill you've ever learned (rated 0-10), log every project you've built, and instantly share it all via a unique public portfolio URL (/portfolio/<your-username>). Update it once, and your shareable portfolio updates automatically.

---

## Features

| Area | What It Does |
|---|---|
| **Authentication** | Secure register / login / logout with hashed passwords (Werkzeug) and CSRF-protected forms |
| **Skill Tracking** | Add skills with name, primary category (12 built-in), subcategory, 0-10 proficiency level, description, and tags |
| **Project Management** | Log projects with title, description, tech stack, GitHub URL, live demo URL, image URL, and status |
| **Analytics Dashboard** | Stats cards (total skills, project count, avg skill level) + two Chart.js charts |
| **Profile Editor** | Edit name, bio, GitHub username, LinkedIn URL, personal portfolio URL, and profile picture |
| **Public Portfolio** | Shareable page at `/portfolio/<username>` showing profile, skills with progress bars, and projects |
| **Print / PDF Portfolio** | Browser-printable portfolio at `/portfolio/print/<username>` with print-optimised CSS |
| **Chart API** | `/dashboard/api/skills_data` returns JSON for dashboard chart rendering |

---

## Tech Stack

**Backend**
- Python 3, Flask 2.3.3
- Flask-SQLAlchemy 3.0.5 - ORM and database management
- Flask-Login 0.6.3 - session authentication
- Flask-WTF 1.1.1 / WTForms 3.0.1 - forms and CSRF protection
- Werkzeug 2.3.7 - WSGI utilities and password hashing
- WeasyPrint 60.1 - PDF/print portfolio rendering
- Pillow 10.1.0 - profile picture image handling
- python-dotenv 1.0.0 - environment variable loading

**Frontend**
- Tailwind CSS (CDN) - utility-first styling
- Chart.js (CDN) - skills analytics charts
- Font Awesome 6.4 - icons
- Google Fonts: Poppins (headings), Inter (body)
- Vanilla JavaScript - dropdowns, tooltips, confirmations, chart initialisation

**Database**
- SQLite by default (zero-config, file `skillsync.db`)
- Configurable via `DATABASE_URL` env var for any SQLAlchemy-supported DB

---

## Data Models

### User
| Field | Type | Notes |
|---|---|---|
| `username` | String(80) | Unique, indexed |
| `email` | String(120) | Unique, indexed |
| `password_hash` | String(128) | Werkzeug PBKDF2-SHA256 hash |
| `first_name` / `last_name` | String(50) | Required |
| `bio` | Text | Optional |
| `github_username` | String(100) | Links to GitHub profile on public page |
| `linkedin_url` | String(255) | Optional |
| `portfolio_url` | String(255) | Optional |
| `profile_picture` | String(255) | Stored under `static/uploads/` |
| `created_at` / `last_login` | DateTime | Auto-tracked |

### Skill
| Field | Type | Notes |
|---|---|---|
| `name` | String(100) | Required |
| `category` | String(50) | One of 12 preset categories |
| `subcategory` | String(50) | Optional free-text |
| `level` | Integer 0-10 | Proficiency score |
| `description` | Text | Optional |
| `tags` | String(200) | Comma-separated |

**Skill categories:** Programming Languages, Web Technologies, Frameworks & Libraries, Databases & Storage, Cloud Services, DevOps & Tools, Mobile Development, Design & Multimedia, AI & Machine Learning, Security & Authentication, Soft Skills, Other

### Project
| Field | Type | Notes |
|---|---|---|
| `title` | String(150) | Required |
| `description` | Text | Required |
| `tech_stack` | String(255) | Comma-separated technologies |
| `github_url` | String(255) | Optional |
| `demo_url` | String(255) | Optional |
| `image_url` | String(255) | Optional |
| `status` | String(20) | `completed`, `in-progress`, or `planned` |

---

## Route Map

| Method | URL | Description |
|---|---|---|
| GET | `/` | Landing page (redirects to dashboard if logged in) |
| GET/POST | `/auth/register` | New user registration |
| GET/POST | `/auth/login` | Login |
| GET | `/auth/logout` | Logout |
| GET | `/dashboard/` | Main dashboard with stats and charts |
| GET | `/dashboard/skills` | Paginated skills list |
| GET/POST | `/dashboard/add_skill` | Add a new skill |
| GET | `/dashboard/projects` | Paginated projects list |
| GET/POST | `/dashboard/add_project` | Add a new project |
| GET/POST | `/dashboard/profile` | Edit profile and upload picture |
| GET | `/dashboard/api/skills_data` | JSON data for charts |
| GET | `/portfolio/<username>` | Public shareable portfolio |
| GET | `/portfolio/print/<username>` | Printable portfolio (owner only) |

---

## Project Structure

`
SkillSync/
|-- run.py                  # App entry point, creates DB tables on first run
|-- config.py               # Config class (SECRET_KEY, DB URI, pagination)
|-- recreate_db.py          # Drop and recreate all tables (dev reset utility)
|-- update_db.py            # Incremental DB migration utility
|-- requirements.txt
|-- .env                    # You create this: SECRET_KEY, DATABASE_URL
|-- app/
    |-- __init__.py         # Application factory (create_app)
    |-- extensions.py       # db, login_manager, bootstrap instances
    |-- models.py           # User, Skill, Project SQLAlchemy models
    |-- forms.py            # WTForms: Login, Register, Profile, Skill, Project
    |-- routes/
    |   |-- auth.py         # /auth/* register, login, logout
    |   |-- dashboard.py    # /dashboard/* skills, projects, profile, chart API
    |   |-- main.py         # / and public portfolio view
    |   |-- portfolio.py    # /portfolio/print/<username> printable view
    |   |-- api.py          # Reserved for future REST API endpoints
    |-- templates/
    |   |-- base.html               # Base layout: Tailwind, Chart.js, FA icons
    |   |-- index.html              # Landing / marketing page
    |   |-- portfolio_public.html   # Public portfolio (skills + projects + links)
    |   |-- portfolio_print.html    # Print-optimised portfolio (@media print CSS)
    |   |-- portfolio_pdf.html      # PDF export variant
    |   |-- resume.html             # Resume view
    |   |-- auth/
    |   |   |-- login.html
    |   |   |-- register.html
    |   |-- dashboard/
    |       |-- dashboard.html      # Stats cards + Chart.js canvases
    |       |-- skills.html         # Paginated skill cards
    |       |-- add_skill.html      # Skill form
    |       |-- projects.html       # Paginated project cards
    |       |-- add_project.html    # Project form
    |       |-- profile.html        # Profile edit form
    |-- static/
        |-- css/main.css
        |-- js/
        |   |-- main.js       # Dropdowns, tooltips, confirmations, chart init
        |   |-- skills.js     # Skills page interactivity
        |   |-- projects.js   # Projects page interactivity
        |   |-- search.js     # Client-side search
        |-- uploads/          # User profile pictures
`

---

## UI Design

**Color palette**

| Role | Hex |
|---|---|
| Primary Blue | `#2563EB` |
| Accent Violet | `#7C3AED` |
| Background | `#F8FAFC` |
| Dark Text | `#0F172A` |

**Typography:** Poppins (headings), Inter (body)

**Layout:** Top navigation bar with user dropdown, full-width responsive card grid for content.

---

## Setup & Running

### 1. Clone the repo

`ash
git clone https://github.com/Jeremiah-Jefry/SkillSync.git
cd SkillSync
`

### 2. Create a virtual environment

`ash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
`

### 3. Install dependencies

`ash
pip install -r requirements.txt
`

### 4. Create a .env file

`
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///skillsync.db
`

`DATABASE_URL` is optional -- SQLite is the default.

### 5. Run the app

`ash
python run.py
`

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

`
Request
  Flask App (create_app factory)
    Blueprint: main       -- landing page, public portfolio
    Blueprint: auth       -- register / login / logout
    Blueprint: dashboard  -- skill & project CRUD, profile, chart API
    Blueprint: portfolio  -- printable portfolio view
      SQLAlchemy Models: User -> Skills, User -> Projects
`

- The navbar auto-switches between public and authenticated states via `current_user.is_authenticated`.
- Flash messages show success/danger feedback on all form submissions.
- Skills (20/page) and projects (10/page) are paginated server-side.
- The login `next` parameter is validated to only allow relative paths (open redirect protection).

---

## Security

- Passwords are hashed with Werkzeug PBKDF2-SHA256.
- All forms are CSRF-protected by Flask-WTF.
- Profile picture uploads use `secure_filename` and are restricted to `.jpg`/`.jpeg`/`.png`.
- The print portfolio route enforces owner-only access (403 for other users).
- `SECRET_KEY` and `DATABASE_URL` are loaded from environment variables, never hardcoded.

---

## Roadmap

- [ ] AI-powered resume generator
- [ ] Skill recommendations based on project tech stacks
- [ ] GitHub API integration to auto-import repositories as projects
- [ ] RESTful API layer (`api.py` blueprint is scaffolded, not yet implemented)
- [ ] PWA / mobile-optimised experience
- [ ] Peer portfolio discovery and social features

---

## Author

**Jeremiah Jefry** -- Creator & Developer

---

## License

MIT License -- open source, free to use and adapt.