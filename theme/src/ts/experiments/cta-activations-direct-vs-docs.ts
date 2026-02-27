import { gb } from "../../../stencil/src/util/util";
import { getQueryVariable } from "../util";

gb.setRenderer(() => {
    const experimentKey = "cta-activations-direct-vs-docs";
    const featureKey = "20260226-cta-activations-direct-vs-docs";

    // If the feature is enabled or the URL contains a query variable matching the experiment key, apply the variant.
    if (gb.isOn(featureKey) || getQueryVariable(experimentKey) === "1") {

        // Find all CTA linkbuttons with the qualifying selector.
        document.querySelectorAll<HTMLAnchorElement>(`a[data-role="cta-get-started"]`).forEach(el => {

            // Update the button label and href to point to the Getting Started guide.
            el.textContent = "Get Started";
            el.title = "Get Started with Pulumi";
            el.href = "/docs/get-started/";

            // Remove the `target` and `rel` attributes. (We don't want to pop a new tab for these.)
            el.removeAttribute("target");
            el.removeAttribute("rel");
        });
    }
});
