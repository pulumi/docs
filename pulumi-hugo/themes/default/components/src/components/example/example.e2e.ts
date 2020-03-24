import { newE2EPage } from '@stencil/core/testing';

describe("pulumi-example", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-example></pulumi-example>");

        const element = await page.find("pulumi-example");
        expect(element).toHaveClass("hydrated");
    });
});
