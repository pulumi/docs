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
        $("h2, h3").each(function () {
            var $el = $(this);
            var id = $el.attr("id");
            var text = $el.text();
            var linkTitle = $el.data("link-title");
            var tag = $el.prop("tagName").toLowerCase();
            if (id && text) {
                found = true;
                $ul.append("<li class='" + tag + "'><a href='#" + id + "'>" + (linkTitle || text) + "</a></li>");
            }
        });

        // It's hidden by default. If we added links to the list, show it.
        if (found) {
            $(".on-this-page").show();
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
