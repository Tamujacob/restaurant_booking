// ─── MENU DATA ────────────────────────────────────
const menuData = [
  // BREAKFAST
  { id:1, cat:'breakfast', name:'Strawberry Pancakes', desc:'Fluffy pancakes topped with fresh strawberry compote and whipped cream.', price:28000, badge:'Popular', emoji:'🥞',
    img:'https://images.unsplash.com/photo-1565299543923-37dd37887442?w=400&q=80' },
  { id:2, cat:'breakfast', name:'Breakfast Burger', desc:'Loaded breakfast patty burger with egg, cheese, and grilled tomato.', price:32000, badge:'New', emoji:'🍔',
    img:'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&q=80' },
  { id:3, cat:'breakfast', name:'Full English Breakfast', desc:'Eggs, bacon, sausage, beans, toast, and fresh grilled tomatoes.', price:35000, badge:'', emoji:'🍳',
    img:'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?w=400&q=80' },
  { id:4, cat:'breakfast', name:'Avocado Toast', desc:'Sourdough toast with smashed avocado, poached egg, and chili flakes.', price:24000, badge:'Healthy', emoji:'🥑',
    img:'https://images.unsplash.com/photo-1541519227354-08fa5d50c820?w=400&q=80' },
  { id:5, cat:'breakfast', name:'Chicken Waffles', desc:'Crispy chicken on golden Belgian waffles drizzled with maple syrup.', price:36000, badge:'Fan Fave', emoji:'🧇',
    img:'https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=400&q=80' },
  { id:6, cat:'breakfast', name:'Omelette & Wedges', desc:'Three-egg cheese omelette served with seasoned potato wedges.', price:26000, badge:'', emoji:'🍳',
    img:'https://images.unsplash.com/photo-1510693206972-df098062cb71?w=400&q=80' },

  // MAINS
  { id:7, cat:'mains', name:'Buffalo Chicken Wrap', desc:'Crispy buffalo chicken, lettuce, tomato, and ranch in a toasted wrap.', price:30000, badge:'Spicy', emoji:'🌯',
    img:'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&q=80' },
  { id:8, cat:'mains', name:'Pasta Carbonara', desc:'Classic Italian pasta with creamy egg sauce, pancetta, and parmesan.', price:29000, badge:'', emoji:'🍝',
    img:'https://images.unsplash.com/photo-1612874742237-6526221588e3?w=400&q=80' },
  { id:9, cat:'mains', name:'Grilled Salmon', desc:'Atlantic salmon fillet with steamed vegetables and lemon butter sauce.', price:48000, badge:'Premium', emoji:'🐟',
    img:'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=400&q=80' },
  { id:10, cat:'mains', name:'Club Sandwich', desc:'Triple-decker with turkey, bacon, lettuce, tomato, and mayo on toasted bread.', price:27000, badge:'', emoji:'🥪',
    img:'https://images.unsplash.com/photo-1567234669003-dce7a7a88821?w=400&q=80' },
  { id:11, cat:'mains', name:'Caesar Salad', desc:'Crisp romaine, croutons, parmesan, and house Caesar dressing.', price:22000, badge:'Light', emoji:'🥗',
    img:'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&q=80' },
  { id:12, cat:'mains', name:'BBQ Beef Ribs', desc:'Slow-cooked ribs glazed with smoky BBQ sauce, served with fries.', price:55000, badge:'Premium', emoji:'🍖',
    img:'https://images.unsplash.com/photo-1544025162-d76694265947?w=400&q=80' },

  // DRINKS
  { id:13, cat:'drinks', name:'Flat White', desc:'Smooth espresso with steamed micro-foam milk — our barista specialty.', price:12000, badge:'Bestseller', emoji:'☕',
    img:'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80' },
  { id:14, cat:'drinks', name:'Peanut Butter Milkshake', desc:'Our legendary creamy milkshake with real peanut butter and chocolate.', price:16000, badge:'Must Try', emoji:'🥛',
    img:'https://images.unsplash.com/photo-1568158879083-c42860933ed7?w=400&q=80' },
  { id:15, cat:'drinks', name:'Mango Smoothie', desc:'Fresh mango blended with yoghurt, honey, and a squeeze of lime.', price:14000, badge:'Fresh', emoji:'🥭',
    img:'https://images.unsplash.com/photo-1553530979-fbb9e4aee36f?w=400&q=80' },
  { id:16, cat:'drinks', name:'Iced Latte', desc:'Double espresso over ice with your choice of milk.', price:13000, badge:'', emoji:'🧊',
    img:'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=400&q=80' },
  { id:17, cat:'drinks', name:'Fresh Passion Juice', desc:'Tropical passion fruit juice, freshly squeezed and chilled.', price:10000, badge:'Local Fave', emoji:'🍹',
    img:'https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400&q=80' },
  { id:18, cat:'drinks', name:'Hot Chocolate', desc:'Rich Belgian dark chocolate with steamed milk and marshmallows.', price:13000, badge:'', emoji:'🍫',
    img:'https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?w=400&q=80' },

  // DESSERTS
  { id:19, cat:'desserts', name:'Chocolate Lava Cake', desc:'Warm chocolate cake with a molten centre, served with vanilla ice cream.', price:20000, badge:'Indulgent', emoji:'🍫',
    img:'https://images.unsplash.com/photo-1574085733277-851d9d856a3a?w=400&q=80' },
  { id:20, cat:'desserts', name:'New York Cheesecake', desc:'Classic baked cheesecake with a buttery biscuit base and berry coulis.', price:18000, badge:'Bestseller', emoji:'🍰',
    img:'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&q=80' },
  { id:21, cat:'desserts', name:'Crêpe Suzette', desc:'Thin crêpes with orange butter caramel sauce, served warm.', price:16000, badge:'', emoji:'🍮',
    img:'https://images.unsplash.com/photo-1519676867240-f03562e64548?w=400&q=80' },
  { id:22, cat:'desserts', name:'Ice Cream Sundae', desc:'Three scoops of gelato, hot fudge, caramel, whipped cream & a cherry.', price:15000, badge:'Fun', emoji:'🍨',
    img:'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&q=80' },
  { id:23, cat:'desserts', name:'Tiramisu', desc:'Classic Italian dessert with mascarpone, espresso, and cocoa dust.', price:19000, badge:'Italian', emoji:'🍮',
    img:'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400&q=80' },
  { id:24, cat:'desserts', name:'Fruit Salad', desc:'Seasonal fresh fruits with a drizzle of honey and mint leaves.', price:12000, badge:'Healthy', emoji:'🍓',
    img:'https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&q=80' },
];

// ─── CART STATE ───────────────────────────────────
const cart = {};

// ─── RENDER MENU ──────────────────────────────────
function renderMenu(filter = 'all') {
  const grid = document.getElementById('menuGrid');
  grid.innerHTML = '';
  menuData.forEach(item => {
    const div = document.createElement('div');
    div.className = 'menu-item' + (filter === 'all' || item.cat === filter ? ' visible' : '');
    div.innerHTML = `
      <div class="item-img">
        <img src="${item.img}" alt="${item.name}" loading="lazy" onerror="this.style.display='none'" />
        ${item.badge ? `<span class="item-badge">${item.badge}</span>` : ''}
      </div>
      <div class="item-body">
        <div class="item-name">${item.name}</div>
        <div class="item-desc">${item.desc}</div>
        <div class="item-footer">
          <div class="item-price">UGX ${item.price.toLocaleString()}</div>
          <button class="add-btn" onclick="addToCart(${item.id})" title="Add to order">+</button>
        </div>
      </div>
    `;
    grid.appendChild(div);
  });
}

// ─── TAB SWITCHING ────────────────────────────────
function switchTab(cat) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  const tabs = ['all', 'breakfast', 'mains', 'drinks', 'desserts'];
  const idx = tabs.indexOf(cat);
  if (idx >= 0) document.querySelectorAll('.tab-btn')[idx]?.classList.add('active');
  renderMenu(cat);
  if (cat !== 'all') {
    setTimeout(() => document.getElementById('menu').scrollIntoView({ behavior: 'smooth' }), 10);
  }
}

// ─── CART FUNCTIONS ───────────────────────────────
function addToCart(id) {
  const item = menuData.find(i => i.id === id);
  if (!item) return;
  cart[id] = cart[id] ? { ...cart[id], qty: cart[id].qty + 1 } : { ...item, qty: 1 };
  updateCartUI();
  showToast(`${item.emoji} ${item.name} added!`);
}

function removeFromCart(id) {
  if (!cart[id]) return;
  if (cart[id].qty > 1) cart[id].qty--;
  else delete cart[id];
  updateCartUI();
}

function updateCartUI() {
  const items = Object.values(cart);
  const total = items.reduce((s, i) => s + i.price * i.qty, 0);
  const count = items.reduce((s, i) => s + i.qty, 0);

  document.getElementById('cartCount').textContent = count;

  const cartItemsEl = document.getElementById('cartItems');
  const cartFooter = document.getElementById('cartFooter');

  if (items.length === 0) {
    cartItemsEl.innerHTML = `
      <div class="cart-empty">
        <div class="cart-empty-icon">🛒</div>
        <div>Your order is empty</div>
        <small>Add items from the menu</small>
      </div>`;
    cartFooter.style.display = 'none';
  } else {
    cartFooter.style.display = 'block';
    document.getElementById('cartTotal').textContent = `UGX ${total.toLocaleString()}`;
    cartItemsEl.innerHTML = items.map(item => `
      <div class="cart-item">
        <div class="ci-emoji">${item.emoji}</div>
        <div class="ci-info">
          <div class="ci-name">${item.name}</div>
          <div class="ci-price">UGX ${(item.price * item.qty).toLocaleString()}</div>
          <div class="ci-qty">
            <button class="qty-btn" onclick="removeFromCart(${item.id})">−</button>
            <span class="qty-val">${item.qty}</span>
            <button class="qty-btn" onclick="addToCart(${item.id})">+</button>
          </div>
        </div>
      </div>
    `).join('');
  }
}

function openCart() {
  document.getElementById('cartSidebar').classList.add('open');
  document.getElementById('cartOverlay').classList.add('open');
}

function closeCart() {
  document.getElementById('cartSidebar').classList.remove('open');
  document.getElementById('cartOverlay').classList.remove('open');
}

function checkout() {
  const items = Object.values(cart);
  if (items.length === 0) return;
  Object.keys(cart).forEach(k => delete cart[k]);
  updateCartUI();
  closeCart();
  showModal('🎉', 'Order Placed!', 'Thank you! Your order has been received. Our kitchen is already working on it. Estimated delivery: 30–45 minutes.');
}

// ─── BOOKING ──────────────────────────────────────
function submitBooking() {
  const first = document.getElementById('bookFirst').value.trim();
  const last = document.getElementById('bookLast').value.trim();
  const email = document.getElementById('bookEmail').value.trim();
  const date = document.getElementById('bookDate').value;
  const time = document.getElementById('bookTime').value;
  const location = document.getElementById('bookLocation').value;

  if (!first || !last || !email || !date || !time) {
    showToast('⚠️ Please fill all required fields');
    return;
  }

  const d = new Date(date);
  const dateStr = d.toLocaleDateString('en-UG', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
  showModal('📅', 'Table Reserved!', `Thank you, ${first}! Your table at Café Javas ${location} is reserved for ${dateStr} at ${time}. A confirmation will be sent to ${email}.`);
  ['bookFirst', 'bookLast', 'bookEmail', 'bookPhone', 'bookDate', 'bookTime', 'bookNote'].forEach(id => {
    document.getElementById(id).value = '';
  });
}

// ─── TOAST ────────────────────────────────────────
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ─── MODAL ────────────────────────────────────────
function showModal(icon, title, msg) {
  document.getElementById('modalIcon').textContent = icon;
  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalMsg').textContent = msg;
  document.getElementById('modalOverlay').classList.add('open');
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
}

// ─── NAV HAMBURGER ────────────────────────────────
function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('mobile-open');
}

// ─── INIT ─────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  renderMenu('all');
  updateCartUI();

  // Set min date for booking to today
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('bookDate').setAttribute('min', today);
});