const filterResourceItems = (filters) => {
    const events = $(".event-list").find(".event-card");
    const monthLabels = $(".event-list").find(".month-label");
    $(monthLabels).css("display", "none")
    const noResultsMessage = $(".pulumi-event-list-container").find(".no-results");
    $(noResultsMessage).removeClass("hidden");

    if (filters.length > 0) {
        $(events).each((i, event) => {
            const tags = ($(event).attr("data-filters")).split(" ");
            const dateLabel = $(event).attr("data-month-label");

            if (!tags.includes(location.hash.slice(1))) {
                $(event).css("display", "none");
            } else {
                let matches = 0;
                tags.forEach(tag => {
                    if (filters.includes(tag)) {
                        matches++;
                    }
                });
                if (matches > 0) {
                    $(noResultsMessage).addClass("hidden");
                    $(event).css("display", "block");
                    $(`.month-label.${dateLabel}`).css("display", "block");
                } else {
                    $(event).css("display", "none");
                }
            }
        });
    } else {
        $(events).each((i, event) => {
            const tags = ($(event).attr("data-filters")).split(" ");
            const dateLabel = $(event).attr("data-month-label");

            if (!tags.includes(location.hash.slice(1))) {
                $(event).css("display", "none");
                const dateLabel = $(event).attr("data-month-label");
            } else {
                $(noResultsMessage).addClass("hidden");
                $(event).css("display", "block");
                $(`.month-label.${dateLabel}`).css("display", "block");
            }
        });
    }
}

$(".pulumi-event-list-container").on("filterSelect", event => {
    const detail: unknown = event.detail;
    const filters = detail as any[];
    const filtersText: string[] = [];

    filters.forEach(filter => {
        filtersText.push(filter.value);
    });

    filterResourceItems(filtersText);
});

$(window).on('hashchange', function() {
    const options = $('pulumi-filter-select-option').toArray() as Array<any>;
    let selectedFilters = [];

    options.forEach((option) => {
        const shadow = option.shadowRoot;
        if($(shadow).find('.selected').length > 0) {
            selectedFilters.push(option.value);
        }
    })
    filterResourceItems(selectedFilters);
});

$(function () {
    const resourcesEventListFilterNav = document.getElementById("event-list-filter-nav");
    if (resourcesEventListFilterNav) {
        // When the arrows are selected, they scroll the tertiary nav in either direction.
        $("#slideForward").on("click", function () {
            // The width of an individual tab, so the scroll brings one additional full tab into view.
            resourcesEventListFilterNav.scrollLeft += 180;
        });

        $("#slideBackwards").on("click", function () {
            // The width of an individual tab, so the scroll moves one full tab into view.
            resourcesEventListFilterNav.scrollLeft -= 180;
        });

        // If the last or first items are fully in view (depending on the scroll direction),
        // the scroll arrow button is hidden from view (since it's no longer possible to scroll).
        const options = {
            root: document.getElementById("event-list-filter-nav"),
            // To count as in view, the tab must be 100% in view.
            threshold: 1.0,
        };

        const controlScrollForwardVisibility = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    $("#slideForward").addClass("hidden");
                } else {
                    $("#slideForward").removeClass("hidden");
                }
            });
        };

        const scrollForwardObserver = new IntersectionObserver(controlScrollForwardVisibility, options);
        const lastNavItem = document.querySelector("#event-list-filter-nav li:last-of-type");
        scrollForwardObserver.observe(lastNavItem);

        const controlScrollBackwardVisibility = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    $("#slideBackwards").addClass("hidden");
                } else {
                    $("#slideBackwards").removeClass("hidden");
                }
            });
        };
        const scrollBackwardObserver = new IntersectionObserver(controlScrollBackwardVisibility, options);
        const firstNavItem = document.querySelector("#event-list-filter-nav li:first-of-type");
        scrollBackwardObserver.observe(firstNavItem);
    }
});
