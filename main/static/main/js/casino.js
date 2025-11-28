document.addEventListener("DOMContentLoaded", () => {
  /* ===== ФОН: ЛЕТЯЧІ ФІШКИ І КАРТИ ===== */
  const overlay = document.getElementById("casino-overlay");
  if (overlay) {
    const chipCount = 8;
    const cardCount = 6;

    for (let i = 0; i < chipCount; i++) {
      const chip = document.createElement("div");
      chip.className = "casino-chip";
      chip.style.left = Math.random() * 100 + "vw";
      chip.style.top = Math.random() * 80 + "vh";
      chip.style.animationDelay = (Math.random() * 5).toFixed(2) + "s";
      chip.style.animationDuration = (12 + Math.random() * 8).toFixed(2) + "s";
      overlay.appendChild(chip);
    }

    for (let i = 0; i < cardCount; i++) {
      const card = document.createElement("div");
      card.className = "casino-card-float";
      card.style.left = Math.random() * 100 + "vw";
      card.style.top = Math.random() * 80 + "vh";
      card.style.animationDelay = (Math.random() * 6).toFixed(2) + "s";
      card.style.animationDuration = (16 + Math.random() * 8).toFixed(2) + "s";
      overlay.appendChild(card);
    }
  }

  // стилі для фішок/карт
  const style = document.createElement("style");
  style.textContent = `
    .casino-chip {
      position: fixed;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      border: 4px solid #facc15;
      box-shadow: 0 0 18px rgba(0,0,0,0.9);
      background:
        radial-gradient(circle at 30% 30%, #fefce8, #facc15 50%, #b91c1c 80%);
      opacity: 0.6;
      pointer-events: none;
      z-index: -1;
      animation-name: chipFloat;
      animation-timing-function: ease-in-out;
      animation-iteration-count: infinite;
    }

    .casino-card-float {
      position: fixed;
      width: 70px;
      height: 100px;
      border-radius: 10px;
      background:
        linear-gradient(135deg, #0f172a 0, #020617 35%, #0f172a 70%, #020617 100%);
      border: 2px solid rgba(248, 250, 252, 0.8);
      box-shadow: 0 0 24px rgba(0,0,0,1);
      opacity: 0.55;
      transform-origin: center;
      pointer-events: none;
      z-index: -1;
      overflow: hidden;
      animation-name: cardFloat;
      animation-timing-function: ease-in-out;
      animation-iteration-count: infinite;
    }

    .casino-card-float::before {
      content: "A";
      position: absolute;
      top: 6px;
      left: 10px;
      font-size: 18px;
      color: #f97316;
      font-weight: 700;
    }

    .casino-card-float::after {
      content: "♠";
      position: absolute;
      bottom: 8px;
      right: 10px;
      font-size: 20px;
      color: #22c55e;
    }

    @keyframes chipFloat {
      0%   { transform: translate3d(0, 0, 0) scale(1); opacity: 0.0; }
      10%  { opacity: 0.6; }
      50%  { transform: translate3d(-20px, -30px, 0) scale(1.06); }
      100% { transform: translate3d(20px, -60px, 0) scale(0.9); opacity: 0; }
    }

    @keyframes cardFloat {
      0%   { transform: translate3d(0, 0, 0) rotate(-6deg); opacity: 0.0; }
      15%  { opacity: 0.55; }
      50%  { transform: translate3d(10px, -40px, 0) rotate(6deg); }
      100% { transform: translate3d(-10px, -80px, 0) rotate(-4deg); opacity: 0; }
    }
  `;
  document.head.appendChild(style);

  /* ===== ПЛАВНИЙ СКРОЛ + data-work ===== */
  const scrollButtons = document.querySelectorAll("[data-scroll]");
  scrollButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetSelector = btn.getAttribute("data-scroll");
      const target = document.querySelector(targetSelector);

      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }

      const workType = btn.getAttribute("data-work");
      if (workType) {
        const select = document.querySelector('select[name="work_type"]');
        if (select) {
          select.value = workType;
        }
      }
    });
  });

  // плавний скрол для посилань типу href="#..."
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const id = link.getAttribute("href");
      if (!id || id === "#") return;
      const block = document.querySelector(id);
      if (!block) return;
      e.preventDefault();
      block.scrollIntoView({ behavior: "smooth" });
    });
  });

  /* ===== ЕФЕКТ НА ФОРМІ ПРИ САБМІТІ (БЕЗ БЛОКУВАННЯ POST) ===== */
  const form = document.getElementById("orderForm");
  const panel = document.getElementById("order-card");

  if (form && panel) {
    form.addEventListener("submit", () => {
      panel.classList.remove("form-win");
      // перезапуск анімації
      void panel.offsetWidth;
      panel.classList.add("form-win");
      // без preventDefault -> Django отримує POST
    });
  }
});
