# ☕ Café Javas Website Clone

> A clone of the [Café Javas Uganda](https://cafejavas.co.ug) restaurant website — rebuilt from scratch using HTML, CSS, JavaScript, and Django as the backend.

---

## 🍽️ About This Project

This project is a **clone of the official Café Javas website** — one of Uganda's most popular restaurant chains, known for its great food, perfected drinks, and warm hospitality across Kampala and beyond.

The clone replicates the look, feel, and core functionality of the Café Javas website, including their menu categories (Big on Breakfast, Generous Big Meals, Perfected Drinks, and Decadent Desserts), their branch locations, table booking experience, and overall warm coffee-shop aesthetic.

It is built for **learning and portfolio purposes** using vanilla HTML, CSS, and JavaScript on the frontend, with **Django** powering the backend.

---

## ✨ What the Clone Includes

| Feature | Description |
|---|---|
| 🏠 Home Page | Hero banner with CTAs, animated entrance, and a stats bar |
| 🍳 Menu | 24 food and drink items across 4 categories with live filtering |
| 🛒 Order Food | Slide-out cart to add items, adjust quantities, and place an order |
| 📅 Book a Table | Reservation form with date, time, guests, location, and special requests |
| 🏢 About Us | Brand story, values, and a photo layout matching Café Javas' identity |
| 📍 Locations | All 9 Uganda branches (Kampala + Entebbe) listed with opening hours |
| 🔐 Admin Login | Custom branded admin login page matching the Café Javas identity |
| 📱 Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## 🗂️ File Structure

```
restaurant_booking/
├── cafejavas/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                       # Django app
│   ├── templates/
│   │   ├── index.html          # Main website page
│   │   └── login.html          # Custom admin login page
│   ├── static/
│   │   ├── styles/
│   │   │   └── index.css       # All styling and responsive layout
│   │   └── scripts/
│   │       └── index.js        # Menu data, cart logic, and interactions
│   ├── views.py                # Page views
│   ├── urls.py                 # App URL routes
│   ├── models.py               # Database models
│   └── admin.py
├── manage.py                   # Django management commands
├── README.md
└── .gitignore
```

---

## 🚀 Running the Project

### Requirements
- Python 3.x
- Django

### Install Django
```bash
pip install django
```

### Run the development server
```bash
py manage.py runserver
```

Then open your browser at:
```
http://127.0.0.1:8000/          → Main website
http://127.0.0.1:8000/login/    → Admin login page
http://127.0.0.1:8000/admin/    → Django admin dashboard
```

### Create an admin superuser
```bash
py manage.py createsuperuser
```

### Apply migrations
```bash
py manage.py migrate
```

---

## 🎨 Design & Branding

The clone closely mirrors Café Javas' warm, coffee-house visual identity:

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

All frontend interactivity lives in `index.js`:

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

## 🐍 Django Overview

| File | Purpose |
|---|---|
| `cafejavas/settings.py` | Project configuration — installed apps, static files, templates |
| `cafejavas/urls.py` | Root URL router — points to the `core` app |
| `core/views.py` | Renders the home page and admin login page |
| `core/urls.py` | Defines URL patterns for all pages |
| `core/models.py` | Database models (bookings, orders — to be built out) |

---

## 🍴 Adding a New Menu Item

All menu items are stored as objects in the `menuData` array inside `index.js`. To add a new dish, just add a new entry:

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

The page will automatically render it — no changes to HTML needed.

---

## 📍 Locations in the Clone

Matching the real Café Javas branches:

- Kira Road, Kampala
- Kampala Boulevard
- Oasis Mall, Kampala
- Nakawa, Kampala
- Namirembe, Kampala
- Lugogo, Kampala
- Bombo Road, Kampala
- Parliamentary Avenue, Kampala
- Victoria Mall, Entebbe

---

## 🛠️ Built With

- **HTML5** — Page structure
- **CSS3** — Styling, grid, flexbox, animations
- **Vanilla JavaScript** — All frontend interactivity, no frameworks
- **Django** — Python backend framework
- **SQLite** — Default Django database
- **Google Fonts** — Playfair Display, Lato, Dancing Script
- **Unsplash** — Food photography

---

## 🔮 Planned Backend Features

| Feature | Status |
|---|---|
| Save table bookings to database | 🔜 Coming soon |
| Store menu items in database | 🔜 Coming soon |
| Order tracking system | 🔜 Coming soon |
| User accounts and login | 🔜 Coming soon |
| Django admin dashboard | ✅ Available at `/admin/` |

---

## ⚠️ Disclaimer

This is an **unofficial clone** built strictly for educational and portfolio purposes. It is not affiliated with, endorsed by, or connected to Café Javas Uganda in any way. All brand names, menu items, and location data are the property of Café Javas.

To visit the real Café Javas website, go to 👉 [cafejavas.co.ug](https://cafejavas.co.ug)