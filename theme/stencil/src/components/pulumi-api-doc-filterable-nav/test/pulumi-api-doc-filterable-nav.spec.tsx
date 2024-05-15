import { newSpecPage } from "@stencil/core/testing";
import { PulumiApiDocFilterableNav } from "../pulumi-api-doc-filterable-nav";

describe("pulumi-api-doc-filterable-nav", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [PulumiApiDocFilterableNav],
            html: `<pulumi-api-doc-filterable-nav></pulumi-api-doc-filterable-nav>`,
        });
        expect(page.root).toEqualHtml(`
      <pulumi-api-doc-filterable-nav>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-api-doc-filterable-nav>
    `);
    });
});
