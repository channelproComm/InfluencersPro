document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.getElementById('bodyContent');
  
    darkModeToggle.addEventListener('click', function () {
      body.classList.toggle('dark-mode');
    });
  });