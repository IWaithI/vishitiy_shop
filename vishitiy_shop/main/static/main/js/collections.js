document.addEventListener('DOMContentLoaded', function () {
    // Обработка кликов на карточки
    const collectionCards = document.querySelectorAll('.collect');
    collectionCards.forEach(function(card) {
        card.addEventListener('click', function() {
            const collectionId = card.getAttribute('data-collection-id');
            if (collectionId) {
                const newUrl = `/products/?type=&collection=${collectionId}`;
                window.location.href = newUrl;
            } else {
                console.error('Collection ID not found');
            }
        });
    });
});