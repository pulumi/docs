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
    //----------------------------------------
    // Essentials
    //----------------------------------------
    var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

    // Set up toggle functionality.
    bindToggles(".toggle");
    bindToggles(".toggleVisible");

    // Create a mini TOC if desired.
    generateMiniToc();

    // breakpoints
    var $screen_xxs = 320;
    var $screen_xs = 480;
    var $screen_sm = 576;
    var $screen_md = 768;
    var $screen_lg = 991;
    var $screen_xlg = 1200;

    // find out if is touch device
    function is_touch_device() {
        return (('ontouchstart' in window)
            || (navigator.MaxTouchPoints > 0)
            || (navigator.msMaxTouchPoints > 0));
        //navigator.msMaxTouchPoints for microsoft IE backwards compatibility
    }

    // Add slideDown animation to Bootstrap dropdown when expanding.
    $('.dropdown:not(.main-nav-wrapper-wrapper)').on('show.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

    // Add slideUp animation to Bootstrap dropdown when collapsing.
    $('.dropdown:not(.main-nav-wrapper-wrapper)').on('hide.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });

    // mobile dropdown
    $('.main-header .dropdown').on('show.bs.dropdown', function () {
        var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        if (windowWidth < $screen_md) {
            $('body').addClass('no-scroll');
        }
    }).on('hide.bs.dropdown', function () {
        $('body').removeClass('no-scroll');
    });

    var originalWindowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    $(window).resize(function () {
        var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

        //prevent functions from recalculating on scroll on mobile. when scrolling on iphone, the bottom appears/disappears and the browser thinks this is resizing
        //execute these functions on width resize only
        if (windowWidth != originalWindowWidth) { //if width resized
        }
    });
}(jQuery));
