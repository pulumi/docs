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

        if (target.nodeName.toLowerCase() === "button" || target.nodeName.toLowerCase() === "i") {
            // target.closest("li").classList.toggle("collapsed");
            target.closest("li").classList.toggle("expanded");
            event.stopPropagation();
            event.preventDefault();
        }
    }

    componentDidRender() {
        this.el.querySelectorAll("li > a").forEach(item => {

            const a = item.parentElement.querySelector("a");
            const label = a.textContent;
            a.textContent = "";

            const span = document.createElement("span");
            span.textContent = label;

            a.appendChild(span);
        });

        this.el.querySelectorAll("li > ul").forEach(item => {

            const a = item.parentElement.querySelector("a");
            const label = a.textContent;
            a.textContent = "";

            const button = document.createElement("button");
            const i = document.createElement("i");
            i.classList.add("fa", "fa-caret-right");
            button.appendChild(i);

            const span = document.createElement("span");
            span.textContent = label;

            // a.closest("li").classList.add("expandable");
            a.appendChild(button);
            a.appendChild(span);
        });

        const activeItem = this.el.querySelector("a.active");
        if (activeItem) {
            console.log(({ activeItem }));
            let parent = activeItem.closest("pulumi-docs-nav li.expandable");
            console.log({ parent });
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
