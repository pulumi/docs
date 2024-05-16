import { Component, h, Element, Event, EventEmitter, Listen, Method, State } from "@stencil/core";
import { Filter } from "./filter-select-option";

export interface PackageFilter {
    kind: "type" | "category" | "status";
    label: string;
    value: string;
}

@Component({
    tag: "pulumi-filter-select",
    shadow: true,
    styles: `
        div {
            display: flex;
        }
    `,
})
export class FilterSelect {
    @Element()
    el: HTMLElement;

    @State()
    filters: Filter[] = [];

    @Event({ composed: true, bubbles: true })
    filterSelect: EventEmitter<any[]>; // Momentary laziness -- will come back to this.

    @Method()
    reset() {
        this.options.forEach(option => (option.selected = false));
        this.groups.forEach(group => group.close());
        this.filterSelect.emit([]);

        return Promise.resolve(null);
    }

    @Method()
    select(filter: Filter) {
        this.options.forEach(option => {
            if (option.value === filter.value) {
                option.select();
            }
        });
        return Promise.resolve();
    }

    @Method()
    deselect(filter: Filter) {
        this.options.forEach(option => {
            if (option.value === filter.value) {
                option.deselect();
            }
        });
        return Promise.resolve();
    }

    @Listen("optionChange")
    onOptionChange(event: Event) {
        event.stopPropagation();

        this.filters = this.options
            .filter(option => option.selected)
            .map(option => {
                const group = option.closest("pulumi-filter-select-option-group");
                return {
                    group: group.name,
                    value: option.value,
                    label: option.label,
                };
            });

        this.filterSelect.emit(this.filters);
    }

    private get groups() {
        return Array.from(this.el.querySelectorAll("pulumi-filter-select-option-group"));
    }

    private get options() {
        return Array.from(this.el.querySelectorAll("pulumi-filter-select-option"));
    }

    render() {
        return (
            <div>
                <slot />
            </div>
        );
    }
}
