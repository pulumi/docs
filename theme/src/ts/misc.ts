import {LocalStorageService} from "./state";


const navigationState = new LocalStorageService("navigation-toggle-state");
loadToggleStates();

function bindToggle(el) {
    $(".toggleButton", el).click(function () {
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

function loadToggleStates() {
    // checks whether the menu item refers to the current page the
    // user is on.
    const isCurrentPage = (el) => {
        const browserUrl = window.location.href;
        const anchorRef = $(el).find('a').attr('href');
        return browserUrl.includes(anchorRef);
    };

    $(".toggle-topLevel, .toggleVisible-topLevel").each(function (i, el) {
        if (navigationState.getKey(el.id) == "expanded" || isCurrentPage(el)) {
            $(el).addClass("toggleVisible").removeClass("toggle");
        } else if (navigationState.getKey(el.id) == "collapsed") {
            $(el).addClass("toggle").removeClass("toggleVisible");
        }

        // Control open/closed folder icons if they exist as a subelement of the parent toggle-able item.
        $(el).click(function () {
            const folderOpenIcon = $(el).find(".folder-open");
            const folderClosedIcon = $(el).find(".folder");
            if (folderOpenIcon.length > 0) {
                folderOpenIcon.addClass("folder").removeClass("folder-open")
            } else if (folderClosedIcon.length > 0) {
                folderClosedIcon.addClass("folder-open").removeClass("folder")
            }
        });
    });

    $(".toggleVisible, .toggleVisible-topLevel").each(function (i, el) {
        // Scroll to active item in list.
        if (isCurrentPage(el)) {
            $("#left-nav").animate({
                scrollTop: $(el).offset().top - 145
            }, 0);
        }
    });
}

function updateToggleState(el, toggleState) {
    navigationState.updateKey(el.id, toggleState)
}

function bindTopLevelToggle(el) {
    $(".toggleButton-topLevel", el).click(function () {
        if ($(this).closest(".toggle-topLevel, .toggleVisible-topLevel")[0] != el) {
            // Only trigger the closest toggle header.
            return;
        }

        if ($(el).is(".toggle")) {
            $(el).addClass("toggleVisible").removeClass("toggle");
            updateToggleState(el, "expanded");
        } else {
            $(el).addClass("toggle").removeClass("toggleVisible");
            updateToggleState(el, "collapsed");
        }
    });
}

function bindTopLevelToggles(selector) {
    $(selector).each(function (i, el) {
        bindTopLevelToggle(el);
    });
}

function bindToggles(selector) {
    $(selector).each(function (i, el) {
        bindToggle(el);
    });
}

export function generateOnThisPage() {
    // Hide the table of contents by default. We explicitly decide when to show it
    // below based on if elements exist to display.
    $(".table-of-contents").hide();

    var $ul = $(".table-of-contents .content ul.table-of-contents-list");
    if ($ul) {
        var found = false;
        var headings = [];

        $("h2, h3, h4").each(function () {
            var $el = $(this);
            // Skip if this heading is inside a hidden element
            if ($el.closest('.hidden').length > 0) {
                return;
            }
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
            $(".table-of-contents").show();

            // Highlight the first heading whose offset from top is greater than the current scroll
            // position, to best indicate your location within the page hierarchy.
            const setActiveItem = () => {
                var active;
                for (var heading of headings) {
                    if (!active && heading.element.offset().top >= window.scrollY) {
                        active = heading;
                    }
                    heading.listItem.toggleClass("active", heading === active);
                }
            };

            $(window).on("scroll", function () {
                setActiveItem();
            });

            setActiveItem();
        }
    }
}

// Function to watch for OpenAPI content loading and regenerate table of contents
function setupOpenAPIContentObserver() {
    // Only set up the observer if we're on a page with OpenAPI content
    if (document.querySelector('.docs-content') && document.querySelector('[data-openapi-content]')) {
        return; // Observer already set up or not needed
    }
    
    // Check if we're on an OpenAPI docs page
    const metaTags = document.querySelectorAll('meta');
    let isOpenAPIPage = false;
    
    metaTags.forEach(tag => {
        if (tag.getAttribute('property') === 'openapi_docs' && tag.getAttribute('content') === 'true') {
            isOpenAPIPage = true;
        }
    });
    
    if (!isOpenAPIPage) {
        return; // Not an OpenAPI page
    }

    // Create a mutation observer to detect when API content is added
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                // If h3 elements have been added and table of contents is empty, regenerate it
                const h3Elements = document.querySelectorAll('h3');
                const tocItems = document.querySelectorAll('.table-of-contents-list li');
                
                if (h3Elements.length > 0 && tocItems.length === 0) {
                    // Clear the existing table of contents
                    const tocList = document.querySelector('.table-of-contents-list');
                    if (tocList) {
                        tocList.innerHTML = '';
                    }
                    
                    // Regenerate the table of contents
                    generateOnThisPage();
                    
                    // We've done our job, disconnect the observer
                    observer.disconnect();
                }
            }
        });
    });
    
    // Start observing the docs content area
    const docsContent = document.querySelector('.docs-content');
    if (docsContent) {
        observer.observe(docsContent, { childList: true, subtree: true });
    }
}

(function ($) {
    const observer = new IntersectionObserver(
        ([e]) => {
            e.target.classList.toggle("is-pinned", e.intersectionRatio < 1);
            const pinnedSearchContainerEl = document.querySelector(".header-pinned");
            const dotOverlay = document.querySelector(".hide-on-pinned");
            const heroTitle = document.querySelector(".header-hero-title");

            if (e.isIntersecting) {
                $(pinnedSearchContainerEl).addClass("hidden");
                $(pinnedSearchContainerEl).removeClass("flex");

                $(dotOverlay).removeClass("hidden");
                $(dotOverlay).addClass("flex");

                $(heroTitle).removeClass("hidden");
                $(heroTitle).addClass("flex");

            } else {
                $(pinnedSearchContainerEl).removeClass("hidden");
                $(pinnedSearchContainerEl).addClass("flex");

                $(dotOverlay).addClass("hidden");
                $(dotOverlay).removeClass("flex");

                $(heroTitle).addClass("hidden");
                $(heroTitle).removeClass("flex");

            }
        },
        { threshold: [1] },
    );

    const headerContainerEl = document.querySelector(".header-container");
    // The header-container won't be available in the registry.
    // If the registry's top nav bar is available attach the observer to that.
    if (!headerContainerEl) {
        const registryNavBar = document.querySelector(".top-nav-bar.registry");
        if (registryNavBar) {
            observer.observe(registryNavBar);
        }
    } else {
        observer.observe(headerContainerEl);
    }

    // Set up toggle functionality.
    bindToggles(".toggle");
    bindToggles(".toggleVisible");

    bindTopLevelToggles(".toggle-topLevel");
    bindTopLevelToggles(".toggleVisible-topLevel");

    // Create "On This Page" in the right nav.
    generateOnThisPage();
    
    // Set up observer for OpenAPI content
    $(document).ready(function() {
        setupOpenAPIContentObserver();
    });

    // Mobile menu toggles.
    $(".nav-header-toggle").click(function () {
        $(".nav-header-items").toggleClass("hidden");
    });
    $(".blog-sidebar-toggle").click(function () {
        $(".blog-sidebar-content").toggleClass("hidden");
    });
    $(".docs-sidebar-toggle").click(function () {
        $(".docs-sidebar-content").toggleClass("hidden");
    });

    // Shuffle lists that want to be shuffled.
    $("ul[data-shuffle='true']").each(function (i, list) {
        var items = $(list).find("> li");

        items.each(function (i, item) {
            $(item).css("order", Math.ceil(Math.random() * items.length));
        });

        $(list).removeClass("invisible");
    });

    $(`#about-nav li[data-filter-name="who-we-are"]`).addClass("active-about-nav-item");

    $(function () {
        $("#about-nav li").click(function () {
            const activeClassName = "active-about-nav-item";
            $(this).addClass(activeClassName);

            const activeLink = $(this).data("filter-name");
            const allLinks = ["who-we-are", "what-we-believe", "community", "history", "awards", "newsroom", "join-us"]
            const inactiveLinks = allLinks.filter(link => link !== activeLink);

            inactiveLinks.forEach(link => {
                $(`#about-nav li[data-filter-name="${link}"]`).removeClass(activeClassName);
            })

        });
    });

    // Wrap "required" asterisks in tooltips.
    $("dl.resources-properties dt.property-required.property-replacement")
        .removeAttr("title")
        .find(".property-indicator")
        .replaceWith(' <div class="multi-property-container"> ' + "<pulumi-tooltip>" + '    <span class="property-indicator"></span>' + '    <span slot="content">This property is required.</span>' + "</pulumi-tooltip>" + "</pulumi-tooltip>" + ' <div class="replacement-container"> ' + "<pulumi-tooltip>" + '    <span class="property-indicator-replacement">' + ' <img src="/icons/replacement-property.svg"/>' + '</span>' + '    <span slot="content">Changes to this property will trigger replacement.</span>' + "</pulumi-tooltip>" + "</div>" + "</div>");
    $("dl.resources-properties dt.property-required:not(.property-replacement)")
        .removeAttr("title")
        .find(".property-indicator")
        .replaceWith("<pulumi-tooltip>" + '    <span class="property-indicator"></span>' + '    <span slot="content">This property is required.</span>' + "</pulumi-tooltip>");

    $("dl.resources-properties dt.property-replacement:not(.property-required)")
        .removeAttr("title")
        .find(".property-indicator")
        .replaceWith("<pulumi-tooltip>" + '    <span class="property-indicator-replacement">' + ' <img src="/icons/replacement-property.svg"/>' + '</span>' + '    <span slot="content">Changes to this property will trigger replacement.</span>' + "</pulumi-tooltip>");
})(jQuery);
