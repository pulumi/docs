// Consent-aware media (YouTube embeds).
//
// Under the OneTrust provider, layouts/partials/youtube-src.html renders a
// YouTube iframe with its URL in data-pulumi-consent-src instead of src, so the
// embed loads no YouTube resources — and sets no YouTube cookies — until the
// visitor allows Targeting (C0004). This module promotes those iframes to a
// real src once C0004 is granted, via the shared runWithPulumiConsent bridge.
//
// Under the Segment provider the partial renders a normal src, so there is
// nothing to promote and this module is a no-op.

function activateConsentMedia() {
    const runWithConsent = (window as any).runWithPulumiConsent as ((category: string, callback: () => void) => void) | undefined;
    const iframes = Array.from(document.querySelectorAll<HTMLIFrameElement>("iframe[data-pulumi-consent-src]"));

    for (const iframe of iframes) {
        // Init-once: deleting the data attribute on load keeps a later rescan
        // (or a second grant event) from re-assigning src.
        const load = () => {
            const src = iframe.dataset.pulumiConsentSrc;
            if (!src) return;
            iframe.src = src;
            delete iframe.dataset.pulumiConsentSrc;
        };

        if (typeof runWithConsent === "function") {
            runWithConsent("C0004", load);
        } else {
            load();
        }
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", activateConsentMedia);
} else {
    activateConsentMedia();
}

export {};
