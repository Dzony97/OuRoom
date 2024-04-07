document.addEventListener('DOMContentLoaded', function() {
  var showSettings = "{{ show_settings }}";  // Pobierz flagę z kontekstu
  var settingsIcon = document.querySelector('.settings-icon');
  var profileInfo = document.querySelector('.profile-info');
  var settingsMenu = document.getElementById('settings-menu');

  if (showSettings === "True") {
    settingsMenu.style.display = "block";  // Pokaż menu ustawień
    profileInfo.style.display = "none";    // Ukryj informacje o profilu
  }

  settingsIcon.addEventListener('click', function() {
    if (settingsMenu.style.display === "none") {
      settingsMenu.style.display = "block";
      profileInfo.style.display = "none";
    } else {
      settingsMenu.style.display = "none";
      profileInfo.style.display = "block";
    }
  });
});