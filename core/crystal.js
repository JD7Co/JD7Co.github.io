// JD7 ARTEFACT CORE — кристалл

import { cycleTheme, restoreTheme } from './theme.js';

export function initCrystal() {
  const crystal = document.getElementById('jd7-crystal');

  if (!crystal) return;

  // восстановить тему
  restoreTheme();

  // клик по кристаллу
  crystal.addEventListener('click', () => {
    cycleTheme();
    crystal.classList.add('crystal-flash');
    setTimeout(() => crystal.classList.remove('crystal-flash'), 460);
  });
}