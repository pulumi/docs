import { Component, h, State, EventEmitter, Event } from "@stencil/core";
import debounce from "lodash-es/debounce";

@Component({
    tag: "pulumi-registry-list-search",
    styleUrl: "pulumi-registry-list-search.scss",
    shadow: false,
})
export class PulumiRegistryListSearch {
    @Event({ composed: true, bubbles: true })
    packageSearch: EventEmitter<string>;

    constructor() {
        // We debounce the filter call so that we are not performing unnecessary work while
        // a user is in the middle of typing their filter criteria.
        this.debouncedFilter = debounce(this.debouncedFilter, 300);
    }

    @State()
    filterContent: string = "";

    debouncedFilter(event: HTMLInputElement) {
        this.filterContent = event.value;
        this.packageSearch.emit(this.filterContent);
    }

    onChange(event: HTMLInputElement) {
        this.debouncedFilter(event);
    }

    // When using the search-specific X button. Doesn't affect the other filters.
    onClearFilter() {
        this.filterContent = "";
        this.packageSearch.emit(this.filterContent);
        return;
    }

    // When a user selects the reset button that appears if there are no matched
    // results for any filters/search.  No need to emit the event, because this starts
    // over with all packages.
    reset() {
      this.filterContent = "";
    }

    render() {
        return (
            <div class="input-container">
                <svg class="search-icon ph-icon ph-icon--regular" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true" focusable="false">
                    <path d="M230.6,49.53A15.81,15.81,0,0,0,216,40H40A16,16,0,0,0,28.19,66.76l.08.09L96,139.17V216a16,16,0,0,0,24.87,13.32l32-21.34A16,16,0,0,0,160,194.66V139.17l67.74-72.32.08-.09A15.8,15.8,0,0,0,230.6,49.53ZM40,56h0Zm106.18,74.58A8,8,0,0,0,144,136v58.66L112,216V136a8,8,0,0,0-2.16-5.47L40,56H216Z"/>
                </svg>
                <input
                    class="registry-filter-input"
                    placeholder="Filter by package name..."
                    onInput={(event: InputEvent) => this.onChange(event.target as HTMLInputElement)}
                    value={this.filterContent}
                    autocomplete="off"
                ></input>
                {this.filterContent && (
                    <div class="clear-container">
                        <button onClick={this.onClearFilter.bind(this)} class="clear-filter-button">
                            <svg class="ph-icon ph-icon--regular" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true" focusable="false">
                                <path d="M205.66,194.34a8,8,0,0,1-11.32,11.32L128,139.31,61.66,205.66a8,8,0,0,1-11.32-11.32L116.69,128,50.34,61.66A8,8,0,0,1,61.66,50.34L128,116.69l66.34-66.35a8,8,0,0,1,11.32,11.32L139.31,128Z"/>
                            </svg>
                        </button>
                    </div>
                )}
            </div>
        );
    }
}
