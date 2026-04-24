// JD7 JUSTICE ENGINE
// Loads cases from /justice/cases.json

export async function initJustice() {
  const grid = document.getElementById("cases-grid");
  if (!grid) return;

  try {
    const res = await fetch("/justice/cases.json");
    const data = await res.json();

    data.cases.forEach(c => {
      const card = document.createElement("div");
      card.className = "case-card";

      card.innerHTML = `
        <div class="case-tag">${c.tag}</div>
        <div class="case-title">${c.title}</div>
        <div class="case-desc">${c.desc}</div>
        <div class="case-note">${c.note}</div>
      `;

      grid.appendChild(card);
    });

  } catch (e) {
    grid.innerHTML = `<div style="opacity:0.7;">Не удалось загрузить кейсы. Позже можно добавить оффлайн‑версию.</div>`;
  }
}