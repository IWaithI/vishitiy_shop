const arrowUp = `
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="#f00" class="bi bi-arrow-up-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 0 0 8a8 8 0 0 0 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"/>
</svg>
<p class="mt-2 text-white">Гортай вгору</p>
`
const arrowDown = `
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="#f00" class="bi bi-arrow-down-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"/>
</svg>
<p class="mt-2 text-white">Гортай вниз</p>
`
function scrollPage() {
    const el = document.querySelector("#scrollButton");
    // var currentPosition = window.scrollY;
    // var windowHeight = window.innerHeight;
    const bodyHeight = document.body.scrollHeight;
    if (el.dataset.direction === "up") {
        // Прокрутка вверх
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        // Прокрутка вниз
        window.scrollTo({ top: bodyHeight, behavior: 'smooth' });
    }
}

function switchArrow() {
    const el = document.querySelector("#scrollButton");
    const currentPosition = window.scrollY;

    if (currentPosition < 100) {
        el.innerHTML = arrowDown;
        el.dataset.direction = "down";
    } else {
        el.innerHTML = arrowUp;
        el.dataset.direction = "up";
    }
}

switchArrow();

window.addEventListener('scroll', switchArrow);

document.querySelector("#scrollButton").addEventListener('click', scrollPage);