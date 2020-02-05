function bindToggle(el) {
    $(".toggleButton", el).click(function() {
        if ($(this).closest(".toggle, .toggleVisible")[0] != el) {
            // Only trigger the closest toggle header.
            return;
        }

        if ($(el).is(".toggle")) {
            $(el).addClass("toggleVisible").removeClass("toggle");
        } else {
            $(el).addClass("toggle").removeClass("toggleVisible");
        }
    });
}

function bindToggles(selector) {
    $(selector).each(function(i, el) {
        bindToggle(el);
    });
}

function generateOnThisPage() {
    var $ul = $(".on-this-page > ul");
    if ($ul) {
        var found = false;
        var headings = [];

        $("h2, h3").each(function () {
            var $el = $(this);
            var id = $el.attr("id");
            var text = $el.text();
            var linkTitle = $el.data("link-title");
            var tag = $el.prop("tagName").toLowerCase();

            if (id && text) {
                found = true;
                var li = $("<li class='" + tag + "'><a href='#" + id + "'>" + (linkTitle || text) + "</a></li>");
                $ul.append(li);

                // Capture associated heading and list-item elements, so we can mark list
                // items active when they become visible.
                headings.push({
                    element: $el,
                    listItem: li,
                });
            }
        });

        // It's hidden by default. If we added links to the list, show it.
        if (found) {
            $(".on-this-page").show();

            // Highlight the first heading whose offset from top is greater than the current scroll
            // position, to best indicate your location within the page hierarchy.
            function setActiveItem() {
                var active;
                for (var heading of headings) {
                    if (!active && heading.element.offset().top >= window.scrollY) {
                        active = heading;
                    }
                    heading.listItem.toggleClass("font-bold", heading === active);
                }
            }

            $(window).on("scroll", function() {
                setActiveItem();
            });

            setActiveItem();
        }
    }
}

// Extracts a query string variable from the browser's location.
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");

    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");

        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    }
}

(function ($) {

    // Set up toggle functionality.
    bindToggles(".toggle");
    bindToggles(".toggleVisible");

    // Create "On This Page" in the right nav.
    generateOnThisPage();

    // Mobile menu toggles.
    $(".nav-header-toggle").click(function() {
        $(".nav-header-items").toggleClass("hidden");
    });
    $(".blog-sidebar-toggle").click(function () {
        $(".blog-sidebar-content").toggleClass("hidden");
    });

    // Shuffle lists that want to be shuffled.
    $("ul[data-shuffle='true']")
        .each(function(i, list) {
            var items = $(list).find("> li");

            items.each(function(i, item) {
                $(item).css("order", Math.ceil(Math.random() * items.length));
            });

            $(list).removeClass("invisible");
        });
}(jQuery));
