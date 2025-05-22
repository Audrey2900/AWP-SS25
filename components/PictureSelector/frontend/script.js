function sendMessage(type, data) {
  const msg = Object.assign({ isStreamlitMessage: true, type }, data);
  window.parent.postMessage(msg, "*");
}

window.addEventListener("DOMContentLoaded", () => {
  sendMessage("streamlit:componentReady", { apiVersion: 1 });

  const images = document.querySelectorAll(".selectable");
  const actions = [
    { label: "eröffnet veganen Dönerladen", keyword: "Döner" },
    { label: "flieht vor der Polizei", keyword: "Polizei" },
    { label: "als Marvel-Schurke", keyword: "Schurke" },
    { label: "wird beim Stehlen von Gartenzwergen erwischt", keyword: "Zwerg" }
  ];

  const actionContainer = document.getElementById("action-container");
  const actionImage = document.getElementById("action-image");
  const actionName = document.getElementById("action-name");
  const spinner = document.getElementById("spinner");

  images.forEach(img => {
    img.addEventListener("click", () => {
      images.forEach(i => i.classList.remove("selected"));
      img.classList.add("selected");

      const selectedName = img.dataset.name;
      sendMessage("streamlit:setComponentValue", { value: selectedName });

      actionContainer.innerHTML = "";

      actions.forEach(action => {
        const button = document.createElement("button");
        button.textContent = action.label;
        button.classList.add("action-button");

        button.addEventListener("click", () => {
          const actionImagePath = `./PictureGeneration/${selectedName}_${action.keyword}.webp`;

          // Bild und Text ausblenden
          actionImage.style.display = "none";
          actionName.style.display = "none";

          // Spinner anzeigen
          spinner.style.display = "block";

          // Nach 10 Sekunden anzeigen
          setTimeout(() => {
            actionImage.src = actionImagePath;
            actionImage.alt = `${selectedName} ${action.label}`;
            actionImage.style.display = "block";

            // Zeige zusammengesetzten Satz statt "und"
            actionName.textContent = `${selectedName} ${action.label}`;
            actionName.style.display = "block";

            spinner.style.display = "none";
          }, 10000);
        });

        actionContainer.appendChild(button);
      });
    });
  });
});
