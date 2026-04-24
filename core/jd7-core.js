// === JD7 GLOBAL STATE ===
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
  if (saved) JD7State = JSON.parse(saved);
}
jd7LoadState();

// === XP SYSTEM ===
function jd7AddXP(amount) {
  JD7State.xp += amount;

  if (JD7State.xp >= JD7State.nextLevelXP) {
    JD7State.level++;
    JD7State.xp -= JD7State.nextLevelXP;
    JD7State.nextLevelXP = Math.floor(JD7State.nextLevelXP * 1.5);
  }

  jd7SaveState();
  jd7UpdateXPUI();
}

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

// === MENU ===
function jd7ToggleMenu() {
  const links = document.getElementById('jd7-links');
  if (links) links.classList.toggle('open');
}

// === TOGGLE BLOCKS ===
function toggleTasks(id) {
  const block = document.getElementById(id);
  if (!block) return;
  block.style.display = block.style.display === "block" ? "none" : "block";
}