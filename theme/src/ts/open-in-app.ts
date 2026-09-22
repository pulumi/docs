type ShareFn = (data: { text: string }) => Promise<void>;

const HANDOFF_GRACE_MS = 1500;

function trackOpen(name: string | null): void {
    const analytics = (window as any).analytics;
    if (!name || !analytics || typeof analytics.track !== "function") {
        return;
    }
    analytics.track("open-in-app", { name, url: window.location.pathname });
}

function fallbackFor(link: HTMLAnchorElement): HTMLElement | null {
    const next = link.nextElementSibling;
    return next instanceof HTMLElement && next.hasAttribute("data-open-fallback") ? next : null;
}

function initSchemeLinks(): void {
    document.querySelectorAll<HTMLAnchorElement>("[data-open-scheme]").forEach(link => {
        const fallback = fallbackFor(link);

        link.addEventListener("click", () => {
            trackOpen(link.getAttribute("data-track"));
            if (!fallback) {
                return;
            }

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
            }, HANDOFF_GRACE_MS);
        });
    });
}

function initShareButtons(): void {
    const share = (navigator as { share?: ShareFn }).share;
    if (!share) {
        return;
    }

    document.querySelectorAll<HTMLElement>("[data-share-text]").forEach(button => {
        button.removeAttribute("hidden");

        button.addEventListener("click", async () => {
            const text = button.getAttribute("data-share-text") || "";
            const shared = await share.call(navigator, { text }).then(() => true, () => false);
            if (shared) {
                trackOpen(button.getAttribute("data-track"));
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initSchemeLinks();
    initShareButtons();
});
