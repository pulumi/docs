import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-greenhouse-jobs-list", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-greenhouse-jobs-list></pulumi-greenhouse-jobs-list>");

        const element = await page.find("pulumi-greenhouse-jobs-list");
        expect(element).toHaveClass("hydrated");
    });
});
