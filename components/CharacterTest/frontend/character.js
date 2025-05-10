function sendMessage(type, data) {
  const msg = Object.assign({ isStreamlitMessage: true, type }, data);
  window.parent.postMessage(msg, "*");
}

window.addEventListener("DOMContentLoaded", () => {
  sendMessage("streamlit:componentReady", { apiVersion: 1 });
  sendMessage("streamlit:setComponentValue", { value: "ready" });
});