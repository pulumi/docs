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

    it("renders a language chooser as a toolbar with a logo label and abbreviated tabs", async () => {
        const page = await newE2EPage();
        await page.setContent(`<pulumi-chooser type="language" options="typescript,go,python"></pulumi-chooser>`);

        const element = await page.find("pulumi-chooser");
        expect(element).toHaveClass("hydrated");

        // The toolbar wrapper and left-hand label (logo + full name) render.
        const toolbar = await element.find(".chooser-toolbar");
        expect(toolbar).not.toBeNull();
        const label = await element.find(".chooser-toolbar-label");
        expect(label).not.toBeNull();
        const logo = await element.find(".chooser-toolbar-logo");
        expect(logo).not.toBeNull();

        // The tabs show uppercased file-extension abbreviations, not full names.
        const items = await element.findAll(".chooser-toolbar ul > li a");
        const labels = items.map(item => item.textContent.trim());
        expect(labels).toEqual(["TS", "PY", "GO"]);
    });

    it("renders a non-language chooser as plain name tabs with no toolbar", async () => {
        const page = await newE2EPage();
        await page.setContent(`<pulumi-chooser type="os" options="macos,linux,windows"></pulumi-chooser>`);

        const element = await page.find("pulumi-chooser");
        expect(element).toHaveClass("hydrated");

        // No toolbar wrapper for non-language choosers.
        const toolbar = await element.find(".chooser-toolbar");
        expect(toolbar).toBeNull();

        // Tabs render the full option names.
        const items = await element.findAll("ul > li a");
        const labels = items.map(item => item.textContent.trim());
        expect(labels).toEqual(["macOS", "Windows", "Linux"]);
    });
});
