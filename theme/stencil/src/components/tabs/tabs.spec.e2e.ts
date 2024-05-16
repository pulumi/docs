import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-tabs", () => {

    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-tabs></pulumi-tabs>");

        const element = await page.find("pulumi-tabs");
        expect(element).not.toBeNull();
    });

    describe("given multiple tabs", () => {
        let tabContent: string;

        beforeEach(() => {
            tabContent = `
                <pulumi-tab label="Label 1">
                    <p>Here is some content for label 1.</p>
                </pulumi-tab>
                <pulumi-tab label="Label 2">
                    <p>Here is some content for label 2.</p>
                </pulumi-tab>
            `;
        });

        it("renders the tabs", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-tabs>${tabContent}</pulumi-tabs>`);

            const elements = await page.findAll("pulumi-tab");
            expect(elements.length).toBe(2);
        });

        it("shows the first tab by default", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-tabs>${tabContent}</pulumi-tabs>`);

            const tabs = await page.findAll("pulumi-tab");
            expect(tabs[0].getAttribute("active")).toBe("true");
            expect(tabs[1].getAttribute("active")).not.toBe("true");

            const tab0Active = await tabs[0].getProperty("active");
            const tab1Active = await tabs[1].getProperty("active");
            expect(tab0Active).toBe(true);
            expect(tab1Active).toBe(false);
        });

        it("supports switching between tabs", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-tabs>${tabContent}</pulumi-tabs>`);

            const elements = await page.findAll("pulumi-tab");
            expect(elements[0].getAttribute("active")).toBe("true");
            expect(elements[1].getAttribute("active")).not.toBe("true");

            const tabControls = await page.findAll("pulumi-tabs >>> li a");
            expect(tabControls.length).toBe(2);

            expect(elements[0].getAttribute("active")).toBe("true");
            expect(elements[1].getAttribute("active")).not.toBe("true");

            tabControls[1].click();
            await page.waitForChanges();

            expect(elements[0].getAttribute("active")).not.toBe("true");
            expect(elements[1].getAttribute("active")).toBe("true");
        });

        describe("when an active tab is specified", () => {

            beforeEach(() => {
                tabContent = `
                    <pulumi-tab label="Label 1">
                        <p>Here is some content for label 1.</p>
                    </pulumi-tab>
                    <pulumi-tab label="Label 2" active="true">
                        <p>Here is some content for label 2.</p>
                    </pulumi-tab>
                `;
            });

            it("shows the specified tab", async () => {
                const page = await newE2EPage();
                await page.setContent(`<pulumi-tabs>${tabContent}</pulumi-tabs>`);

                const elements = await page.findAll("pulumi-tab");
                expect(elements[0].getAttribute("active")).not.toBe("true");
                expect(elements[1].getAttribute("active")).toBe("true");
            });
        });
    })
});
