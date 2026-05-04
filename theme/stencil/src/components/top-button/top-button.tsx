import { Component, Listen, State, h } from "@stencil/core";

// Scroll to top button.
@Component({
    tag: "pulumi-top-button",
    styleUrl: "top-button.scss",
    shadow: false,
})
export class TopButton {
    @State()
    visible: string;

    @Listen("scroll", { target: "window" })
    handleScroll() {
        this.setVisibility();
    }

    componentWillRender() {
        this.setVisibility();
    }

    render() {
        let buttonClass = `btn-scroll-top ${this.visible}`;
        return (
            <a class={buttonClass} title="Scroll to top" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--bold" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false">
                    <path d="M213.66,165.66a8,8,0,0,1-11.32,0L128,91.31,53.66,165.66a8,8,0,0,1-11.32-11.32l80-80a8,8,0,0,1,11.32,0l80,80A8,8,0,0,1,213.66,165.66Z"/>
                </svg>
            </a>
        );
    }

    setVisibility() {
        this.visible = window.scrollY > 2500 ? "visible" : "hidden";
    }
}
