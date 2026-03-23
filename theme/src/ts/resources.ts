const filterResourceItems = (filters) => {
    const events = document.querySelectorAll<HTMLElement>(".event-list .event-card");
    const monthLabels = document.querySelectorAll<HTMLElement>(".event-list .month-label");
    monthLabels.forEach(el => el.style.display = "none");
    const noResultsMessage = document.querySelector(".pulumi-event-list-container .no-results");
    noResultsMessage?.classList.remove("hidden");

    if (filters.length > 0) {
        events.forEach(event => {
            const tags = (event.getAttribute("data-filters") || "").split(" ");
            const dateLabel = event.getAttribute("data-month-label");

            if (!tags.includes(location.hash.slice(1))) {
                event.style.display = "none";
            } else {
                let matches = 0;
                tags.forEach(tag => {
                    if (filters.includes(tag)) {
                        matches++;
                    }
                });
                if (matches > 0) {
                    noResultsMessage?.classList.add("hidden");
                    event.style.display = "block";
                    document.querySelectorAll<HTMLElement>(`.month-label.${dateLabel}`).forEach(el => el.style.display = "block");
                } else {
                    event.style.display = "none";
                }
            }
        });
    } else {
        events.forEach(event => {
            const tags = (event.getAttribute("data-filters") || "").split(" ");
            const dateLabel = event.getAttribute("data-month-label");

            if (!tags.includes(location.hash.slice(1))) {
                event.style.display = "none";
            } else {
                noResultsMessage?.classList.add("hidden");
                event.style.display = "block";
                document.querySelectorAll<HTMLElement>(`.month-label.${dateLabel}`).forEach(el => el.style.display = "block");
            }
        });
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
