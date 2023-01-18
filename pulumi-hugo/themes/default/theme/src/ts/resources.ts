/**
 * sortResourceItems sorts the visible items in the resource list.
 *
 * @param {bool} sortDescending Whether the items should be sorted in descending order.
 */
function sortResourceItems(sortDescending) {
    const resourceList = $("ul.resource-list");
    const items = resourceList.children("li").detach();

    Array.from(items).sort(function (a, b) {
        const firstDate = $(a).attr("data-display-date");
        const secondDate = $(b).attr("data-display-date");

        if (sortDescending) {
            return new Date(firstDate).getTime() < new Date(secondDate).getTime() ? 1 : -1;
        }
        return new Date(firstDate).getTime() > new Date(secondDate).getTime() ? 1 : -1;
    });

    resourceList.append(items);
}

$(function () {
    const pathParts = location.pathname.split("/");
    if (pathParts.length > 1 && pathParts[1] === "resources") {
        window.addEventListener("hashchange", function () {
            const shouldSortDescending = location.hash !== "#upcoming";
            sortResourceItems(shouldSortDescending);
        });

        $(document).ready(function () {
            const shouldSortDescending = location.hash !== "#upcoming";
            sortResourceItems(shouldSortDescending);
        });
    }
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