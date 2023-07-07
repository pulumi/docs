let docsMainNavToggleWrapper = $(".docs-main-nav-toggle-wrapper");
let docsNavToggleIcon = $(".docs-nav-toggle-icon");

$(window).on("resize", function () {
    setDocsMainNavPosition();
    setTableOfContentsVisibility();
    setMainNavHeight();
}).trigger('resize');

$(window).on("scroll", function () {
    setDocsMainNavPosition();
}).trigger('resize');

$(window).on("load", function() {
    setDocsMainNavPosition();
    setTableOfContentsVisibility();
    setMainNavHeight();
});

(function (document, $) {
    let docsToggle = $(".docs-nav-toggle");

    docsToggle.on("click", function () {
        docsMainNavToggleWrapper.toggleClass("docs-nav-show");
        docsMainNavToggleWrapper.toggleClass("docs-nav-hide");
        docsNavToggleIcon.toggleClass("close-docs-main-nav");
        docsNavToggleIcon.toggleClass("open-docs-main-nav");
        setTableOfContentsVisibility()
    });

    let packageCardCheckbox = $("#accordion-checkbox-package-card");
    let packageCardBackground = $("#accordion-package-card");

    packageCardCheckbox.on("change", function () {
        if (packageCardCheckbox.is(":checked")) {
            packageCardBackground.css("background", "#fff");
        }
        else {
            packageCardBackground.css("background", "#f9f9f9");
        }
    
    });
    

    function loadContentWidthState() {
        const contentWidthState = window.localStorage.getItem("content-width-state");
        if (contentWidthState === "expanded") {
            expandContentWidth();
        } else {
            collapseContentWidth();
        }
    }

    let collapseContentButton = $("#collapse-content-button")
    let expandContentButton = $("#expand-content-button")
    
    function expandContentWidth() {
        $(".docs-main-content").addClass("docs-content-width-expanded");
        if (window.location.pathname.startsWith("/registry")) {
            $(".docs-main-content").addClass("expand-registry");
        }
        $("#docs-home-banner").find("p").addClass("wider");
        $("#docs-home-banner").css("background-image", `url("/images/docs/docs-home-header-background-desktop-wide.svg")`);
        collapseContentButton.removeClass("hide");
        expandContentButton.addClass("hide");
        window.localStorage.setItem("content-width-state", "expanded");
    }

    function collapseContentWidth() {
        $(".docs-main-content").removeClass("docs-content-width-expanded");
        $("#docs-home-banner").find("p").removeClass("wider");
        $("#docs-home-banner").css("background-image", `url("/images/docs/docs-home-header-background-desktop.svg")`);
        collapseContentButton.addClass("hide");
        expandContentButton.removeClass("hide");
        window.localStorage.setItem("content-width-state", "collaped");
    }

    expandContentButton.on("click", expandContentWidth);
    collapseContentButton.on("click", collapseContentWidth);

    loadContentWidthState();
})(document, jQuery);

function setDocsMainNavPosition() {
    if ($(this).width() <= 1280) {
        if (docsMainNavToggleWrapper.hasClass("docs-nav-show")) {
            docsNavToggleIcon.removeClass("open-docs-main-nav")
            docsNavToggleIcon.addClass("close-docs-main-nav");
        } else if (docsMainNavToggleWrapper.hasClass("docs-nav-hide")) {
            docsNavToggleIcon.removeClass("close-docs-main-nav")
            docsNavToggleIcon.addClass("open-docs-main-nav");
        }
    } 

    let mainNav = $(".main-nav");
    let mainNavToggle = $(".docs-nav-toggle");
    let docsTypeNavSearch = $(".docs-type-nav-search");
    let docsToggleOffset = 94;

    if (document.getElementsByClassName("docs-list-main").length > 0) {
        if ($(".docs-list-main").get(0).getBoundingClientRect().y <= 0) {
            mainNav.css("margin-top", docsTypeNavSearch.height() - Math.max($(".top-nav-container").get(0).getBoundingClientRect().y, 0));
            mainNavToggle.css("top", docsToggleOffset + docsTypeNavSearch.height() - Math.max($(".top-nav-container").get(0).getBoundingClientRect().y, 0));
        } else {
            mainNav.css("margin-top", 0);
        }
    }

    if ($(this).width() > 1280) {
        docsMainNavToggleWrapper.removeClass("docs-nav-show");
        docsMainNavToggleWrapper.removeClass("docs-nav-hide");   
    } else if (!docsMainNavToggleWrapper.hasClass("docs-nav-hide") && !docsMainNavToggleWrapper.hasClass("docs-nav-show")) {
        docsMainNavToggleWrapper.addClass("docs-nav-hide");
    }
}

function setTableOfContentsVisibility() {
    let docsTableOfContents = $(".docs-toc-desktop");

    if (window.innerWidth > 1024 && window.innerWidth <= 1280) {
        if (docsMainNavToggleWrapper.hasClass("docs-nav-show")) {
            docsTableOfContents.hide();
        } else {
            docsTableOfContents.show();
        }
    } else if (window.innerWidth > 1280) {
        docsTableOfContents.show();
    } else {
        docsTableOfContents.hide();
    }
}

function setMainNavHeight() {
    $(".docs-main-nav").css("height",  $(".docs-footer").height() + window.innerHeight);
}
