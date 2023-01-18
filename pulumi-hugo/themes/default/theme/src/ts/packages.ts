const filterByTextAndTags = (filters, filterText) => {
    // We custom match these so that if someone searches "amazon" they also get all
    // the "aws" results and vice versa, same for Google Cloud.
    const AMAZON_STRING: string = "amazon";
    const AWS_STRING: string = "aws";
    const GOOGLE_CLOUD_STRING: string = "gcp";
    const GCP_STRING: string = "google cloud";
    const GOOGLE_STRING: string = "google";

    const packages = $(".all-packages").find(".package");

    const noSelectedType = filters.find(f => f.group === "type") === undefined;
    const noSelectedCategory = filters.find(f => f.group === "category") === undefined;

    // Even if we have 0 filters or no filter text, if the other still exists, we
    // still need to show a filtered list of results.
    if (filters.length > 0 || filterText) {
        $(packages).addClass("hidden");

        $(packages).each((i, package) => {
            const el = $(package).find("[data-category]");

            const packageType = el.attr("data-type");
            const packageCategory = el.attr("data-category");
            const packageIsNative = packageType === "native-provider";

            const packageHasSelectedType =
                !!filters.find(f => f.group === "type" && f.value === packageType) || (filters.find(f => f.group === "type" && f.value === "provider") && packageIsNative);
            const packageHasSelectedCategory = !!filters.find(f => f.group === "category" && f.value === packageCategory);

            const packageTitle = el.attr("data-title");
            const downcasedPackageTitle = packageTitle.toLowerCase();
            const downcasedFilterText = filterText?.trim().toLowerCase();

            let packageIsAMatch;

            if (downcasedFilterText === AMAZON_STRING || downcasedFilterText === AWS_STRING){
                packageIsAMatch = downcasedPackageTitle.includes(AMAZON_STRING) || downcasedPackageTitle.includes(AWS_STRING);
            } else if (downcasedFilterText === GOOGLE_CLOUD_STRING || downcasedFilterText === GCP_STRING || downcasedFilterText === GOOGLE_STRING){
                packageIsAMatch = downcasedPackageTitle.includes(GOOGLE_CLOUD_STRING) || downcasedPackageTitle.includes(GCP_STRING) || downcasedPackageTitle.includes(GOOGLE_STRING);
            } else {
                packageIsAMatch = downcasedPackageTitle.includes(downcasedFilterText);
            }

            /**
                Show the package if it matches any of the selected filters. For example:

                * If type Component and type Provider are selected, show packages that are
                  tagged as either "component" OR "provider", since those two filters belong
                  to the same option group.

                * If type Component and use-case Cloud are selected, show packages that
                  are tagged as both "component" AND "cloud", since those two filters
                  belong to different option groups.

                * If nothing is selected from a given group, assume the intent is to see
                  everything in that group (so don't apply any of the filters within it).

                * If there is text to filter on, only show packages that meet the above criteria
                  AND match the filter text.  If there is no text, show the full matching package list.
             */
            if ((packageHasSelectedType || noSelectedType) && (packageHasSelectedCategory || noSelectedCategory) && (!filterText || packageIsAMatch)) {
                $(package).removeClass("hidden");
            }
        });
    } else {
        $(packages).removeClass("hidden");
    }
}

$(".section-registry").on("filterSelect", event => {
    const source: any = event.target;
    const detail: unknown = event.detail;
    const filters = detail as any[];


    // We need to cross reference the search input when filter change, so that
    // users get the combined results of the two mechanisms.
    const searchElement = $("pulumi-registry-list-search").get(0) as any;
    const inputElement = $(searchElement).find('.registry-filter-input');
    const filterText = inputElement.val() as string;

    filterByTextAndTags(filters, filterText);

    // Update the list of active filters.
    const activeTags = $("ul.active-tags");
    activeTags.empty();

    filters.forEach(filter => {
        const tag = $($("#active-tag-template").html());
        tag.appendTo(activeTags);
        tag.attr("data-filter-group", filter.group).attr("data-filter-value", filter.value);
        tag.find("span").text(filter.label);
        tag.find("button").on("click", () => source.deselect(filter));
    });

    // Apply selections on the DOM, so cards and tags can use them as well.
    $(".packages, .active-tags")
        .attr(
            "data-selected-types",
            filters
                .filter(f => f.group === "type")
                .map(t => t.value)
                .join(","),
        )
        .attr(
            "data-selected-categories",
            filters
                .filter(f => f.group === "category")
                .map(t => t.value)
                .join(","),
        );

    // Update the count-badge value.
    const allCount = $(".all-packages .package:not(.hidden)").length;
    $(".all-count").text(allCount);

    // Close the menu.
    $("pulumi-filter-select-option-group").each((i, el: any) => el.close());
});

$(".section-registry .no-results .reset").on("click", event => {
    event.stopPropagation();

    const search = $("pulumi-registry-list-search").get(0) as any;
    search.reset();

    const fs = $("pulumi-filter-select").get(0) as any;
    fs.reset();

    filterByTextAndTags([], "");

    // Update the count-badge value.
    const allCount = $(".all-packages .package:not(.hidden)").length;
    $(".all-count").text(allCount);
});

$(".section-registry").on("packageSearch", event => {
    const filterText = event.detail as any;
   
    // We need to cross reference the filter tags when search changes, so that
    // users get the combined results of the two mechanisms.
    const filters = [];
    const activeTags = $("ul.active-tags").find("li");

    if (activeTags.length > 0){
        activeTags.each((i, tag) => {
            const el = $(tag);
            const tagCategory = el.attr("data-filter-group");
            const tagValue = el.attr("data-filter-value");
            const tagLabel = el.attr("data-filter-label");

            filters.push({group: tagCategory, value: tagValue, label: tagLabel})
        })
    };

    filterByTextAndTags(filters, filterText);

    // Update the count-badge value.
    const allCount = $(".all-packages .package:not(.hidden)").length;
    $(".all-count").text(allCount);
});


document.addEventListener("DOMContentLoaded", function () {
    const logoNavMenuButton = $(".logo-nav-button");
    const bgMask = $(".logo-nav-bg-mask");
    const logoNavMenu = $("#logo-nav-menu");

    function toggleMenu() {
        logoNavMenu.toggleClass("hidden");
        const navMenuVisible = logoNavMenu.is(":visible");
        logoNavMenuButton.attr("aria-expanded", `${navMenuVisible}`);
        $(".logo-nav-button .mobile-menu-toggle-icon").toggleClass("hidden");
        bgMask.toggleClass("hidden");
    }

    logoNavMenuButton.on("click", toggleMenu);
    // This handles closing the menu when selecting outside for Registry.
    bgMask.on("click", toggleMenu);

    // This handles closing the menu when selecting outside for non-Registry.
    $(document).on("click", function (event) {
        if ($(event.target).closest(logoNavMenuButton).length === 0 &&
            $(event.target).closest(logoNavMenu).length === 0 &&
            logoNavMenu.is(":visible")) {
            toggleMenu();
        }
    });

    // Close the menu when the page is scrolled past point where the
    // practitioner nav is replaced with the sticky search nav.
    $(document).on("scroll", function () {
        const PRACTITIONER_NAV_HEIGHT = 53;
        const scrollY = window.scrollY;
        if (scrollY > PRACTITIONER_NAV_HEIGHT && logoNavMenu.is(":visible")) {
            toggleMenu();
        }
    });
});

(function (document, $) {
    function rotateCaret(direction) {
        if (direction === "up") {
            $(".package-card-caret").removeClass("fa-chevron-circle-down")
            $(".package-card-caret").addClass("fa-chevron-circle-up")
        }
        if (direction === "down") {
            $(".package-card-caret").removeClass("fa-chevron-circle-up")
            $(".package-card-caret").addClass("fa-chevron-circle-down")
        }
    }

    // Controls the expanding and collapsing of the package card.
    let expanded = true;
    $(".package-card-compact").click(function() {
        if(expanded) {
            $(".package-card-expand").show()
            $(".package-card-compact").removeClass("bg-gray-100")
            $(".package-card-compact").addClass("package-card-compact-expanded")
            rotateCaret("up")
        } else {
            $(".package-card-expand").hide()
            $(".package-card-compact").addClass("bg-gray-100")
            $(".package-card-compact").removeClass("package-card-compact-expanded")
            rotateCaret("down")
        }
        expanded = !expanded
    })

    // Moves the package card slightly down once the search bar
    // starts to overlap it.
    $(window).scroll(function () {
        // 80 is the scroll position where the search bar starts
        // to overlap the package card.
        if ($(window).scrollTop() > 80) {
            $(".package-card").css("margin-top","55px");
        } else {
            $(".package-card").css("margin-top","0px");
        }
    });

})(document, jQuery);