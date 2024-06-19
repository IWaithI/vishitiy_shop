document.addEventListener("DOMContentLoaded", () => {
  showMessages()
})

function showMessages() {
  const messages = document.querySelectorAll('.msg');
  if (messages.length > 0) {
    handleClass(messages, 'opacity-0', 'opacity-100')
    setTimeout(() => {
      handleClass(messages, 'opacity-100', 'opacity-0')
    }, 5000)
  }
}

function handleClass(objects, className1, className2) {
  objects.forEach(obj => obj.classList.remove(className1))
  objects.forEach(obj => obj.classList.add(className2))
}