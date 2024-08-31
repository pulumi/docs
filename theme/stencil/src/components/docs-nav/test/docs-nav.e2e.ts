import { newE2EPage } from "@stencil/core/testing";

describe("docs-nav", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<docs-nav></docs-nav>");

        const element = await page.find("docs-nav");
        expect(element).toHaveClass("hydrated");
    });
});
