#  Harvest & Hearth

> *From Harvest to Hearth — Every Meal, Made Warm.*

A full-stack restaurant management platform covering **cafe, lunch, and supper** — built with Django, featuring customer accounts, Google Sign-In, staff role management, and a live order/booking system. Live demo: [cafe-javas-clone-restaurant.onrender.com](https://cafe-javas-clone-restaurant.onrender.com)

---

## 🍽️ About This Project

**Harvest & Hearth** is a restaurant platform designed to feel warm and welcoming from morning coffee through to supper. It combines a polished customer-facing website — menu browsing, table booking, and food ordering — with a full backend system for staff to manage physical and online orders, customer accounts, and day-to-day operations.

The platform covers three meal periods — cafe, lunch, and supper — with real authentication, role-based staff access, and a complete order pipeline from browsing to checkout.

Built for **learning and portfolio purposes**, combining vanilla HTML, CSS, and JavaScript on the frontend with **Django** powering the backend.

---

##  Features

| Feature | Description |
|---|---|
| 🏠 Home Page | Hero banner with CTAs, animated entrance, and a stats bar |
| 🍳 Menu | Food and drink items across categories (breakfast, mains, drinks, desserts) with live filtering |
| 🛒 Order Food | Slide-out cart to add items, adjust quantities, and place an order — online or in-person |
| 📅 Book a Table | Reservation form with date, time, guests, location, and special requests |
| 🏢 About Us | Brand story, values, and a warm, coffee-house-inspired identity |
| 📍 Locations | Multiple branches listed with opening hours |
| 🔐 Account Login/Signup | Customer accounts required to book or order, with email verification |
| 🌐 Google Sign-In | One-click sign-in via Google (django-allauth), auto-linked to existing accounts by email |
| 👥 Staff Roles | Manager, Receptionist (Physical Orders), Receptionist (Online Orders) — each with role-gated tools |
| 🧾 Physical Order Desk | Walk-in order form for receptionists, tagging orders by source (physical vs. online) |
| 📊 Dashboard | Staff dashboard with role-gated tools, order source, and table info |
| 🔌 REST API | Built with Django REST Framework |
| 📱 Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## 🗂 File Structure

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
│   │   └── login.html          # Custom admin login page
│   ├── static/
│   │   ├── styles/
│   │   │   └── index.css       # All styling and responsive layout
│   │   └── scripts/
│   │       └── index.js        # Menu data, cart logic, and interactions
│   ├── views.py                # Page views
│   ├── urls.py                 # App URL routes
│   ├── models.py               # Database models (StaffProfile, bookings, orders)
│   └── admin.py
├── manage.py                   # Django management commands
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Running the Project

### Requirements
- Python 3.x
- Django + django-allauth (see `requirements.txt`)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
py manage.py migrate
```

### Create an admin superuser
```bash
py manage.py createsuperuser
```

### Run the development server
```bash
py manage.py runserver
```

Then open your browser at:
```
http://127.0.0.1:8000/          → Main website
http://127.0.0.1:8000/login/    → Customer login / signup (incl. Google Sign-In)
http://127.0.0.1:8000/admin/    → Django admin dashboard
```

> **Note:** Email verification uses Django's console email backend in local development — verification links print to your terminal instead of sending real emails.

---

##  Design & Branding

Harvest & Hearth keeps the warm, coffee-house visual identity it started with:

| Element | Value |
|---|---|
| Primary Accent | `#C97B3A` — Caramel |
| Dark Background | `#1A0A00` — Espresso |
| Light Background | `#F5EDD9` — Cream |
| Heading Font | Playfair Display |
| Body Font | Lato |
| Logo Font | Dancing Script |

---

## 🔐 Authentication & Accounts

- Customers must sign up or log in to book a table or place an order (`next` param redirects them back to what they clicked after logging in)
- Manual `authenticate()`-based login flow in `customer_login.html` / `views.py`
- **Google Sign-In** via django-allauth — new Google logins auto-generate a username and link to an existing account by matching email (custom adapter in `core/adapters.py`), skipping allauth's manual signup form
- **Email verification** required for username/password signups — blocks unverified accounts at login, without locking out pre-existing users who have no verification record

---

##  Staff & Roles

- `StaffProfile` model with three roles:
  - **Manager**
  - **Receptionist – Physical Orders**
  - **Receptionist – Online Orders**
- Superuser-only "Create Staff" page
- Physical/walk-in order form for receptionists — orders tagged `source='physical'` or `source='online'`
- Dashboard shows role-gated staff tools and order source/table info

---

##  JavaScript Overview (`index.js`)

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

## 🛠️ Built With

- **HTML5 / CSS3 / Vanilla JavaScript** — Frontend, no frameworks
- **Django** — Python backend framework
- **Django REST Framework** — REST API
- **django-allauth** — Google Sign-In and account/email verification
- **SQLite** — Database (demo)
- **Google Fonts** — Playfair Display, Lato, Dancing Script

---

##  Roadmap

| Feature | Status |
|---|---|
| Customer accounts, login, and email verification | ✅ Done |
| Google Sign-In | ✅ Done |
| Staff roles & physical order desk | ✅ Done |
| Django admin dashboard | ✅ Available at `/admin/` |
| Order status tracking | 🔜 In progress |
| Menu management via API | 🔜 In progress |
| Full customer profile page | 🔜 In progress |
| PostgreSQL for production | 🔜 Planned |

---

