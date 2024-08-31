import { newSpecPage } from "@stencil/core/testing";
import { DocsToc } from "../docs-toc";

describe("docs-toc", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [DocsToc],
            html: `<pulumi-docs-toc></pulumi-docs-toc>`,
        });
        expect(page.root).toEqualHtml(`
      <pulumi-docs-toc>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-docs-toc>
    `);
    });
});
