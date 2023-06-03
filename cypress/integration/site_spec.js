describe("www.pulumi.com", () => {

    describe("home page", () => {

        beforeEach(() => {
            cy.visit("/");
        });

        it("loads and applies CSS", () => {
            // Checking the computed background-color value validates that the CSS bundle
            // was properly loaded and applied.
            cy.get(".header-container")
                .invoke("css", "background-color")
                .should("equal", "rgb(255, 255, 255)");
        });

        it("loads and applies JavaScript", () => {
            // Checking the carousel validates that the JS bundle was loaded and applied
            // (excluding Stencil components, which are bundled separately).
            cy.get(".header-container")
                .should("not.have.class", "is-pinned");

            cy.scrollTo(0, 250);

            cy.get(".header-container")
                .should("have.class", "is-pinned");
        });
    });

    describe("getting started", () => {

        beforeEach(() => {
            cy.visit("/docs/clouds/aws/get-started");
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

    describe("python SDK docs", () => {
        beforeEach(() => {
            cy.visit("/docs/reference/pkg/python/pulumi");
        });

        // Regression test for https://github.com/pulumi/docs/issues/1396, which has happened multiple times.
        // The CSS is applied by targeting specific node structures due to the way our Python docs are generated.
        it("is styled correctly", () => {
            cy.get("#pulumi-python-sdk")
                .invoke("css", "--pulumi-python-sdk")
                .should("equal", "true");
        });
    });
});
