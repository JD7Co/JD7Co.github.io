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
