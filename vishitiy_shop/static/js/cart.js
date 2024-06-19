import { HandleManyCounters } from "/static/js/counter.js";
import { CartClient } from "/static/js/cart-client.js";

document.addEventListener("DOMContentLoaded", () => {
    initCounter();
    initRemove();
})

function initCounter() {
    const decrementButtons = document.querySelectorAll('.cart-decrement-btn');
    const incrementButtons = document.querySelectorAll('.cart-increment-btn');
    new HandleManyCounters(incrementButtons, decrementButtons)
}

function initRemove() {
    const cart = new CartClient();
    const removeForms = document.querySelectorAll('.remove-from-cart-form');

    removeForms.forEach((form) => {
        form.addEventListener('submit', cart.remove.bind(cart))
    })
}
