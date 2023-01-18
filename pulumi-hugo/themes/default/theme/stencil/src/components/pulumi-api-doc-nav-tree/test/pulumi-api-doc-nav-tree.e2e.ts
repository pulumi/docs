import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-api-doc-nav-tree", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-api-doc-nav-tree></pulumi-api-doc-nav-tree>");

        const element = await page.find("pulumi-api-doc-nav-tree");
        expect(element).toHaveClass("hydrated");
    });
});
