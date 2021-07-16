import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-multi-select-form", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-multi-select-form></pulumi-multi-select-form>");

        const element = await page.find("pulumi-multi-select-form");
        expect(element).toHaveClass("hydrated");
    });
});
