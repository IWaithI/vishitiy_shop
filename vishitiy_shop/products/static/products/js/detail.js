// Импорт класса HandleCounter из файла counter.js для управления счетчиком товаров
import { HandleCounter } from "/static/js/counter.js";

// Импорт функции showToast из файла notifications.js для отображения всплывающих уведомлений
import { showToast } from "/static/js/notifications.js";

// Импорт класса CartClient из файла cart-client.js для взаимодействия с корзиной товаров
import { CartClient } from "/static/js/cart-client.js";

// Ожидание загрузки документа перед инициализацией функций
document.addEventListener("DOMContentLoaded", () => {
  initCounter(); // Вызов функции инициализации счетчика
  initAddToCart(); // Вызов функции инициализации добавления в корзину
});

// Функция инициализации счетчика товаров
function initCounter() {
  const decrementButton = document.querySelector('.product-decrement-btn'); 
  const incrementButton = document.querySelector('.product-increment-btn'); 
  new HandleCounter(decrementButton, incrementButton); // Создать экземпляр класса HandleCounter для управления счетчиком
}

// Функция инициализации добавления товара в корзину
function initAddToCart() {
  const cart = new CartClient(); // Создать экземпляр класса CartClient для работы с корзиной
  const form = document.querySelector('#add-to-cart-form'); // Найти форму добавления товара в корзину
  form.addEventListener('submit', (e) => { // Добавить обработчик события отправки формы
    e.preventDefault(); // Предотвратить стандартное поведение отправки формы

    // Проверить выбран ли размер и цвет товара перед добавлением в корзину
    const sizeSelected = form.querySelector('input[name="size"]:checked');
    const colorSelected = form.querySelector('input[name="color"]:checked');
    if (!sizeSelected || !colorSelected) {
      return showToast('Будь ласка, оберіть розмір та колiр перед додаванням до кошика', 'warning'); // Показать всплывающее уведомление, если размер или цвет не выбраны
    }
    cart.add.bind(cart)(e); // Вызвать метод добавления товара в корзину, привязанный к объекту cart
  });
}