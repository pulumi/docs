import { Component, Element, h, Prop, State, } from '@stencil/core';
import { parseCookie, parseUTMCookieString, getQueryVariable } from "../../util/util";

interface UTMData {
    campaign: string;
    source: string;
    medium: string;
}

// The types of form events we expect to receive from HubSpot.
// https://legacydocs.hubspot.com/docs/methods/forms/advanced_form_options
type HubSpotFormEvent = "onBeforeFormInit" | "onBeforeValidationInit" | "onFormReady" | "onFormSubmit" | "onFormDefinitionFetchError";

@Component({
    tag: "pulumi-hubspot-form",
    styleUrl: "hubspot-form.scss",
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

    // Whether the HubSpot form is loading.
    @State()
    isLoading: boolean = true;

    // Whether the HubSpot form was successfully loaded.
    @State()
    didLoad: boolean = false;

    @Element()
    el: HTMLElement;

    // The HTML element that will contain the HubSpot form.
    hubspotFormTargetId: string;

    // The handler for HubSpot window messages.
    messageHandler: (event: MessageEvent) => void;

    componentDidLoad() {

        if (!this.formId) {
            throw new Error("The required attribute `form-id` was not provided.");
        }

        this.hubspotFormTargetId = `hubspotForm_${this.formId}`;

        // Check for an existing HubSpot global. If there isn't one already, load
        // the HubSpot form script dynamically.
        const hubspotGlobal = window["hbspt"];
        if (hubspotGlobal) {
            this.createForm(hubspotGlobal);
        } else {
            this.loadHubSpotFormsScript();
        }

        // Register for window messages from HubSpot.
        this.messageHandler = this.onMessage.bind(this);
        window.addEventListener("message", this.messageHandler);
    }

    disconnectedCallback() {
        window.removeEventListener("message", this.messageHandler);
    }

    // HubSpot form events are dispatched as window message events.
    private onMessage(event: MessageEvent) {

        // Ignore any non-HubSpot-form-related events.
        if (event.data?.type !== "hsFormCallback") {
            return;
        }

        const eventName: HubSpotFormEvent = event.data.eventName;
        const utmData = this.getUTMCookieData();

        // When the form is ready, update its hidden fields with UTM values.
        if (eventName === "onFormReady") {
            this.isLoading = false;
            this.didLoad = true;

            // Hidden form fields end up wrapped in divs with display:none, which leaves their parent
            // fieldsets taking up vertical space for no reason. So we hide those as well.
            const hiddenFields = this.el.querySelectorAll(`input[type="hidden"]`);
            hiddenFields.forEach((field: HTMLInputElement) => {
                const fieldset = field.closest("fieldset");
                if (fieldset) {
                    fieldset.style.display = "none";
                }
            });

            const utmCampaignInput: HTMLInputElement = this.el.querySelector(`input[name="last_utm_campaign"]`);
            if (utmCampaignInput) {
                utmCampaignInput.value = utmData.campaign;
            }

            const utmSourceInput: HTMLInputElement = this.el.querySelector(`input[name="last_utm_source"]`);
            if (utmSourceInput) {
                utmSourceInput.value = utmData.source;
            }

            const utmMediumInput: HTMLInputElement = this.el.querySelector(`input[name="last_utm_medium"]`);
            if (utmMediumInput) {
                utmMediumInput.value = utmData.medium;
            }

            // Set the internal ad id.
            this.setInternalAdId();
        }

        // When the form is submitted, notify Segment.
        if (eventName === "onFormSubmit") {
            const emailAddress: HTMLInputElement = this.el.querySelector(`input[name="email"]`);
            this.notifySegment(emailAddress.value, utmData);
        }

        // When there are problems loading the form, show a failure message.
        if (eventName === "onFormDefinitionFetchError") {
            this.isLoading = false;
            this.didLoad = false;
        }
    }

    // Send a tracking event to Segment.
    private notifySegment(emailAddress: string, utmData: UTMData) {
        const analytics = (window as any).analytics;
        const analyticsAvailable = analytics && analytics.track && (typeof analytics.track === "function");

        if (analyticsAvailable) {
            const submissionData = {
                formId: this.formId,
                email: emailAddress,
                utmCampaign: utmData.campaign,
                utmSource: utmData.source,
                utmMedium: utmData.medium,
            };

            analytics.track("form-submission", submissionData);
        }
    }

    // Get the Internal Ad ID query param and update the corresponding form field.
    private setInternalAdId() {
        const internalAdId = getQueryVariable("iaid");
        if (internalAdId) {
            const internalAdIdInput: HTMLInputElement = this.el.querySelector(`input[name="last_internal_ad_conversion"]`);
            if (internalAdIdInput) {
                internalAdIdInput.value = internalAdId;
            }
        }
    }

    // Parse the current cookie and return any UTM fields.
    private getUTMCookieData(): UTMData {
        const cookies = parseCookie();
        const utmCookie: any = parseUTMCookieString(cookies["__utmzz"]);

        return {
            campaign: utmCookie.utmccn || "(not set)",
            source: utmCookie.utmcsr || "(direct)",
            medium: utmCookie.utmcmd || "(none)",
        };
    }

    // Load the HubSpot forms library.
    private loadHubSpotFormsScript() {
        const script = document.createElement("script");
        script.setAttribute("src", "//js.hsforms.net/forms/v2.js");

        script.onload = () => {
            const hubspotGlobal = window["hbspt"];
            if (hubspotGlobal) {
                this.createForm(hubspotGlobal);
            } else {
                this.isLoading = false;
                this.didLoad = false;
            }
        };

        script.onerror = () => {
            this.isLoading = false;
            this.didLoad = false;
        };

        // Append the script to the DOM.
        document.body.appendChild(script);
    }

    private createForm(hubspot: any) {
        hubspot.forms.create({
            portalId: "4429525",
            formId: this.formId,
            css: "",
            cssClass: this.class,
            goToWebinarWebinarKey: this.goToWebinarKey,
            target: `#${this.hubspotFormTargetId}`,
        });
    }

    private renderIsLoadingForm() {
        return <p>
            <i class="fa fa-spinner fa-spin mr-2"></i>
        </p>;
    }

    private renderFailedToLoadForm() {
        return <p>
            There was an problem loading this form. Please try refreshing your
            browser, and if you continue to see this message, let us know
            at <a href="mailto:support@pulumi.com">support@pulumi.com</a>.
        </p>;
    }

    render() {
        return <div id={this.hubspotFormTargetId}>
            { !this.didLoad && !this.isLoading ? this.renderFailedToLoadForm() : this.renderIsLoadingForm() }
        </div>;
    }
}
