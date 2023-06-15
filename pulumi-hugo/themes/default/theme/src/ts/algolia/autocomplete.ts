import algoliasearch, { SearchClient } from "algoliasearch/lite";
import { autocomplete, getAlgoliaResults, getAlgoliaFacets } from "@algolia/autocomplete-js";
import { getTags, getTagsPlugin, setTags, Tag, iconForTag, labelForTag, mapTagsToFilters, groupBy, formatCount, debounce, listenForEvents } from "./utils";

// CSS selector of the element to convert into an autocomplete control.
const autocompleteContainer = "#search";

// Algolia index settings. It's expected these are set as data-* attributes on the
// `autocompleteContainer` element.
let appID: string;
let searchKey: string;
let indexName: string;

// The autocomplete search client.
let searchClient: SearchClient;

// The set of tags (or "facets"), that the autocomplete control should use for filtering. At least
// one facet is required and must be set as a comma-delimited list on the `autocompleteContainer`
// (e.g., data-facets="Docs,Registry").
let baseTags: Tag[];

// Initialize the autocomplete control.
function initAutocomplete(el: HTMLElement) {

    // Read the index settings from the container element.
    appID = el.getAttribute("data-app-id");
    searchKey = el.getAttribute("data-search-key");
    indexName = el.getAttribute("data-index");
    baseTags = el.getAttribute("data-facets").split(",").map(f => ({ label: f, facet: "section" }));

    if (!appID || !searchKey ||!indexName ||!baseTags) {
        console.error(`Autocomplete element found, but one or more require attributes were missing.`)
        return;
    }

    // Initialize the search client.
    searchClient = algoliasearch(appID, searchKey);

    // Returns an autocomplete "source" consisting of a list of facets (e.g, "Docs", "Registry") and
    // the number of results within that facet that match the query provided.
    // https://www.algolia.com/doc/ui-libraries/autocomplete/core-concepts/sources/
    function getFacetsSource(query, state, setContext) {
        return {
            sourceId: "sections",

            // https://www.algolia.com/doc/ui-libraries/autocomplete/core-concepts/sources/#param-getitems
            getItems: () => {

                // https://www.algolia.com/doc/ui-libraries/autocomplete/api-reference/autocomplete-js/getAlgoliaFacets/
                return getAlgoliaFacets({
                    searchClient,
                    queries: [
                        {
                            indexName,
                            facet: "section",
                            params: {
                                query,
                                filters: mapTagsToFilters(
                                    groupBy(baseTags, (tag: any) => tag.facet as string),
                                ),
                            },
                        },
                    ],

                    // Note that for this source, we deliberately drop the results on the floor (by
                    // returning an empty array) because we only care about the number of results
                    // per facet; we don't need the facets themselves because we already have them.
                    transformResponse({ facetHits }) {

                        // Save the item counts on the autocomplete context (its internal state).
                        setContext({
                            facetHits,
                        });

                        // Return an empty list.
                        return [];
                    }
                })
            },
            templates: {
                item: () => null,
            },
        };
    }

    // Returns an autocomplete source consisting of the list of actual search results.
    // https://www.algolia.com/doc/ui-libraries/autocomplete/api-reference/autocomplete-js/getAlgoliaResults/
    function getResultsSource(query, state, refresh) {
        return {
            sourceId: "results",
            getItems: ({ state }) => {
                return getAlgoliaResults({
                    searchClient,
                    queries: [
                        {
                            indexName,
                            query,
                            params: {
                                filters: mapTagsToFilters(
                                    groupBy(
                                        getTags(state), (tag: any) => tag.facet as string,
                                    ),
                                ),
                                // The existence of these params suggests that paging actually
                                // *does* work in autocomplete (since this is the autocomplete API).
                                // TODO: Make use of these, either with pagination or infinite scroll.
                                hitsPerPage: 50,
                                page: 0,
                            },
                        },
                    ],
                })
            },

            // Tells the autocomplete control which URL to use for navigation (specifically keyboard navigation).
            // https://www.algolia.com/doc/ui-libraries/autocomplete/core-concepts/sources/#param-getitemurl
            getItemUrl: ({ item }) => {
                const url = new URL([document.location.origin, item.href].join(""));
                return url.toString();
            },

            // Templates are the snippets of HTML to use for rendering the autocomplete panel's header,
            // item list, footer, and no-results view.
            // https://www.algolia.com/doc/ui-libraries/autocomplete/core-concepts/templates/
            templates: {
                header: ({ html, state }) => {
                    const facetHits = state.context.facetHits[0] as any[];
                    const allCount = facetHits.reduce((acc, f) => acc + f.count, 0);

                    // If only one facet was specified, return a single, non-interactive tab for "all results".
                    if (baseTags.length === 1) {
                        return html`
                            <ul class="header">
                                <li class="${ getTags(state).length === baseTags.length ? "active" : "" }">
                                    <button>
                                        <img src="${ iconForTag("all") }" />
                                        <span class="label">All results</span>
                                        <span class="count count-${allCount}">
                                            ${ formatCount(allCount) }
                                        </span>
                                    </button>
                                </li>
                            </ul>
                        `;
                    }

                    // Otherwise, return a list of tabs -- one "all results" tab and then one tab per facet.
                    return html`
                        <ul class="header">
                            <li class="${ getTags(state).length === baseTags.length ? "active" : "" }">
                                <button
                                    onclick="${ event => {
                                        // When the "All results" tab is activated, reset the state
                                        // to use all facets, then reload results.
                                        event.stopPropagation();
                                        setTags(state, baseTags);
                                        refresh();
                                    }}">
                                    <img src="${ iconForTag("all") }" />
                                    <span class="label">All results</span>
                                    <span class="count count-${allCount}">
                                        ${ formatCount(allCount) }
                                    </span>
                                </button>
                            </li>

                            ${ baseTags.map(tag => {

                                // Make a tab for each facet, including item counts. Disable tabs with zero results.
                                const facetHit = facetHits.find(f => f.label === tag.label);
                                const isActive = getTags(state).length === 1 && getTags(state)[0].label === tag.label;
                                const isDisabled = !facetHit || facetHit.count === 0;
                                const facetCount = facetHit ? facetHit.count : 0;

                                return html`
                                    <li class="${ isActive ? "active" : "" } ${ isDisabled ? "disabled" : ""}">
                                        <button disabled="${ isDisabled }"
                                            onclick="${ event => {
                                                // When a regular tab is activated, reset the state
                                                // to that facet and reload.
                                                event.stopPropagation();
                                                setTags(state, [ { label: tag.label, facet: "section" } ]);
                                                refresh();
                                            }}">
                                            <img src="${ iconForTag(tag.label) }"/>
                                            <span class="label">${ labelForTag(tag.label) }</span>
                                            <span class="count count-${ facetCount }">${ formatCount(facetCount) }</span>
                                        </button>
                                    </li>`
                            })}
                        </ul>
                    `;
                },
                item: ({ state, item, components, html }) => {
                    return html`
                        <div class="result my-3 px-1">
                            <a class="container" href="${ item.href }">
                                <div class="ancestors">${ ((item.ancestors || []) as string[]).join(" / ") }</div>
                                <div class="item">
                                    <div class="title">
                                        <span>
                                            <!-- When there's an h1 param present, use that; otherwise, use the title. -->
                                            ${ item.h1
                                                ? components.Highlight({ hit: item, attribute: "h1" })
                                                : components.Highlight({ hit: item, attribute: "title" })
                                            }
                                        </span>
                                        <span class="label ${ labelForTag(item.section).toLowerCase() } ${ getTags(state).length === 1 ? "hidden" : "" }">
                                            ${ labelForTag(item.section) }
                                        </span>
                                    </div>
                                    <div class="description">
                                        ${ item.description !== "" && components.Highlight({ hit: item, attribute: "description" }) }
                                    </div>
                                </div>
                            </a>
                        </div>
                    `;
                },
                footer: ({ html }) => {
                    return html`
                        <div>
                            <span>↑ ↓ to navigate</span>
                            <span>↵ to select</span>
                            <span>esc to close</span>
                        </div>
                    `;
                },
                noResults: ({ html, state }) => {
                    if (!state.query) {
                        return;
                    }

                    return html`
                        <img src="/images/search/no-results.svg"/>
                        <p>We couldn't find any results for <mark>${ state.query }</mark>.</p>
                    `;
                },
            },
        };
    }

    // Start listening for keyboard events.
    const keyEventsState = listenForEvents();

    // Activate the autocomplete control. See the Algolia docs for configuration details.
    // https://www.algolia.com/doc/ui-libraries/autocomplete/api-reference/autocomplete-js/autocomplete
    autocomplete({
        container: el,
        placeholder: "Search (⌘/ctrl-k)",

        // Whether to open the panel when the input gets focus (i.e., before a query is submitted).
        openOnFocus: false,

        // Whether to render the control as a modal dialog or drop-down. Empty string means modal.
        detachedMediaQuery: "",

        // The (zero-based) item that should be selected by default.
        defaultActiveItemId: 0,

        // Handler for any change that occurs on the state of the autocomplete control.
        onStateChange: ({ state, prevState, setCollections }) => {

            // When a query is "cleared out" by the user, reset the list of facets to "all" and drop
            // any existing results to start fresh.
            if (prevState.query !== "" && state.query === "") {
                setCollections([]);
                setTags(state, baseTags);
            }

            // When there's an active item, and an arrow key was just pressed, scroll the active
            // item into view.
            if (state.activeItemId >= 0) {
                const items = document.querySelectorAll(`.aa-Item`);

                if (items) {
                    const item = items.item(state.activeItemId);

                    if (item && keyEventsState.upDownPressed) {
                        item.scrollIntoView({ behavior: "smooth", block: "nearest" });
                    }
                }

                // Reset the arrow-key flag.
                keyEventsState.upDownPressed = false;
            }
        },

        // Returns the list of autocomplete sources to use for each query. Our control uses two
        // sources: one for obtaining query result counts by facet, another for obtaining actual
        // query results.
        getSources: ({ query, state, refresh, setContext }) => {
            const sources = [];

            sources.push(getFacetsSource(query, state, setContext))
            sources.push(getResultsSource(query, state, refresh));

            // Debounce requests to keep from sending too many queries to Algolia.
            return debounce(sources);
        },

        // https://www.algolia.com/doc/ui-libraries/autocomplete/core-concepts/plugins/
        plugins: [
            getTagsPlugin(baseTags),
        ],
    });
}

// Wait until the DOM is ready before looking for any autocomplete controls on the page.
window.addEventListener("DOMContentLoaded", () => {
    const el = document.querySelector(autocompleteContainer) as HTMLElement;
    if (el) {
        initAutocomplete(el);
    }
});
