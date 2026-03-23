const filterResourceItems = (filters) => {
    const monthGroups = document.querySelectorAll<HTMLElement>(".event-list .month-label");
    const noResultsMessage = document.querySelector(".template-event-list .no-results");
    noResultsMessage?.classList.remove("hidden");

    const activeTab = location.hash.slice(1) || "upcoming";

    monthGroups.forEach(group => {
        const groupFilters = (group.getAttribute("data-filters") || "").split(" ");

        // Hide groups not matching the active tab.
        if (!groupFilters.includes(activeTab)) {
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

document.addEventListener("DOMContentLoaded", function () {
    const resourcesEventListFilterNav = document.getElementById("event-list-filter-nav");
    if (resourcesEventListFilterNav) {
        document.getElementById("slideForward")?.addEventListener("click", function () {
            resourcesEventListFilterNav.scrollLeft += 180;
        });

        document.getElementById("slideBackwards")?.addEventListener("click", function () {
            resourcesEventListFilterNav.scrollLeft -= 180;
        });

        const options = {
            root: resourcesEventListFilterNav,
            threshold: 1.0,
        };

        const controlScrollForwardVisibility = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    document.getElementById("slideForward")?.classList.add("hidden");
                } else {
                    document.getElementById("slideForward")?.classList.remove("hidden");
                }
            });
        };

        const scrollForwardObserver = new IntersectionObserver(controlScrollForwardVisibility, options);
        const lastNavItem = document.querySelector("#event-list-filter-nav li:last-of-type");
        if (lastNavItem) scrollForwardObserver.observe(lastNavItem);

        const controlScrollBackwardVisibility = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    document.getElementById("slideBackwards")?.classList.add("hidden");
                } else {
                    document.getElementById("slideBackwards")?.classList.remove("hidden");
                }
            });
        };
        const scrollBackwardObserver = new IntersectionObserver(controlScrollBackwardVisibility, options);
        const firstNavItem = document.querySelector("#event-list-filter-nav li:first-of-type");
        if (firstNavItem) scrollBackwardObserver.observe(firstNavItem);
    }
});
