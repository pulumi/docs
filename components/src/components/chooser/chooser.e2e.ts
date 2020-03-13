import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-chooser", () => {

    it("renders a list items", async () => {
        const page = await newE2EPage();
        await page.setContent(`<pulumi-chooser type="language" options="typescript,go,python"></pulumi-chooser>`);

        const element = await page.find("pulumi-chooser");
        expect(element).toHaveClass("hydrated");

        const items = await element.findAll("ul > li");
        expect(items.length).toEqual(3);
    });
});
