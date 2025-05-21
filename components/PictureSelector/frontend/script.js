function sendMessage(type, data) {
  const msg = Object.assign({ isStreamlitMessage: true, type }, data);
  window.parent.postMessage(msg, "*");
}

window.addEventListener("DOMContentLoaded", () => {
  sendMessage("streamlit:componentReady", { apiVersion: 1 });

  const images = document.querySelectorAll(".selectable");

  images.forEach(img => {
    img.addEventListener("click", () => {
      images.forEach(i => i.classList.remove("selected"));
      
      img.classList.add("selected");

      const selectedName = img.dataset.name;
      sendMessage("streamlit:setComponentValue", { value: selectedName });
    });
  });
});
