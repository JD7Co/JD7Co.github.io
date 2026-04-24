// JD7 THEME ENGINE
// Управляет 4 темами: dark, light, ebook, plasma

export const THEMES = [
  'theme-dark',
  'theme-light',
  'theme-ebook',
  'theme-plasma'
];

const THEME_KEY = 'jd7_theme';

export function applyTheme(themeClass) {
  THEMES.forEach(t => document.body.classList.remove(t));
  document.body.classList.add(themeClass);
  localStorage.setItem(THEME_KEY, themeClass);
}

export function getCurrentThemeIndex() {
  for (let i = 0; i < THEMES.length; i++) {
    if (document.body.classList.contains(THEMES[i])) return i;
  }
  return 0;
}

export function cycleTheme() {
  const current = getCurrentThemeIndex();
  const next = (current + 1) % THEMES.length;
  applyTheme(THEMES[next]);
}

export function restoreTheme() {
  const saved = localStorage.getItem(THEME_KEY);
  if (saved && THEMES.includes(saved)) {
    applyTheme(saved);
  } else {
    applyTheme('theme-dark');
  }
}