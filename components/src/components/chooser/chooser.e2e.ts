import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-chooser", () => {

    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-chooser></pulumi-chooser>");

        const element = await page.find("pulumi-chooser");
        expect(element).toHaveClass("hydrated");
    });
});
