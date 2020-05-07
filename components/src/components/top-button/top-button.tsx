import { Component, Listen, Prop, h } from '@stencil/core';

// Scroll to top button.
@Component({
  tag: 'pulumi-top-button',
  styleUrl: 'top-button.scss',
  shadow: false
})

export class TopButton {

  @Prop({ mutable: true })
  scrollPostion: number;

  @Listen('scroll', { target: 'window' })
  handleScroll() {
    this.scrollPostion = window.scrollY;
  }

  componentWillRender() {
    this.scrollPostion = window.scrollY;
  }

  render() {
    return (
      <div>
          <a class="top-button fas fa-chevron-up" title="Scroll to top" style={{display: this.scrollPostion < 2500 ? "none" : ""}}></a>
      </div>
    );
  }
}
