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

    // Home-page carousel. Items cycle every four seconds. Clicking a label stops the
    // cycling and shows the selected item.
    var carouselIndex = 1;

    var carouselInterval = window.setInterval(function() {
        showCarouselItem(carouselIndex);
        carouselIndex++;

        if (carouselIndex > 2) {
            carouselIndex = 0;
        }
    }, 4000);

    $(".carousel-item-label").click(function() {
        clearInterval(carouselInterval);

        var i = $(".carousel-item-label").index(this);
        showCarouselItem(i);
    });

    function showCarouselItem(i) {
        $(".carousel-item")
            .css("opacity", 0)
            .eq(i)
            .css("opacity", 1);

        $(".carousel-item-label")
            .removeClass("border-b-2")
            .eq(i)
            .addClass("border-b-2");
    }

}(jQuery));
