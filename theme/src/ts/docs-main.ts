import { onPageEvent } from "./navigation";

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

    if ($(".section-docs .docs-list-main").length > 0) {
        if ($(".section-docs .docs-list-main").get(0).getBoundingClientRect().y <= 0) {
            mainNav.css("margin-top", docsTypeNavSearch.height() - Math.max($(".top-nav-container").get(0).getBoundingClientRect().y, 0));
            mainNavToggle.css("top", docsToggleOffset + docsTypeNavSearch.height() - Math.max($(".top-nav-container").get(0).getBoundingClientRect().y, 0));
        } else {
            mainNav.css("margin-top", 0);
        }
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

onPageEvent("load", () => {
    let docsToggle = $(".docs-nav-toggle");

    docsToggle.on("click", function () {
        docsMainNavToggleWrapper.toggleClass("docs-nav-show");
        docsMainNavToggleWrapper.toggleClass("docs-nav-hide");
        docsNavToggleIcon.toggleClass("close-docs-main-nav");
        docsNavToggleIcon.toggleClass("open-docs-main-nav");
        setTableOfContentsVisibility()
    });

    let collapseContentButton = $("#collapse-content-button");
    let expandContentButton = $("#expand-content-button");

    function expandContentWidth() {
        $(".docs-main-content").addClass("docs-content-width-expanded");

        collapseContentButton.removeClass("hide");
        expandContentButton.addClass("hide");
        window.localStorage.setItem("content-width-state", "expanded");
    }

    function collapseContentWidth() {
        $(".docs-main-content").removeClass("docs-content-width-expanded");
        collapseContentButton.addClass("hide");
        expandContentButton.removeClass("hide");
        window.localStorage.setItem("content-width-state", "collapsed");
    }

    function loadContentWidthState() {
        const contentWidthState = window.localStorage.getItem("content-width-state");
        if (contentWidthState === "expanded") {
            expandContentWidth();
        } else {
            collapseContentWidth();
        }
    }

    expandContentButton.on("click", expandContentWidth);
    collapseContentButton.on("click", collapseContentWidth);

    loadContentWidthState();
    setDocsMainNavPosition();
    setTableOfContentsVisibility();
    setMainNavHeight();

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
