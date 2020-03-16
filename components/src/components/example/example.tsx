import { Component, Host, h } from '@stencil/core';

@Component({
    tag: "pulumi-example",
    styleUrl: "example.scss",
    shadow: false
})
export class Example {

    render() {
        return (
            <Host>
                <slot></slot>
            </Host>
        );
    }
}
