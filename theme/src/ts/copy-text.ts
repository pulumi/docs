// Generic copy-to-clipboard control, opt-in via data attributes (no-op on pages
// without one):
//   [data-copy-text="…"]   click → writes the attribute value to the clipboard
//   [data-copy-idle]       descendants shown until a copy succeeds
//   [data-copy-done]       descendants shown for CONFIRM_MS after a copy succeeds
//   [data-track="…"]       optional; names the control in the analytics event
//
// Distinct from copybutton.ts, which scans for rendered code blocks and injects
// its own button; this one styles nothing and copies a literal string.

const CONFIRM_MS = 2000;

// tracking.ts registers `document.querySelectorAll("a")` only, so a data-track
// on a button reaches nothing. Fire the event here instead, mirroring how
// copybutton.ts emits its own "copy-code-block".
function trackCopy(name: string | null): void {
    const analytics = (window as any).analytics;
    if (!name || !analytics || typeof analytics.track !== "function") {
        return;
    }
    analytics.track("copy-text", { name, url: window.location.pathname });
}

// navigator.clipboard only exists in a secure context, so on the plain-HTTP S3
// preview builds it is undefined and the modern path is unavailable. Fall back
// to a selected off-screen textarea, which works there. Returns whether the text
// actually reached the clipboard, so the caller never reports a false success.
async function copyText(text: string): Promise<boolean> {
    if (window.isSecureContext && navigator.clipboard) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch {
            // Permission denied or the document lost focus — try the fallback.
        }
    }

    const field = document.createElement("textarea");
    field.value = text;
    field.setAttribute("readonly", "");
    field.setAttribute("aria-hidden", "true");
    field.tabIndex = -1;
    // Off-screen, and sized to nothing with no border or padding, so there is
    // nothing to render even if a browser were to ignore the offset.
    field.style.cssText =
        "position:fixed;top:0;left:-9999px;width:1px;height:1px;padding:0;border:0;opacity:0;pointer-events:none";
    document.body.appendChild(field);

    // Preserve whatever the user had selected before we hijack the selection.
    const selection = document.getSelection();
    const previous = selection && selection.rangeCount > 0 ? selection.getRangeAt(0) : null;

    field.select();
    let copied = false;
    try {
        copied = document.execCommand("copy");
    } catch {
        copied = false;
    }

    field.remove();
    if (selection && previous) {
        selection.removeAllRanges();
        selection.addRange(previous);
    }
    return copied;
}

function initCopyText() {
    document.querySelectorAll<HTMLElement>("[data-copy-text]").forEach(control => {
        const idle = control.querySelectorAll<HTMLElement>("[data-copy-idle]");
        const done = control.querySelectorAll<HTMLElement>("[data-copy-done]");
        let timer: number | undefined;

        control.addEventListener("click", async () => {
            if (!(await copyText(control.getAttribute("data-copy-text") || ""))) {
                return;
            }
            trackCopy(control.getAttribute("data-track"));
            idle.forEach(el => el.setAttribute("hidden", ""));
            done.forEach(el => el.removeAttribute("hidden"));
            window.clearTimeout(timer);
            timer = window.setTimeout(() => {
                done.forEach(el => el.setAttribute("hidden", ""));
                idle.forEach(el => el.removeAttribute("hidden"));
            }, CONFIRM_MS);
        });
    });
}

document.addEventListener("DOMContentLoaded", initCopyText);
