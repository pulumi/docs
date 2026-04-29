declare global {
    interface Window {
        analytics?: {
            track: (event: string, properties?: Record<string, unknown>) => void;
        };
    }
}

const VALID_FILTERS = ["all", "news", "press", "awards"] as const;
type Filter = (typeof VALID_FILTERS)[number];

const ARCHIVE_PAGE_SIZE = 20;

const isValidFilter = (value: string): value is Filter =>
    (VALID_FILTERS as readonly string[]).includes(value);

const filterFromHash = (): Filter => {
    const hash = location.hash.slice(1);
    return isValidFilter(hash) ? hash : "all";
};

const trackEvent = (event: string, properties: Record<string, unknown>) => {
    window.analytics?.track(event, properties);
};

// Pagination state per filter pane.
const archiveVisible: Record<Filter, number> = {
    all: ARCHIVE_PAGE_SIZE,
    news: ARCHIVE_PAGE_SIZE,
    press: ARCHIVE_PAGE_SIZE,
    awards: ARCHIVE_PAGE_SIZE,
};

const state = {
    filter: filterFromHash(),
};

const updatePaneVisibility = () => {
    document.querySelectorAll<HTMLElement>("[data-filter-section]").forEach(pane => {
        pane.classList.toggle("hidden", pane.dataset.filterSection !== state.filter);
    });
};

const updateArchive = (filter: Filter) => {
    const pane = document.querySelector<HTMLElement>(`[data-filter-section="${filter}"]`);
    if (!pane) return;

    const items = Array.from(pane.querySelectorAll<HTMLElement>(".newsroom-archive-list li[data-archive-item]"));
    const visibleCount = Math.min(archiveVisible[filter], items.length);

    items.forEach((item, i) => {
        item.style.display = i < visibleCount ? "" : "none";
    });

    const loadMoreBtn = pane.querySelector<HTMLButtonElement>(".newsroom-load-more");
    loadMoreBtn?.classList.toggle("hidden", visibleCount >= items.length);

    const countEl = pane.querySelector<HTMLElement>(".newsroom-count");
    if (countEl) {
        countEl.textContent = items.length === 0
            ? ""
            : `Showing ${visibleCount} of ${items.length} archived items`;
    }
};

const updateView = () => {
    updatePaneVisibility();
    updateArchive(state.filter);

    // Empty-state message: shown if the active pane has neither a featured grid nor an archive list.
    const pane = document.querySelector<HTMLElement>(`[data-filter-section="${state.filter}"]`);
    const noResults = document.querySelector<HTMLElement>(".pulumi-newsroom-list-container .no-results");
    const hasContent = !!pane?.querySelector(".newsroom-featured-section, .newsroom-archive-section");
    noResults?.classList.toggle("hidden", hasContent);
};

const onHashChange = () => {
    const next = filterFromHash();
    if (next === state.filter) return;
    state.filter = next;
    archiveVisible[next] = ARCHIVE_PAGE_SIZE; // Reset to first page when filter changes.
    updateView();
    trackEvent("newsroom-filter", { filter: next });
};

const wireUpLoadMore = () => {
    document.querySelectorAll<HTMLButtonElement>(".newsroom-load-more").forEach(button => {
        const pane = button.closest<HTMLElement>("[data-filter-section]");
        const filter = pane?.dataset.filterSection as Filter | undefined;
        if (!filter || !isValidFilter(filter)) return;

        button.addEventListener("click", () => {
            archiveVisible[filter] += ARCHIVE_PAGE_SIZE;
            updateArchive(filter);
            trackEvent("newsroom-load-more", {
                filter,
                visible: archiveVisible[filter],
            });
            if (!button.classList.contains("hidden")) {
                button.focus();
            }
        });
    });
};

if (document.querySelector(".pulumi-newsroom-list-container")) {
    updateView();
    wireUpLoadMore();
    window.addEventListener("hashchange", onHashChange);
}
