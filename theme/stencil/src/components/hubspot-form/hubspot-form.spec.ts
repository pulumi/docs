import { HubspotForm } from "./hubspot-form";

describe("pulumi-hubspot-form", () => {
    it("builds", () => {
        expect(new HubspotForm()).toBeTruthy();
    });
});

describe("confirmed Gravity demo conversion", () => {
    const formId = "32b46b45-6717-4d11-ae15-4b9a21afeacd";
    const browser = window as any;
    let form: any;
    let track: jest.Mock;

    beforeEach(() => {
        form = new HubspotForm() as any;
        form.formId = formId;
        form.gravityConversionId = "submission-1";
        form.getUTMCookieData = jest.fn(() => ({}));
        form.hubspotFormSubmitted = { emit: jest.fn() };
        track = jest.fn();
        browser.analytics = { track };
        browser.pulumiConsent = { isAllowed: jest.fn(category => category === "C0004") };
        browser.gravityPixel = { getCAPIData: jest.fn(() => ({ user_data: { grclid: "synthetic" } })) };
    });

    afterEach(() => {
        delete browser.analytics;
        delete browser.pulumiConsent;
        delete browser.gravityPixel;
    });

    function confirm(origin = window.location.origin, id = formId) {
        form.onMessage({ origin, data: { type: "hsFormCallback", eventName: "onFormSubmitted", id } });
    }

    it("tracks once after confirmed success with consent and pixel context", () => {
        confirm();
        confirm();
        expect(track).toHaveBeenCalledTimes(1);
        expect(track).toHaveBeenCalledWith("Demo Request Confirmed", {
            conversionConfirmed: true,
            conversionId: "demo-submission-1",
            formId,
            gravity: { user_data: { grclid: "synthetic" } },
        }, { context: { consent: { categoryPreferences: { C0004: true } } } });
    });

    it("does not track without advertising consent", () => {
        browser.pulumiConsent.isAllowed = () => false;
        confirm();
        expect(track).not.toHaveBeenCalled();
    });

    it("does not track unrelated forms, mismatched callbacks or missing submissions", () => {
        confirm(window.location.origin, "another-form");
        expect(track).not.toHaveBeenCalled();
        form.formId = "support-request";
        confirm(window.location.origin, "support-request");
        expect(track).not.toHaveBeenCalled();
        form.formId = formId;
        form.gravityConversionId = undefined;
        confirm();
        expect(track).not.toHaveBeenCalled();
    });

    it("rejects callbacks from an unrelated origin", () => {
        confirm("https://unrelated.example");
        expect(track).not.toHaveBeenCalled();
    });
});
