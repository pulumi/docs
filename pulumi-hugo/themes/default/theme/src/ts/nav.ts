import {LocalStorageService} from "./state";

(function (document, $) {
    // The main navigation bar. Binds handlers for showing and hiding
    // the big purple submenu on non-touch devices.

    var isTouchDevice = "ontouchstart" in document;

    if (!isTouchDevice) {
        $(".nav-header-items li a").mouseenter(function (event) {
            var item = $(event.target).data("submenu");
            $(".submenu-item").hide();
            $(".submenu-item-" + item).show();
        });

        $(".submenu").mouseleave(function (event) {
            // Only hide the submenu if the mouse moves to an element that
            // isn't the main menu.
            if (event.relatedTarget !== $("nav.nav-main").get(0)) {
                $(".submenu-item").hide();
            }
        });
    }

    // Handlers for mobile navigation menus.
    (function () {
        let whyPulumiOpened = false;
        let learnOpened = false;

        $("#why-pulumi-menu-label").click(function() {
            $("#mobile-dropdown").scroll();
            if (whyPulumiOpened) {
                $("#mobile-dropdown").animate({
                    scrollTop: top
                }, 300);
            } else {
                $("#mobile-dropdown").animate({
                    scrollTop: $("#why-pulumi-mobile-menu").position().top - 115
                }, 300);
            }
            whyPulumiOpened = !whyPulumiOpened;
        });
    
        $("#learn-menu-label").click(function() {
            $("#mobile-dropdown").scroll();
            if (learnOpened) {
                $("#mobile-dropdown").animate({
                    scrollTop: top
                }, 300);
            } else {
                $("#mobile-dropdown").animate({
                    scrollTop: $("#learn-mobile-menu").position().top - 115
                }, 300);
            }
            learnOpened = !learnOpened;
        });
    })();

    // track banner state in local storage.
    const bannerState = new LocalStorageService("banner-state");
    const banner = $("#dismissable-banner");
    loadBannerState();

    // load saved state of the banner from local storage.
    function loadBannerState() {
        if (bannerState.getKey("dismissed") !== "true") {
            $(banner).css({"display": "block"});
        } else {
            $(banner).css({"display": "none"});
        }
    }

    // click handler for banner dismiss button.
    $("#dismiss-banner").on("click", function (e) {
        // intercept href event, so we don't navigate to the link.
        e.preventDefault();
        
        $(banner).css({"display": "none"});
        bannerState.updateKey("dismissed", "true");
    })

})(document, jQuery);
