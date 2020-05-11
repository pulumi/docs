import { Component, h } from "@stencil/core";

@Component({
    tag: "pulumi-examples",
    styleUrl: "examples.scss",
    shadow: false
})
export class Examples {

    render() {
        return (
            <div>
                <slot></slot>
            </div>
        );
    }
}
