import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-api-doc-nav-node", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-api-doc-nav-node></pulumi-api-doc-nav-node>");

        const element = await page.find("pulumi-api-doc-nav-node");
        expect(element).toHaveClass("hydrated");
    });
});
