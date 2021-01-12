/**
 * sortResourceItems sorts the visible items in the resource list.
 *
 * @param {bool} sortDescending Whether the items should be sorted in descending order.
 */
function sortResourceItems(sortDescending) {
    const resourceList = $("ul.resource-list");
    const items = resourceList.children("li");

    items.detach().sort(function(a,b) {
        const firstDate = $(a).attr("data-display-date");
        const secondDate = $(b).attr("data-display-date");

        if (sortDescending) {
            return new Date(firstDate).getTime() < new Date(secondDate).getTime() ? 1 : -1;
        }
        return new Date(firstDate).getTime() > new Date(secondDate).getTime() ? 1 : -1;
    });

    resourceList.append(items);
}

$(function() {
    const pathParts = location.pathname.split("/");
    if (pathParts.length > 1 && pathParts[1] === "resources") {
        window.addEventListener("hashchange", function() {
            const shouldSortDescending = location.hash !== "#upcoming";
            sortResourceItems(shouldSortDescending);
        });

        $(document).ready(function() {
            const shouldSortDescending = location.hash !== "#upcoming";
            sortResourceItems(shouldSortDescending);
        });
    }
});
