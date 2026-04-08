import {LocalStorageService} from "./state";


const navigationState = new LocalStorageService("navigation-toggle-state");
loadToggleStates();

function bindToggle(el: HTMLElement) {
    el.querySelectorAll(".toggleButton").forEach(btn => {
        btn.addEventListener("click", function () {
            if (this.closest(".toggle, .toggleVisible") !== el) {
                return;
            }

            if (el.classList.contains("toggle")) {
                el.classList.add("toggleVisible");
                el.classList.remove("toggle");
            } else {
                el.classList.add("toggle");
                el.classList.remove("toggleVisible");
            }
        });
    });
}

function loadToggleStates() {
    const isCurrentPage = (el: HTMLElement) => {
        const browserUrl = window.location.href;
        const anchor = el.querySelector('a');
        const anchorRef = anchor ? anchor.getAttribute('href') : '';
        return browserUrl.includes(anchorRef);
    };

    document.querySelectorAll(".toggle-topLevel, .toggleVisible-topLevel").forEach((el: HTMLElement) => {
        if (navigationState.getKey(el.id) == "expanded" || isCurrentPage(el)) {
            el.classList.add("toggleVisible");
            el.classList.remove("toggle");
        } else if (navigationState.getKey(el.id) == "collapsed") {
            el.classList.add("toggle");
            el.classList.remove("toggleVisible");
        }

        el.addEventListener("click", function () {
            const folderOpenIcon = el.querySelector(".folder-open");
            const folderClosedIcon = el.querySelector(".folder");
            if (folderOpenIcon) {
                folderOpenIcon.classList.add("folder");
                folderOpenIcon.classList.remove("folder-open");
            } else if (folderClosedIcon) {
                folderClosedIcon.classList.add("folder-open");
                folderClosedIcon.classList.remove("folder");
            }
        });
    });

    document.querySelectorAll(".toggleVisible, .toggleVisible-topLevel").forEach((el: HTMLElement) => {
        if (isCurrentPage(el)) {
            const leftNav = document.getElementById("left-nav");
            if (leftNav) {
                leftNav.scrollTop = el.offsetTop - 145;
            }
        }
    });
}

function updateToggleState(el: HTMLElement, toggleState: string) {
    navigationState.updateKey(el.id, toggleState)
}

function bindTopLevelToggle(el: HTMLElement) {
    el.querySelectorAll(".toggleButton-topLevel").forEach(btn => {
        btn.addEventListener("click", function () {
            if (this.closest(".toggle-topLevel, .toggleVisible-topLevel") !== el) {
                return;
            }

            if (el.classList.contains("toggle")) {
                el.classList.add("toggleVisible");
                el.classList.remove("toggle");
                updateToggleState(el, "expanded");
            } else {
                el.classList.add("toggle");
                el.classList.remove("toggleVisible");
                updateToggleState(el, "collapsed");
            }
        });
    });
}

function bindTopLevelToggles(selector: string) {
    document.querySelectorAll(selector).forEach((el: HTMLElement) => {
        bindTopLevelToggle(el);
    });
}

function bindToggles(selector: string) {
    document.querySelectorAll(selector).forEach((el: HTMLElement) => {
        bindToggle(el);
    });
}

export function generateOnThisPage() {
    const tocs = document.querySelectorAll<HTMLElement>(".table-of-contents");
    tocs.forEach(toc => toc.style.display = "none");

    const uls = document.querySelectorAll(".table-of-contents .content ul.table-of-contents-list");
    if (uls.length === 0) return;

    let found = false;
    const headingItems: { element: HTMLElement, listItems: HTMLElement[] }[] = [];

    document.querySelectorAll("h2, h3").forEach((el: HTMLElement) => {
        if (el.closest('.hidden')) {
            return;
        }
        const id = el.getAttribute("id");
        const text = el.textContent;
        const linkTitle = el.dataset.linkTitle;
        const tag = el.tagName.toLowerCase();

        if (id && text) {
            found = true;
            const listItems: HTMLElement[] = [];
            uls.forEach(ul => {
                const li = document.createElement("li");
                li.className = tag;
                const a = document.createElement("a");
                a.href = '#' + id;
                a.textContent = linkTitle || text;
                li.appendChild(a);
                ul.appendChild(li);
                listItems.push(li);
            });

            headingItems.push({ element: el, listItems });
        }
    });

    if (found) {
        tocs.forEach(toc => toc.style.display = "");

        const setActiveItem = () => {
            let active = null;
            for (const heading of headingItems) {
                if (!active && heading.element.offsetTop >= window.scrollY) {
                    active = heading;
                }
                heading.listItems.forEach(li => li.classList.toggle("active", heading === active));
            }
        };

        window.addEventListener("scroll", setActiveItem);
        setActiveItem();
    }
}

(function () {
    const observer = new IntersectionObserver(
        ([e]) => {
            e.target.classList.toggle("is-pinned", e.intersectionRatio < 1);
            const pinnedSearchContainerEl = document.querySelector(".header-pinned") as HTMLElement;
            const dotOverlay = document.querySelector(".hide-on-pinned") as HTMLElement;
            const heroTitle = document.querySelector(".header-hero-title") as HTMLElement;

            if (e.isIntersecting) {
                pinnedSearchContainerEl?.classList.add("hidden");
                pinnedSearchContainerEl?.classList.remove("flex");

                dotOverlay?.classList.remove("hidden");
                dotOverlay?.classList.add("flex");

                heroTitle?.classList.remove("hidden");
                heroTitle?.classList.add("flex");

            } else {
                pinnedSearchContainerEl?.classList.remove("hidden");
                pinnedSearchContainerEl?.classList.add("flex");

                dotOverlay?.classList.add("hidden");
                dotOverlay?.classList.remove("flex");

                heroTitle?.classList.add("hidden");
                heroTitle?.classList.remove("flex");

            }
        },
        { threshold: [1] },
    );

    const headerContainerEl = document.querySelector(".header-container");
    if (!headerContainerEl) {
        const registryNavBar = document.querySelector(".top-nav-bar.registry");
        if (registryNavBar) {
            observer.observe(registryNavBar);
        }
    } else {
        observer.observe(headerContainerEl);
    }

    bindToggles(".toggle");
    bindToggles(".toggleVisible");

    bindTopLevelToggles(".toggle-topLevel");
    bindTopLevelToggles(".toggleVisible-topLevel");

    generateOnThisPage();

    document.querySelector(".nav-header-toggle")?.addEventListener("click", () => {
        document.querySelector(".nav-header-items")?.classList.toggle("hidden");
    });
    document.querySelector(".blog-sidebar-toggle")?.addEventListener("click", () => {
        document.querySelector(".blog-sidebar-content")?.classList.toggle("hidden");
    });
    document.querySelector(".docs-sidebar-toggle")?.addEventListener("click", () => {
        document.querySelector(".docs-sidebar-content")?.classList.toggle("hidden");
    });

    document.querySelectorAll("ul[data-shuffle='true']").forEach((list: HTMLElement) => {
        const items = list.querySelectorAll(":scope > li") as NodeListOf<HTMLElement>;
        items.forEach(item => {
            item.style.order = String(Math.ceil(Math.random() * items.length));
        });
        list.classList.remove("invisible");
    });

    const aboutNavItem = document.querySelector(`#about-nav li[data-filter-name="who-we-are"]`);
    if (aboutNavItem) {
        aboutNavItem.classList.add("active-about-nav-item");
    }

    document.querySelectorAll("#about-nav li").forEach(li => {
        li.addEventListener("click", function () {
            const activeClassName = "active-about-nav-item";
            this.classList.add(activeClassName);

            const activeLink = (this as HTMLElement).dataset.filterName;
            const allLinks = ["who-we-are", "what-we-believe", "community", "history", "awards", "newsroom", "join-us"];
            const inactiveLinks = allLinks.filter(link => link !== activeLink);

            inactiveLinks.forEach(link => {
                document.querySelector(`#about-nav li[data-filter-name="${link}"]`)?.classList.remove(activeClassName);
            });
        });
    });

    // Wrap "required" asterisks in tooltips.
    document.querySelectorAll("dl.resources-properties dt.property-required.property-replacement").forEach(dt => {
        dt.removeAttribute("title");
        const indicator = dt.querySelector(".property-indicator");
        if (indicator) {
            const wrapper = document.createElement("div");
            wrapper.innerHTML = ' <div class="multi-property-container"> ' + "<pulumi-tooltip>" + '    <span class="property-indicator"></span>' + '    <span slot="content">This property is required.</span>' + "</pulumi-tooltip>" + "</pulumi-tooltip>" + ' <div class="replacement-container"> ' + "<pulumi-tooltip>" + '    <span class="property-indicator-replacement">' + ' <img src="/icons/replacement-property.svg"/>' + '</span>' + '    <span slot="content">Changes to this property will trigger replacement.</span>' + "</pulumi-tooltip>" + "</div>" + "</div>";
            indicator.replaceWith(wrapper.firstElementChild);
        }
    });
    document.querySelectorAll("dl.resources-properties dt.property-required:not(.property-replacement)").forEach(dt => {
        dt.removeAttribute("title");
        const indicator = dt.querySelector(".property-indicator");
        if (indicator) {
            const wrapper = document.createElement("div");
            wrapper.innerHTML = "<pulumi-tooltip>" + '    <span class="property-indicator"></span>' + '    <span slot="content">This property is required.</span>' + "</pulumi-tooltip>";
            indicator.replaceWith(wrapper.firstElementChild);
        }
    });

    document.querySelectorAll("dl.resources-properties dt.property-replacement:not(.property-required)").forEach(dt => {
        dt.removeAttribute("title");
        const indicator = dt.querySelector(".property-indicator");
        if (indicator) {
            const wrapper = document.createElement("div");
            wrapper.innerHTML = "<pulumi-tooltip>" + '    <span class="property-indicator-replacement">' + ' <img src="/icons/replacement-property.svg"/>' + '</span>' + '    <span slot="content">Changes to this property will trigger replacement.</span>' + "</pulumi-tooltip>";
            indicator.replaceWith(wrapper.firstElementChild);
        }
    });
})();
