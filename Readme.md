# ☕ Café Javas Website Clone

> A pixel-perfect clone of the [Café Javas Uganda](https://cafejavas.co.ug) restaurant website — rebuilt from scratch using plain HTML, CSS, and JavaScript.

---

## 🍽️ About This Project

This project is a **clone of the official Café Javas website** — one of Uganda's most popular restaurant chains, known for its great food, perfected drinks, and warm hospitality across Kampala and beyond.

The clone replicates the look, feel, and core functionality of the Café Javas website, including their menu categories (Big on Breakfast, Generous Big Meals, Perfected Drinks, and Decadent Desserts), their branch locations, table booking experience, and overall warm coffee-shop aesthetic.

It was built purely for **learning and portfolio purposes** — no frameworks, no libraries, just HTML, CSS, and vanilla JavaScript.

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
| 📱 Responsive | Fully mobile-friendly — works on phones, tablets, and desktops |

---

## 🗂️ File Structure

```
cafe-javas-clone/
├── index.html          # All page structure and content
├── index.js            # Menu data, cart logic, booking, and interactions
└── styles/
    └── index.css       # Full styling, layout, animations, and responsiveness
```

---

## 🚀 Running the Project

No setup or installation required. It runs entirely in the browser.

### Quickest way — open directly
Double-click `index.html` and it opens in your browser. Done.

### Recommended — Live Server (VS Code)
1. Install the **Live Server** extension in VS Code
2. Right-click `index.html`
3. Select **"Open with Live Server"**

### Alternative — Node.js
```bash
npx serve .
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

All interactivity lives in `index.js`. Here's what each function does:

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
- **Vanilla JavaScript** — All interactivity, no frameworks
- **Google Fonts** — Playfair Display, Lato, Dancing Script
- **Unsplash** — Food photography

---

## ⚠️ Disclaimer

This is an **unofficial clone** built strictly for educational and portfolio purposes. It is not affiliated with, endorsed by, or connected to Café Javas Uganda in any way. All brand names, menu items, and location data are the property of Café Javas.

To visit the real Café Javas website, go to 👉 [cafejavas.co.ug](https://cafejavas.co.ug)