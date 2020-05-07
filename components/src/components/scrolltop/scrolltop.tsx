import { Component, h } from "@stencil/core";

@Component({
    tag: "scroll-top",
    styleUrl: "scrolltop.scss",
    shadow: false
})

export class ScrollTop {

    render() {
        return (
            <div>
                <a class="top-button fas fa-chevron-up" title="Go to top"></a>"
            </div>
        );
    }
}
