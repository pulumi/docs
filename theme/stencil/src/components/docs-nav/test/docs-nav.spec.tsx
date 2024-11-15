import { newSpecPage } from "@stencil/core/testing";
import { DocsNav } from "../docs-nav";

describe("docs-nav", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [DocsNav],
            html: `<docs-nav></docs-nav>`,
        });
        expect(page.root).toEqualHtml(`
      <docs-nav>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </docs-nav>
    `);
    });
});
