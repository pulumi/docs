const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const test = require("node:test");
const source = fs.readFileSync('layouts/partials/gravity.html', "utf8").replace(/<\/?script>/g, "");
function harness(groups = "", readyState = "complete") {
    const listeners = {}, scripts = [], calls = [];
    let reloads = 0;
    const window = { OnetrustActiveGroups: groups, location: { reload() { reloads++; } }, addEventListener(name, fn) { listeners[name] = fn; } };
    const document = { readyState, createElement() { return {}; }, getElementsByTagName() { return [{ parentNode: { insertBefore(s) { scripts.push(s); } } }]; } };
    const context = vm.createContext({ window, document, Array, Date, gravity: (...args) => calls.push(args) });
    vm.runInContext(source, context);
    return { scripts, calls, get reloads() { return reloads; }, consent(groups) { listeners.OneTrustGroupsUpdated({ detail: groups }); }, load() { listeners.load(); } };
}
test("blocks Gravity until explicit advertising consent", () => {
    for (const groups of ["", "C0001,C0002", "C0003"]) {
        const h = harness(groups); h.load(); assert.equal(h.scripts.length, 0);
        h.consent(["C0004"]); assert.equal(h.scripts.length, 1);
        assert.equal(h.scripts[0].src, "https://code.trygravity.com/gr-pix.js");
        assert.equal(h.calls[0][1], "f9505c8e-5d0b-4159-88b8-53bd2d5f2c8a");
    }
});
test("defers preexisting permission until page load and initializes once", () => {
    const h = harness("C0001,C0004", "loading"); assert.equal(h.scripts.length, 0);
    h.load(); h.load(); h.consent(["C0004"]); assert.equal(h.scripts.length, 1); assert.equal(h.calls.length, 1);
});
test("withdrawal reloads and does not inject another pixel", () => {
    const h = harness("C0004"); h.consent(["C0001"]); assert.equal(h.reloads, 1); assert.equal(h.scripts.length, 1);
});
