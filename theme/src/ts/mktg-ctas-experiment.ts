import { gb } from "../../stencil/src/util/util";
import { getQueryVariable } from "./util";

// A/B test for the marketing CTA changes originally shipped in #20347:
//   - Top-nav "Get started" button destination
//   - Homepage hero secondary button
//
// Control (rendered server-side) is the pre-#20347 behavior. For the treatment
// bucket, this reapplies the #20347 changes on the client. Gated on the
// GrowthBook boolean feature `20260723-mktg-ctas`; preview the variant directly
// with `?variant-mktg-ctas=1`.
//
// Anti-flicker: on the homepage, an inline snippet in head.html hides the hero
// secondary CTA (via `mktg-ctas-pending` on <html>) before first paint so its
// label doesn't visibly flip. We reveal it here once the decision is final
// (GrowthBook features loaded, or a URL override). head.html also reveals after
// a 400ms timeout as a safety net, so a slow/blocked GrowthBook can never leave
// the button hidden.
const EXPERIMENT_KEY = "20260723-mktg-ctas";

const VARIANT = {
    navHref: "/docs/iac/get-started",
    heroSecondaryText: "Download open source",
    heroSecondaryHref: "/docs/install/",
};

function isVariant(): boolean {
    const urlVariant = getQueryVariable("variant-mktg-ctas");
    return urlVariant ? urlVariant === "1" : gb.isOn(EXPERIMENT_KEY);
}

// Apply the treatment (if bucketed) and reveal the held hero CTA. Runs only once
// the decision is final, so control and variant both reveal from here.
function applyAndReveal() {
    if (isVariant()) {
        // Top-nav "Get started" CTA (desktop + mobile sheet): repoint to the docs guide.
        document
            .querySelectorAll<HTMLAnchorElement>(
                'a[data-track="header-signup"], a[data-track="header-signup-mobile"]',
            )
            .forEach(cta => {
                cta.href = VARIANT.navHref;
            });

        // Homepage hero secondary: swap "Contact us" for "Download open source".
        if (window.location.pathname === "/") {
            document
                .querySelectorAll<HTMLAnchorElement>('a[data-role="cta-secondary"]')
                .forEach(secondary => {
                    if (/contact us/i.test(secondary.textContent || "")) {
                        secondary.textContent = VARIANT.heroSecondaryText;
                        secondary.href = VARIANT.heroSecondaryHref;
                    }
                });
        }
    }

    // Reveal the held hero secondary (both arms) now that the decision is applied.
    document.documentElement.classList.remove("mktg-ctas-pending");
}

function whenDomReady(fn: () => void) {
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", fn, { once: true });
    } else {
        fn();
    }
}

// Flag path: GrowthBook calls the renderer once feature values have loaded, so
// the decision is final here for both control and variant.
gb.setRenderer(() => {
    whenDomReady(applyAndReveal);
});

// URL-override preview (`?variant-mktg-ctas=1`): apply immediately without
// waiting for GrowthBook.
if (getQueryVariable("variant-mktg-ctas")) {
    whenDomReady(applyAndReveal);
}
