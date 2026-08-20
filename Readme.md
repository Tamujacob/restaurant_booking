# Harvest & Hearth

> *From Harvest to Hearth — Every Meal, Made Warm.*

![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-ff1709?style=flat&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white)

A full-stack restaurant management platform covering **cafe, lunch, and supper** — built with Django, featuring customer accounts, Google Sign-In, staff role management, a REST API, and an admin dashboard.

**Live demo:** [https://harvest-and-hearth.onrender.com](https://harvest-and-hearth.onrender.com)

---

## About This Project

**Harvest & Hearth** is a restaurant platform designed to feel warm and welcoming from morning coffee through to supper. It combines a polished customer-facing website — menu browsing, table booking, and food ordering — with a full backend system for staff to manage physical and online orders, customer accounts, and day-to-day operations.

The platform covers three meal periods — cafe, lunch, and supper — with real authentication, role-based staff access, a REST API layer, an admin dashboard, and a complete order pipeline from browsing to checkout.

Built for **learning and portfolio purposes**, combining vanilla HTML, CSS, and JavaScript on the frontend with **Django** powering the backend.

**Status:** Under active development — core booking, ordering, accounts, and dashboard features are live; order status tracking and menu management via the API are still being built.

---

## Features

| Feature | Description |
|---|---|
| Home Page | Hero banner with CTAs, animated entrance, and a stats bar |
| Menu | Food and drink items across categories (breakfast, mains, drinks, desserts) with live filtering |
| Order Food | Slide-out cart to add items, adjust quantities, and place an order — online or in-person |
| Book a Table | Reservation form with date, time, guests, location, and special requests |
| Feedback | Customer feedback form with rating and branch selection |
| About Us | Brand story, values, and a warm, coffee-house-inspired identity |
| Locations | Multiple branches listed with opening hours |
| Account Login/Signup | Customer accounts required to book or order, with email verification |
| Google Sign-In | One-click sign-in via Google (django-allauth), auto-linked to existing accounts by email |
| Staff Roles | Manager, Receptionist (Physical Orders), Receptionist (Online Orders) — each with role-gated tools |
| Physical Order Desk | Walk-in order form for receptionists, tagging orders by source (physical vs. online) |
| Admin Dashboard | Protected dashboard with stat cards for bookings, orders, and feedback |
| REST API | Five endpoints built with Django REST Framework |
| Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## REST API Endpoints

Built with **Django REST Framework**. All endpoints are accessible at the base URL of the live demo, and each has a browsable API view in the browser.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/menu/` | Returns all available menu items |
| `GET` | `/api/locations/` | Returns all active branch locations |
| `POST` | `/api/bookings/` | Submit a new table booking |
| `POST` | `/api/orders/` | Submit a new food order |
| `POST` | `/api/feedback/` | Submit customer feedback |

---

## Admin Dashboard

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

Create a superuser to access it:
```bash
python manage.py createsuperuser
```

---

## Authentication & Accounts

- Customers must sign up or log in to book a table or place an order (`next` param redirects them back to what they clicked after logging in)
- Manual `authenticate()`-based login flow in `customer_login.html` / `views.py`
- **Google Sign-In** via django-allauth — new Google logins auto-generate a username and link to an existing account by matching email (custom adapter in `core/adapters.py`), skipping allauth's manual signup form
- **Email verification** required for username/password signups — blocks unverified accounts at login, without locking out pre-existing users who have no verification record
- **Password reset** flow via django-allauth — branded request, "check your email," set-new-password, and expired-link pages, sharing a common base template

---

## Staff & Roles

- `StaffProfile` model with three roles:
  - **Manager**
  - **Receptionist – Physical Orders**
  - **Receptionist – Online Orders**
- Superuser-only "Create Staff" page
- Physical/walk-in order form for receptionists — orders tagged `source='physical'` or `source='online'`
- Dashboard shows role-gated staff tools and order source/table info

---

## Project Structure

restaurant_booking/
├── cafejavas/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── core/ # Django app
│ ├── adapters.py # Custom allauth adapter (Google sign-in auto-linking)
│ ├── templates/
│ │ ├── index.html # Main website page
│ │ ├── customer_login.html # Customer login/signup page (with Google Sign-In)
│ │ ├── customer_signup.html # Customer account creation page
│ │ ├── staff_login.html # Staff/admin login page
│ │ ├── dashboard.html # Admin dashboard
│ │ ├── create_staff.html # Superuser-only staff creation page
│ │ ├── physical_order.html # Walk-in order desk for receptionists
│ │ └── account/
│ │ ├── auth_base.html # Shared base template for auth pages
│ │ ├── password_reset.html # Request reset link
│ │ ├── password_reset_done.html # "Check your email" confirmation
│ │ └── password_reset_from_key.html # Set new password / expired link
│ ├── static/
│ │ ├── styles/
│ │ │ └── index.css # All styling and responsive layout
│ │ └── scripts/
│ │ └── index.js # Menu data, cart logic, and interactions
│ ├── views.py # Template views + API views
│ ├── serializers.py # DRF serializers for all models
│ ├── forms.py # Django forms for template-based submissions
│ ├── urls.py # All URL patterns (template + API routes)
│ ├── models.py # TableBooking, Order, OrderItem, MenuItem, Location, CustomerFeedback, StaffProfile
│ └── admin.py # Django admin registration
├── manage.py # Django management commands
├── requirements.txt
├── build.sh # Render build script (collectstatic + migrate)
├── README.md
└── .gitignore

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Django 5 |
| REST API | Django REST Framework |
| Auth | django-allauth (Google Sign-In, email verification, password reset) |
| Database | SQLite (development) |
| Static files | WhiteNoise |
| Deployment | Render (auto-deploy from GitHub) |
| Version control | Git + GitHub (main / dev branch workflow) |


## Running Locally

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

Then visit:127.0.0.1/8080
