function setDocsMainNavPosition() {
    const docsMainNavToggleWrapper = document.querySelector(".docs-main-nav-toggle-wrapper");
    const docsNavToggleIcon = document.querySelector(".docs-nav-toggle-icon");

    if (window.innerWidth <= 1024) {
        if (docsMainNavToggleWrapper?.classList.contains("docs-nav-show")) {
            docsNavToggleIcon?.classList.remove("open-docs-main-nav");
            docsNavToggleIcon?.classList.add("close-docs-main-nav");
        } else if (docsMainNavToggleWrapper?.classList.contains("docs-nav-hide")) {
            docsNavToggleIcon?.classList.remove("close-docs-main-nav");
            docsNavToggleIcon?.classList.add("open-docs-main-nav");
        }
    }

    const mainNav = document.querySelector<HTMLElement>(".main-nav");
    const mainNavToggle = document.querySelector<HTMLElement>(".docs-nav-toggle");
    const docsTypeNavSearch = document.querySelector<HTMLElement>(".docs-type-nav-search");
    const docsToggleOffset = 94;

    const docsListMain = document.querySelector(".section-docs .docs-list-main") as HTMLElement;
    if (docsListMain) {
        const topNavContainer = document.querySelector(".top-nav-container") as HTMLElement;
        if (docsListMain.getBoundingClientRect().y <= 0) {
            const searchHeight = docsTypeNavSearch?.offsetHeight || 0;
            const topNavY = topNavContainer ? Math.max(topNavContainer.getBoundingClientRect().y, 0) : 0;
            if (mainNav) mainNav.style.marginTop = (searchHeight - topNavY) + "px";
            if (mainNavToggle) mainNavToggle.style.top = (docsToggleOffset + searchHeight - topNavY) + "px";
        } else {
            if (mainNav) mainNav.style.marginTop = "0";
        }
    }

    if (window.innerWidth > 1024) {
        docsMainNavToggleWrapper?.classList.remove("docs-nav-show");
        docsMainNavToggleWrapper?.classList.remove("docs-nav-hide");
    } else if (!docsMainNavToggleWrapper?.classList.contains("docs-nav-hide") && !docsMainNavToggleWrapper?.classList.contains("docs-nav-show")) {
        docsMainNavToggleWrapper?.classList.add("docs-nav-hide");
    }
}

function setTableOfContentsVisibility() {
    const docsTableOfContents = document.querySelector<HTMLElement>(".docs-toc-desktop");
    if (docsTableOfContents) {
        docsTableOfContents.style.display = window.innerWidth < 1280 ? "none" : "";
    }
}

function setMainNavHeight() {
    const docsMainNav = document.querySelector<HTMLElement>(".docs-main-nav");
    const docsFooter = document.querySelector<HTMLElement>(".docs-footer");
    if (docsMainNav && docsFooter) {
        docsMainNav.style.height = (docsFooter.offsetHeight + window.innerHeight) + "px";
    }
}

function handleResize() {
    setDocsMainNavPosition();
    setTableOfContentsVisibility();
    setMainNavHeight();
}

window.addEventListener("resize", handleResize);
window.addEventListener("scroll", setDocsMainNavPosition);
window.addEventListener("load", handleResize);
handleResize();

(function () {
    const docsMainNavToggleWrapper = document.querySelector(".docs-main-nav-toggle-wrapper");
    const docsNavToggleIcon = document.querySelector(".docs-nav-toggle-icon");

    document.querySelector(".docs-nav-toggle")?.addEventListener("click", function () {
        docsMainNavToggleWrapper?.classList.toggle("docs-nav-show");
        docsMainNavToggleWrapper?.classList.toggle("docs-nav-hide");
        docsNavToggleIcon?.classList.toggle("close-docs-main-nav");
        docsNavToggleIcon?.classList.toggle("open-docs-main-nav");
        setTableOfContentsVisibility();
    });

    const packageCardCheckbox = document.getElementById("accordion-checkbox-package-card") as HTMLInputElement;
    const packageCardBackground = document.getElementById("accordion-package-card") as HTMLElement;

    if (packageCardCheckbox && packageCardBackground) {
        packageCardCheckbox.addEventListener("change", function () {
            packageCardBackground.style.background = packageCardCheckbox.checked ? "#fff" : "#f9f9f9";
        });
    }

    function loadContentWidthState() {
        const contentWidthState = window.localStorage.getItem("content-width-state");
        if (contentWidthState === "expanded") {
            expandContentWidth();
        } else {
            collapseContentWidth();
        }
    }

    const collapseContentButton = document.getElementById("collapse-content-button");
    const expandContentButton = document.getElementById("expand-content-button");

    function expandContentWidth() {
        document.querySelectorAll(".docs-main-content").forEach(el => {
            el.classList.add("docs-content-width-expanded");
            if (window.location.pathname.startsWith("/registry")) {
                el.classList.add("expand-registry");
            }
        });
        collapseContentButton?.classList.remove("hide");
        expandContentButton?.classList.add("hide");
        window.localStorage.setItem("content-width-state", "expanded");
    }

    function collapseContentWidth() {
        document.querySelectorAll(".docs-main-content").forEach(el => {
            el.classList.remove("docs-content-width-expanded");
        });
        collapseContentButton?.classList.add("hide");
        expandContentButton?.classList.remove("hide");
        window.localStorage.setItem("content-width-state", "collapsed");
    }

    expandContentButton?.addEventListener("click", expandContentWidth);
    collapseContentButton?.addEventListener("click", collapseContentWidth);

    loadContentWidthState();
})();
