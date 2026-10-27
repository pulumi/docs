// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for consent-gated YouTube embeds, run against jsdom with the real
// OneTrust bridge. From the theme directory:
//
//     yarn test-ts
//
// The page is built the way head.html builds it under the onetrust provider:
// the inline bootstrap queues runWithPulumiConsent calls, and
// installOneTrustBridge() takes over and replays them. Consent changes are
// driven through OneTrust's own globals and the OneTrustGroupsUpdated event.

import * as assert from "assert";
import { test } from "node:test";

import { installOneTrustBridge } from "./consent-manager/onetrust";

const { JSDOM } = require("jsdom");

const MODULE_PATH = "./consent-media";
const VIDEO_URL = "https://www.youtube-nocookie.com/embed/abc123";

interface Harness {
    win: any;
    iframe: HTMLIFrameElement;
    srcWrites: string[];
    setGroups: (groups: string) => void;
    installBridge: () => void;
    rescan: () => void;
}

let previousWindow: any;

async function mount(): Promise<Harness> {
    if (previousWindow) {
        previousWindow.close();
    }
    const dom = new JSDOM(`<!doctype html><body><iframe title="video" data-pulumi-consent-src="${VIDEO_URL}"></iframe></body>`, {
        url: "https://www.pulumi.com/blog/some-post/",
    });
    const win = dom.window;
    previousWindow = win;

    // head.html's onetrust bootstrap, verbatim in behavior.
    const queue = (win.__pulumiConsentQueue = [] as any[]);
    win.runWithPulumiConsent = (category: string, callback: () => void) => {
        queue.push({ category, callback });
    };
    win.OptanonWrapper = () => win.dispatchEvent(new win.Event("OneTrustGroupsUpdated"));

    const iframe = win.document.querySelector("iframe") as HTMLIFrameElement;

    // Record every assignment to src, so "only once" means one write, not
    // merely "ends with the right value".
    const srcWrites: string[] = [];
    const proto = Object.getPrototypeOf(iframe);
    const desc = Object.getOwnPropertyDescriptor(win.HTMLIFrameElement.prototype, "src") || Object.getOwnPropertyDescriptor(proto, "src");
    Object.defineProperty(iframe, "src", {
        configurable: true,
        get() {
            return desc.get.call(this);
        },
        set(value: string) {
            srcWrites.push(value);
            desc.set.call(this, value);
        },
    });

    const g: any = globalThis;
    g.window = win;
    g.document = win.document;

    // Let jsdom finish parsing so the module activates synchronously on require.
    if (win.document.readyState === "loading") {
        await new Promise(resolve => win.document.addEventListener("DOMContentLoaded", resolve));
    }

    delete require.cache[require.resolve(MODULE_PATH)];
    const mod = require(MODULE_PATH);

    return {
        win,
        iframe,
        srcWrites,
        setGroups: groups => {
            win.OptanonActiveGroups = groups;
            win.OptanonWrapper();
        },
        installBridge: () => installOneTrustBridge(win),
        rescan: () => mod.activateConsentMedia(),
    };
}

test("iframe src stays unset until OneTrust resolves", async () => {
    const h = await mount();
    h.installBridge();
    assert.strictEqual(h.iframe.getAttribute("src"), null);
    assert.strictEqual(h.iframe.dataset.pulumiConsentSrc, VIDEO_URL);
    assert.strictEqual(h.srcWrites.length, 0);
});

test("iframe src stays unset while C0004 is withheld, even with other categories granted", async () => {
    const h = await mount();
    h.installBridge();
    h.setGroups(",C0001,C0002,C0003,");
    assert.strictEqual(h.iframe.getAttribute("src"), null);
    assert.strictEqual(h.iframe.dataset.pulumiConsentSrc, VIDEO_URL);
    assert.strictEqual(h.srcWrites.length, 0);
});

test("iframe src is set from data-pulumi-consent-src once C0004 is granted", async () => {
    const h = await mount();
    h.installBridge();
    h.setGroups(",C0001,");
    h.setGroups(",C0001,C0004,");
    assert.strictEqual(h.iframe.getAttribute("src"), VIDEO_URL);
    assert.strictEqual(h.iframe.hasAttribute("data-pulumi-consent-src"), false);
    assert.deepStrictEqual(h.srcWrites, [VIDEO_URL]);
});

test("a call queued before the bridge installs loads when C0004 is granted", async () => {
    // The module ran against the bootstrap queue; the bridge replays it.
    const h = await mount();
    h.win.OptanonActiveGroups = ",C0001,C0004,";
    h.installBridge();
    assert.strictEqual(h.iframe.getAttribute("src"), VIDEO_URL);
    assert.deepStrictEqual(h.srcWrites, [VIDEO_URL]);
});

test("repeated grants, revoke/regrant, and rescans assign src only once", async () => {
    const h = await mount();
    h.installBridge();
    // A rescan before consent queues a second loader for the same iframe.
    h.rescan();
    h.setGroups(",C0001,C0004,");
    h.setGroups(",C0001,C0004,");
    h.setGroups(",C0001,");
    h.setGroups(",C0001,C0004,");
    h.rescan();
    assert.deepStrictEqual(h.srcWrites, [VIDEO_URL]);
    assert.strictEqual(h.iframe.getAttribute("src"), VIDEO_URL);
});
