import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-tooltip", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-tooltip></pulumi-tooltip>");

        const element = await page.find("pulumi-tooltip");
        expect(element).toHaveClass("hydrated");
    });
});
