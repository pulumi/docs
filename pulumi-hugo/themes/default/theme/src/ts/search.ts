// Swiftype appends the autocomplete results container to the body element, which prevents us
// from being able to position it in a way that scrolls alongside the other content in the L2 nav.
// So we listen for DOM changes, and when Swiftype appends the element, we reposition it below the
// input field.

// Only bother doing this if we're on a page with a search box.
if (document.querySelector("#search-container")) {
    const observer = new MutationObserver((mutations, observer) => {
        var [mutation] = mutations;

        // Only bother when nodes are added.
        if (mutation && mutation.addedNodes && mutation.addedNodes.length > 0) {
            const [newNode] = Array.from(mutation.addedNodes) as HTMLElement[];
            const hasLoadedSwiftype = newNode && typeof newNode.getAttribute === "function" && newNode.getAttribute("id") === "st-injected-content";

            if (hasLoadedSwiftype) {
                // Find our results container and reparent the Swiftype container with it.
                var resultsContainer = document.querySelector("#search-results");
                if (resultsContainer) {
                    const autocompleteSuggestionBox = document.querySelector(".st-default-autocomplete");
                    resultsContainer.appendChild(autocompleteSuggestionBox);
                }

                // Stop listening.
                observer.disconnect();
            }
        }
    });

    // Start listening for DOM mutation events.
    observer.observe(document.querySelector("body"), {
        attributes: false,
        childList: true, // New childNodes are all we care about.
        subtree: false,
    });
}
