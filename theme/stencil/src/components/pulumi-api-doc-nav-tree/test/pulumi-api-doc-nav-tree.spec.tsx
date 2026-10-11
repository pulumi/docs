import { newSpecPage } from "@stencil/core/testing";
import { PulumiApiDocNavTree } from "../pulumi-api-doc-nav-tree";

describe("pulumi-api-doc-nav-tree", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [PulumiApiDocNavTree],
            html: `<pulumi-api-doc-nav-tree></pulumi-api-doc-nav-tree>`,
        });
        expect(page.root).toEqualHtml(`
      <pulumi-api-doc-nav-tree>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-api-doc-nav-tree>
    `);
    });
});
