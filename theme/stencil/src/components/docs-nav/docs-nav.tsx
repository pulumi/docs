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
        const targetType = target.nodeName.toLowerCase();

        if (targetType === "button" || targetType === "i") {
            target.closest("li").classList.toggle("expanded");
            event.stopPropagation();
            event.preventDefault();
        }
    }

    componentDidRender() {
        const activeItem = this.el.querySelector("a.active");

        // Expand the active item.
        if (activeItem) {
            let parent = activeItem.closest("pulumi-docs-nav li.expandable");

            while (parent) {
                parent.classList.add("expanded");
                parent = parent.parentElement.closest("pulumi-docs-nav li.expandable");
            }
        }
    }

    render() {
        return <slot></slot>;
    }
}
