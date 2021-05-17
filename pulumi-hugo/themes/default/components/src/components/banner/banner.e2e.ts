import { newE2EPage, E2EPage, E2EElement } from '@stencil/core/testing';

describe("pulumi-banner", () => {

    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-banner></pulumi-banner>");

        const element = await page.find("pulumi-banner");
        expect(element).toHaveClass("hydrated");
    });

    it("is not visible", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-banner></pulumi-banner>");

        const element = await page.find("pulumi-banner");
        expect(element).not.toHaveAttribute("visible");
    });

    describe("given a name", () => {
        let page: E2EPage;
        let element: E2EElement;

        beforeEach(async () => {
            page = await newE2EPage();
            await page.setContent(`
                <pulumi-root></pulumi-root>
                <pulumi-banner name="some-name">
                    <div>Some content</div>
                </pulumi-banner>
            `);

            element = await page.find("pulumi-banner");
        });

        it("is visible", async () => {
            expect(element).toHaveAttribute("visible");
        });

        it("does not show a dismiss icon", async () => {
            const dismissButton = await element.find(".dismiss");
            await dismissButton.waitForNotVisible();
        });

        describe("when the banner is marked dismissible", () => {

            beforeEach(async () => {
                page = await newE2EPage();
                await page.setContent(`
                    <pulumi-root></pulumi-root>
                    <pulumi-banner name="some-name" dismissible>
                        <div>Some content</div>
                    </pulumi-banner>
                `);

                element = await page.find("pulumi-banner");
            });

            it("shows a dismiss icon", async () => {
                const dismissButton = await element.find(".dismiss");
                await dismissButton.waitForVisible();
            });

            describe("and the banner is dismissed", () => {

                beforeEach(async () => {
                    const dismissButton = await element.find(".dismiss");
                    await dismissButton.click();
                });

                it("dismisses the banner", async () => {
                    expect(element).not.toHaveAttribute("visible");
                });
            });
        });
    });
});
