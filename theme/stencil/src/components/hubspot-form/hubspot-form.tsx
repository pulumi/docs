import { Component, Element, Event, EventEmitter, h, Method, Prop, State } from "@stencil/core";
import { parseCookie, parseUTMCookieString, getQueryVariable } from "../../util/util";

interface UTMData {
    campaign: string;
    source: string;
    medium: string;
}

// Monotonic counter so multiple instances of the same HubSpot form on one page
// (e.g. the blog header + the footer) each get a unique target-container id —
// HubSpot's forms.create() targets a single element id, so duplicate ids would
// leave the second form unrendered.
let hubspotInstanceCount = 0;

// The types of form events we expect to receive from HubSpot.
// https://legacydocs.hubspot.com/docs/methods/forms/advanced_form_options
type HubSpotFormEvent = "onBeforeFormInit" | "onBeforeValidationInit" | "onFormReady" | "onFormSubmit" | "onFormSubmitted" | "onFormDefinitionFetchError";

const REASSIGNABLE_INPUT_TYPES = ["text", "email", "tel", "url", "search", "number"];

@Component({
    tag: "pulumi-hubspot-form",
    styleUrl: "hubspot-form.scss",
    shadow: false,
})
export class HubspotForm {
    // The formId is the HubSpot defined form ID this form will submit to.
    @Prop()
    formId: string;

    // The salesforceCampaignId is the ID for the associated SalesForce Campaign.
    @Prop()
    salesforceCampaignId: string;

    // The goToWebinarKey is used to automatically register users for a webinar
    // after they submit a form (optional).
    @Prop()
    goToWebinarKey?: string;

    // The class name to be applied to the form (optional).
    @Prop()
    class?: string;

    // Optional LinkedIn conversion ID to fire on form submission.
    @Prop()
    linkedinConversionId?: number;

    // Prefills form fields from URL query parameters, as a JSON string mapping
    // HubSpot field internal name -> query param name:
    //   prefill='{"email": "email", "pulumi_organization_name_s_": "org"}'
    // Applied on onFormReady. A missing param, missing field, or malformed JSON
    // leaves the form untouched.
    @Prop()
    prefill?: string;

    @Prop()
    carryOverValues?: Record<string, string>;

    // Emitted once HubSpot confirms the submission, so a page can render its own
    // confirmation UI. `values` holds the submitted values in display form.
    @Event({ composed: true, bubbles: true })
    hubspotFormSubmitted: EventEmitter<{ formId: string; values: Record<string, string> }>;

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

    private observer: IntersectionObserver;

    // The field values as of onFormSubmit, held for the onFormSubmitted event.
    private submittedValues: Record<string, string> = {};

    componentWillLoad() {
        if (!this.formId) {
            throw new Error("The required attribute `form-id` was not provided.");
        }

        this.hubspotFormTargetId = `hubspotForm_${this.formId}_${hubspotInstanceCount++}`;
    }

    componentDidLoad() {
        this.messageHandler = this.onMessage.bind(this);
        window.addEventListener("message", this.messageHandler);

        // Lazy-load HubSpot script when the form scrolls into view.
        this.observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                this.observer.disconnect();
                const hubspotGlobal = window["hbspt"];
                if (hubspotGlobal) {
                    this.createForm(hubspotGlobal);
                } else {
                    this.loadHubSpotFormsScript();
                }
            }
        }, { rootMargin: "200px" });
        this.observer.observe(this.el);
    }

    disconnectedCallback() {
        window.removeEventListener("message", this.messageHandler);
        this.observer?.disconnect();
    }

    // HubSpot form events are dispatched as window message events.
    private onMessage(event: MessageEvent) {
        // Ignore any non-HubSpot-form-related events.
        if (event.data?.type !== "hsFormCallback") {
            return;
        }

        // HubSpot broadcasts form callbacks on `window`, so filter to this
        // instance — but only when an id is present, or lifecycle events that
        // omit one would be dropped.
        if (event.data.id && event.data.id !== this.formId) {
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

            if (this.carryOverValues) {
                this.fillEmptyFields(this.carryOverValues);
            }

            this.applyPrefill();
        }

        // When the form is submitted, notify Segment and fire any conversion tracking.
        if (eventName === "onFormSubmit") {
            const emailAddress: HTMLInputElement = this.el.querySelector(`input[name="email"]`);
            if (emailAddress) {
                this.notifySegment(emailAddress.value, utmData);
            }

            // Capture the values now: by the time onFormSubmitted fires, HubSpot
            // has replaced the form with its inline thank-you message.
            this.submittedValues = this.collectFieldValues();

            // Fire LinkedIn conversion tracking if a conversion ID is set.
            if (this.linkedinConversionId && typeof (window as any).lintrk === "function") {
                (window as any).lintrk("track", { conversion_id: this.linkedinConversionId });
            }
        }

        if (eventName === "onFormSubmitted") {
            this.hubspotFormSubmitted.emit({ formId: this.formId, values: this.submittedValues });
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
        const analyticsAvailable = analytics && analytics.track && typeof analytics.track === "function";

        if (analyticsAvailable && emailAddress !== "") { // Don't track empty email addresses
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

    // Prefill fields from the query string, per the `prefill` map.
    private applyPrefill() {
        if (!this.prefill) {
            return;
        }

        try {
            const fieldsToParams: Record<string, string> = JSON.parse(this.prefill);
            const values: Record<string, string> = {};

            Object.keys(fieldsToParams).forEach(fieldName => {
                const value = getQueryVariable(fieldsToParams[fieldName]);
                if (value) {
                    values[fieldName] = value;
                }
            });

            this.applyValues(values);
        } catch (e) {
            // Malformed prefill map, or a query string getQueryVariable can't parse.
        }
    }

    private applyValues(values: Record<string, string>) {
        this.writeFields(values, false);
    }

    private fillEmptyFields(values: Record<string, string>) {
        this.writeFields(values, true);
    }

    private writeFields(values: Record<string, string>, skipFilled: boolean) {
        Object.keys(values).forEach(fieldName => {
            const value = values[fieldName];
            if (!value) {
                return;
            }

            const field: HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement = this.el.querySelector(`[name="${fieldName}"]`);
            if (!field || (skipFilled && field.value)) {
                return;
            }

            // HubSpot validates off its own state, so it needs both events to
            // register the value. `window.Event` because Stencil's `Event`
            // decorator shadows the global constructor here.
            field.value = value;
            field.dispatchEvent(new window.Event("input", { bubbles: true }));
            field.dispatchEvent(new window.Event("change", { bubbles: true }));
        });
    }

    @Method()
    async getCarryOverValues(): Promise<Record<string, string>> {
        const values: Record<string, string> = {};

        this.el.querySelectorAll("input, textarea, select").forEach((field: HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement) => {
            if (!field.name) {
                return;
            }

            if (field instanceof HTMLInputElement && !REASSIGNABLE_INPUT_TYPES.includes(field.type)) {
                return;
            }

            values[field.name] = field.value;
        });

        return values;
    }

    // The form's current values, keyed by field name, in display form.
    private collectFieldValues(): Record<string, string> {
        const values: Record<string, string> = {};

        this.el.querySelectorAll("input, select, textarea").forEach((field: HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement) => {
            if (!field.name || (field as HTMLInputElement).type === "hidden") {
                return;
            }

            if (field instanceof HTMLSelectElement) {
                // The option's text, not its raw value.
                values[field.name] = field.selectedOptions.length ? field.selectedOptions[0].text : "";
                return;
            }

            const inputType = (field as HTMLInputElement).type;
            if (inputType === "checkbox" || inputType === "radio") {
                if ((field as HTMLInputElement).checked) {
                    values[field.name] = field.value;
                }
                return;
            }

            values[field.name] = field.value;
        });

        return values;
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
            sfdcCampaignId: this.salesforceCampaignId,
        });
    }

    private renderIsLoadingForm() {
        // Compact, height-constrained spinner (Phosphor circle-notch, rotated via
        // Tailwind's animate-spin) so the loading state matches the rendered form
        // height and doesn't shift layout.
        return (
            <span class="inline-flex h-9 items-center justify-center text-gray-500" role="status" aria-label="Loading">
                <svg xmlns="http://www.w3.org/2000/svg" class="size-5 animate-spin" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false">
                    <path d="M232,128a104,104,0,0,1-208,0c0-41,23.81-78.36,60.66-95.27a8,8,0,0,1,6.68,14.54C60.15,75.42,40,105.69,40,128a88,88,0,0,0,176,0c0-22.31-20.15-52.58-51.34-80.73a8,8,0,0,1,6.68-14.54C208.19,49.64,232,87,232,128Z"/>
                </svg>
            </span>
        );
    }

    private renderFailedToLoadForm() {
        return (
            <p>
                There was a problem loading this form. Please try refreshing your browser, and if you continue to see this message, let us know at{" "}
                <a href="mailto:support@pulumi.com">support@pulumi.com</a>.
            </p>
        );
    }

    render() {
        return <div id={this.hubspotFormTargetId}>{!this.didLoad && !this.isLoading ? this.renderFailedToLoadForm() : this.renderIsLoadingForm()}</div>;
    }
}
