// JD7 ACCESSIBILITY PANEL

const FILTER_KEY = 'jd7_filter';

export function initAccessPanel() {
  const body = document.body;
  const btn = document.getElementById('access-button');
  const panel = document.getElementById('access-panel');
  const backdrop = document.getElementById('access-backdrop');
  const closeBtn = document.getElementById('access-close');
  const chips = Array.from(document.querySelectorAll('.access-chip'));

  function openPanel() {
    backdrop.classList.add('active');
    panel.classList.add('active');
  }

  function closePanel() {
    backdrop.classList.remove('active');
    panel.classList.remove('active');
  }

  btn.addEventListener('click', openPanel);
  closeBtn.addEventListener('click', closePanel);
  backdrop.addEventListener('click', closePanel);

  function clearFilters() {
    body.classList.remove('filter-green', 'filter-red', 'filter-yellow', 'filter-blue');
    chips.forEach(c => c.classList.remove('active'));
  }

  function applyFilter(name) {
    clearFilters();
    if (name) {
      body.classList.add('filter-' + name);
      const chip = chips.find(c => c.dataset.filter === name);
      if (chip) chip.classList.add('active');
      localStorage.setItem(FILTER_KEY, name);
    } else {
      localStorage.removeItem(FILTER_KEY);
    }
  }

  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const name = chip.dataset.filter;
      const active = chip.classList.contains('active');
      applyFilter(active ? null : name);
    });
  });

  // восстановить фильтр
  const saved = localStorage.getItem(FILTER_KEY);
  if (saved) applyFilter(saved);
}