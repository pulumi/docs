// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for the /support/new/ client module, run against jsdom. From the
// theme directory:
//
//     yarn test-support-form
//
// Why these exist at this level rather than as narrow unit tests: every defect
// this file was written in response to was an *interaction* bug, not a bad
// function. The draft restore, the query-param prefill, and the rendered
// <option> list all read and write the same controls, and the bugs lived in
// which one won. Testing setControlValue in isolation would have caught none of
// them. So each test drives the real module against a real DOM.
//
// support-form.ts registers itself on DOMContentLoaded and exports nothing, so
// the module is required *after* the fixture is installed and the event is
// dispatched by hand — the same wiring path a browser takes.

import * as assert from "assert";
import { test } from "node:test";

const { JSDOM } = require("jsdom");

const MODULE_PATH = "./support-form";
const PAGE_URL = "https://www.pulumi.com/support/new/";

// Mirrors the DOM contract documented at the top of support-form.ts and rendered
// by layouts/page/support-new.html. `extraPriorities` exists so a test can prove
// the module reads the options actually rendered rather than a hardcoded copy.
function formHtml(extraPriorities: string[] = []): string {
    const options = ["normal", "urgent"]
        .concat(extraPriorities)
        .map(v => `<option value="${v}">${v}</option>`)
        .join("");
    return `
    <div data-support-form-root>
      <div data-support-form-card>
        <form action="/api/support" method="post" novalidate data-support-form>
          <input id="support-email" name="email" type="email" maxlength="254">
          <p id="support-email-error" hidden></p>
          <input id="support-name" name="name" type="text" maxlength="200">
          <p id="support-name-error" hidden></p>
          <input id="support-organization" name="organization" type="text" maxlength="200">
          <p id="support-organization-error" hidden></p>
          <select id="support-priority" name="priority" required>${options}</select>
          <p id="support-priority-error" hidden></p>
          <input id="support-subject" name="subject" type="text" maxlength="200">
          <p id="support-subject-error" hidden></p>
          <textarea id="support-description" name="description" maxlength="20000"></textarea>
          <p data-support-form-counter="support-description" hidden></p>
          <p id="support-description-error" hidden></p>
          <div class="sr-only" aria-hidden="true">
            <label for="support-website">Leave this field empty</label>
            <input id="support-website" name="website" type="text" tabindex="-1">
          </div>
          <div role="alert" data-support-form-banner hidden></div>
          <button type="submit" data-support-form-submit data-label="Submit" data-busy-label="Submitting…"></button>
        </form>
      </div>
      <div data-support-form-confirmation hidden tabindex="-1">
        <span data-support-form-value="organization"></span>
        <span data-support-form-value="subject"></span>
      </div>
    </div>`;
}

interface Harness {
    doc: Document;
    win: any;
    control: (id: string) => any;
    errorText: (field: string) => string;
    submit: () => Promise<void>;
    fetchCalls: Array<{ url: string; body: any }>;
    setFetch: (impl: (url: string, init: any) => Promise<any>) => void;
}

// Builds a page, installs the globals the module reaches for, requires it fresh,
// and fires DOMContentLoaded so it wires itself up.
function mount(options: { url?: string; draft?: any; extraPriorities?: string[]; breakStorage?: boolean } = {}): Harness {
    const dom = new JSDOM(`<!doctype html><body>${formHtml(options.extraPriorities)}</body>`, {
        url: options.url || PAGE_URL,
    });
    const win = dom.window;

    if (options.draft !== undefined) {
        win.sessionStorage.setItem("pulumi-support-form-draft", JSON.stringify(options.draft));
    }

    const fetchCalls: Array<{ url: string; body: any }> = [];
    let fetchImpl = async (_url: string, _init: any) => ({
        ok: true,
        status: 200,
        json: async () => ({ ok: true, id: "req-1", ticketId: "ticket-1" }),
    });

    const g: any = globalThis;
    for (const key of [
        "document",
        "Event",
        "HTMLElement",
        "HTMLInputElement",
        "HTMLSelectElement",
        "HTMLTextAreaElement",
        "HTMLFormElement",
        "HTMLButtonElement",
    ]) {
        g[key] = (win as any)[key];
    }
    g.window = win;

    // The module reads a BARE global `sessionStorage`, not window.sessionStorage,
    // so the global is what has to be installed — and what has to throw when the
    // test is exercising the blocked-storage path (private windows, storage
    // disabled), which the module documents as degrading to no persistence.
    Object.defineProperty(g, "sessionStorage", {
        configurable: true,
        get() {
            if (options.breakStorage) {
                throw new Error("blocked");
            }
            return win.sessionStorage;
        },
    });

    g.fetch = (url: string, init: any) => {
        fetchCalls.push({ url, body: init && init.body ? JSON.parse(init.body) : undefined });
        return fetchImpl(url, init);
    };

    delete require.cache[require.resolve(MODULE_PATH)];
    require(MODULE_PATH);
    win.document.dispatchEvent(new win.Event("DOMContentLoaded"));

    const doc: Document = win.document;
    const control = (id: string) => doc.getElementById(`support-${id}`) as any;

    return {
        doc,
        win,
        control,
        fetchCalls,
        setFetch: impl => {
            fetchImpl = impl as any;
        },
        errorText: field => {
            const el = doc.getElementById(`support-${field}-error`);
            return el && !(el as any).hidden ? el.textContent || "" : "";
        },
        submit: async () => {
            const form = doc.querySelector("[data-support-form]") as any;
            form.dispatchEvent(new win.Event("submit", { bubbles: true, cancelable: true }));
            // Let the handler's promise chain settle.
            await new Promise(resolve => setTimeout(resolve, 0));
        },
    };
}

// Types a value the way a person would, so the module's own listeners fire.
function type(harness: Harness, field: string, value: string): void {
    const input = harness.control(field);
    input.value = value;
    input.dispatchEvent(new harness.win.Event("input", { bubbles: true }));
}

function choose(harness: Harness, field: string, value: string): void {
    const input = harness.control(field);
    input.value = value;
    input.dispatchEvent(new harness.win.Event("change", { bubbles: true }));
}

function readDraft(harness: Harness): any {
    const raw = harness.win.sessionStorage.getItem("pulumi-support-form-draft");
    return raw ? JSON.parse(raw) : undefined;
}

// --- Query-param prefill -------------------------------------------------

test("prefills a <select> from the query string", () => {
    // Regression: the prefill guarded on `!input.value`, which is never true for
    // a <select> whose first option is selected by default — so ?priority= was
    // silently dead for every visitor.
    const h = mount({ url: `${PAGE_URL}?priority=urgent` });
    assert.strictEqual(h.control("priority").value, "urgent");
});

test("prefills text inputs from the query string", () => {
    const h = mount({ url: `${PAGE_URL}?subject=CLI+crash&email=a%40b.co` });
    assert.strictEqual(h.control("subject").value, "CLI crash");
    assert.strictEqual(h.control("email").value, "a@b.co");
});

test("ignores a query-string priority that is not a rendered option", () => {
    const h = mount({ url: `${PAGE_URL}?priority=bogus` });
    // Left on the default rather than blanked — assigning an unmatched value to
    // a <select> would silently clear it and post an empty priority.
    assert.strictEqual(h.control("priority").value, "normal");
});

// --- Draft vs. prefill ---------------------------------------------------

test("a recovered draft outranks the query string", () => {
    const h = mount({ url: `${PAGE_URL}?priority=urgent&subject=FromUrl`, draft: { priority: "normal", subject: "FromDraft" } });
    assert.strictEqual(h.control("subject").value, "FromDraft");
    assert.strictEqual(h.control("priority").value, "normal");
});

test("a deliberately chosen default is not reverted by the query string", () => {
    // The mirror of the prefill bug. A user who opened ?priority=urgent, decided
    // it wasn't urgent, and picked "normal" must not have "urgent" restored on
    // their next visit. "Differs from the rendered default" is not the same
    // predicate as "the user chose it".
    const h = mount({ url: `${PAGE_URL}?priority=urgent`, draft: { priority: "normal" } });
    assert.strictEqual(h.control("priority").value, "normal");
});

test("an untouched field never enters the draft", () => {
    // A <select> always reports a value, so saving every field would put
    // priority into the draft after a single keystroke elsewhere — which is what
    // made a stale default outrank the URL in the first place.
    const h = mount();
    type(h, "email", "a@b.co");
    h.win.document.querySelector("[data-support-form]").dispatchEvent(new h.win.Event("input", { bubbles: true }));
    return new Promise<void>(resolve => {
        setTimeout(() => {
            const draft = readDraft(h);
            assert.deepStrictEqual(Object.keys(draft || {}), ["email"]);
            resolve();
        }, 600);
    });
});

test("a touched select is kept in the draft", () => {
    const h = mount();
    choose(h, "priority", "urgent");
    return new Promise<void>(resolve => {
        setTimeout(() => {
            assert.strictEqual((readDraft(h) || {}).priority, "urgent");
            resolve();
        }, 600);
    });
});

test("a restored draft survives the next save", () => {
    // restoreDraft marks what it restored as touched; without that, the next
    // save would drop the very entries just recovered.
    const h = mount({ draft: { email: "a@b.co", subject: "Recovered" } });
    type(h, "name", "Jane");
    return new Promise<void>(resolve => {
        setTimeout(() => {
            const draft = readDraft(h) || {};
            assert.strictEqual(draft.email, "a@b.co");
            assert.strictEqual(draft.subject, "Recovered");
            assert.strictEqual(draft.name, "Jane");
            resolve();
        }, 600);
    });
});

test("degrades quietly when sessionStorage is unavailable", () => {
    // Private windows and blocked storage throw on access. The form must still
    // work, and the query-param prefill must still run.
    const h = mount({ url: `${PAGE_URL}?priority=urgent`, breakStorage: true });
    assert.strictEqual(h.control("priority").value, "urgent");
    type(h, "email", "a@b.co");
    assert.strictEqual(h.control("email").value, "a@b.co");
});

// --- Validation ----------------------------------------------------------

test("accepts a priority the layout renders but the module never hardcoded", async () => {
    // Guards the third sync point: front matter, the server enum, and the client.
    // If the client kept its own copy of the list, adding an option would make it
    // permanently unsubmittable with no server round trip to explain why.
    const h = mount({ extraPriorities: ["low"] });
    choose(h, "priority", "low");
    type(h, "email", "a@b.co");
    type(h, "name", "Jane");
    type(h, "organization", "example-corp");
    type(h, "subject", "Subject");
    type(h, "description", "A description well past ten characters.");
    await h.submit();
    assert.strictEqual(h.errorText("priority"), "");
    assert.strictEqual(h.fetchCalls.length, 1, "expected the submission to reach the API");
    assert.strictEqual(h.fetchCalls[0].body.priority, "low");
});

test("blocks submission and reports per-field errors", async () => {
    const h = mount();
    type(h, "email", "not-an-email");
    await h.submit();
    assert.match(h.errorText("email"), /valid email/i);
    assert.strictEqual(h.fetchCalls.length, 0, "an invalid form must not reach the API");
});

test("normalizes a pasted console URL to the bare organization name", async () => {
    const h = mount();
    type(h, "email", "a@b.co");
    type(h, "name", "Jane");
    type(h, "organization", "https://app.pulumi.com/example-corp/stacks/dev");
    type(h, "subject", "Subject");
    type(h, "description", "A description well past ten characters.");
    await h.submit();
    assert.strictEqual(h.errorText("organization"), "");
    assert.strictEqual(h.fetchCalls[0].body.organization, "example-corp");
});

test("rejects an over-long organization by length, not by character rules", () => {
    const h = mount();
    type(h, "organization", "a".repeat(41));
    h.control("organization").dispatchEvent(new h.win.Event("blur", { bubbles: true }));
    const form = h.doc.querySelector("[data-support-form]") as any;
    form.dispatchEvent(new h.win.Event("submit", { bubbles: true, cancelable: true }));
    const message = h.errorText("organization");
    assert.match(message, /characters/);
    assert.doesNotMatch(message, /hyphens/);
});

test("clears a field error once the user fixes it", () => {
    const h = mount();
    const form = h.doc.querySelector("[data-support-form]") as any;
    form.dispatchEvent(new h.win.Event("submit", { bubbles: true, cancelable: true }));
    assert.notStrictEqual(h.errorText("email"), "");
    type(h, "email", "a@b.co");
    assert.strictEqual(h.errorText("email"), "");
    assert.strictEqual(h.control("email").getAttribute("aria-invalid"), null);
});

// --- Submission ----------------------------------------------------------

function fillValid(h: Harness): void {
    type(h, "email", "a@b.co");
    type(h, "name", "Jane");
    type(h, "organization", "example-corp");
    type(h, "subject", "Subject");
    type(h, "description", "A description well past ten characters.");
}

test("posts JSON to the same-origin endpoint and shows the confirmation", async () => {
    const h = mount();
    fillValid(h);
    await h.submit();
    assert.strictEqual(h.fetchCalls[0].url, "/api/support");
    assert.strictEqual((h.doc.querySelector("[data-support-form-card]") as any).hidden, true);
    assert.strictEqual((h.doc.querySelector("[data-support-form-confirmation]") as any).hidden, false);
});

test("renders recap values as text, never as markup", async () => {
    // The recap echoes the user's own input back into the page. textContent is
    // what keeps that from being a self-XSS foothold via ?subject=.
    const h = mount();
    fillValid(h);
    type(h, "subject", "<img src=x onerror=alert(1)>");
    await h.submit();
    const slot = h.doc.querySelector('[data-support-form-value="subject"]') as any;
    assert.strictEqual(slot.textContent, "<img src=x onerror=alert(1)>");
    assert.strictEqual(slot.querySelector("img"), null, "the value must not have been parsed as HTML");
});

test("maps a 422 from the server back onto its fields", async () => {
    const h = mount();
    h.setFetch(async () => ({
        ok: false,
        status: 422,
        json: async () => ({ ok: false, error: "validation_failed", fields: { organization: "Server says no." } }),
    }));
    fillValid(h);
    await h.submit();
    assert.strictEqual(h.errorText("organization"), "Server says no.");
});

test("keeps the draft and shows the banner when the endpoint is unreachable", async () => {
    // PR previews and `make serve` have no /api/support origin. The entries must
    // survive so a retry doesn't cost the user their description.
    const h = mount();
    h.setFetch(async () => {
        throw new Error("network down");
    });
    fillValid(h);
    await h.submit();
    assert.strictEqual((h.doc.querySelector("[data-support-form-banner]") as any).hidden, false);
    assert.strictEqual((h.doc.querySelector("[data-support-form-confirmation]") as any).hidden, true);
    assert.strictEqual(h.control("description").value, "A description well past ten characters.");
});

test("omits the honeypot key entirely from a real submission", async () => {
    // An untouched honeypot is left out of the payload rather than sent empty,
    // so a genuine submission is byte-identical to one from a client that has
    // never seen the form — which is what the documented API shape describes.
    const h = mount();
    fillValid(h);
    await h.submit();
    assert.ok(!("website" in h.fetchCalls[0].body), "an empty honeypot must not appear in the payload");
});

// --- The layout half of the DOM contract ---------------------------------

test("the rendered layout still provides every id the module depends on", () => {
    // The fixture above is hand-written, so it could drift from the template that
    // actually renders the page. These ids are literal strings in the layout, so
    // checking them here catches a rename without needing a Hugo build.
    const fs = require("fs");
    const path = require("path");
    const layout = fs.readFileSync(
        path.join(__dirname, "..", "..", "layouts", "page", "support-new.html"),
        "utf8",
    );
    for (const id of [
        "support-email",
        "support-name",
        "support-organization",
        "support-priority",
        "support-subject",
        "support-description",
        "support-website",
    ]) {
        assert.ok(layout.includes(`id="${id}"`), `layout is missing id="${id}"`);
        assert.ok(layout.includes(`id="${id}-error"`) || id === "support-website", `layout is missing #${id}-error`);
    }
    for (const hook of [
        "data-support-form-root",
        "data-support-form-card",
        "data-support-form",
        "data-support-form-banner",
        "data-support-form-submit",
        "data-support-form-confirmation",
    ]) {
        assert.ok(layout.includes(hook), `layout is missing ${hook}`);
    }
});
