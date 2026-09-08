import { createTagsPlugin } from "@algolia/autocomplete-plugin-tags";

// Tags used for filtering results.
export interface Tag {
    label: string;
    facet: string;
}

// Converts a list of tags into an Algolia filter query.
// https://www.algolia.com/doc/guides/managing-results/refine-results/filtering/in-depth/filters-and-facetfilters/
export function mapTagsToFilters(tagsByFacet, operator = "AND") {
    const result = Object
        .keys(tagsByFacet)
        .map(facet => {
            return `(${tagsByFacet[facet]
                .map(({ label }) => `${facet}:"${label}"`)
                .join(' OR ')})`;
        })
        .join(` ${operator} `);

    return result;
}

// Groups a collection of items by key.
export function groupBy(items, predicate) {
    return items.reduce((acc, item) => {
        const key = predicate(item);

        if (!acc.hasOwnProperty(key)) {
            acc[key] = [];
        }

        acc[key].push(item);
        return acc;
    }, {});
}

// Creates a "tags plugin" for use with the autocomplete control. This plugin maps a set of tags to
// Algolia "facets" for filtering results.
// https://www.algolia.com/doc/ui-libraries/autocomplete/api-reference/autocomplete-plugin-tags/createTagsPlugin/
export function getTagsPlugin(baseTags) {
    return createTagsPlugin({
        initialTags: baseTags,
        transformSource: ({ source }) => {
            return undefined;
        },
        getTagsSubscribers: () => {
            return [
                {
                    sourceId: "section",
                    getTag: ({ item }) => {
                        return item;
                    },
                },
            ];
        },
    });
}

// Sets the list of tags to use for autocomplete filtering.
export function setTags(state, tags: Tag[]) {
    state.context?.tagsPlugin?.setTags(tags);
}

// Returns the list of currently applied tags.
export function getTags(state): Tag[] {
    return state.context?.tagsPlugin?.tags || [];
}

// Returns a function that returns a promise to be resolved after some delay.
function debouncePromise(fn, time): any {
    let timerId = undefined;

    return (...args) => {
        if (timerId) {
            clearTimeout(timerId);
        }

        return new Promise((resolve) => {
            timerId = setTimeout(() => resolve(fn(...args)), time);
        });
    };
}

// Delays sending queries to Algolia by the specified number of milliseconds. (Without this, we'd
// send a query on every keystroke, which is snappy but expensive.)
export const debounce = debouncePromise(items => Promise.resolve(items), 220);

// Listens for search-relevant events.
export function listenForEvents() {

    // Tiny object make it easier to share data between event handlers and the autocomplete instance.
    const sharedData = {

        // Whether an up or down arrow key was just pressed. The control uses this to decide whether
        // to scroll the active item into view.
        upDownPressed: false,
    };

    // Handle command/control-k events by triggering the search button directly.
    window.addEventListener("keydown", (event: KeyboardEvent) => {
        if ((event.key.toLowerCase() === "k" && (event.metaKey || event.ctrlKey))) {
            event.preventDefault();

            const searchButton = document.querySelector(`.aa-DetachedSearchButton`) as HTMLButtonElement;
            searchButton.click();
        }
    });

    // Handle arrow up/down. It's a bit odd that we have to do this manually, as it *should* be
    // handled by the Algolia control itself, but there's a bug in that control that prevents the
    // code from locating the item to scroll to, so we have to do it ourselves. Note that we use the
    // capture phase to be sure we get notified *before* the control's state changes; if we didn't,
    // we wouldn't be notified of the keypress until afterward, at which point it'd be too late to
    // know whether the state change had resulted from a keypress (and to scroll accordingly).
    window.addEventListener("keydown", (event: KeyboardEvent) => {
        if ((event.key === "ArrowUp" || event.key === "ArrowDown") && event.target === document.querySelector(`.aa-DetachedFormContainer .aa-Input`)) {
            sharedData.upDownPressed = true;
        }
    }, { capture: true });

    // When the clear button is clicked, don't close the modal; instead, clear the value and leave
    // the modal open. To do this, we have to listen for clicks on the `body` element, because the
    // modal doesn't exist when the page is rendered -- and could be created and destroyed many
    // times within a given pageview.
    document.body.addEventListener("click", (event) => {
        const clickedElement = event.target as HTMLElement;

        // If the thing clicked was a clear button or one of its descendants, stop the event and
        // clear the input field.
        if (clickedElement?.closest(".aa-ClearButton")) {
            event.stopPropagation();
            event.preventDefault();

            const input = clickedElement.closest(".aa-Form")?.querySelector(".aa-Input") as HTMLInputElement;
            if (input) {
                input.value = "";
                input.focus();
                input.dispatchEvent(new Event("input"));
            };
        }
    });

    // Return the shared-data object.
    return sharedData;
}

// Formats numbers greater than 1000 by rounding them up and rendering as "1K".
export function formatCount(count: number) {
    return count > 1000 ? `${Math.ceil(count / 1000)}K` : count.toString();
}

// Returns the label to use for a given tag.
export function labelForTag(facet) {
    if (facet === "Registry") {
        return "Packages";
    }
    return facet;
}

// Returns the icon to use for a given tag.
export function iconForTag(label: string) {
    switch (label) {
        case "Docs":
            return "/icons/docs.svg";
        case "Registry":
            return "/icons/registry.svg";
    }
    return "/icons/list.svg";
}
