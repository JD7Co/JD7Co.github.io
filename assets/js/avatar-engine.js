// JD7 Avatar Engine v3.2
const JD7AvatarEngine = {
    avatar: null,

    init() {
        console.log("JD7 Avatar Engine v3.2 запущен");

        // Выбираем случайный аватар
        this.avatar = JD7_AVATARS[Math.floor(Math.random() * JD7_AVATARS.length)];

        // Рендерим
        this.renderAvatar();
        this.renderGreeting();
    },

    renderAvatar() {
        const container = document.getElementById("jd7-avatar");
        if (!container) return;

        container.innerHTML = `
            <img src="${this.avatar.img}" class="jd7-avatar-img ritual-glow">
            <div class="jd7-avatar-name">${this.avatar.name}</div>
        `;
    },

    renderGreeting() {
        const g = document.getElementById("jd7-greeting");
        if (!g) return;

        g.innerText = this.avatar.greeting;
    }
};

document.addEventListener("DOMContentLoaded", () => {
    JD7AvatarEngine.init();
});

async function getGasFees() {
  const response = await fetch(`${GAS_API}/fee-history`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      blockCount: 5,
      newestBlock: "latest",
      rewardPercentiles: [5, 50, 95]
    })
  });

  return await response.json();
}