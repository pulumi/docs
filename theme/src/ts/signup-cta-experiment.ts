import { gb } from "../../stencil/src/util/util";
import { getQueryVariable } from "./util";

const EXPERIMENT_KEY = "20250224-signup-cta-get-started";

function runSignupCtaExperiment() {
    const urlVariant = getQueryVariable("variant-signup-cta");
    const showGetStarted = urlVariant ? urlVariant === "1" : gb.isOn(EXPERIMENT_KEY);

    // Desktop: header-cta Stencil component renders an <a> with data-track="header-signup"
    const desktopCtas = document.querySelectorAll<HTMLAnchorElement>('a[data-track="header-signup"]');
    desktopCtas.forEach(cta => {
        if (showGetStarted) {
            cta.textContent = "Get Started";
            cta.href = "https://www.pulumi.com/docs/get-started/";
            cta.title = "Get started with Pulumi";
        } else {
            cta.textContent = "Sign up";
            cta.href = "https://app.pulumi.com/signup?utm_source=header-button";
            cta.title = "Sign up";
        }
    });

    // Mobile: header sign-up link with data-track="header-signup-mobile"
    const mobileCtas = document.querySelectorAll<HTMLAnchorElement>('a[data-track="header-signup-mobile"]');
    mobileCtas.forEach(cta => {
        if (showGetStarted) {
            cta.textContent = " Get Started ";
            cta.href = "https://www.pulumi.com/docs/get-started/";
            cta.title = "Get started with Pulumi";
        } else {
            cta.textContent = " Sign Up ";
            cta.href = "https://app.pulumi.com/signup";
            cta.title = "Sign up for Pulumi Cloud";
        }
    });
}

gb.setRenderer(() => {
    runSignupCtaExperiment();
});
