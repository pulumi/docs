/**
 * Handle uncaught exceptions from third-party scripts.
 * 
 * The vector.co pixel.js script throws an uncaught exception when it detects a cloud provider environment.
 * This happens in the GitHub Actions runner but not locally, causing tests to fail in CI.
 * 
 * We catch and ignore this specific error while still allowing other legitimate errors to fail the tests.
 */
Cypress.on('uncaught:exception', (err) => {
    // Return false to prevent the error from failing the test
    if (err.message.includes('Cloud provider detected')) {
        return false;
    }
    // Return true for other errors to fail the test
    return true;
});

describe("www.pulumi.com", () => {

    describe("home page", () => {

        beforeEach(() => {
            // Force a desktop viewport so the new nav's desktop affordances render
            // (the nav-desktop breakpoint is 1200px).
            cy.viewport(1280, 800);
            cy.visit("/");
        });

        it("loads and applies CSS", () => {
            // Checking the computed background-color value validates that the CSS bundle
            // was properly loaded and applied.
            cy.get("header.sticky")
                .invoke("css", "background-color")
                .should("equal", "rgb(255, 255, 255)");
        });

        it("loads and applies JavaScript", () => {
            // Clicking a nav trigger button toggles aria-expanded via the header-nav
            // bundle's click handler — proves that bundle was loaded and ran.
            // force: true bypasses Cypress's pointer-events actionability check, which
            // can flake in CI when the overlay's data-attribute Tailwind variant hasn't
            // applied yet. The click handler is still exercised end-to-end.
            cy.get("[data-nav-trigger-button]").first()
                .should("have.attr", "aria-expanded", "false")
                .click({ force: true })
                .should("have.attr", "aria-expanded", "true");
        });
    });

    describe("getting started", () => {

        beforeEach(() => {
            cy.visit("/docs/iac/get-started/aws/begin");
        });

        describe("when an OS is selected", () => {

            beforeEach(() => {
                cy.get(`pulumi-chooser[type="os"] li:last`).click();
            });

            it("activates the selected OS", () => {
                cy.get(`pulumi-choosable[type="os"][value="macos"] > div`)
                    .should("not.have.class", "active");
                cy.get(`pulumi-choosable[type="os"][value="linux"] > div`)
                    .should("have.class", "active");
            });
        });
    });
});
