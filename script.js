
document.getElementById('form').addEventListener('submit', function(event) {
  event.preventDefault();
  document.getElementById('message').textContent = 'ДАННЫЕ ЗАПИСАНЫ';
});