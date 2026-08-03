// Blog post page enhancements, all opt-in via data attributes rendered by the
// post templates (no-ops elsewhere):
//   [data-blog-toc]        sidebar TOC → scrollspy (highlights the current h2)
//   [data-section-toc]     section-based sidebar TOC (case studies, whitepapers) → same scrollspy
//   [data-copy-link]       share-row button → copies data-url to the clipboard
//   [data-post-progress]   fixed bar under the nav → reading progress (scaleX)

// The "reading line": a heading (or the content top) counts as reached once it
// scrolls above this viewport offset. Just past the headings' 6rem
// scroll-margin-top, so the heading you click via the TOC registers as active
// instead of the one after it.
const READING_LINE = 100;

function onScrollRaf(update: () => void) {
    let rafPending = false;
    const onScroll = () => {
        if (rafPending) {
            return;
        }
        rafPending = true;
        requestAnimationFrame(() => {
            rafPending = false;
            update();
        });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
}

function initTocScrollspy(toc: HTMLElement | null) {
    if (!toc) {
        return;
    }
    const items = Array.from(toc.querySelectorAll<HTMLAnchorElement>("a[href^='#']"))
        .map(link => ({ link, heading: document.getElementById(decodeURIComponent(link.hash.slice(1))) }))
        .filter((item): item is { link: HTMLAnchorElement; heading: HTMLElement } => item.heading !== null);
    if (items.length === 0) {
        return;
    }

    onScrollRaf(() => {
        // Active = the last heading above the reading line; none before the first.
        let active: HTMLAnchorElement | null = null;
        for (const item of items) {
            if (item.heading.getBoundingClientRect().top <= READING_LINE) {
                active = item.link;
            }
        }
        for (const item of items) {
            item.link.classList.toggle("is-active", item.link === active);
        }
    });
}

function initCopyLink() {
    document.querySelectorAll<HTMLElement>("[data-copy-link]").forEach(btn => {
        const idle = btn.querySelector<HTMLElement>("[data-copy-link-idle]");
        const done = btn.querySelector<HTMLElement>("[data-copy-link-done]");
        let timer: number | undefined;
        btn.addEventListener("click", async () => {
            try {
                await navigator.clipboard.writeText(btn.getAttribute("data-url") || location.href);
            } catch {
                return;
            }
            idle?.setAttribute("hidden", "");
            done?.removeAttribute("hidden");
            window.clearTimeout(timer);
            timer = window.setTimeout(() => {
                done?.setAttribute("hidden", "");
                idle?.removeAttribute("hidden");
            }, 2000);
        });
    });
}

function initProgressBar() {
    const bar = document.querySelector<HTMLElement>("[data-post-progress]");
    const content = document.querySelector<HTMLElement>(".blog-post-content");
    if (!bar || !content) {
        return;
    }

    onScrollRaf(() => {
        // 0 when the content top crosses the reading line, 1 when the content
        // bottom clears the viewport. Posts shorter than the viewport jump to 1.
        const rect = content.getBoundingClientRect();
        const total = rect.height - window.innerHeight + READING_LINE;
        const progress = total > 0 ? (READING_LINE - rect.top) / total : 1;
        bar.style.transform = `scaleX(${Math.min(1, Math.max(0, progress))})`;
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initTocScrollspy(document.querySelector<HTMLElement>("[data-blog-toc]"));
    initTocScrollspy(document.querySelector<HTMLElement>("[data-section-toc]"));
    initCopyLink();
    initProgressBar();
});
