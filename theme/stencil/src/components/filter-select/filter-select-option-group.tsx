import { Component, h, Element, Prop, Method, Listen } from "@stencil/core";
@Component({
    tag: "pulumi-filter-select-option-group",
    shadow: true,
    styles: `
        :host {
            width: max-content;
        }

        .menu {
            position: relative;
            transition: all 100ms;
            opacity: 0;
            top: -2px;
            pointer-events: none;
            z-index: 10;
        }

        .menu > div {
            position: absolute;
        }

        .button {
            cursor: pointer;
        }

        .button .toggle {
            margin-right: 0.5em;
        }

        .toggle {
            display: flex;
        }

        .toggle slot {
            position: relative;
            display: block;
        }

        :host([expanded]) .menu {
            opacity: 1;
            top: 0;
            pointer-events: auto;
        }

        /* SVG chevron caret, sitting in the toggle's pr-7 gutter. This data-URI is
           duplicated from $form-caret-svg in theme/src/scss/_forms.scss (shadow DOM
           can't read the SCSS var) — keep the two in sync. */
        .toggle slot::after {
            position: absolute;
            right: 0.625rem;
            top: 50%;
            width: 1rem;
            height: 1rem;
            content: "";
            transform: translateY(-50%);
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='none' viewBox='0 0 16 16'%3E%3Cpath stroke='%239997a0' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='m4 6 4 4 4-4'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: center;
            background-size: 1rem;
            transition: transform 100ms;
        }

        :host([expanded]) .toggle slot::after {
            transform: translateY(-50%) rotate(180deg);
        }
    `,
})
export class FilterSelectOptionGroup {
    @Element()
    el: HTMLElement;

    @Prop()
    name: string;

    @Prop({ reflect: true })
    expanded: boolean;

    onToggle() {
        this.expanded = !this.expanded;
    }

    @Listen("click", { target: "document" })
    onDocumentClick(event: Event) {
        if (!this.el.contains(event.target as HTMLElement) && this.expanded) {
            this.close();
        }
    }

    @Method()
    close() {
        this.expanded = false;
        return Promise.resolve(null);
    }

    render() {
        return (
            <div>
                <div class="button" role="button" onClick={this.onToggle.bind(this)}>
                    <span class="toggle" part="toggle">
                        <slot name="toggle" />
                    </span>
                </div>
                <div class="menu">
                    <div>
                        <slot />
                    </div>
                </div>
            </div>
        );
    }
}
