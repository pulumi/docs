import { newSpecPage } from "@stencil/core/testing";
import { PulumiApiDocNavNode } from "../pulumi-api-doc-nav-node";

describe("pulumi-api-doc-nav-node", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [PulumiApiDocNavNode],
            html: `<pulumi-api-doc-nav-node></pulumi-api-doc-nav-node>`,
        });
        expect(page.root).toEqualHtml(`
      <pulumi-api-doc-nav-node>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-api-doc-nav-node>
    `);
    });
});
