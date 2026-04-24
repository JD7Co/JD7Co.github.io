// JD7 EFFECTS — параллакс и будущие эффекты

export function initEffects() {
  const bg = document.querySelector('.parallax-bg');
  if (!bg) return;

  document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 6;
    const y = (e.clientY / window.innerHeight - 0.5) * 6;
    bg.style.transform = `translate(${x}px, ${y}px)`;
  });
}