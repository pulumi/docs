import { Component, Element, Host, h } from "@stencil/core";

@Component({
    tag: "pulumi-examples",
    styleUrl: "examples.scss",
    shadow: false
})
export class Examples {

    @Element()
    el: HTMLElement;

    children: Element[];

    componentWillLoad() {
        this.children = Array.from(this.el.children);
        this.el.innerHTML = "";
    }

    render() {
        return (
            <Host>
                {
                    this.children.map(c => <pulumi-example innerHTML={c.outerHTML}></pulumi-example>)
                }
            </Host>
        );
    }
}
