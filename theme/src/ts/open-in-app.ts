// Behavior for the agent launchers on /agent-onboarding/ (see
// layouts/partials/agent-launchers.html), opt-in via data attributes so this is
// a no-op on every other page:
//   [data-open-scheme]     anchor to a custom scheme; reveals its fallback line
//                          if the page never lost focus after the click
//   [data-open-fallback]   the hidden sibling <p> that reveal targets
//   [data-share-text="…"]  button that calls navigator.share, hidden where the
//                          API is absent
//   [data-track="…"]       optional; names the control in the analytics event
//
// The scheme-handler detection is a heuristic, and can only ever be one:
// browsers expose no way to ask whether a scheme has a registered handler. We
// infer a successful handoff from the page losing focus. Safari on macOS shows
// a "cannot open the page" alert for an unregistered scheme and Firefox shows a
// chooser — both of which blur the page and so read as a handoff, leaving the
// fallback line hidden. The copy button above the launchers is the real safety
// net; this just helps in the common (Chromium) case.

const FALLBACK_MS = 1500;

// tracking.ts registers `document.querySelectorAll("a")` only, so an anchor
// already emits link-click (carrying the destination); this event adds the "did
// it hand off" signal, and is the only event a <button> gets. `url` is the page
// the control was on, matching trackCopy in copy-text.ts and link-click.
function trackOpen(name: string | null): void {
    const analytics = (window as any).analytics;
    if (!name || !analytics || typeof analytics.track !== "function") {
        return;
    }
    analytics.track("open-in-app", { name, url: window.location.pathname });
}

// The fallback <p> immediately follows its anchor in the partial.
function fallbackFor(link: HTMLAnchorElement): HTMLElement | null {
    const next = link.nextElementSibling;
    return next instanceof HTMLElement && next.hasAttribute("data-open-fallback") ? next : null;
}

function initSchemeLinks(): void {
    document.querySelectorAll<HTMLAnchorElement>("[data-open-scheme]").forEach(link => {
        const fallback = fallbackFor(link);

        // Never preventDefault: the navigation is what opens the app.
        link.addEventListener("click", () => {
            trackOpen(link.getAttribute("data-track"));
            if (!fallback) {
                return;
            }

            // A retry should start from a clean slate rather than leaving last
            // attempt's line up while this one is still in flight.
            fallback.setAttribute("hidden", "");

            let handedOff = false;
            const noteHandoff = () => {
                handedOff = true;
            };
            const onVisibility = () => {
                if (document.visibilityState === "hidden") {
                    noteHandoff();
                }
            };
            window.addEventListener("blur", noteHandoff, { once: true });
            document.addEventListener("visibilitychange", onVisibility);

            window.setTimeout(() => {
                window.removeEventListener("blur", noteHandoff);
                document.removeEventListener("visibilitychange", onVisibility);
                if (!handedOff) {
                    fallback.removeAttribute("hidden");
                }
            }, FALLBACK_MS);
        });
    });
}

function initShareButtons(): void {
    // The Web Share API postdates this project's TypeScript (3.9), whose
    // lib.dom Navigator has no `share`.
    const share: ((data: { text: string }) => Promise<void>) | undefined = (navigator as any).share;
    if (!share) {
        return;
    }

    document.querySelectorAll<HTMLElement>("[data-share-text]").forEach(button => {
        button.removeAttribute("hidden");

        button.addEventListener("click", async () => {
            try {
                await share.call(navigator, { text: button.getAttribute("data-share-text") || "" });
            } catch {
                // The user dismissed the sheet — not a failure, and not an event.
                return;
            }
            trackOpen(button.getAttribute("data-track"));
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initSchemeLinks();
    initShareButtons();
});
