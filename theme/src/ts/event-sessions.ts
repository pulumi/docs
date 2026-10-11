// Session tabs on event pages that run more than once (an Americas slot and an
// EMEA slot, say). The tabs are plain links to "#session-<label>" and nothing on
// the page carries that id, so the hash is pure state: switching sessions swaps
// the panels in place rather than scrolling somewhere. Same pattern as the
// /events/ filter tabs.
//
// The server renders the default session's panels visible and the rest hidden
// (see layouts/partials/events/type-content.html), so this only has to react to
// the hash — with no JS the page still shows one complete, coherent session.
//
// The tabs use the shared underline tab system (shared/_tabs.scss), whose active
// state is the `is-active` class toggled below.

const TAB_SELECTOR = "[data-session-tab]";
const PANEL_SELECTOR = "[data-session-panel]";

const activateSession = (key: string) => {
    const tabs = Array.from(document.querySelectorAll<HTMLAnchorElement>(TAB_SELECTOR));

    // An unrelated hash (#register from the mobile CTA, say) must leave the
    // panels alone rather than hiding every one of them.
    if (!tabs.some(tab => tab.dataset.sessionTab === key)) {
        return;
    }

    tabs.forEach(tab => {
        const isActive = tab.dataset.sessionTab === key;
        tab.classList.toggle("is-active", isActive);
        if (isActive) {
            tab.setAttribute("aria-current", "true");
        } else {
            tab.removeAttribute("aria-current");
        }
    });

    // Unhiding a panel is what triggers the HubSpot form inside it to load: the
    // component lazy-loads on an IntersectionObserver, which can't fire while
    // the panel is display:none.
    document.querySelectorAll<HTMLElement>(PANEL_SELECTOR).forEach(panel => {
        panel.hidden = panel.dataset.sessionPanel !== key;
    });
};

const activateFromHash = () => {
    const key = location.hash.slice(1);
    if (key) {
        activateSession(key);
    }
};

if (document.querySelector(TAB_SELECTOR)) {
    activateFromHash();
    window.addEventListener("hashchange", activateFromHash);
}
