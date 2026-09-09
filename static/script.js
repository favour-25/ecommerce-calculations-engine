const nairaFmt = (n) =>
  "₦" + Number(n).toLocaleString("en-NG", { minimumFractionDigits: 2 });

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2000);
}

async function loadProducts() {
  const res = await fetch("/api/products");
  const products = await res.json();
  const list = document.getElementById("product-list");
  list.innerHTML = "";

  products.forEach((p) => {
    const card = document.createElement("div");
    card.className = "product-card";
    card.innerHTML = `
      <h3>${p.name}</h3>
      <div class="price">${nairaFmt(p.price)}</div>
      <div class="stock">${p.quantity_in_stock} in stock</div>
      <button ${p.quantity_in_stock === 0 ? "disabled" : ""}>
        ${p.quantity_in_stock === 0 ? "Out of stock" : "Add to cart"}
      </button>
    `;
    card.querySelector("button").addEventListener("click", () => addToCart(p.id));
    list.appendChild(card);
  });
}

async function addToCart(productId) {
  const res = await fetch("/api/cart/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ product_id: productId, quantity: 1 }),
  });
  const data = await res.json();

  if (!res.ok) {
    showToast(data.error || "Could not add item.");
    return;
  }

  showToast("Added to cart");
  renderCart(data);
  loadProducts(); // refresh stock counts
}

async function loadCart() {
  const res = await fetch("/api/cart");
  const data = await res.json();
  renderCart(data);
}

function renderCart(data) {
  const itemsEl = document.getElementById("cart-items");
  const summaryEl = document.getElementById("cart-summary");

  itemsEl.innerHTML = data.items.length
    ? data.items
        .map(
          (i) => `
        <div class="cart-line">
          <span>${i.name} × ${i.quantity}</span>
          <span>${nairaFmt(i.line_total)}</span>
        </div>`
        )
        .join("")
    : "<p style='color:#6b7280;font-size:0.9rem;'>Cart is empty.</p>";

  summaryEl.innerHTML = `
    <div><span>Subtotal</span><span>${nairaFmt(data.subtotal)}</span></div>
    <div><span>Discount</span><span>-${nairaFmt(data.discount)}</span></div>
    <div><span>Tax (7.5%)</span><span>${nairaFmt(data.tax)}</span></div>
    <div class="total"><span>Total</span><span>${nairaFmt(data.total)}</span></div>
  `;
}

document.getElementById("reset-cart").addEventListener("click", async () => {
  await fetch("/api/cart/reset", { method: "POST" });
  showToast("Cart cleared");
  loadCart();
  loadProducts();
});

loadProducts();
loadCart();