document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-include]").forEach(async el => {
    const file = el.getAttribute("data-include");
    const response = await fetch(file);
    el.innerHTML = await response.text();
  });
});
