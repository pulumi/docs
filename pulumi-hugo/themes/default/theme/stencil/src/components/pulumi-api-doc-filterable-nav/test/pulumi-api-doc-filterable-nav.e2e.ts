import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-api-doc-filterable-nav", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-api-doc-filterable-nav></pulumi-api-doc-filterable-nav>");

        const element = await page.find("pulumi-api-doc-filterable-nav");
        expect(element).toHaveClass("hydrated");
    });
});
