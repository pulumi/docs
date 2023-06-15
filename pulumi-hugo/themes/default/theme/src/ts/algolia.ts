import algoliasearch from "algoliasearch/lite";
import { autocomplete, getAlgoliaResults, getAlgoliaFacets } from "@algolia/autocomplete-js";
import { createTagsPlugin } from "@algolia/autocomplete-plugin-tags";

const autocompleteContainer = "#search";
let appID: string;
let searchKey: string;
let indexName: string;
let searchClient;
let baseTags: { label: string; facet: string; }[];

window.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector(autocompleteContainer)) {
        initAutocomplete(autocompleteContainer);
    }
});

let wasKeyEvent = false;
window.addEventListener("keydown", (event: KeyboardEvent) => {
    if ((event.key.toLowerCase() === "k" && (event.metaKey || event.ctrlKey))) {
        event.preventDefault();

        const searchButton = document.querySelector(`${autocompleteContainer} .aa-DetachedSearchButton`) as HTMLButtonElement;
        searchButton.click();
        return;
    }

    if ((event.key === "ArrowUp" || event.key === "ArrowDown") && event.target === document.querySelector(`.aa-DetachedFormContainer .aa-Input`)) {
        wasKeyEvent = true;
        return;
    }
});

function mapTagsToAlgoliaFilters(tagsByFacet, operator = "AND") {
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

function groupBy(items, predicate) {
    return items.reduce((acc, item) => {
        const key = predicate(item);

        if (!acc.hasOwnProperty(key)) {
            acc[key] = [];
        }

        acc[key].push(item);
        return acc;
    }, {});
}

function getTags(state) {
    return state.context?.tagsPlugin?.tags || [];
}

function setTags(state, tags) {
    state.context?.tagsPlugin?.setTags(tags);
}

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

const debounced = debouncePromise(items => Promise.resolve(items), 220);

function initAutocomplete(container) {
    const el = document.querySelector(autocompleteContainer);

    appID = el.getAttribute("data-app-id");
    searchKey = el.getAttribute("data-search-key");
    indexName = el.getAttribute("data-index");
    baseTags = el.getAttribute("data-facets").split(",").map(f => ({ label: f, facet: "section" }));
    searchClient = algoliasearch(appID, searchKey);

    const tagsPlugin = createTagsPlugin({
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

    function getFacetsSource(query, state, setContext) {
        return {
            sourceId: "sections",
            getItems: () => {
                return getAlgoliaFacets({
                    searchClient,
                    queries: [
                        {
                            indexName,
                            facet: "section",
                            params: {
                                query,
                                filters: mapTagsToAlgoliaFilters(
                                    groupBy(
                                        baseTags,
                                        (tag: any) => {
                                            return tag.facet as string;
                                        },
                                    ),
                                ),
                            },
                        },
                    ],
                    transformResponse({ facetHits }) {
                        setContext({
                            facetHits,
                        });
                        return [];
                    }
                })
            },
            templates: {
                item: () => null,
            },
        };
    }

    function formatResultCount(count: number) {
        return count > 1000 ? `${Math.ceil(count / 1000)}K` : count.toString();
    }

    function labelForTag(label) {
        if (label === "Registry") {
            return "Packages";
        }
        return label;
    }

    function iconForTag(label: string) {
        switch (label) {
            case "Docs":
                return "/icons/docs.svg";
            case "Registry":
                return "/icons/registry.svg";
        }
        return "/icons/list.svg";
    }

    function getResultsSource(query, state, refresh) {
        const filters = mapTagsToAlgoliaFilters(
            groupBy(
                getTags(state),
                (tag: any) => {
                    return tag.facet as string;
                },
            ),
        );

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
                                filters,
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
            getItemUrl: ({ item }) => {
                const url = new URL([document.location.origin, item.href].join(""));
                return url.toString();
            },
            templates: {
                header: ({ html, state }) => {
                    const facetHits = state.context.facetHits[0] as any[];
                    const allCount = facetHits.reduce((acc, f) => acc + f.count, 0);

                    if (baseTags.length === 1) {
                        return html`
                            <ul class="header">
                                <li class="${ getTags(state).length === baseTags.length ? "active" : "" }">
                                    <button>
                                        <img src="${ iconForTag("all") }" />
                                        <span class="label">All results</span>
                                        <span class="count count-${allCount}">
                                            ${ formatResultCount(allCount) }
                                        </span>
                                    </button>
                                </li>
                            </ul>`;
                    }

                    return html`
                        <ul class="header">
                            <li class="${ getTags(state).length === baseTags.length ? "active" : "" }">
                                <button
                                    onclick="${ event => {
                                        event.stopPropagation();
                                        setTags(state, baseTags);
                                        refresh();
                                    }}">
                                    <img src="${ iconForTag("all") }" />
                                    <span class="label">All results</span>
                                    <span class="count count-${allCount}">
                                        ${ formatResultCount(allCount) }
                                    </span>
                                </button>
                            </li>

                            ${ baseTags.map(tag => {
                                const facetHit = facetHits.find(f => f.label === tag.label);
                                const isActive = getTags(state).length === 1 && getTags(state)[0].label === tag.label;
                                const isDisabled = !facetHit || facetHit.count === 0;
                                const facetCount = facetHit ? facetHit.count : 0;

                                return html`
                                    <li class="${ isActive ? "active" : "" } ${ isDisabled ? "disabled" : ""}">
                                        <button disabled="${ isDisabled }"
                                            onclick="${ event => {
                                                event.stopPropagation();
                                                setTags(state, [ { label: tag.label, facet: "section" } ]);
                                                refresh();
                                            }}">
                                            <img src="${ iconForTag(tag.label) }"/>
                                            <span class="label">${ labelForTag(tag.label) }</span>
                                            <span class="count count-${ facetCount }">${ formatResultCount(facetCount) }</span>
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

    function maybeScrollTo(itemID) {
        const items = document.querySelectorAll(`.aa-Item`);

        if (items) {
            const item = items.item(itemID);

            if (item && wasKeyEvent) {
                item.scrollIntoView({ behavior: "smooth", block: "nearest" });
            }

            wasKeyEvent = false;
        }
    }

    const ac = autocomplete({
        container,
        openOnFocus: false,
        placeholder: "Search (⌘/ctrl-k)",
        detachedMediaQuery: "",
        defaultActiveItemId: 0,
        onStateChange: ({ state, prevState, setCollections }) => {
            if (prevState.query !== "" && state.query === "") {
                setCollections([]);
                setTags(state, baseTags);
            }

            if (state.activeItemId >= 0) {
                maybeScrollTo(state.activeItemId);
            }
        },
        getSources: ({ query, state, refresh, setContext }) => {
            const sources = [];

            sources.push(getFacetsSource(query, state, setContext))
            sources.push(getResultsSource(query, state, refresh));

            return debounced(sources);
        },
        plugins: [
            tagsPlugin,
        ],
    });
}
