const filterResourceItems = (filters) => {
    const monthGroups = document.querySelectorAll<HTMLElement>(".event-list .month-label");
    const separator = document.querySelector<HTMLElement>(".event-list .event-list-separator");
    const noResultsMessage = document.querySelector(".template-event-list .no-results");
    noResultsMessage?.classList.remove("hidden");

    const activeTab = location.hash.slice(1) || "all";

    monthGroups.forEach(group => {
        const groupFilters = (group.getAttribute("data-filters") || "").split(" ");

        // For the "all" tab, show all groups. Otherwise, only show matching tab.
        if (activeTab !== "all" && !groupFilters.includes(activeTab)) {
            group.style.display = "none";
            return;
        }

        const cards = group.querySelectorAll<HTMLElement>("li[data-filters]");
        let visibleCards = 0;

        cards.forEach(card => {
            const tags = (card.getAttribute("data-filters") || "").split(" ");

            if (filters.length > 0) {
                const matches = filters.some(f => tags.includes(f));
                if (matches) {
                    card.style.display = "";
                    visibleCards++;
                } else {
                    card.style.display = "none";
                }
            } else {
                card.style.display = "";
                visibleCards++;
            }
        });

        group.style.display = visibleCards > 0 ? "block" : "none";
        if (visibleCards > 0) {
            noResultsMessage?.classList.add("hidden");
        }
    });

    // Show separator only on "all" tab when no filters are active.
    if (separator) {
        separator.style.display = (activeTab === "all" && filters.length === 0) ? "" : "none";
    }
}

document.querySelector(".pulumi-event-list-container")?.addEventListener("filterSelect", (event: CustomEvent) => {
    const filters = event.detail as any[];
    const filtersText: string[] = [];

    filters.forEach(filter => {
        filtersText.push(filter.value);
    });

    filterResourceItems(filtersText);
});

window.addEventListener('hashchange', function() {
    const options = Array.from(document.querySelectorAll('pulumi-filter-select-option')) as any[];
    let selectedFilters = [];

    options.forEach((option) => {
        const shadow = option.shadowRoot;
        if (shadow?.querySelector('.selected')) {
            selectedFilters.push(option.value);
        }
    });
    filterResourceItems(selectedFilters);
});

// Apply initial filter state on page load.
if (document.querySelector(".template-event-list")) {
    filterResourceItems([]);
}
