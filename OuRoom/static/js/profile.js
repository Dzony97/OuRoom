document.addEventListener('DOMContentLoaded', function() {
  const showSettings = "{{ show_settings }}";  // Flag
  const settingsIcon = document.querySelector('.settings-icon');
  const profileInfo = document.querySelector('.profile-info');
  const settingsMenu = document.getElementById('settings-menu');

  if (showSettings === "True") {
    settingsMenu.style.display = "block";  // Show settings menu
    profileInfo.style.display = "none";    // Hide profile information
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