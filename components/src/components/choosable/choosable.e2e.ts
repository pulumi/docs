import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-choosable", () => {

    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-choosable></pulumi-choosable>");

        const element = await page.find("pulumi-choosable");
        expect(element).toHaveClass("hydrated");
    });
});
