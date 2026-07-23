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
const EXPERIMENT_KEY = "20260723-mktg-ctas";

const VARIANT = {
    navHref: "/docs/iac/get-started",
    heroSecondaryText: "Download open source",
    heroSecondaryHref: "/docs/install/",
};

function applyMktgCtasVariant() {
    const urlVariant = getQueryVariable("variant-mktg-ctas");
    const showVariant = urlVariant ? urlVariant === "1" : gb.isOn(EXPERIMENT_KEY);
    if (!showVariant) {
        return;
    }

    // Top-nav "Get started" CTA (desktop + mobile sheet): repoint to the docs guide.
    document
        .querySelectorAll<HTMLAnchorElement>(
            'a[data-track="header-signup"], a[data-track="header-signup-mobile"]',
        )
        .forEach(cta => {
            cta.href = VARIANT.navHref;
        });

    // Homepage hero secondary button: swap "Contact us" for "Download open source".
    if (window.location.pathname === "/") {
        document
            .querySelectorAll<HTMLAnchorElement>('a[data-role="cta-get-started"]')
            .forEach(primary => {
                // The nav CTAs also carry data-role="cta-get-started"; we only want
                // the hero's primary button, so skip anything inside the header.
                if (primary.closest("header") || primary.closest("[data-nav-sheet]")) {
                    return;
                }
                const secondary =
                    primary.parentElement?.querySelector<HTMLAnchorElement>("a.btn-outline");
                if (secondary && /contact us/i.test(secondary.textContent || "")) {
                    secondary.textContent = VARIANT.heroSecondaryText;
                    secondary.href = VARIANT.heroSecondaryHref;
                }
            });
    }
}

// Re-run whenever GrowthBook (re)renders, e.g. once feature values have loaded.
gb.setRenderer(() => {
    applyMktgCtasVariant();
});

// Also run once directly: covers the `?variant-mktg-ctas=1` preview and the case
// where the renderer fires before the DOM is ready.
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyMktgCtasVariant);
} else {
    applyMktgCtasVariant();
}
