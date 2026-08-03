// Generic copy-to-clipboard control, opt-in via data attributes (no-op on pages
// without one):
//   [data-copy-text="…"]   click → writes the attribute value to the clipboard
//   [data-copy-idle]       descendants shown until a copy succeeds
//   [data-copy-done]       descendants shown for CONFIRM_MS after a copy succeeds
//
// Distinct from copybutton.ts, which scans for rendered code blocks and injects
// its own button; this one styles nothing and copies a literal string.

const CONFIRM_MS = 2000;

function initCopyText() {
    document.querySelectorAll<HTMLElement>("[data-copy-text]").forEach(control => {
        const idle = control.querySelectorAll<HTMLElement>("[data-copy-idle]");
        const done = control.querySelectorAll<HTMLElement>("[data-copy-done]");
        let timer: number | undefined;

        control.addEventListener("click", async () => {
            try {
                await navigator.clipboard.writeText(control.getAttribute("data-copy-text") || "");
            } catch {
                return;
            }
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
