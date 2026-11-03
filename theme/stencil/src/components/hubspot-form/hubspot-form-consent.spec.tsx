import { newSpecPage, SpecPage } from "@stencil/core/testing";
import { HubspotForm } from "./hubspot-form";

// The consent gate under the OneTrust provider: the form must not load the
// HubSpot library until Functional (C0003) consent is granted.
//
// window.runWithPulumiConsent is a small fake of the OneTrust bridge's contract
// (theme/src/ts/consent-manager/onetrust.ts, tested in onetrust.test.ts): queue
// per category, run each callback at most once when its category is granted.
// The real engine isn't imported because it lives outside this package's
// rootDir, and `stencil build` type-checks spec files too, emitting the import
// into src/ts/.
class FakeConsent {
    private granted = new Set<string>();
    private queue: Array<{ category: string; callback: () => void }> = [];

    run(category: string, callback: () => void) {
        this.queue.push({ category, callback });
        this.drain();
    }

    setGroups(groups: Set<string>) {
        this.granted = groups;
        this.drain();
    }

    private drain() {
        const ready = this.queue.filter(item => this.granted.has(item.category));
        this.queue = this.queue.filter(item => !this.granted.has(item.category));
        ready.forEach(item => item.callback());
    }
}

const BLOCKED_TEXT = "This form needs functional cookies to load.";
const HUBSPOT_SCRIPT = 'script[src*="js.hsforms.net"]';

let engine: FakeConsent;
let observerCallback: (entries: any[]) => void;
let openConsentManager: jest.Mock;

class FakeObserver {
    constructor(cb: (entries: any[]) => void) {
        observerCallback = cb;
    }
    observe() {}
    disconnect() {}
}

beforeEach(() => {
    engine = new FakeConsent();
    observerCallback = undefined;
    openConsentManager = jest.fn();
    // The component reads the bare global, which the mock window doesn't provide.
    (globalThis as any).IntersectionObserver = FakeObserver;
});

afterEach(() => {
    delete (globalThis as any).IntersectionObserver;
});

// newSpecPage builds a fresh window, so globals go on page.win. The form only
// asks for consent once it scrolls into view, which the test triggers here.
async function mountInView(hbspt?: any): Promise<SpecPage> {
    const page = await newSpecPage({
        components: [HubspotForm],
        html: `<pulumi-hubspot-form form-id="abc-123"></pulumi-hubspot-form>`,
    });
    const win = page.win as any;
    win.runWithPulumiConsent = (category: string, callback: () => void) => engine.run(category, callback);
    win.consentManager = { openConsentManager };
    if (hbspt) {
        win.hbspt = hbspt;
    }
    observerCallback([{ isIntersecting: true }]);
    await page.waitForChanges();
    return page;
}

function grant(groups: string[]) {
    engine.setGroups(new Set(groups));
}

function placeholderButton(page: SpecPage): HTMLButtonElement | undefined {
    return Array.from(page.root.querySelectorAll("button")).find(b => b.textContent.includes("Open Cookie Settings")) as HTMLButtonElement;
}

describe("pulumi-hubspot-form consent gate", () => {
    it("shows the blocked-consent placeholder while C0003 is not granted", async () => {
        const page = await mountInView();
        expect(page.root.textContent).toContain(BLOCKED_TEXT);
        expect(placeholderButton(page)).toBeTruthy();
        expect(page.doc.querySelector(HUBSPOT_SCRIPT)).toBeNull();

        // Other categories don't unblock it.
        grant(["C0001", "C0002", "C0004"]);
        await page.waitForChanges();
        expect(page.root.textContent).toContain(BLOCKED_TEXT);
        expect(page.doc.querySelector(HUBSPOT_SCRIPT)).toBeNull();
    });

    it("opens Cookie Settings when the placeholder button is clicked", async () => {
        const page = await mountInView();
        placeholderButton(page).click();
        expect(openConsentManager).toHaveBeenCalledTimes(1);
    });

    it("loads the HubSpot script and drops the placeholder once C0003 is granted", async () => {
        const page = await mountInView();
        grant(["C0001", "C0003"]);
        await page.waitForChanges();
        expect(page.root.textContent).not.toContain(BLOCKED_TEXT);
        expect(placeholderButton(page)).toBeUndefined();
        expect(page.doc.querySelectorAll(HUBSPOT_SCRIPT).length).toBe(1);

        // A repeated grant doesn't append the library again.
        grant(["C0001", "C0003"]);
        await page.waitForChanges();
        expect(page.doc.querySelectorAll(HUBSPOT_SCRIPT).length).toBe(1);
    });

    it("creates the form directly when the HubSpot library is already on the page", async () => {
        const create = jest.fn();
        const page = await mountInView({ forms: { create } });
        expect(create).not.toHaveBeenCalled();

        grant(["C0001", "C0003"]);
        await page.waitForChanges();
        expect(create).toHaveBeenCalledTimes(1);
        expect(create.mock.calls[0][0]).toMatchObject({ formId: "abc-123" });
        expect(page.root.textContent).not.toContain(BLOCKED_TEXT);
    });
});
