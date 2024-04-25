import { Component, Host, h } from "@stencil/core";

@Component({
    tag: "pulumi-swipeable",
    shadow: false,
})
export class Swipeable {
    render() {
        return (
            <Host class="swiper-slide">
                <slot></slot>
            </Host>
        );
    }
}
