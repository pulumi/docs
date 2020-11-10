import { Component, Prop, h, State } from '@stencil/core';
import { waitForWindowPropertyToExist, parseCookie, parseUTMCookieString } from "../../util/util";

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

    // When the component loads we need to wait for the 'hbspt' property to
    // propogate up to the global window object. Then once it is available
    // we should create the HubSpot form.
    componentDidLoad() {
        waitForWindowPropertyToExist("hbspt").then((hbspt: any) => {
            hbspt.forms.create({
                portalId: "4429525",
                formId: this.formId,
                css: "",
                cssClass: this.class,
                goToWebinarWebinarKey: this.goToWebinarKey,
                target: `#hubspotForm_${this.formId}`,
            });
            this.isLoading = false;
            this.didLoad = true;
        }).catch((err) => {
            this.isLoading = false;
            console.log("Unable to load HubSpot form.");
            console.log(err);
        });

        // Add an listener to send an event to Segment with the UTM
        // parameters when the form is submitted.
        const analytics = (window as any).analytics;
        const analyticsAvailable = analytics.track && (typeof analytics.track === "function");

        var cookies = parseCookie();
        var utmCookie: any = parseUTMCookieString(cookies["__utmzz"]);

        if (analyticsAvailable) {
            // Listen for the HubSpot form to be loaded.
            window.addEventListener('message', event => {
                if(event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormReady') {
                    const form = document.querySelector(".hbspt-form form") as HTMLFormElement;
                    const email = document.querySelector(".hbspt-form form input[name='email']") as HTMLInputElement;

                    // Send an analytics event with the UTM values when the form is submitted.
                    form.on("submit", () => {
                        const submissionData = {
                            formId: form.attr("data-form-id"),
                            email: email.value,
                            utmCampaign: utmCookie.utmccn || "(not set)",
                            utmSource: utmCookie.utmcsr || "(direct)",
                            utmMedium: utmCookie.utmcmd || "(none)",
                        };

                        analytics.track("form-submission", submissionData);
                    });
                }
            });
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
