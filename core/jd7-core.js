// JD7 CORE — базовые функции

// Тоггл блоков (используется в SCHOOL)
function jd7Toggle(id) {
  const block = document.getElementById(id);
  if (!block) return;
  block.style.display = block.style.display === "block" ? "none" : "block";
}

// Простейший XP‑движок
function jd7SetXP(barId, textId, current, max) {
  const bar = document.getElementById(barId);
  const text = document.getElementById(textId);
  if (!bar || !text) return;

  const percent = Math.min(100, (current / max) * 100);
  bar.style.width = percent + '%';
  text.innerText = 'Current XP: ' + current + ' / ' + max;
}
// JD7 CORE — базовые функции для всех модулей

// Тоггл блоков (используется в SCHOOL)
function jd7Toggle(id) {
  const block = document.getElementById(id);
  if (!block) return;
  block.style.display = block.style.display === "block" ? "none" : "block";
}

// XP‑движок (универсальный)
function jd7SetXP(barId, textId, current, max) {
  const bar = document.getElementById(barId);
  const text = document.getElementById(textId);
  if (!bar || !text) return;

  const percent = Math.min(100, (current / max) * 100);
  bar.style.width = percent + '%';
  text.innerText = 'Current XP: ' + current + ' / ' + max;
}

// Навигация между модулями (будет расширяться)
function jd7Go(url) {
  window.location.href = url;
}
// Меню (бургер)
function jd7ToggleMenu() {
  const links = document.getElementById('jd7-links');
  if (links) {
    links.classList.toggle('open');
  }
}