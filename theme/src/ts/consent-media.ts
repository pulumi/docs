// Consent-aware media (YouTube embeds).
//
// Under the OneTrust provider, layouts/partials/youtube-src.html renders a
// YouTube iframe with its URL in data-pulumi-consent-src instead of src, so the
// embed loads no YouTube resources, and sets no YouTube cookies, until the
// visitor allows Targeting (C0004). Until then the iframe shows a placeholder
// (rendered into its srcdoc, so it keeps the embed's size) explaining why, with
// buttons to allow Targeting or open Cookie Settings. Once C0004 is granted the
// iframe gets its real src, and any original srcdoc (the click-to-play
// thumbnail some embeds use) is restored.
//
// Under the Segment provider the partial renders a normal src, so there is
// nothing to promote and this module is a no-op.

const TARGETING = "C0004";

export const PLACEHOLDER_HTML = `<!doctype html>
<html><head><meta charset="utf-8"><style>
html,body{height:100%;margin:0}
body{display:flex;align-items:center;justify-content:center;background:#1a1036;color:#fff;font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;text-align:center;padding:16px;box-sizing:border-box}
p{margin:0 0 12px;max-width:42ch}
button{font:inherit;cursor:pointer;border-radius:6px;padding:6px 14px;margin:4px;border:1px solid #fff;background:transparent;color:#fff}
button[data-consent-allow]{background:#fff;color:#1a1036}
</style></head><body><div>
<p>This video is hosted on YouTube, which sets targeting cookies. Allowing it turns on targeting cookies across the site.</p>
<button type="button" data-consent-allow>Allow targeting cookies</button>
<button type="button" data-consent-settings>Cookie settings</button>
</div></body></html>`;

export function allowTargeting() {
    (window as any).OneTrust?.UpdateConsent?.("Category", `${TARGETING}:1`);
}

export function openCookieSettings() {
    (window as any).consentManager?.openConsentManager?.();
}

// Hook the placeholder's buttons up to this window. The srcdoc document is
// same-origin, so the parent can reach into it once it has loaded.
export function wirePlaceholder(doc: Document) {
    doc.querySelector("[data-consent-allow]")?.addEventListener("click", allowTargeting);
    doc.querySelector("[data-consent-settings]")?.addEventListener("click", openCookieSettings);
}

export function activateConsentMedia() {
    const runWithConsent = (window as any).runWithPulumiConsent as (category: string, callback: () => void) => void;
    const iframes = Array.from(document.querySelectorAll<HTMLIFrameElement>("iframe[data-pulumi-consent-src]"));

    for (const iframe of iframes) {
        // Init-once: a rescan skips iframes that already have a placeholder.
        if (iframe.dataset.pulumiConsentPlaceholder !== undefined) continue;

        const originalSrcdoc = iframe.getAttribute("srcdoc");
        iframe.dataset.pulumiConsentPlaceholder = "";
        iframe.addEventListener(
            "load",
            () => {
                if (iframe.contentDocument) wirePlaceholder(iframe.contentDocument);
            },
            { once: true },
        );
        iframe.srcdoc = PLACEHOLDER_HTML;

        // Deleting the data attribute on load keeps a second grant event from
        // re-assigning src.
        const load = () => {
            const src = iframe.dataset.pulumiConsentSrc;
            if (!src) return;
            iframe.src = src;
            delete iframe.dataset.pulumiConsentSrc;
            delete iframe.dataset.pulumiConsentPlaceholder;
            if (originalSrcdoc === null) {
                iframe.removeAttribute("srcdoc");
            } else {
                iframe.srcdoc = originalSrcdoc;
            }
        };

        runWithConsent(TARGETING, load);
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", activateConsentMedia);
} else {
    activateConsentMedia();
}
