//  CART STATE 
const cart = {};


//  TAB SWITCHING 
function switchTab(cat) {
  // update active tab button
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  const tabs = ['all', 'breakfast', 'mains', 'drinks', 'desserts'];
  const idx = tabs.indexOf(cat);
  if (idx >= 0) document.querySelectorAll('.tab-btn')[idx]?.classList.add('active');

  // show or hide cards based on their data-cat attribute
  document.querySelectorAll('.menu-item').forEach(card => {
    if (cat === 'all' || card.dataset.cat === cat) {
      card.classList.add('visible');
    } else {
      card.classList.remove('visible');
    }
  });
}

//  CART FUNCTIONS 
function addToCart(id, name, price, emoji) {
  cart[id] = cart[id]
    ? { ...cart[id], qty: cart[id].qty + 1 }
    : { id, name, price, emoji, qty: 1 };
  updateCartUI();
  showToast(`${emoji} ${name} added!`);
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
            <button class="qty-btn" onclick="addToCart(${item.id}, '${item.name}', ${item.price}, '${item.emoji}')">+</button>
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


//  TOAST 
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

//  MODAL 
function showModal(icon, title, msg) {
  document.getElementById('modalIcon').textContent = icon;
  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalMsg').textContent = msg;
  document.getElementById('modalOverlay').classList.add('open');
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
}

//  NAV HAMBURGER 
function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('mobile-open');
}

// INIT 
document.addEventListener('DOMContentLoaded', () => {
  updateCartUI();

  // Set min date for booking to today
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('bookDate').setAttribute('min', today);
});