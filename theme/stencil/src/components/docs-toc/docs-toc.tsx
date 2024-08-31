import { Component, h, Element } from "@stencil/core";

@Component({
    tag: "pulumi-docs-toc",
    styleUrl: "docs-toc.scss",
    shadow: false,
})
export class DocsToc {
    headings: Element[];

    @Element()
    el: HTMLElement;

    componentWillLoad() {
        const headingSelector = "main h2[id]:not(.no-toc), main h3[id]:not(.no-toc)";

        this.headings = Array.from(document.querySelectorAll(headingSelector))
            .filter(heading => heading.getAttribute("id") !== "")
            .filter(heading => !heading.classList.contains("no-anchor"))
            .filter(heading => !heading.classList.contains("no-toc"));

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                const id = entry.target.getAttribute("id");
                const link = this.el.querySelector(`li a[href="#${id}"]`);

                if (link) {
                    if (entry.intersectionRatio > 0) {
                        link.parentElement.classList.add("active");
                    } else {
                        link.parentElement.classList.remove("active");
                    }
                }
            });
        });

        document.querySelectorAll(headingSelector).forEach(heading => {
            observer.observe(heading);
        });
    }

    fixLabel(label: string) {
        return (
            label
                // Trim trailing colons.
                .replace(/:$/, "")
        );
    }

    render() {
        return (
            <div class="max-w-xs">
                <div class="font-display mt-0 mb-4 py-0">
                    <span class="text-sm text-gray-800">On this page</span>
                </div>
                <ol class="list-none p-0 text-sm">
                    {this.headings.map(heading => {
                        return (
                            <li class={`toc-level-${heading.tagName.toLowerCase()}`}>
                                <a class="text-blue-800" href={`#${heading.getAttribute("id")}`}>
                                    {this.fixLabel(heading.textContent)}
                                </a>
                            </li>
                        );
                    })}
                </ol>
            </div>
        );
    }
}
