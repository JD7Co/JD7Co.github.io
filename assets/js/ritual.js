function ritualPulse(element) {
    if (!element) return;
    element.classList.add('ritual-glow');
    setTimeout(() => element.classList.remove('ritual-glow'), 1500);
}

document.addEventListener('DOMContentLoaded', () => {
    const titles = document.querySelectorAll('h1');
    titles.forEach(t => {
        setInterval(() => ritualPulse(t), 3000);
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