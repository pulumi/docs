import { Component, h, Element, Listen, Prop } from "@stencil/core";

@Component({
    tag: "pulumi-docs-nav",
    styleUrl: "docs-nav.scss",
    shadow: false,
})
export class DocsNav {
    @Element()
    el: HTMLElement;

    @Prop({ mutable: true })
    expand: string = "";

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

        // Expand any items marked for auto-expansion.
        this.expand.split(",").forEach(id => {
            this.el.querySelectorAll(`[data-identifier='${id}']`).forEach(el => {
                el.classList.add("expanded");
            });
        });
    }

    render() {
        return <slot></slot>;
    }
}
