import { Component, Element, h, Prop } from '@stencil/core';

@Component({
    tag: "pulumi-tab",
    shadow: true,
})
export class Tab {

    @Prop()
    label: string;

    @Prop()
    active: boolean;

    @Element()
    el: HTMLElement;

    private get styles() {
        return {
            display: this.active ? "block" : "none",
        };
    }

    render() {
        return <div>
            {
                <div role="tabpanel" style={ this.styles } aria-hidden={ !this.active }>
                    <slot></slot>
                </div>
            }
        </div>;
    }
}
