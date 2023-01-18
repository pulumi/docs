import { Component, h, Prop, Element, Event, EventEmitter, Method } from "@stencil/core";

export interface Filter {
    label: string;
    value: string;
}

@Component({
    tag: "pulumi-filter-select-option",
    shadow: true,
    styles: `
        label {
            white-space: nowrap;
        }

        input {
            margin-right: 0.5em;
        }
    `,
})
export class FilterSelectOption {
    @Element()
    el: HTMLElement;

    @Prop()
    label?: string;

    @Prop()
    value: string;

    @Prop()
    selected: boolean;

    @Event({ composed: true, bubbles: true, cancelable: true })
    optionChange: EventEmitter<any>;

    @Method()
    select() {
        this.selected = true;
        this.emit();
        return Promise.resolve();
    }

    @Method()
    deselect() {
        this.selected = false;
        this.emit();
        return Promise.resolve();
    }

    onChange(event: CustomEvent) {
        this.selected = (event.target as HTMLInputElement).checked;
        this.emit();
    }

    private emit() {
        this.optionChange.emit({
            option: { value: this.value, selected: this.selected, label: this.label },
        });
    }

    render() {
        return (
            <div>
                <label>
                    <input type="checkbox" value={this.value} onChange={this.onChange.bind(this)} checked={this.selected} />
                    <slot />
                </label>
            </div>
        );
    }
}
