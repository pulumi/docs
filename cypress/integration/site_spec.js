describe("www.pulumi.com", () => {

    describe("home page", () => {

        beforeEach(() => {
            cy.visit("/");
        });

        it("loads and applies CSS", () => {
            // Checking the computed background-color value validates that the CSS bundle
            // was properly loaded and applied.
            cy.get(".nav-main")
                .invoke("css", "background-color")
                .should("equal", "rgb(55, 26, 71)");
        });

        it("loads and applies JavaScript", () => {
            // Checking the carousel validates that the JS bundle was loaded and applied
            // (excluding Stencil components, which are bundled separately).
            cy.contains("Manage").click();
            cy.get(".carousel-item-description:last")
                .invoke("css", "opacity")
                .should("equal", "1");
        });
    });

    describe("getting started", () => {

        beforeEach(() => {
            cy.visit("/docs/get-started/aws/begin");
        });

        it("renders the OS chooser", () => {
            cy.get(`pulumi-choosable[type="os"][value="macos"] > div`)
                .should("have.class", "active");
            cy.get(`pulumi-choosable[type="os"][value="linux"] > div`)
                .should("not.have.class", "active");
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
