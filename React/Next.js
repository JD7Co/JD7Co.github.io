const GAS_API = import.meta.env.VITE_INFURA_GAS_API;

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