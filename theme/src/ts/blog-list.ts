// Blog listing enhancements: infinite scroll (with a hybrid "Load more" guard)
// and in-place client-side category filtering on the homepage. Progressive
// enhancement — the numbered paginator and real category links are the no-JS /
// crawler fallback, hidden only once this upgrades them.
//
// DOM contract (rendered by the Hugo templates):
//   [data-post-list]           the container holding the list rows
//   [data-post-row]            one post row (also present in the rows fragment)
//   [data-post-grid]           (term pages) the medium-card grid above the list
//   [data-post-card]           one grid card
//   [data-paginator]           the pager wrapper (label + nav); data-next-url = next page URL
//   [data-blog-filter]         the homepage filter bar
//   [data-blog-filter] a[data-category]  a filter pill ("" = All), .is-active

const AUTO_LOAD_LIMIT = 3; // consecutive auto-loads before requiring a click
const REVEAL_STEP = 10; // rows revealed per step when a category filter is active

document.addEventListener("DOMContentLoaded", () => {
    const list = document.querySelector<HTMLElement>("[data-post-list]");
    if (!list) {
        return;
    }

    // Deep /page/N/ landings render classic pagination (server-rendered top +
    // bottom pagers). Skip the infinite-scroll / load-more enhancement so those
    // pagers stay visible and paging is done via normal navigation. Page 1 (no
    // /page/N/ segment) keeps the enhancement.
    if (/\/page\/\d+\/$/.test(location.pathname)) {
        return;
    }

    const paginator = document.querySelector<HTMLElement>("[data-paginator]");
    const filterBar = document.querySelector<HTMLElement>("[data-blog-filter]");

    // --- Homepage list/card view toggle ---------------------------------------
    // Each row carries both a compact and a card representation; `.is-cards` on
    // the list container swaps which one shows (see _blog.scss). Appended /
    // filtered rows clone the same markup, so they inherit the current view for
    // free. The choice is remembered across visits.
    const viewToggle = document.querySelector<HTMLElement>("[data-blog-view-toggle]");
    if (viewToggle) {
        const VIEW_KEY = "pulumi-blog-view";
        const applyView = (view: string) => {
            const cards = view === "cards";
            list.classList.toggle("is-cards", cards);
            viewToggle.querySelectorAll<HTMLElement>("[data-view]").forEach(btn => {
                const on = (btn.dataset.view || "list") === (cards ? "cards" : "list");
                if (on) {
                    btn.setAttribute("aria-current", "page");
                } else {
                    btn.removeAttribute("aria-current");
                }
            });
        };
        let stored: string | null = null;
        try {
            stored = localStorage.getItem(VIEW_KEY);
        } catch {
            // localStorage unavailable (private mode / blocked) — default view.
        }
        if (stored === "cards") {
            applyView("cards");
        }
        viewToggle.addEventListener("click", e => {
            const btn = (e.target as HTMLElement).closest<HTMLElement>("[data-view]");
            if (!btn) {
                return;
            }
            const view = btn.dataset.view || "list";
            applyView(view);
            try {
                localStorage.setItem(VIEW_KEY, view);
            } catch {
                // Ignore persistence failures; the toggle still works this session.
            }
        });
    }

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

    // Bumped every time the filter rewrites the list. Fetches capture the value
    // before awaiting and bail if it moved — otherwise a page load still in
    // flight when a pill is clicked would append its (unfiltered) rows below
    // the filtered list, and of two rapid pill clicks the SLOWER response would
    // win the content while the faster click owns the active pill.
    let generation = 0;

    // Keep the address bar in sync with the page currently at the top of the
    // viewport (replaceState, so Back doesn't step through every loaded page).
    // Driven by a scroll listener, NOT a thin-band IntersectionObserver: a normal
    // wheel scroll can jump a 0-height boundary marker clean over a narrow band, so
    // it never reports as intersecting and the URL would stall. Instead, on each
    // scroll we take the LAST boundary marker that has passed the top of the
    // viewport — monotonic, so it can never be skipped. Markers ([data-page-url])
    // sit in page order in the list.
    const TOP_THRESHOLD = 120; // a boundary counts as "passed" at/above this y
    let syncScheduled = false;
    function syncUrl(): void {
        syncScheduled = false;
        if (mode !== "paginate") {
            return; // filtered/reveal mode owns the URL (a real category term page)
        }
        const markers = list.querySelectorAll<HTMLElement>("[data-page-url]");
        let url = basePath;
        for (let i = 0; i < markers.length; i++) {
            if (markers[i].getBoundingClientRect().top <= TOP_THRESHOLD) {
                url = markers[i].dataset.pageUrl || url;
            } else {
                break;
            }
        }
        if (new URL(url, location.origin).pathname !== location.pathname) {
            history.replaceState(null, "", url);
        }
    }
    window.addEventListener(
        "scroll",
        () => {
            if (!syncScheduled) {
                syncScheduled = true;
                requestAnimationFrame(syncUrl);
            }
        },
        { passive: true },
    );

    function done(): boolean {
        return mode === "paginate" ? !nextUrl : buffer.length === 0;
    }

    async function loadMore(): Promise<void> {
        if (busy || done()) {
            return;
        }
        busy = true;
        const gen = generation;
        try {
            if (mode === "reveal") {
                buffer.splice(0, REVEAL_STEP).forEach(row => {
                    row.style.display = "";
                });
            } else if (nextUrl) {
                const url = nextUrl;
                const res = await fetch(url);
                if (!res.ok) {
                    throw new Error(`HTTP ${res.status}`);
                }
                const text = await res.text();
                if (gen !== generation) {
                    return;
                }
                const doc = new DOMParser().parseFromString(text, "text/html");

                // Boundary marker (read by syncUrl on scroll) for URL sync.
                const marker = document.createElement("div");
                marker.dataset.pageUrl = url;
                marker.style.height = "0";
                marker.setAttribute("aria-hidden", "true");
                list.appendChild(marker);

                // A term page's grid run can span pager pages: fetched grid
                // cards continue the existing [data-post-grid] (the split point
                // is global, so a page with grid cards always follows one that
                // already rendered the grid container).
                const grid = document.querySelector<HTMLElement>("[data-post-grid]");
                if (grid) {
                    doc.querySelectorAll("[data-post-grid] [data-post-card]").forEach(card => {
                        grid.appendChild(document.importNode(card, true));
                    });
                }
                doc.querySelectorAll("[data-post-list] [data-post-row]").forEach(row => {
                    list.appendChild(document.importNode(row, true));
                });
                const pag = doc.querySelector("[data-paginator]");
                nextUrl = pag ? pag.getAttribute("data-next-url") : null;
            }
        } catch {
            // On any fetch error, restore the numbered pager and stop — unless
            // the filter already superseded this request.
            if (gen !== generation) {
                return;
            }
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
        entries => {
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
        filterBar.querySelectorAll<HTMLElement>("[data-category]").forEach(pill => {
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

    // Filtering rewrites the address bar to the REAL category term page URL
    // (/blog/category/<id>/), not a ?category= query on /blog/ — shared and
    // bookmarked links then point at the canonical, indexed page, so its search
    // equity isn't diluted onto /blog/. A reload or no-JS visit lands on the
    // server-rendered term page.
    const originalTitle = document.title;

    function categoryUrl(cat: string): string {
        return cat ? `/blog/category/${cat}/` : basePath;
    }

    function categoryFromLocation(): string {
        const m = location.pathname.match(/^\/blog\/category\/([^/]+)\/$/);
        return m ? m[1] : "";
    }

    function syncTitle(cat: string) {
        const pill = filterBar && cat ? filterBar.querySelector<HTMLElement>(`a[data-category="${cat}"]`) : null;
        document.title = pill ? `${pill.textContent!.trim()} | Pulumi Blog` : originalTitle;
    }

    async function applyCategory(cat: string, push: boolean): Promise<void> {
        const gen = ++generation;
        setActive(cat);

        if (!cat) {
            list.innerHTML = originalHTML;
            mode = "paginate";
            nextUrl = originalNextUrl;
            buffer = [];
            if (push) {
                history.pushState(null, "", basePath);
            }
            syncTitle("");
            rearmSentinel();
            return;
        }

        try {
            const res = await fetch(`/blog/category/${cat}/rows.html`);
            if (!res.ok) {
                throw new Error(`HTTP ${res.status}`);
            }
            const text = await res.text();
            if (gen !== generation) {
                return;
            }
            const doc = new DOMParser().parseFromString(text, "text/html");
            list.innerHTML = "";
            doc.querySelectorAll<HTMLElement>("[data-post-row]").forEach(row => {
                list.appendChild(document.importNode(row, true));
            });
            const rows = Array.from(list.querySelectorAll<HTMLElement>("[data-post-row]"));
            buffer = rows.slice(REVEAL_STEP);
            buffer.forEach(row => {
                row.style.display = "none";
            });
            mode = "reveal";
            nextUrl = null;
            if (push) {
                history.pushState(null, "", categoryUrl(cat));
            }
            syncTitle(cat);
            rearmSentinel();
        } catch {
            // Fall back to a full navigation to the real category page — unless
            // a newer click already superseded this request.
            if (gen === generation) {
                location.href = categoryUrl(cat);
            }
        }
    }

    if (filterBar) {
        filterBar.addEventListener("click", e => {
            const pill = (e.target as HTMLElement).closest<HTMLElement>("[data-category]");
            if (!pill) {
                return;
            }
            e.preventDefault();
            applyCategory(pill.dataset.category || "", true);
        });

        // Re-sync the filter on back/forward within the homepage's history
        // entries.
        window.addEventListener("popstate", () => {
            applyCategory(categoryFromLocation(), false);
        });
    } else {
        // No filter bar: a server-rendered term page, /blog/ page 2+, etc. If
        // the homepage filter pushed history entries and the user then reloaded
        // (landing on this real term page), Back/Forward walks those entries as
        // same-document traversals — the URL changes but this document has no
        // filter to re-render. Turn any path-changing traversal into a real
        // navigation. (Hash-only traversals keep the pathname and are ignored.)
        window.addEventListener("popstate", () => {
            if (location.pathname !== basePath) {
                location.reload();
            }
        });
    }
});
