/* JUNGÜBERNEHMER – kleines Skript: Menü auf dem Handy. Keine Cookies, kein Tracking. */
(function () {
  var button = document.querySelector(".menu-toggle");
  var nav = document.getElementById("hauptnavigation");

  function setOpen(open) {
    if (open) { nav.setAttribute("data-open", ""); } else { nav.removeAttribute("data-open"); }
    button.setAttribute("aria-expanded", String(open));
    button.textContent = open ? "Schließen" : "Menü";
  }

  if (button && nav) {
    button.addEventListener("click", function () { setOpen(!nav.hasAttribute("data-open")); });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.hasAttribute("data-open")) { setOpen(false); button.focus(); }
    });
  }

  if (window.console && console.log) {
    console.log(
      "%cOrange is the new black.",
      "background:#d4422a;color:#222;font:700 16px Poppins,sans-serif;padding:6px 10px",
      "Du schaust unter die Haube? Ruf an: +49 176 30666125"
    );
  }
})();
