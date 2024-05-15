import { Component, Element, h } from "@stencil/core";

@Component({
    tag: "pulumi-examples",
    styleUrl: "examples.scss",
    shadow: false,
})
export class Examples {
    @Element()
    el: HTMLElement;

    componentWillRender() {
        const headings = Array.from(this.el.querySelectorAll("pulumi-examples h3"));

        headings.forEach(heading => {
            // Prepend a span to each heading. We use these to hold the caret symbols.
            const span = document.createElement("span");
            heading.prepend(span);

            // Listen for clicks on headings.
            heading.addEventListener("click", event => {
                const clicked = event.target as HTMLElement;

                // Ignore anchor clicks; we want them to be clickable without triggering
                // any expand/collapse behavior.
                if (clicked.classList.contains("anchorjs-link")) {
                    return;
                }

                // When a heading is clicked, "toggle" it.
                this.toggle(heading);
            });
        });

        // Expand the first example by default.
        if (headings && headings.length > 0) {
            this.toggle(headings[0]);
        }
    }

    // Show or hide the examples associated with each heading.
    private toggle(heading: Element) {
        heading.classList.toggle("expanded");

        // Examples are contained within divs alongside their corresponding headings, so
        // we start with the heading that was clicked, then iterate over the siblings that
        // follow, toggling them also, until we come to one that isn't a div.
        let example = heading.nextElementSibling;

        while (example) {
            if (example.nodeName === "DIV") {
                example.classList.toggle("expanded");
                example = example.nextElementSibling;
            } else {
                break;
            }
        }
    }

    render() {
        return (
            <div>
                <slot></slot>
            </div>
        );
    }
}
