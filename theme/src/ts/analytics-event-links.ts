// Generic click tracking for links that need a distinct, named Segment event
// rather than the ambient "link-click" event tracking.ts fires for every
// anchor on the page. Add data-analytics-event="some-event-name" to any
// anchor and a click on it fires analytics.track("some-event-name", ...)
// with no page-specific JS required.
//
// Does not call preventDefault: navigation (including a cross-domain link)
// proceeds exactly as it would without the attribute.
//
// Anchors are bound once at DOMContentLoaded, so this covers server-rendered
// markup only -- links painted later by a Stencil component (for example, a
// pulumi-multi-select-form CTA) won't be tracked.

document.addEventListener("DOMContentLoaded", () => {
    const analytics = (window as any).analytics;
    const analyticsAvailable = analytics && analytics.track && typeof analytics.track === "function";

    document.querySelectorAll<HTMLAnchorElement>("[data-analytics-event]").forEach(link => {
        link.addEventListener("click", () => {
            const eventName = link.getAttribute("data-analytics-event");
            const trackingData = {
                destinationPath: link.getAttribute("href"),
                url: window.location.pathname,
            };

            if (analyticsAvailable) {
                analytics.track(eventName, trackingData);
            } else {
                console.log("Skipped call to analytics.track:", eventName, trackingData);
            }
        });
    });
});
