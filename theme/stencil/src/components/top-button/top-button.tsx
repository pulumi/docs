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
        let buttonClass = `btn btn-outline btn-icon-lg ${this.visible}`;
        return (
            <a class={buttonClass} title="Scroll to top" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--bold" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false">
                    <path d="M216.49,168.49a12,12,0,0,1-17,0L128,97,56.49,168.49a12,12,0,0,1-17-17l80-80a12,12,0,0,1,17,0l80,80A12,12,0,0,1,216.49,168.49Z"/>
                </svg>
            </a>
        );
    }

    setVisibility() {
        this.visible = window.scrollY > 2500 ? "visible" : "hidden";
    }
}
