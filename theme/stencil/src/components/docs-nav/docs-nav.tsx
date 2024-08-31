import { Component, h, Element, Listen } from "@stencil/core";

@Component({
    tag: "pulumi-docs-nav",
    styleUrl: "docs-nav.scss",
    shadow: false,
})
export class DocsNav {
    @Element()
    el: HTMLElement;

    @Listen("click")
    onClick(event: MouseEvent) {
        const target = event.target as HTMLElement;

        if (target.nodeName.toLowerCase() === "button") {
            target.closest("li").classList.toggle("collapsed");
            event.stopPropagation();
            event.preventDefault();
        }
    }

    componentDidRender() {
        this.el.querySelectorAll("li > ol").forEach(item => {
            const button = document.createElement("button");
            const parent = item.parentElement.querySelector("a");
            parent.appendChild(button);
        });
    }

    render() {
        return <slot></slot>;
    }
}
