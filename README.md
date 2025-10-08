# SkillSync — AI-Powered Portfolio & Skill Tracker

SkillSync is a **full-stack Flask web application** designed to empower students, developers, and professionals to showcase their skills, manage projects, track learning goals, and build a dynamic auto-updating portfolio — all in one place.

---

## 🚀 Overview

**SkillSync** bridges the gap between learning and showcasing. It automatically syncs your skills, projects, and progress, creating a living digital profile that evolves as you grow.

**Core Idea:** Your portfolio should grow *with* you — not be a static resume.

---

## ✨ Features

| Category                             | Description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| 🔐 **Authentication**                | Secure registration & login using Flask-Login                |
| 🧠 **Skill Management**              | Add, edit, and visualize skills (0–10 level system)          |
| 💼 **Project Showcase**              | Display your real projects with GitHub integration           |
| 📊 **Analytics Dashboard**           | Track learning progress, streaks & growth charts             |
| 🌐 **Dynamic Portfolio**             | Auto-generated public portfolio with a unique shareable link |
| 🤖 **AI Resume Generator (Planned)** | Generate resumes dynamically using templates or APIs         |

---

## 🧱 Folder Structure

```
SkillSync/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── extensions.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── dashboard.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── portfolio_public.html
│   └── static/
│       ├── css/
│       │   └── main.css
│       ├── js/
│       │   └── main.js
│       └── images/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

**Backend:** Flask, SQLAlchemy, Flask-WTF, Flask-Login
**Frontend:** HTML, CSS (Tailwind/Custom), JavaScript (Chart.js, Axios)
**Database:** SQLite (dev), MySQL/PostgreSQL (prod)
**APIs:** YouTube Data API, GitHub API, OpenAI API (planned)

---

## 🎨 UI / UX Design

**Theme:** Modern | Clean | Professional Dashboard

**Color Palette:**

* Primary Blue → `#2563EB`
* Accent Violet → `#7C3AED`
* Background → `#F8FAFC`
* Dark Text → `#0F172A`

**Typography:**

* Headings → *Poppins*
* Body → *Inter*

**Layout Overview:**

* **Dashboard:** Sidebar navigation + main content area (skills, projects, analytics)
* **Portfolio Page:** Minimal public view with skills, projects, and contact links.

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/SkillSync.git
cd SkillSync
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run App

```bash
python run.py
```

Then open: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧠 Architecture Overview

**Frontend Layer:** Flask templates (Jinja2) + dynamic JS for charts and API rendering.
**Backend Layer:** Modular Flask Blueprints + ORM models + secure session management.
**Database:** SQLAlchemy ORM with User, Skill, and Project tables.

---



## 💡 Future Enhancements

* 🤖 AI Resume Generator (OpenAI API)
* 📈 Skill Insights with ML-based recommendations
* 🧑‍🤝‍🧑 Learning Circles & Peer Collaboration
* 📱 PWA for mobile tracking
* 🧩 Chrome Extension for quick updates

---

## 🧑‍💻 Contributor

* **Jeremiah Jefry** — Creator, Developer & Visionary behind SkillSync

---

## 📜 License

This project is open-sourced under the **MIT License**.

---

> *“SkillSync isn’t just a tracker — it’s your evolving digital twin of growth.”*
