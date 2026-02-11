function ritualPulse(element) {
    if (!element) return;
    element.classList.add('ritual-glow');
}
function loadTemplate() {
    fetch('/modules/template.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('header').innerHTML = html.split('</header>')[0] + '</header>';
            document.getElementById('footer').innerHTML = html.split('</header>')[1];
        });
}
