// /learn/ overview filter: narrows the directory to a single labeled section
// in place, defaulting to "All". Progressive enhancement — the pills are real
// anchor links (jump to the section) as the no-JS / crawler fallback, and every
// section stays server-rendered in the DOM; this only shows/hides.
//
// DOM contract (rendered by layouts/learn/list.html):
//   [data-learn-filter]                    the filter bar
//   [data-learn-filter] [data-section]     a pill ("" = All), .is-active
//   section[data-section]                    one section, matched by id

document.addEventListener("DOMContentLoaded", () => {
    const filterBar = document.querySelector<HTMLElement>("[data-learn-filter]");
    if (!filterBar) {
        return;
    }

    const pills = Array.from(filterBar.querySelectorAll<HTMLElement>("[data-section]"));
    const sections = Array.from(document.querySelectorAll<HTMLElement>("section[data-section]"));
    const labels = Array.from(document.querySelectorAll<HTMLElement>("[data-section-label]"));

    function apply(id: string): void {
        pills.forEach(pill => {
            const on = (pill.dataset.section || "") === id;
            pill.classList.toggle("is-active", on);
            if (on) {
                pill.setAttribute("aria-current", "page");
            } else {
                pill.removeAttribute("aria-current");
            }
        });
        sections.forEach(section => {
            section.hidden = id !== "" && section.dataset.section !== id;
        });
        // Group labels only make sense in "All" mode — when a single section is
        // shown, the active pill already names it, so hide the redundant label.
        labels.forEach(label => {
            label.hidden = id !== "";
        });
    }

    filterBar.addEventListener("click", e => {
        const pill = (e.target as HTMLElement).closest<HTMLElement>("[data-section]");
        if (!pill) {
            return;
        }
        e.preventDefault();
        const id = pill.dataset.section || "";
        apply(id);
        // Deep-link the selection so a shared URL restores the filtered view; use
        // replaceState so Back doesn't step through every pill click.
        history.replaceState(null, "", id ? `#${id}` : location.pathname + location.search);
    });

    // Honor an incoming hash (shared link) by pre-selecting that section.
    const initial = location.hash.slice(1);
    if (initial && sections.some(s => s.dataset.section === initial)) {
        apply(initial);
    }
});
