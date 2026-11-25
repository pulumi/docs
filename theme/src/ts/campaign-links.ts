const campaignKeys = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];

export function forwardDocsCampaignTags(doc: Document) {
    const { pathname, origin, search } = doc.location;
    if (!/^\/docs(?:\/|$)/.test(pathname)) return;

    const incoming = new URLSearchParams(search);
    const campaign = new URLSearchParams();
    for (const key of campaignKeys) {
        const value = incoming.get(key);
        if (value) campaign.set(key, value);
    }
    if (!campaign.toString()) return;

    function decorate(link: HTMLAnchorElement) {
        const consoleEntry = link.origin === "https://app.pulumi.com" && /^\/(signin|signup)\/?$/.test(link.pathname);
        const marketingEntry = (link.origin === origin || link.origin === "https://www.pulumi.com") && /^\/(up|docs\/install)\/?$/.test(link.pathname);
        if (!consoleEntry && !marketingEntry) return;

        const url = new URL(link.href);
        campaign.forEach((value, key) => url.searchParams.set(key, value));
        if (url.href !== link.href) link.href = url.href;
    }

    doc.querySelectorAll<HTMLAnchorElement>("a[href]").forEach(decorate);
    function onActivate(event: Event) {
        if (event.target instanceof Element) {
            const link = event.target.closest<HTMLAnchorElement>("a[href]");
            if (link) decorate(link);
        }
    }
    for (const type of ["click", "auxclick", "contextmenu"]) {
        doc.addEventListener(type, onActivate, true);
    }
}
