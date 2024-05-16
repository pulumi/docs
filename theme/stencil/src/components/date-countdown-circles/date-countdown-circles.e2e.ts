import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-date-countdown-circles", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-date-countdown-circles></pulumi-date-countdown-circles>");

        const element = await page.find("pulumi-date-countdown-circles");
        expect(element).toHaveClass("hydrated");
    });
});
