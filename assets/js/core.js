document.addEventListener('DOMContentLoaded', () => {
    console.log('JD7 Portal v3.0 loaded');
});
function loadTemplate() {
    fetch('/modules/template.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('header').innerHTML = html.split('</header>')[0] + '</header>';
            document.getElementById('footer').innerHTML = html.split('</header>')[1];
        });
}
<div class="theme-toggle" onclick="toggleTheme()">Тема</div>
async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected:', accounts[0]);
        } catch (e) {
            console.error('Wallet connection rejected');
        }
    } else {
        alert('Web3 кошелёк не найден');
    }
}
document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('fade');
});
