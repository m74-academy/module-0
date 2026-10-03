// Keyboard access for the narrow-screen navigation drawer (academy-bgf.11).
// The theme's menu button is a <label> for a hidden checkbox, so Tab skips it,
// and the closed, offscreen drawer's links stay in the Tab order.
(() => {
  const drawer = document.getElementById("__drawer");
  const button = document.querySelector('.md-header__button[for="__drawer"]');
  const sidebar = document.querySelector(".md-sidebar--primary");
  if (!drawer || !button || !sidebar) return;

  // Matches the theme's breakpoint for the drawer layout.
  const narrow = window.matchMedia("(max-width: 76.234375em)");

  button.setAttribute("role", "button");
  button.setAttribute("tabindex", "0");

  const sync = () => {
    button.setAttribute("aria-expanded", String(drawer.checked));
    sidebar.inert = narrow.matches && !drawer.checked;
  };
  sync();
  drawer.addEventListener("change", sync);
  narrow.addEventListener("change", sync);

  const setOpen = (open) => {
    if (drawer.checked === open) return;
    drawer.checked = open;
    drawer.dispatchEvent(new Event("change"));
  };

  // The theme already opens a focused label on Enter; add Space for a button.
  button.addEventListener("keydown", (event) => {
    if (event.key !== " ") return;
    event.preventDefault();
    setOpen(!drawer.checked);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || !drawer.checked || !narrow.matches) return;
    setOpen(false);
    button.focus();
  });
})();
