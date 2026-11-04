// Tests for layouts/partials/gravity.html: the Gravity pixel must load only through
// the shared OneTrust gate (runWithPulumiConsent "C0004"), after window.load, once.
// Run: node --test scripts/gravity.test.js
const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const raw = fs.readFileSync(path.join(__dirname, "../layouts/partials/gravity.html"), "utf8");

// Render the Hugo template for one consent provider: drop the comment, keep the
// matching branch of the {{ if eq .consentProvider "onetrust" }} block.
function render(provider) {
    let s = raw.replace(/\{\{-? \/\*[\s\S]*?\*\/ -?\}\}/, "");
    s = s.replace(/\{\{- if eq \.consentProvider "onetrust" \}\}([\s\S]*?)\{\{- else \}\}([\s\S]*?)\{\{- end \}\}/,
        (_, onetrust, segment) => (provider === "onetrust" ? onetrust : segment));
    assert.ok(!s.includes("{{"), "unrendered template tags left");
    return s.replace(/<\/?script>/g, "");
}

function harness(provider) {
    const listeners = {}, scripts = [], gates = [], calls = [];
    let reloads = 0;
    const window = {
        location: { reload() { reloads++; } },
        addEventListener(name, fn) { listeners[name] = fn; },
        runWithPulumiConsent(category, fn) { gates.push({ category, fn }); },
    };
    const document = {
        createElement() { return {}; },
        getElementsByTagName() { return [{ parentNode: { insertBefore(s) { scripts.push(s); } } }]; },
    };
    window.window = window;
    vm.runInContext(render(provider), vm.createContext({ window, document, Date }));
    return {
        scripts, gates, calls, listeners,
        get reloads() { return reloads; },
        load() { listeners.load(); },
        grant() { gates.forEach((g) => g.fn()); calls.push(...((window.gravity && window.gravity.q) || [])); },
    };
}

test("nothing runs before window.load", () => {
    const h = harness("onetrust");
    assert.equal(h.gates.length, 0);
    assert.equal(h.scripts.length, 0);
    assert.ok(!("OneTrustGroupsUpdated" in h.listeners), "must not listen to OneTrust events directly");
});

test("after load it waits on the shared C0004 gate and injects nothing until granted", () => {
    const h = harness("onetrust");
    h.load();
    assert.equal(h.gates.length, 1);
    assert.equal(h.gates[0].category, "C0004");
    assert.equal(h.scripts.length, 0);
});

test("granting C0004 injects the pixel once and inits the advertiser id", () => {
    const h = harness("onetrust");
    h.load();
    h.grant();
    h.grant();
    assert.equal(h.scripts.length, 1);
    assert.equal(h.scripts[0].src, "https://code.trygravity.com/gr-pix.js");
    assert.deepEqual(Array.from(h.calls[0]), ["init", "f9505c8e-5d0b-4159-88b8-53bd2d5f2c8a"]);
    assert.equal(h.reloads, 0);
});

test("segment provider waits for consent-managed analytics, not the OneTrust gate", () => {
    const h = harness("segment");
    h.load();
    assert.equal(h.gates.length, 0);
    assert.equal(h.scripts.length, 0);
});
