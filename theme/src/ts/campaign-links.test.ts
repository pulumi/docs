import * as assert from "assert";
import { test } from "node:test";

import { forwardDocsCampaignTags } from "./campaign-links";

const { JSDOM } = require("jsdom");

test("tagged docs links carry the five campaign values through install to Cloud signup", () => {
    const docs = new JSDOM('<a href="/docs/install/#linux">Install</a>', {
        url: "https://www.pulumi.com/docs/iac/?utm_source=email&utm_medium=newsletter&utm_campaign=A%2BB&utm_content=hero&utm_term=infra&gclid=private",
    });
    forwardDocsCampaignTags(docs.window.document);
    const tags = "utm_source=email&utm_medium=newsletter&utm_campaign=A%2BB&utm_content=hero&utm_term=infra";
    const install = docs.window.document.links[0].href;
    assert.strictEqual(install, "https://www.pulumi.com/docs/install/?" + tags + "#linux");

    const next = new JSDOM(
        '<a href="https://app.pulumi.com/signup?plan=team&utm_source=old#plans">Sign up</a><a href="/up/?language=go">Get started</a><a href="https://app.pulumi.com/signin/">Sign in</a>',
        { url: install },
    );
    forwardDocsCampaignTags(next.window.document);
    assert.deepStrictEqual(Array.from(next.window.document.links, (a: HTMLAnchorElement) => a.href), [
        "https://app.pulumi.com/signup?plan=team&" + tags + "#plans",
        "https://www.pulumi.com/up/?language=go&" + tags,
        "https://app.pulumi.com/signin/?" + tags,
    ]);
});

test("ignores untagged visits, Registry pages, and unrelated destinations", () => {
    for (const url of ["https://www.pulumi.com/docs/", "https://www.pulumi.com/registry/?utm_campaign=launch"]) {
        const doc = new JSDOM('<a href="/up/">Get started</a>', { url }).window.document;
        forwardDocsCampaignTags(doc);
        assert.strictEqual(doc.links[0].getAttribute("href"), "/up/");
    }
    const urls = ["/registry/", "/docs/iac/", "https://app.pulumi.com/org", "https://app.pulumi.com.example.org/signup", "https://get.pulumi.com/up/"];
    const doc = new JSDOM(urls.map(url => `<a href="${url}">Link</a>`).join(""), { url: "https://www.pulumi.com/docs/?utm_source=launch" }).window.document;
    forwardDocsCampaignTags(doc);
    assert.deepStrictEqual(Array.from(doc.links, (a: HTMLAnchorElement) => a.getAttribute("href")), urls);
});
