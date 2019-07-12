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

function generateMiniToc() {
    var toc = $(".mini-toc > ul");
    if (toc) {
        $("h2").each(function () {
            var id = $(this).attr("id");
            var text = $(this).text();
            if (id && text) {
                toc.append($("<li/>", {
                    html: "<a href='#" + id + "'>" + text + "</a>"
                }));
            }
        });
    }
}

(function ($) {

    // Set up toggle functionality.
    bindToggles(".toggle");
    bindToggles(".toggleVisible");

    // Create a mini TOC if desired.
    generateMiniToc();

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
