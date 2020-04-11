import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-examples", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-examples></pulumi-examples>");

        const element = await page.find("pulumi-examples");
        expect(element).toHaveClass("hydrated");
    });
});
