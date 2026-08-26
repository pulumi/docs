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
            <label for="support-leave-blank">Leave this field empty</label>
            <input id="support-leave-blank" name="leave_blank" type="text" tabindex="-1" autocomplete="off">
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
// The window from the previous mount, so it can be torn down before the next
// one. This matters more than it looks: the module reads a BARE global
// sessionStorage, and mount() re-points that global at each new window. A
// pending 500ms draft-save timer left behind by an earlier test therefore fires
// during a later one and writes the OLD form's values into the NEW test's
// storage -- every draft assertion downstream is then reading another test's
// work. jsdom's window.close() drops the timers with the window.
let previousWindow: any;

function mount(options: { url?: string; draft?: any; extraPriorities?: string[]; breakStorage?: boolean } = {}): Harness {
    if (previousWindow) {
        previousWindow.close();
    }
    const dom = new JSDOM(`<!doctype html><body>${formHtml(options.extraPriorities)}</body>`, {
        url: options.url || PAGE_URL,
    });
    const win = dom.window;
    previousWindow = win;

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
    const h = mount({ url: `${PAGE_URL}?priority=bogus&subject=FromUrl` });
    // Left on the default rather than blanked — assigning an unmatched value to
    // a <select> would silently clear it and post an empty priority.
    assert.strictEqual(h.control("priority").value, "normal");
    // Positive control: "priority is still normal" is also what you would see
    // if the module never ran at all, since normal is the rendered default. The
    // subject proves the prefill did run and declined this one value.
    assert.strictEqual(h.control("subject").value, "FromUrl", "the prefill must have run at all");
});

// --- Draft vs. prefill ---------------------------------------------------

test("a recovered draft outranks the query string", () => {
    const h = mount({ url: `${PAGE_URL}?priority=urgent&subject=FromUrl`, draft: { priority: "normal", subject: "FromDraft" } });
    assert.strictEqual(h.control("subject").value, "FromDraft");
    assert.strictEqual(h.control("priority").value, "normal");
});

test("a priority the user chose themselves survives a return to the same link", async () => {
    // The mirror of the prefill bug, driven the way it actually happens rather
    // than from a hand-written draft — which would just re-test the precedence
    // above. A visitor opens ?priority=urgent, decides it is not urgent, and
    // picks "normal": that choice has to reach the draft (it is the default
    // value, so only the touched set distinguishes it from an untouched
    // control) and then outrank the same query string on the way back.
    const first = mount({ url: `${PAGE_URL}?priority=urgent` });
    assert.strictEqual(first.control("priority").value, "urgent", "the prefill must have applied");

    choose(first, "priority", "normal");
    await new Promise(resolve => setTimeout(resolve, 600)); // the 500ms save debounce

    const draft = readDraft(first);
    assert.ok(draft, "the choice must have been saved");
    assert.strictEqual(draft.priority, "normal", "a chosen default still counts as touched");

    const second = mount({ url: `${PAGE_URL}?priority=urgent`, draft });
    assert.strictEqual(second.control("priority").value, "normal", "the URL must not reinstate urgent");
});

test("a stale draft option does not suppress the query-string prefill", () => {
    // A draft can name an option the page no longer renders. Counting that as
    // "restored" would make the draft outrank the URL for a value the control
    // never actually took, so someone following an urgent link would file a
    // normal ticket.
    const h = mount({ url: `${PAGE_URL}?priority=urgent`, draft: { priority: "high" } });
    assert.strictEqual(h.control("priority").value, "urgent");
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
    assert.ok(!("leave_blank" in h.fetchCalls[0].body), "an empty honeypot must not appear in the payload");
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
        "support-leave-blank",
    ]) {
        assert.ok(layout.includes(`id="${id}"`), `layout is missing id="${id}"`);
        assert.ok(layout.includes(`id="${id}-error"`) || id === "support-leave-blank", `layout is missing #${id}-error`);
    }
    for (const hook of [
        "data-support-form-root",
        "data-support-form-card",
        "data-support-form-banner",
        "data-support-form-submit",
        "data-support-form-confirmation",
        "data-support-form-counter",
        "data-support-form-value",
    ]) {
        assert.ok(layout.includes(hook), `layout is missing ${hook}`);
    }

    // The bare hook needs its own assertion, anchored to the <form> tag.
    // includes("data-support-form") can never fail -- it is a prefix of all
    // seven hooks above -- and even a delimiter check passes on the layout's
    // own comment, which mentions the "data-support-form*" attributes in prose.
    // Meanwhile this is the most consequential attribute on the page: without
    // it the module returns immediately and the entire form is inert.
    assert.ok(
        /<form[^>]*\sdata-support-form(?![\w-])/.test(layout),
        "the <form> is missing the bare data-support-form hook — the module would not bind at all");

    // Tag identity, not just the id. A <select> turned into an <input> keeps
    // every id intact while silently killing the option-matching that both the
    // prefill and the priority validator depend on.
    assert.ok(
        /<select[^>]*id="support-priority"/.test(layout),
        "support-priority must be a <select> — the prefill and validator match against its options");
    assert.ok(
        /<textarea[^>]*id="support-description"/.test(layout),
        "support-description must be a <textarea>");

    // The options must carry explicit values; without them every priority
    // becomes its label text and ?priority=urgent stops matching.
    assert.ok(
        /<option value="\{\{ \.value \}\}"/.test(layout),
        "priority options must render an explicit value attribute");

    // The honeypot's name is the field the handler drops on, so it is part of
    // the contract even though no JS reads it.
    assert.ok(
        /id="support-leave-blank"[^>]*name="leave_blank"/.test(layout),
        "the honeypot must keep a name with no autofill semantics");
    assert.ok(
        /id="support-leave-blank"[^>]*autocomplete="off"/.test(layout),
        "the honeypot must opt out of autofill — the other half of the same mitigation");
});

// --- The client half of the honeypot -------------------------------------

test("forwards a filled honeypot so the server can drop it", () => {
    // The absence check above only proves a clean submission stays clean. If
    // this half were deleted the server's honeypot would still be well tested
    // and would still never fire, because the browser would stop sending the
    // signal at all.
    return (async () => {
        const h = mount();
        fillValid(h);
        const honeypot = h.control("leave-blank");
        honeypot.value = "http://spam.example.com";
        honeypot.dispatchEvent(new h.win.Event("input", { bubbles: true }));
        await h.submit();
        assert.strictEqual(h.fetchCalls[0].body.leave_blank, "http://spam.example.com");
    })();
});

// --- Draft lifecycle ------------------------------------------------------

// Saving is debounced by 500ms, so these seed sessionStorage directly rather
// than typing and racing the timer — what is under test is what happens to an
// existing draft at the end of a submission, not when it was written.
test("clears the draft once the request is filed", async () => {
    const h = mount({ draft: { subject: "FromDraft" } });
    assert.ok(readDraft(h), "the draft should exist before submitting");
    fillValid(h);
    await h.submit();
    assert.strictEqual(readDraft(h), undefined, "a filed request must not leave a draft behind");
});

test("keeps the draft when the request fails", async () => {
    const h = mount({ draft: { subject: "FromDraft" } });
    fillValid(h);
    h.setFetch(async () => {
        throw new Error("network down");
    });
    await h.submit();
    assert.ok(readDraft(h), "a failed submission must keep the user's work");
});

// --- Failure reporting ----------------------------------------------------

test("shows the banner on a non-422 failure", async () => {
    const h = mount();
    fillValid(h);
    h.setFetch(async () => ({
        ok: false,
        status: 503,
        json: async () => ({ ok: false, error: "unavailable" }),
    }));
    await h.submit();
    const banner = h.doc.querySelector("[data-support-form-banner]") as any;
    assert.strictEqual(banner.hidden, false, "a 503 must be reported, not swallowed");
});

test("shows the banner when a 422 names a field the page does not render", async () => {
    // The server can reject the payload as a whole (_form), which maps to no
    // input. Without the banner the form would appear to do nothing at all.
    const h = mount();
    fillValid(h);
    h.setFetch(async () => ({
        ok: false,
        status: 422,
        json: async () => ({ ok: false, fields: { _form: 'Unexpected field "nope".' } }),
    }));
    await h.submit();
    const banner = h.doc.querySelector("[data-support-form-banner]") as any;
    assert.strictEqual(banner.hidden, false, "a form-level 422 must surface somewhere");
});

// --- Double submission ----------------------------------------------------

test("files one ticket even if submit fires twice while in flight", async () => {
    const h = mount();
    fillValid(h);

    let release: () => void = () => undefined;
    const gate = new Promise<void>(resolve => {
        release = resolve;
    });
    h.setFetch(async () => {
        await gate;
        return { ok: true, status: 200, json: async () => ({ ok: true, id: "req-1", ticketId: "t-1" }) };
    });

    const form = h.doc.querySelector("[data-support-form]") as any;
    form.dispatchEvent(new h.win.Event("submit", { bubbles: true, cancelable: true }));
    form.dispatchEvent(new h.win.Event("submit", { bubbles: true, cancelable: true }));
    release();
    await new Promise(resolve => setTimeout(resolve, 0));

    assert.strictEqual(h.fetchCalls.length, 1, "a second submit while one is in flight must not file a duplicate");
});

// --- Duplicate-submission surfaces ---------------------------------------

test("clears the controls on success, so a Back navigation cannot resubmit", async () => {
    // sessionStorage is cleared, but browsers restore form state themselves on
    // a Back navigation to this history entry. Without an explicit reset the
    // visitor lands on a fully repopulated form with nothing saying the request
    // was already filed -- one click from a duplicate ticket.
    const h = mount();
    fillValid(h);
    await h.submit();

    for (const field of ["email", "name", "organization", "subject", "description"]) {
        assert.strictEqual(h.control(field).value, "", `${field} must be cleared after a successful submit`);
    }
});

test("a pending draft save cannot resurrect the draft after success", async () => {
    // saveDraft is debounced by 500ms. A submit inside that window used to have
    // the timer fire after clearDraft() and write the draft straight back, so a
    // filed request was waiting in the form on the next visit.
    const h = mount();
    fillValid(h);              // schedules a save 500ms out
    await h.submit();          // resolves immediately; clearDraft runs first
    await new Promise(resolve => setTimeout(resolve, 700));

    assert.strictEqual(readDraft(h), undefined, "the debounced save must have been cancelled");
});

// --- Client/server parity ------------------------------------------------

test("normalizes every console-URL shape the server does", () => {
    const h = mount();
    for (const pasted of [
        "https://app.pulumi.com/my-org/stacks/dev",
        "https://www.app.pulumi.com/my-org",
        "app.pulumi.com/my-org",
        "www.app.pulumi.com/my-org",
        "/my-org",
    ]) {
        const org = h.control("organization");
        org.value = pasted;
        org.dispatchEvent(new h.win.Event("blur", { bubbles: true }));
        assert.strictEqual(org.value, "my-org", `${pasted} must normalize to the bare org name`);
        assert.strictEqual(h.errorText("organization"), "", `${pasted} must not be reported as invalid`);
    }
});

test("mirrors the server's length caps rather than posting a doomed payload", async () => {
    // Reachable by prefill and by programmatic fill, both of which bypass the
    // layout's maxlength. Without the mirror these cost a round trip and come
    // back as a 422 the client could have prevented.
    const cases: Array<[string, string]> = [
        ["subject", "a".repeat(201)],
        ["name", "a".repeat(201)],
        ["description", "a".repeat(20001)],
    ];

    for (const [field, value] of cases) {
        const h = mount();
        fillValid(h);
        const input = h.control(field);
        input.value = value;
        input.dispatchEvent(new h.win.Event("input", { bubbles: true }));
        await h.submit();

        assert.strictEqual(h.fetchCalls.length, 0, `an over-long ${field} must not be posted`);
        assert.ok(h.errorText(field), `an over-long ${field} must be reported`);
    }
});

test("refreshes the character counter after a draft restore", () => {
    // The counter runs once at init, before the draft is restored, so a
    // restored long description left it hidden and reading the full limit
    // until the next keystroke.
    const h = mount({ draft: { description: "a".repeat(19000) } });
    const counter = h.doc.querySelector("[data-support-form-counter]") as any;
    assert.strictEqual(counter.hidden, false, "a near-limit restored value must show the counter");
    assert.strictEqual(counter.textContent, "1,000 characters left");
});

// --- The prefill parameters are consumed, not left in the URL --------------

test("strips the prefill parameters from the address bar once applied", () => {
    // They are a handoff mechanism, not state. Left in place they ride along in
    // the referrer, re-apply on a Back navigation after the request was already
    // filed, and lose a ?priority=urgent to the browser's own form restore.
    const h = mount({ url: `${PAGE_URL}?priority=urgent&subject=CLI+crash&email=a%40b.co` });

    assert.strictEqual(h.control("priority").value, "urgent", "the prefill must still be applied");
    assert.strictEqual(h.control("subject").value, "CLI crash");
    assert.strictEqual(h.win.location.search, "", "the parameters must not survive in the URL");
    assert.strictEqual(h.win.location.pathname, "/support/new/", "the path must be unchanged");
});

test("leaves a parameterless URL alone", () => {
    const h = mount();
    assert.strictEqual(h.win.location.search, "");
    assert.strictEqual(h.win.location.pathname, "/support/new/");
});

// --- What the confirmation shows is what was filed -------------------------

test("sanitizes the payload, so the recap cannot show what the ticket will not contain", async () => {
    const h = mount();
    fillValid(h);
    type(h, "subject", "harmless text\rMALICIOUS \u202Ekcatta\u202C");
    await h.submit();

    const sent = h.fetchCalls[0].body.subject;
    assert.strictEqual(sent.indexOf("\r"), -1, "a bare CR must not reach the ticket");
    assert.strictEqual(sent.indexOf("\u202E"), -1, "a bidi override must not reach the ticket");

    const recap = h.doc.querySelector('[data-support-form-value="subject"]') as any;
    assert.strictEqual(recap.textContent, sent, "the recap must show exactly what was filed");
});

// --- The honeypot's name is part of the defence ----------------------------

test("keeps the honeypot on a name autofill will not recognise", () => {
    // As "website" it was a prime autofill target -- password managers store
    // website URLs and match on the field name -- and an autofilled trap
    // destroys a real request: the user is shown the confirmation, their draft
    // is deleted, and no ticket exists.
    const h = mount();
    const honeypot = h.control("leave-blank");
    assert.ok(honeypot, "the honeypot must exist");
    assert.strictEqual(honeypot.name, "leave_blank");
    assert.strictEqual(honeypot.getAttribute("autocomplete"), "off", "the honeypot opts out of autofill");
    assert.strictEqual(h.doc.getElementById("support-website"), null, "the autofill-prone name must be gone");
});

test("validates the same string it posts, not the raw control value", async () => {
    // A value at the limit padded with a character the sanitizer strips. Reading
    // the raw value made the client stricter than the API here (blocked at 201
    // for a string the server would have measured as 200) and looser on the
    // minimum, which is the round trip the mirroring exists to save.
    const h = mount();
    fillValid(h);
    const subject = h.control("subject");
    subject.value = "a".repeat(200) + "\u0000";
    subject.dispatchEvent(new h.win.Event("input", { bubbles: true }));
    await h.submit();

    assert.strictEqual(h.errorText("subject"), "", "a value that sanitizes to the limit must be accepted");
    assert.strictEqual(h.fetchCalls.length, 1, "and must actually be posted");
    assert.strictEqual(h.fetchCalls[0].body.subject.length, 200);

    // The other direction: long enough only because of characters that get stripped.
    const h2 = mount();
    fillValid(h2);
    const description = h2.control("description");
    description.value = "abcdefg" + "\u0000".repeat(5);
    description.dispatchEvent(new h2.win.Event("input", { bubbles: true }));
    await h2.submit();

    assert.ok(h2.errorText("description"), "a description only long enough before sanitizing must be caught here");
    assert.strictEqual(h2.fetchCalls.length, 0, "and must not cost a round trip");
});
