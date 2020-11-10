import { Component, Prop, h, State } from '@stencil/core';
import { waitForWindowPropertyToExist } from "../../util/util";

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
