import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-install", () => {

    describe("by default", () => {
        it("renders the current os preference", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-install></pulumi-install>`);

            const element = await page.find("pulumi-install p span");
            expect(element.textContent).toContain("pulumi");
        });
    });

    describe("when the os is macos", () => {
        it("renders the macos install command", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-install os="macos"></pulumi-install>`);

            const element = await page.find("pulumi-install p span");
            expect(element.textContent).toBe("brew install pulumi");
        });
    });

    describe("when the os is windows", () => {
        it("renders the windows install command", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-install os="windows"></pulumi-install>`);

            const element = await page.find("pulumi-install p span");
            expect(element.textContent).toBe("choco install pulumi");
        });
    });

    describe("when the os is linux", () => {
        it("renders the linux install command", async () => {
            const page = await newE2EPage();
            await page.setContent(`<pulumi-install os="linux"></pulumi-install>`);

            const element = await page.find("pulumi-install p span");
            expect(element.textContent).toBe("curl -fsSL https://get.pulumi.com | sh");
        });
    });
});
