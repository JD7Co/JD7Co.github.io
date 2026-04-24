// JD7 BOTS ENGINE
// Loads bots from /bots/bots.json

export async function initBots() {
  const grid = document.getElementById("bots-grid");

  try {
    const res = await fetch("/bots/bots.json");
    const data = await res.json();

    data.bots.forEach(bot => {
      const card = document.createElement("div");
      card.className = "bot-card";

      card.innerHTML = `
        <div class="bot-img" style="background-image:url('${bot.avatar}')"></div>
        <div class="bot-name">${bot.name}</div>
        <div class="bot-role">${bot.role}</div>

        <div class="bot-status ${bot.status}">
          ${bot.status.toUpperCase()}
        </div>

        <div class="bot-energy">
          <div class="bot-energy-fill" style="width:${bot.energy}%"></div>
        </div>

        <button class="bot-btn">Открыть</button>
      `;

      grid.appendChild(card);
    });

  } catch (e) {
    grid.innerHTML = `<div style="opacity:0.6;">Ошибка загрузки ботов</div>`;
  }
}