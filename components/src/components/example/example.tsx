import { Component, h } from "@stencil/core";

@Component({
    tag: "pulumi-example",
    styleUrl: "example.scss",
    shadow: false
})
export class Example {

    render() {
        return (
            <div>
                <slot></slot>
            </div>
        );
    }
}
