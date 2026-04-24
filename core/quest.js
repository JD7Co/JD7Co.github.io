// JD7 QUESTRUN ENGINE
// XP · LEVELS · MISSIONS · DYNAMIC DIFFICULTY

export function initQuest() {

  const XP_KEY = "jd7_xp";
  const LVL_KEY = "jd7_lvl";

  let xp = parseInt(localStorage.getItem(XP_KEY) || "0");
  let lvl = parseInt(localStorage.getItem(LVL_KEY) || "1");

  const xpFill = document.getElementById("xp-fill");
  const xpText = document.getElementById("xp-text");
  const lvlDisplay = document.getElementById("level-display");
  const missionContainer = document.getElementById("mission-container");

  // XP required grows progressively
  function xpRequired(level) {
    return Math.floor(100 * Math.pow(1.25, level - 1));
  }

  function save() {
    localStorage.setItem(XP_KEY, xp);
    localStorage.setItem(LVL_KEY, lvl);
  }

  function updateUI() {
    const req = xpRequired(lvl);
    const percent = Math.min(100, (xp / req) * 100);

    xpFill.style.width = percent + "%";
    xpText.textContent = `${xp} / ${req} XP`;
    lvlDisplay.textContent = `L${lvl}`;
  }

  function addXP(amount) {
    xp += amount;

    const req = xpRequired(lvl);
    if (xp >= req) {
      xp -= req;
      lvl++;
    }

    save();
    updateUI();
  }

  // Mission definitions
  const missions = [
    {
      category: "Daily",
      difficulty: "Easy",
      xp: 20,
      text: "Открыть JD7 WORLD"
    },
    {
      category: "Daily",
      difficulty: "Medium",
      xp: 35,
      text: "Сменить тему через кристалл"
    },
    {
      category: "Weekly",
      difficulty: "Hard",
      xp: 80,
      text: "Посетить SCHOOL и прочитать 1 уровень"
    },
    {
      category: "Core",
      difficulty: "Elite",
      xp: 150,
      text: "Настроить панель доступности"
    },
    {
      category: "Hidden",
      difficulty: "Hidden",
      xp: 200,
      text: "Найти скрытый ритуал JD7"
    }
  ];

  function renderMissions() {
    missionContainer.innerHTML = "";

    const categories = ["Daily", "Weekly", "Core", "Special", "Hidden"];

    categories.forEach(cat => {
      const section = document.createElement("div");
      section.className = "mission-section";

      const title = document.createElement("div");
      title.className = "mission-title";
      title.textContent = cat;
      section.appendChild(title);

      const list = document.createElement("div");
      list.className = "mission-list";

      missions
        .filter(m => m.category === cat)
        .forEach(m => {
          const card = document.createElement("div");
          card.className = "mission-card";

          card.innerHTML = `
            <div class="mission-text">${m.text}</div>
            <div class="mission-diff">${m.difficulty}</div>
            <button class="mission-btn">Выполнить (+${m.xp} XP)</button>
          `;

          card.querySelector(".mission-btn").addEventListener("click", () => {
            addXP(m.xp);
            card.classList.add("done");
            setTimeout(() => card.remove(), 600);
          });

          list.appendChild(card);
        });

      section.appendChild(list);
      missionContainer.appendChild(section);
    });
  }

  updateUI();
  renderMissions();
}