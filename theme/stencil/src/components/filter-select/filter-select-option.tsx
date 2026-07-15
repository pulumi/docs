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
            display: flex;
            align-items: center;
            gap: 0.5rem;
            white-space: nowrap;
            font-size: 0.8125rem;
            line-height: 1.4;
            cursor: pointer;
        }

        /* Shadcn-style custom checkbox — mirrors .form-checkbox in _forms.scss.
           CSS custom properties inherit through the shadow boundary, so the brand
           tokens resolve here; the white check data-URI is duplicated from
           $form-check-svg (shadow DOM can't read the SCSS var). */
        input[type="checkbox"] {
            appearance: none;
            -webkit-appearance: none;
            margin: 0;
            width: 1rem;
            height: 1rem;
            flex-shrink: 0;
            border: 1px solid var(--color-gray-300, #cbcace);
            border-radius: 4px;
            background-color: #fff;
            background-position: center;
            background-repeat: no-repeat;
            background-size: 0.75rem;
            cursor: pointer;
            transition: all 100ms;
        }

        input[type="checkbox"]:checked {
            background-color: var(--color-violet-primary, #5a30c5);
            border-color: var(--color-violet-primary, #5a30c5);
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='none' viewBox='0 0 16 16'%3E%3Cpath stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m3.5 8 3 3 6-6.5'/%3E%3C/svg%3E");
        }

        input[type="checkbox"]:focus-visible {
            outline: none;
            border-color: var(--color-violet-primary, #5a30c5);
            box-shadow: 0 0 0 3px color-mix(in srgb, var(--color-violet-primary, #5a30c5) 50%, transparent);
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
                    <input type="checkbox" value={this.value} onChange={this.onChange.bind(this)} checked={this.selected} class={`${this.selected ? 'selected' : ''}`}/>
                    <slot />
                </label>
            </div>
        );
    }
}
