let direction = 1;
let pos = 0;

function move() {
  const el = document.getElementById("char");
  if (!el) return;

  pos += direction * 2;

  if (pos >= 500 || pos <= 0) {
    direction *= -1;
  }

  el.style.left = pos + "px";
  requestAnimationFrame(move);
}

window.addEventListener("DOMContentLoaded", move);

console.log("move.js geladen");

// darf nicht in Streamlit verwendet werden, da Streamlit externe, beziehungsweise in einem anderen Ordner liegende, Skripte als Text umwandelt. 
// => Das skript wird unausführbar. 
// => Einzige Möglichkeit das zu umgehen: Skript direkt in die HTML schreiben. 