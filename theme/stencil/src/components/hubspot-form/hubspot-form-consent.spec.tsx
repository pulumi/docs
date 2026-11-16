import { newSpecPage, SpecPage } from "@stencil/core/testing";
import { HubspotForm } from "./hubspot-form";

// Under OneTrust with no consent given, the form still loads: the site has no
// HubSpot tracking code, so the forms library sets no tracking cookies.

const HUBSPOT_SCRIPT = 'script[src*="js.hsforms.net"]';

let observerCallback: (entries: any[]) => void;

class FakeObserver {
    constructor(cb: (entries: any[]) => void) {
        observerCallback = cb;
    }
    observe() {}
    disconnect() {}
}

beforeEach(() => {
    observerCallback = undefined;
    // The component reads the bare global, which the mock window doesn't provide.
    (globalThis as any).IntersectionObserver = FakeObserver;
});

afterEach(() => {
    delete (globalThis as any).IntersectionObserver;
});

// newSpecPage builds a fresh window, so globals go on page.win. OneTrust
// withholding every category means runWithPulumiConsent never calls back.
async function mount(hbspt?: any): Promise<SpecPage> {
    const page = await newSpecPage({
        components: [HubspotForm],
        html: `<pulumi-hubspot-form form-id="abc-123"></pulumi-hubspot-form>`,
    });
    const win = page.win as any;
    win.runWithPulumiConsent = () => {};
    if (hbspt) {
        win.hbspt = hbspt;
    }
    return page;
}

async function scrollIntoView(page: SpecPage) {
    observerCallback([{ isIntersecting: true }]);
    await page.waitForChanges();
}

describe("pulumi-hubspot-form without consent", () => {
    it("waits until the form scrolls into view", async () => {
        const page = await mount();
        expect(page.doc.querySelector(HUBSPOT_SCRIPT)).toBeNull();
    });

    it("loads the HubSpot script", async () => {
        const page = await mount();
        await scrollIntoView(page);
        expect(page.doc.querySelectorAll(HUBSPOT_SCRIPT).length).toBe(1);
    });

    it("creates the form directly when the HubSpot library is already on the page", async () => {
        const create = jest.fn();
        const page = await mount({ forms: { create } });
        await scrollIntoView(page);
        expect(create).toHaveBeenCalledTimes(1);
        expect(create.mock.calls[0][0]).toMatchObject({ formId: "abc-123" });
        expect(page.doc.querySelector(HUBSPOT_SCRIPT)).toBeNull();
    });
});
