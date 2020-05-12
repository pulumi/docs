import { Component, Listen, State, h } from '@stencil/core';

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
        this.setVisibility()
    }
    
    componentWillRender() {
        this.setVisibility()
    }
    
    render() {
        console.log("render")
        let buttonClass = `top-button fas fa-chevron-up ${this.visible}`
        return (
            <div>
                <a class={buttonClass} title="Scroll to top" href="#top" ></a>
            </div>
        );
    }

    setVisibility() {
        this.visible = window.scrollY > 2500 ? "visible" : "hidden";
    }
  
}
