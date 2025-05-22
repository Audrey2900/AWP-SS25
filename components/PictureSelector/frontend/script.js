function sendMessage(type, data) {
  const msg = Object.assign({ isStreamlitMessage: true, type }, data);
  window.parent.postMessage(msg, "*");
}

window.addEventListener("DOMContentLoaded", () => {
  sendMessage("streamlit:componentReady", { apiVersion: 1 });

  const images = document.querySelectorAll(".selectable");
  const actions = ["Döner", "Polizei", "Schurke", "Zwerg"]; // Aktionen definieren
  const actionContainer = document.getElementById("action-container"); // Container für Buttons
  const actionImage = document.getElementById("action-image"); // Bild für die Aktion
  const actionName = document.getElementById("action-name"); // Name der Person und Aktion

  images.forEach(img => {
    img.addEventListener("click", () => {
      images.forEach(i => i.classList.remove("selected"));
      img.classList.add("selected");

      const selectedName = img.dataset.name; // Name der Persönlichkeit
      sendMessage("streamlit:setComponentValue", { value: selectedName });

      // Buttons für Aktionen erstellen
      actionContainer.innerHTML = ""; // Vorherige Buttons entfernen
      actions.forEach(action => {
        const button = document.createElement("button");
        button.textContent = action;
        button.classList.add("action-button");
        button.addEventListener("click", () => {
          const actionImagePath = `./PictureGeneration/${selectedName}_${action}.webp`; // Bildpfad generieren
          actionImage.src = actionImagePath; // Bild aktualisieren
          actionImage.alt = `${selectedName} mit ${action}`; // Alternativtext setzen
          actionImage.style.display = "block"; // Bild sichtbar machen

          // Zusammengesetzten Namen anzeigen
          actionName.textContent = `${selectedName} und ${action}`;
          actionName.style.display = "block"; // Namen sichtbar machen
        });
        actionContainer.appendChild(button);
      });
    });
  });
});
