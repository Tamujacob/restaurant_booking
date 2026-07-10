# ☕ Café Javas Website Clone

> A clone of the [Café Javas Uganda](https://cafejavas.co.ug) restaurant website — rebuilt from scratch using HTML, CSS, JavaScript, and Django as the backend.
>
> 🔗 **Live demo:** [https://cafe-javas-clone-restaurant.onrender.com](https://cafe-javas-clone-restaurant.onrender.com)

---

## 🍽️ About This Project

This project is a **clone of the official Café Javas website** — one of Uganda's most popular restaurant chains, known for its great food, perfected drinks, and warm hospitality across Kampala and beyond.

The clone replicates the look, feel, and core functionality of the Café Javas website, including their menu categories (Big on Breakfast, Generous Big Meals, Perfected Drinks, and Decadent Desserts), their branch locations, table booking experience, and overall warm coffee-shop aesthetic.

It is built for **learning and portfolio purposes** using vanilla HTML, CSS, and JavaScript on the frontend, with **Django** powering the backend, a **REST API** layer built with Django REST Framework, and an **admin dashboard** for managing bookings, orders, and feedback.

---

## ✨ What the Clone Includes

| Feature | Description |
|---|---|
| 🏠 Home Page | Hero banner with CTAs, animated entrance, and a stats bar |
| 🍳 Menu | 24 food and drink items across 4 categories with live filtering |
| 🛒 Order Food | Slide-out cart to add items, adjust quantities, and place an order |
| 📅 Book a Table | Reservation form with date, time, guests, location, and special requests |
| 💬 Feedback | Customer feedback form with rating and branch selection |
| 🏢 About Us | Brand story, values, and a photo layout matching Café Javas' identity |
| 📍 Locations | All 9 Uganda branches (Kampala + Entebbe) listed with opening hours |
| 🔐 Admin Login | Custom branded admin login page matching the Café Javas identity |
| 📊 Admin Dashboard | Protected dashboard showing bookings, orders, and feedback with stat cards |
| 🔌 REST API | Five API endpoints built with Django REST Framework |
| 📱 Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## 🔌 REST API Endpoints

Built with **Django REST Framework**. All endpoints are accessible at the base URL of the live demo.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/menu/` | Returns all available menu items |
| `GET` | `/api/locations/` | Returns all active branch locations |
| `POST` | `/api/bookings/` | Submit a new table booking |
| `POST` | `/api/orders/` | Submit a new food order |
| `POST` | `/api/feedback/` | Submit customer feedback |

The browsable API (DRF's built-in UI) is available at each endpoint in the browser.

---

## 📊 Admin Dashboard

A protected admin dashboard is available at `/dashboard/` — only accessible to staff/superuser accounts.

**Features:**
- Stat cards showing total bookings, orders, and feedback at a glance
- Click any card to reveal the full data table for that section
- Bookings table — name, email, location, date, time, guests, special requests, status badge
- Orders table — name, phone, delivery location, delivery time, total (UGX), status badge
- Feedback table — name, email, branch, star rating badge, message, date
- Sidebar navigation with live counts on each section
- Quick action cards for common tasks
- Status badges colour-coded by state (pending, confirmed, delivered, cancelled, etc.)

Access requires a Django superuser account. Create one with:
```bash
python manage.py createsuperuser
```

---

## 🗂️ Project Structure

```
restaurant_booking/
├── cafejavas/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                       # Main Django app
│   ├── templates/
│   │   ├── index.html          # Main website page
│   │   ├── login.html          # Custom admin login page
│   │   └── dashboard.html      # Admin dashboard
│   ├── static/                 # CSS, JS, images
│   ├── models.py               # TableBooking, Order, OrderItem, MenuItem, Location, CustomerFeedback
│   ├── views.py                # Template views + API views
│   ├── serializers.py          # DRF serializers for all models
│   ├── forms.py                # Django forms for template-based submissions
│   ├── urls.py                 # All URL patterns (template + API routes)
│   └── admin.py                # Django admin registration
├── manage.py
├── requirements.txt
├── build.sh                    # Render build script (collectstatic + migrate)
└── .gitignore
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Django 5 |
| REST API | Django REST Framework |
| Database | SQLite (development) |
| Static files | WhiteNoise |
| Deployment | Render (auto-deploy from GitHub) |
| Version control | Git + GitHub (main / dev branch workflow) |

---

## 🚀 Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/Tamujacob/restaurant_booking.git
cd restaurant_booking
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create a superuser (for dashboard access)**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` for the site and `http://127.0.0.1:8000/dashboard/` for the admin dashboard.

---

## 🌿 Branch Workflow

This project uses a two-branch Git workflow:

| Branch | Purpose |
|---|---|
| `main` | Stable branch — always reflects what's live on Render |
| `dev` | Working branch — all new features are built here |

**Workflow:**
```bash
# Always work on dev
git checkout dev

# Build and commit changes
git add .
git commit -m "Description of change"

# When ready to go live, merge to main
git checkout main
git merge dev
git push origin main
```

Render watches `main` and auto-deploys on every push — no manual deploy steps needed.

---

## 📦 Deployment (Render)

The project is deployed on [Render](https://render.com) as a Web Service.

**Build Command:**
```bash
./build.sh
```

**Start Command:**
```bash
gunicorn cafejavas.wsgi:application
```

**`build.sh` contents:**
```bash
#!/usr/bin/env bash
set -o errexit
python manage.py collectstatic --no-input
python manage.py migrate
```

Every push to `main` on GitHub triggers an automatic redeploy on Render.

---

---

## 📌 Status

> 🚧 **Under active development — approximately 50% complete.**
> Features like the full admin management panel, order status tracking, user authentication, and menu management are still being built.
