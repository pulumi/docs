import { Component, h, State, EventEmitter, Event } from "@stencil/core";
import { debounce } from "lodash";

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
                <i class="search-icon fas fa-filter"></i>
                <input
                    class="registry-filter-input"
                    placeholder="Filter by package name..."
                    onInput={(event: KeyboardEvent) => this.onChange(event.target as HTMLInputElement)}
                    value={this.filterContent}
                ></input>
                {this.filterContent && (
                    <div class="clear-container">
                        <button onClick={this.onClearFilter.bind(this)} class="clear-filter-button">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                )}
            </div>
        );
    }
}
