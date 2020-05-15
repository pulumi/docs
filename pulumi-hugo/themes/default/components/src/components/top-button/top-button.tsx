import { Component, Listen, State, h } from "@stencil/core";

// Scroll to top button.
@Component({
    tag: "pulumi-top-button",
    styleUrl: "top-button.scss",
    shadow: false
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
        let buttonClass = `btn-scroll-top fas fa-chevron-up ${this.visible}`
        return (
                <a class={buttonClass} title="Scroll to top" href="#"></a>
        );
    }

    setVisibility() {
        this.visible = window.scrollY > 2500 ? "visible" : "hidden";
    }
}
