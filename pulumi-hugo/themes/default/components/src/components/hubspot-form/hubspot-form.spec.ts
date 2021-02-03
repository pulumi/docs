import { HubspotForm } from "./hubspot-form";

describe("pulumi-hubspot-form", () => {
    it("builds", () => {
        expect(new HubspotForm()).toBeTruthy();
    });
});
