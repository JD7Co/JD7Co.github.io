// === JD7 GLOBAL STATE ===
// Хранит XP, уровень, прогресс, настройки
// В будущем будет заменено на localStorage / cloud sync
let JD7State = {
  xp: 120,
  level: 1,
  nextLevelXP: 300
};

// Сохранение состояния
function jd7SaveState() {
  localStorage.setItem('JD7State', JSON.stringify(JD7State));
}

// Загрузка состояния
function jd7LoadState() {
  const saved = localStorage.getItem('JD7State');
  if (saved) {
    JD7State = JSON.parse(saved);
  }
}
jd7LoadState();

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
// JD7 XP SYSTEM — глобальное состояние
const JD7State = {
  xp: 120,
  level: 1,
  nextLevelXP: 300
};

// Формула получения XP
function jd7AddXP(amount) {
  JD7State.xp += amount;

  // Проверка уровня
  if (JD7State.xp >= JD7State.nextLevelXP) {
    JD7State.level++;
    JD7State.xp = JD7State.xp - JD7State.nextLevelXP;
    JD7State.nextLevelXP = Math.floor(JD7State.nextLevelXP * 1.5);
  }

  // Обновление UI если есть
  jd7UpdateXPUI();
}

// Обновление UI
function jd7UpdateXPUI() {
  const bar = document.getElementById('xp-bar');
  const text = document.getElementById('xp-text');
  const level = document.getElementById('xp-level');

  if (!bar || !text || !level) return;

  const percent = Math.min(100, (JD7State.xp / JD7State.nextLevelXP) * 100);

  bar.style.width = percent + '%';
  text.innerText = `XP: ${JD7State.xp} / ${JD7State.nextLevelXP}`;
  level.innerText = `Level ${JD7State.level}`;
}