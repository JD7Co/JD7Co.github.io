document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-include]").forEach(async el => {
    const file = el.getAttribute("data-include");
    const response = await fetch(file);
    el.innerHTML = await response.text();
  });
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