// Blog listing enhancements: infinite scroll (with a hybrid "Load more" guard)
// and in-place client-side category filtering on the homepage. Progressive
// enhancement — the numbered paginator and real category links are the no-JS /
// crawler fallback, hidden only once this upgrades them.
//
// DOM contract (rendered by the Hugo templates):
//   [data-post-list]           the container holding the list rows
//   [data-post-row]            one post row (also present in the rows fragment)
//   [data-paginator]           the numbered pager; data-next-url = next page URL
//   [data-blog-filter]         the homepage filter bar
//   [data-blog-filter] a[data-category]  a filter pill ("" = All), .is-active

const AUTO_LOAD_LIMIT = 3; // consecutive auto-loads before requiring a click
const REVEAL_STEP = 10; // rows revealed per step when a category filter is active

document.addEventListener("DOMContentLoaded", () => {
    const list = document.querySelector<HTMLElement>("[data-post-list]");
    if (!list) {
        return;
    }

    const paginator = document.querySelector<HTMLElement>("[data-paginator]");
    const filterBar = document.querySelector<HTMLElement>("[data-blog-filter]");

    // Snapshot the server-rendered "All" state so the filter can restore it.
    const originalHTML = list.innerHTML;
    const originalNextUrl = paginator ? paginator.getAttribute("data-next-url") : null;
    const basePath = location.pathname;

    // Hide the numbered pager; JS takes over paging. It stays in the DOM for
    // no-JS clients and crawlers.
    if (paginator) {
        paginator.style.display = "none";
    }

    // Shared sentinel + "Load more" button, placed just below the list.
    const controls = document.createElement("div");
    controls.className = "mt-8 flex empty:hidden";
    const loadMoreBtn = document.createElement("button");
    loadMoreBtn.type = "button";
    loadMoreBtn.className = "btn btn-outline";
    loadMoreBtn.textContent = "Load more";
    loadMoreBtn.hidden = true;
    controls.appendChild(loadMoreBtn);

    const sentinel = document.createElement("div");
    sentinel.setAttribute("aria-hidden", "true");
    sentinel.style.height = "1px";

    const anchor = paginator || list;
    anchor.parentElement!.insertBefore(sentinel, anchor.nextSibling);
    sentinel.parentElement!.insertBefore(controls, sentinel.nextSibling);

    // Mode: "paginate" fetches successive /page/N/; "reveal" shows buffered rows
    // (used when a category filter is active — the whole category is fetched once
    // and revealed 10 at a time).
    let mode: "paginate" | "reveal" = "paginate";
    let nextUrl: string | null = originalNextUrl;
    let buffer: HTMLElement[] = [];
    let autoLoads = 0;
    let busy = false;
    let intersecting = false;
    let pumping = false;

    // Keep the address bar in sync with the page currently at the top of the
    // viewport (replaceState, so Back doesn't step through every loaded page).
    const markerObserver = new IntersectionObserver(
        (entries) => {
            for (const e of entries) {
                if (e.isIntersecting) {
                    const url = (e.target as HTMLElement).dataset.pageUrl;
                    if (url) {
                        history.replaceState(null, "", url);
                    }
                }
            }
        },
        { rootMargin: "0px 0px -80% 0px" },
    );

    function done(): boolean {
        return mode === "paginate" ? !nextUrl : buffer.length === 0;
    }

    async function loadMore(): Promise<void> {
        if (busy || done()) {
            return;
        }
        busy = true;
        try {
            if (mode === "reveal") {
                buffer.splice(0, REVEAL_STEP).forEach((row) => {
                    row.style.display = "";
                });
            } else if (nextUrl) {
                const res = await fetch(nextUrl);
                if (!res.ok) {
                    throw new Error(`HTTP ${res.status}`);
                }
                const doc = new DOMParser().parseFromString(await res.text(), "text/html");

                // Boundary marker for URL sync.
                const marker = document.createElement("div");
                marker.dataset.pageUrl = nextUrl;
                marker.style.height = "0";
                marker.setAttribute("aria-hidden", "true");
                list.appendChild(marker);
                markerObserver.observe(marker);

                doc.querySelectorAll("[data-post-list] [data-post-row]").forEach((row) => {
                    list.appendChild(document.importNode(row, true));
                });
                const pag = doc.querySelector("[data-paginator]");
                nextUrl = pag ? pag.getAttribute("data-next-url") : null;
            }
        } catch {
            // On any fetch error, restore the numbered pager and stop.
            if (paginator) {
                paginator.style.display = "";
            }
            nextUrl = null;
            buffer = [];
        } finally {
            busy = false;
        }
    }

    // The load loop. IntersectionObserver only fires on TRANSITIONS, so we can't
    // rely on it to re-trigger while the sentinel stays in view (e.g. right after
    // a short page loads, or after a "Load more" click). Instead the observer
    // just tracks whether the sentinel is visible; this pump does the looping —
    // auto-loading up to the cap, then handing off to the button.
    async function pump(): Promise<void> {
        if (pumping) {
            return;
        }
        pumping = true;
        try {
            while (intersecting && !done() && autoLoads < AUTO_LOAD_LIMIT) {
                loadMoreBtn.hidden = true;
                autoLoads++;
                await loadMore();
            }
            if (done()) {
                io.disconnect();
                sentinel.remove();
                loadMoreBtn.hidden = true;
            } else if (intersecting && autoLoads >= AUTO_LOAD_LIMIT) {
                // Hand off to a manual click so the content below (series strip,
                // CTA, footer) stays reachable.
                loadMoreBtn.hidden = false;
            }
        } finally {
            pumping = false;
        }
    }

    const io = new IntersectionObserver(
        (entries) => {
            intersecting = entries[0].isIntersecting;
            if (intersecting) {
                pump();
            }
        },
        { rootMargin: "700px 0px" },
    );
    io.observe(sentinel);

    loadMoreBtn.addEventListener("click", () => {
        // Resume auto-loading for another burst; the sentinel is still in view,
        // so pump() continues from here.
        autoLoads = 0;
        loadMoreBtn.hidden = true;
        pump();
    });

    // --- Homepage category filter ---------------------------------------------

    function setActive(cat: string) {
        if (!filterBar) {
            return;
        }
        filterBar.querySelectorAll<HTMLElement>("[data-category]").forEach((pill) => {
            const on = (pill.dataset.category || "") === cat;
            pill.classList.toggle("is-active", on);
            if (on) {
                pill.setAttribute("aria-current", "page");
            } else {
                pill.removeAttribute("aria-current");
            }
        });
    }

    function rearmSentinel() {
        autoLoads = 0;
        loadMoreBtn.hidden = true;
        if (!sentinel.isConnected) {
            controls.parentElement!.insertBefore(sentinel, controls);
        }
        if (!done()) {
            // Force a fresh intersection callback so pump() re-evaluates.
            io.unobserve(sentinel);
            io.observe(sentinel);
        }
    }

    async function applyCategory(cat: string, push: boolean): Promise<void> {
        setActive(cat);

        if (!cat) {
            list.innerHTML = originalHTML;
            mode = "paginate";
            nextUrl = originalNextUrl;
            buffer = [];
            if (push) {
                history.pushState(null, "", basePath);
            }
            rearmSentinel();
            return;
        }

        try {
            const res = await fetch(`/blog/category/${cat}/rows.html`);
            if (!res.ok) {
                throw new Error(`HTTP ${res.status}`);
            }
            const doc = new DOMParser().parseFromString(await res.text(), "text/html");
            list.innerHTML = "";
            doc.querySelectorAll<HTMLElement>("[data-post-row]").forEach((row) => {
                list.appendChild(document.importNode(row, true));
            });
            const rows = Array.from(list.querySelectorAll<HTMLElement>("[data-post-row]"));
            buffer = rows.slice(REVEAL_STEP);
            buffer.forEach((row) => {
                row.style.display = "none";
            });
            mode = "reveal";
            nextUrl = null;
            if (push) {
                history.pushState(null, "", `?category=${cat}`);
            }
            rearmSentinel();
        } catch {
            // Fall back to a full navigation to the real category page.
            location.href = `/blog/category/${cat}/`;
        }
    }

    if (filterBar) {
        filterBar.addEventListener("click", (e) => {
            const pill = (e.target as HTMLElement).closest<HTMLElement>("[data-category]");
            if (!pill) {
                return;
            }
            e.preventDefault();
            applyCategory(pill.dataset.category || "", true);
        });

        // Restore a ?category=<id> deep link on load.
        const initial = new URLSearchParams(location.search).get("category");
        if (initial) {
            applyCategory(initial, false);
        }

        // Re-sync the filter on back/forward within the homepage.
        window.addEventListener("popstate", () => {
            const cat = new URLSearchParams(location.search).get("category") || "";
            applyCategory(cat, false);
        });
    }
});
