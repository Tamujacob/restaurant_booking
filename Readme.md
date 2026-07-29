# Harvest & Hearth

> *From Harvest to Hearth — Every Meal, Made Warm.*

A full-stack restaurant management platform covering **cafe, lunch, and supper** — built with Django, featuring customer accounts, Google Sign-In, staff role management, a REST API, and an admin dashboard.

> 🔗 **Live demo:** [https://cafe-javas-clone-restaurant.onrender.com](https://cafe-javas-clone-restaurant.onrender.com)

---

## 🍽️ About This Project

**Harvest & Hearth** is a restaurant platform designed to feel warm and welcoming from morning coffee through to supper. It combines a polished customer-facing website — menu browsing, table booking, and food ordering — with a full backend system for staff to manage physical and online orders, customer accounts, and day-to-day operations.

The platform covers three meal periods — cafe, lunch, and supper — with real authentication, role-based staff access, a REST API layer, an admin dashboard, and a complete order pipeline from browsing to checkout.

Built for **learning and portfolio purposes**, combining vanilla HTML, CSS, and JavaScript on the frontend with **Django** powering the backend.

> 🚧 **Status:** Under active development — core booking, ordering, accounts, and dashboard features are live; order status tracking and menu management via the API are still being built.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏠 Home Page | Hero banner with CTAs, animated entrance, and a stats bar |
| 🍳 Menu | Food and drink items across categories (breakfast, mains, drinks, desserts) with live filtering |
| 🛒 Order Food | Slide-out cart to add items, adjust quantities, and place an order — online or in-person |
| 📅 Book a Table | Reservation form with date, time, guests, location, and special requests |
| 💬 Feedback | Customer feedback form with rating and branch selection |
| 🏢 About Us | Brand story, values, and a warm, coffee-house-inspired identity |
| 📍 Locations | Multiple branches listed with opening hours |
| 🔐 Account Login/Signup | Customer accounts required to book or order, with email verification |
| 🌐 Google Sign-In | One-click sign-in via Google (django-allauth), auto-linked to existing accounts by email |
| 👥 Staff Roles | Manager, Receptionist (Physical Orders), Receptionist (Online Orders) — each with role-gated tools |
| 🧾 Physical Order Desk | Walk-in order form for receptionists, tagging orders by source (physical vs. online) |
| 📊 Admin Dashboard | Protected dashboard with stat cards for bookings, orders, and feedback |
| 🔌 REST API | Five endpoints built with Django REST Framework |
| 📱 Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## 🔌 REST API Endpoints

Built with **Django REST Framework**. All endpoints are accessible at the base URL of the live demo, and each has a browsable API view in the browser.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/menu/` | Returns all available menu items |
| `GET` | `/api/locations/` | Returns all active branch locations |
| `POST` | `/api/bookings/` | Submit a new table booking |
| `POST` | `/api/orders/` | Submit a new food order |
| `POST` | `/api/feedback/` | Submit customer feedback |

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

Create a superuser to access it:
```bash
python manage.py createsuperuser
```

---

## 🔐 Authentication & Accounts

- Customers must sign up or log in to book a table or place an order (`next` param redirects them back to what they clicked after logging in)
- Manual `authenticate()`-based login flow in `customer_login.html` / `views.py`
- **Google Sign-In** via django-allauth — new Google logins auto-generate a username and link to an existing account by matching email (custom adapter in `core/adapters.py`), skipping allauth's manual signup form
- **Email verification** required for username/password signups — blocks unverified accounts at login, without locking out pre-existing users who have no verification record

---

## 👥 Staff & Roles

- `StaffProfile` model with three roles:
  - **Manager**
  - **Receptionist – Physical Orders**
  - **Receptionist – Online Orders**
- Superuser-only "Create Staff" page
- Physical/walk-in order form for receptionists — orders tagged `source='physical'` or `source='online'`
- Dashboard shows role-gated staff tools and order source/table info

---

## 🗂️ Project Structure

```
restaurant_booking/
├── cafejavas/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                       # Django app
│   ├── adapters.py             # Custom allauth adapter (Google sign-in auto-linking)
│   ├── templates/
│   │   ├── index.html          # Main website page
│   │   ├── customer_login.html # Customer login/signup page (with Google Sign-In)
│   │   ├── login.html          # Custom admin login page
│   │   └── dashboard.html      # Admin dashboard
│   ├── static/
│   │   ├── styles/
│   │   │   └── index.css       # All styling and responsive layout
│   │   └── scripts/
│   │       └── index.js        # Menu data, cart logic, and interactions
│   ├── views.py                # Template views + API views
│   ├── serializers.py          # DRF serializers for all models
│   ├── forms.py                # Django forms for template-based submissions
│   ├── urls.py                 # All URL patterns (template + API routes)
│   ├── models.py               # TableBooking, Order, OrderItem, MenuItem, Location, CustomerFeedback, StaffProfile
│   └── admin.py                # Django admin registration
├── manage.py                   # Django management commands
├── requirements.txt
├── build.sh                    # Render build script (collectstatic + migrate)
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Django 5 |
| REST API | Django REST Framework |
| Auth | django-allauth (Google Sign-In, email verification) |
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

Then visit:
```
http://127.0.0.1:8000/            → Main website
http://127.0.0.1:8000/login/      → Customer login / signup (incl. Google Sign-In)
http://127.0.0.1:8000/dashboard/  → Admin dashboard
http://127.0.0.1:8000/admin/      → Django admin
```

> **Note:** Email verification uses Django's console email backend in local development — verification links print to your terminal instead of sending real emails.

---

## 🎨 Design & Branding

Harvest & Hearth keeps a warm, coffee-house visual identity:

| Element | Value |
|---|---|
| Primary Accent | `#C97B3A` — Caramel |
| Dark Background | `#1A0A00` — Espresso |
| Light Background | `#F5EDD9` — Cream |
| Heading Font | Playfair Display |
| Body Font | Lato |
| Logo Font | Dancing Script |

---

## 🧠 JavaScript Overview (`index.js`)

| Function | Purpose |
|---|---|
| `renderMenu(filter)` | Reads menu data and builds the cards on the page |
| `switchTab(cat)` | Filters displayed items by category |
| `addToCart(id)` | Adds a dish to the cart |
| `removeFromCart(id)` | Reduces quantity or removes item from cart |
| `updateCartUI()` | Refreshes the cart sidebar with current items and total price |
| `checkout()` | Submits the order and shows a confirmation |
| `submitBooking()` | Validates and confirms a table reservation |
| `showToast(msg)` | Displays a brief notification pop-up |
| `showModal(...)` | Shows a full confirmation dialog |
| `toggleMenu()` | Opens or closes the mobile navigation menu |

---

## 🍴 Adding a New Menu Item

Menu items are stored as objects in the `menuData` array inside `index.js`:

```js
{
  id: 25,                  // Must be unique
  cat: 'mains',            // breakfast | mains | drinks | desserts
  name: 'Rolex',           // Display name
  desc: 'Ugandan street food — egg and veggies rolled in a chapati.',
  price: 15000,            // Price in UGX (number, no quotes)
  badge: 'Local Fave',     // Optional tag shown on the card
  emoji: '🌯',             // Shown in the cart
  img: 'https://...'       // Food image URL
}
```

The page will automatically render it — no HTML changes needed.

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

## ☁️ Deployment (Render)

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

Every push to `main` triggers an automatic redeploy on Render.

---

## 🔮 Roadmap

| Feature | Status |
|---|---|
| Customer accounts, login, and email verification | ✅ Done |
| Google Sign-In | ✅ Done |
| Staff roles & physical order desk | ✅ Done |
| REST API (menu, locations, bookings, orders, feedback) | ✅ Done |
| Admin dashboard | ✅ Done |
| Order status tracking | 🔜 In progress |
| Menu management via API | 🔜 In progress |
| Full customer profile page | 🔜 In progress |
| PostgreSQL for production | 🔜 Planned |

---

## ⚠️ Disclaimer

Harvest & Hearth is an independent project built strictly for educational and portfolio purposes. Menu items, branch names, and location data are placeholder content for demonstration purposes only.