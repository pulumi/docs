import { Component, Element, Host, h, Method, State } from '@stencil/core';
import { getUUID } from "../../util/util";

/**
 * The ToolTip component shows a tooltip bubble above another element when you hover over
 * (or, on mobile tap on) it. Use the named `content` slot for supplying the markup to
 * show in the bubble.
 *
 * Usage:

 * <pulumi-tooltip>
 *     <i class="fas fa-question-circle"></i>
 *     <span slot="content">
 *         You hovered over (or tapped on) the thing!
 *     </span>
 * </pulumi-tooltip>
 */
@Component({
    tag: "pulumi-tooltip",
    shadow: false,
})
export class Tooltip {

    @Element()
    el: HTMLElement;

    // The id property is just a unique identifier that binds the tooltip to the control
    // it relates to, for better accessibility.
    @State()
    id: string;

    // Whether the tooltip is currently visible.
    @State()
    active: boolean;

    // Show the tooltip.
    @Method()
    async show() {
        return new Promise<void>(resolve => {
            this.active = true;

            // Wait 100ms to allow for the fade-in transition to complete.
            setTimeout(() => resolve(), 100);
        });
    }

    // Hide the tooltip.
    @Method()
    async hide() {
        return new Promise<void>(resolve => {
            this.active = false;

            // Wait 100ms to allow for the fade-out transition to complete.
            setTimeout(() => resolve(), 100);
        });
    }

    componentDidLoad() {
        this.id = getUUID();
        this.active = false;

        // Toggle the tooltip when the target element is hovered or tapped.
        const target = this.el.querySelector(".tooltip-target");
        target.addEventListener("mouseover", () => this.active = true);
        target.addEventListener("mouseout", () => this.active = false);
        target.addEventListener("touchstart", () => this.active = true);
        target.addEventListener("touchend", () => this.active = false);
    }

    render() {
        return (
            <Host>
                <span class={`tooltip-target ${ this.active ? "active" : "" }`} aria-labelledby={ this.id }>
                    <slot></slot>
                </span>
                <span id={ this.id } class="tooltip-content" role="tooltip">
                    <slot name="content"></slot>
                </span>
            </Host>
        );
    }
}
