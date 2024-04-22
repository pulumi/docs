import { Component, h, Element, Prop, Method, Listen } from "@stencil/core";
@Component({
    tag: "pulumi-filter-select-option-group",
    shadow: true,
    styles: `
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
            width: 100%;
        }

        :host([expanded]) .menu {
            opacity: 1;
            top: 0;
            pointer-events: auto;
        }

        .toggle slot::after {
            position: absolute;
            right: 0.5em;
            top: 50%;
            transform: translateY(-50%);
            content: "▾";
        }

        :host([expanded]) .toggle slot::after {
            transform: rotate(180deg) translateY(50%);
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
