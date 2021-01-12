import { Component, Prop, h, State } from '@stencil/core';
import { waitForWindowPropertyToExist, parseCookie, parseUTMCookieString, waitForElementToExist } from "../../util/util";

@Component({
    tag: 'pulumi-hubspot-form',
    styleUrl: 'hubspot-form.scss',
    shadow: false
})
export class HubspotForm {
    // The formId is the HubSpot defined form ID this form will submit to.
    @Prop()
    formId: string;

    // The goToWebinarKey is used to automatically register users for a webinar
    // after they submit a form (optional).
    @Prop()
    goToWebinarKey?: string;

    // The class name to be applied to the form (optional).
    @Prop()
    class?: string;

    // isLoading lets us know if the form is loading.
    @State()
    isLoading: boolean = true;

    // didLoad lets us know if the form successfully loaded.
    @State()
    didLoad: boolean = false;

    // The window event listener used to handle submitting form data to Segment.
    windowEventHandler: (this: Window, ev: MessageEvent) => any;

    // When the component loads we need to wait for the 'hbspt' property to
    // propagate up to the global window object. Then once it is available
    // we should create the HubSpot form.
    componentDidLoad() {
        const hsFormTargetId = `#hubspotForm_${this.formId}`;

        waitForWindowPropertyToExist("hbspt").then((hbspt: any) => {
            hbspt.forms.create({
                portalId: "4429525",
                formId: this.formId,
                css: "",
                cssClass: this.class,
                goToWebinarWebinarKey: this.goToWebinarKey,
                target: hsFormTargetId,
            });
            this.isLoading = false;
            this.didLoad = true;

            // Hidden form fields from HubSpot created forms causes gaps to appear in
            // the form which is less then desirable. So we need to find the hidden
            // form fields and then hide the parent <fieldset> for it. We will also need
            // to populate those fields with the correct values.
            waitForElementToExist(`${hsFormTargetId} form div[class="input"]`).then(() => {
                const fieldSets = document.querySelectorAll(`${hsFormTargetId} form fieldset div[style*="display:none"]`);
                fieldSets.forEach((fieldset: any) => {
                    fieldset.parentElement.style.display = "none";
                });

                // Populate the UTM parameter fields.
                const cookies = parseCookie();
                const utmCookie: any = parseUTMCookieString(cookies["__utmzz"]);
                const utmCampaign = utmCookie.utmccn || "(not set)";
                const utmSource = utmCookie.utmcsr || "(direct)";
                const utmMedium = utmCookie.utmcmd || "(none)";

                const utmCampaignInput = document.querySelector<HTMLInputElement>(`${hsFormTargetId} input[name="last_utm_campaign"]`);
                if (utmCampaignInput) {
                    utmCampaignInput.value = utmCampaign;
                }

                const utmSourceInput = document.querySelector<HTMLInputElement>(`${hsFormTargetId} input[name="last_utm_source"]`);
                if (utmSourceInput) {
                    utmSourceInput.value = utmSource;
                }

                const utmMediumInput = document.querySelector<HTMLInputElement>(`${hsFormTargetId} input[name="last_utm_medium"]`);
                if (utmMediumInput) {
                    utmMediumInput.value = utmMedium;
                }
            });
        }).catch((err) => {
            this.isLoading = false;
            console.log("Unable to load HubSpot form.");
            console.log(err);
        });

        // Listen for the HubSpot form to be loaded.
        this.windowEventHandler = this.handleWindowMessage.bind(this);
        window.addEventListener("message", this.windowEventHandler);
    }

    disconnectedCallback() {
        window.removeEventListener("message", this.windowEventHandler);
    }

    private handleWindowMessage(event: MessageEvent) {
        if (event.data.type === "hsFormCallback" && event.data.eventName === "onFormReady") {
            const form = document.querySelector("form.hs-form") as HTMLFormElement;
            form.addEventListener("submit", () => this.handleFormSubmission(form.getAttribute("data-form-id")));
        }
    }

    // When the form is submitted we also send an event to Segment with the relevant UTM tags.
    private handleFormSubmission(formId: string) {
        const analytics = (window as any).analytics;
        const analyticsAvailable = analytics && analytics.track && (typeof analytics.track === "function");

        if (analyticsAvailable) {
            const cookies = parseCookie();
            const utmCookie: any = parseUTMCookieString(cookies["__utmzz"]);
            const email = document.querySelector("form.hs-form input[name='email']") as HTMLInputElement;

            const submissionData = {
                formId: formId,
                email: email.value,
                utmCampaign: utmCookie.utmccn || "(not set)",
                utmSource: utmCookie.utmcsr || "(direct)",
                utmMedium: utmCookie.utmcmd || "(none)",
            };

            analytics.track("form-submission", submissionData);
        }
    }

    renderIsLoadingForm() {
        return(
            <div>
                <i class="fa fa-spinner fa-spin mr-2"></i>
                <span>Loading Form</span>
            </div>
        );
    }

    renderFailedToLoadForm() {
        return(
            <div>
                There was an issue loading this form. Please try and refresh
                your browser. If you continuing running into an issue please reach
                out to support@pulumi.com.
            </div>
        );
    }

    render() {
        return [
            <script src="//js.hsforms.net/forms/v2.js"></script>,
            <div id={`hubspotForm_${this.formId}`}>
                { !this.didLoad && !this.isLoading ? this.renderFailedToLoadForm() : this.renderIsLoadingForm() }
            </div>
        ];
    }
}
