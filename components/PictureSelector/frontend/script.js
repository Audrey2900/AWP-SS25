function sendMessage(type, data) {
  const msg = Object.assign({ isStreamlitMessage: true, type }, data);
  window.parent.postMessage(msg, "*");
}

window.addEventListener("DOMContentLoaded", () => {
  sendMessage("streamlit:componentReady", { apiVersion: 1 });

  const images = document.querySelectorAll(".selectable");
  const actions = [
    { label: "eröffnet veganen Dönerladen", keyword: "Doener" },
    { label: "flieht vor der Polizei", keyword: "Polizei" },
    { label: "als Marvel-Schurke", keyword: "Schurke" },
    { label: "wird beim Stehlen von Gartenzwergen erwischt", keyword: "Zwerg" }
  ];

  const actionContainer = document.getElementById("action-container");
  const actionImage = document.getElementById("action-image");
  const actionName = document.getElementById("action-name");
  const spinner = document.getElementById("spinner");

  // Merker für die aktuelle Bildvariante je Kombination
  const variantIndexMap = {};

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
          const comboKey = `${selectedName}_${action.keyword}`;
          if (!(comboKey in variantIndexMap)) {
            variantIndexMap[comboKey] = Math.floor(Math.random() * 3) + 1;
          } else {
            variantIndexMap[comboKey] = (variantIndexMap[comboKey] % 3) + 1;
          }

          const variant = variantIndexMap[comboKey];
          const actionImagePath = `./PictureGeneration/${selectedName}_${action.keyword}_${variant}.webp`;

          actionImage.style.display = "none";
          actionName.style.display = "none";
          spinner.style.display = "block";

          // Buttons deaktivieren
          const allButtons = document.querySelectorAll(".action-button");
          allButtons.forEach(btn => btn.disabled = true);

          const randomDelay = Math.floor(Math.random() * (10000 - 5000 + 1)) + 5000;

          setTimeout(() => {
            const tempImage = new Image();
            tempImage.src = actionImagePath;
            tempImage.onload = () => {
              actionImage.src = actionImagePath;
              actionImage.alt = `${selectedName} ${action.label}`;
              actionImage.style.display = "block";
              actionName.textContent = `${selectedName} ${action.label}`;
              actionName.style.display = "block";
              spinner.style.display = "none";

              // Buttons wieder aktivieren
              allButtons.forEach(btn => btn.disabled = false);
            };
          }, randomDelay);
        });

        actionContainer.appendChild(button);
      });
    });
  });
});
