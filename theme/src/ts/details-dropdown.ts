// Close <details data-dropdown> menus on outside click or Escape. Opt in by
// adding `data-dropdown` to a <details> used as a dropdown (e.g. the blog header
// RSS menu). Native <details> toggles on summary click but never closes itself
// when focus moves elsewhere; this restores that expected dropdown behavior.

function closeAll(except?: Element) {
    document
        .querySelectorAll<HTMLDetailsElement>("details[data-dropdown][open]")
        .forEach((d) => {
            if (d !== except) {
                d.open = false;
            }
        });
}

document.addEventListener("click", (e) => {
    const target = e.target as Node;
    document
        .querySelectorAll<HTMLDetailsElement>("details[data-dropdown][open]")
        .forEach((d) => {
            if (!d.contains(target)) {
                d.open = false;
            }
        });
});

document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        const open = document.querySelector<HTMLDetailsElement>("details[data-dropdown][open]");
        if (open) {
            open.open = false;
            open.querySelector<HTMLElement>("summary")?.focus();
        }
    }
});

// Only one dropdown open at a time.
document.addEventListener("toggle", (e) => {
    const d = e.target as HTMLElement;
    if (d instanceof HTMLDetailsElement && d.open && d.hasAttribute("data-dropdown")) {
        closeAll(d);
    }
}, true);
