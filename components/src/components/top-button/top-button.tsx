import { Component, Listen, State, h } from '@stencil/core';

// Scroll to top button.
@Component({
  tag: "pulumi-top-button",
  styleUrl: "top-button.scss",
  shadow: false
})
export class TopButton {

  @State()
  visible: boolean;

  @Listen("scroll", { target: "window" })
  handleScroll() {
    this.visible = window.scrollY > 2500;
  }

  componentWillRender() {
    this.visible = window.scrollY > 2500;
  }

  render() {
    return (
      <div>
          <a class="top-button fas fa-chevron-up" title="Scroll to top" onClick={this.onClick} style={{display: this.visible ? "" : "none"}}></a>
      </div>
    );
  }

  onClick() {
    window.scrollTo(0, 0)
  }
}
