// JD7 NFT ENGINE
// Loads collections from /nft/collections/*.json

export async function initNFT() {
  const root = document.getElementById("nft-root");

  const collections = [
    { name: "JD7 Avatars", file: "avatars.json" },
    { name: "JD7 Artefacts", file: "artefacts.json" },
    { name: "JD7 Keys", file: "keys.json" },
    { name: "JD7 Releases", file: "releases.json" }
  ];

  for (const col of collections) {
    const section = document.createElement("div");

    const title = document.createElement("div");
    title.className = "collection-title";
    title.textContent = col.name;

    const grid = document.createElement("div");
    grid.className = "nft-grid";

    try {
      const res = await fetch(`/nft/collections/${col.file}`);
      const data = await res.json();

      data.items.forEach(item => {
        const card = document.createElement("div");
        card.className = "nft-card";

        card.innerHTML = `
          <div class="nft-img" style="background-image:url('${item.image}')"></div>
          <div class="nft-name">${item.name}</div>
          <div class="nft-desc">${item.desc}</div>
        `;

        grid.appendChild(card);
      });

    } catch (e) {
      grid.innerHTML = `<div style="opacity:0.6;">Ошибка загрузки коллекции</div>`;
    }

    section.appendChild(title);
    section.appendChild(grid);
    root.appendChild(section);
  }
}