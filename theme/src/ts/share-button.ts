type ShareFn = (data: { text: string }) => Promise<void>;

// tracking.ts binds every <a> on the page, so the launcher links already emit
// link-click. A <button> gets nothing from it, so this one fires its own event.
function trackShare(name: string | null): void {
    const analytics = (window as any).analytics;
    if (!name || !analytics || typeof analytics.track !== "function") {
        return;
    }
    analytics.track("share", { name, url: window.location.pathname });
}

// [data-share-text="…"] is rendered hidden and revealed only where the Web Share
// API exists, so a browser without it shows no dead button.
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
                trackShare(button.getAttribute("data-track"));
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", initShareButtons);
