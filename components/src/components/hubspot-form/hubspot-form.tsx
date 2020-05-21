import { Component, Prop, Listen, h } from '@stencil/core';
import { Store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { addSubmittedFormId } from "../../store/actions/form";

interface HubSpotFormOptions {
    portalId: string;
    formId: string;
    css: string;
    cssClass: string;
    goToWebinarWebinarKey: string | undefined;
    target: string;
}

@Component({
    tag: 'pulumi-hubspot-form',
    styleUrl: 'hubspot-form.css',
})
export class HubspotForm {
    private storeUnsubscribe: Unsubscribe;

    // A handle to the application store.
    @Prop({ context: "store" })
    store: Store;

    // The ID for the container we will attach the form to.
    formContainerId = "hubSpotInlineForm";

    // Check if the form has been loaded.
    private _isLoaded = false;

    // The ID of the form in HubSpot.
    @Prop()
    formId: string;

    // OPTIONAL: CSS class(es) to assign to the form.
    @Prop()
    cssClass: string;

    // OPTIONAL: The key for the GoToWebinar Webinar the form is assciated with. This
    // value is required to automatically register people in GoToWebinar when the form
    // is submitted.
    @Prop()
    goToWebinarKey: string;

    // OPTIONAL: If this value is set to true, then the component will render a button
    // instead of the form.
    @Prop()
    hideIfSubmitted: boolean;

    // OPTIONAL: The URL for the button to direct a user to when the form is hidden.
    @Prop()
    hiddenFormButtonURL: string;

    // OPTIONAL: The text for the button when the form is hidden.
    @Prop()
    hiddenFormButtonText: string;

    // OPTIONAL: The class names for the button when the form is hidden.
    @Prop()
    hiddenFormButtonClass: string;

    // Has this form been submitted by the user before.
    @Prop({ mutable: true })
    hasSubmittedForm: boolean;

    // Dispatch function for handling submitted forms.
    addSubmittedFormId: typeof addSubmittedFormId;

    // When the document is rendered, let's check to see if the form we are about
    // to load has already been submitted and set up our action function.
    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {
        this.store.mapDispatchToProps(this, { addSubmittedFormId });

        // If the form is not marked as one to hide, then return.
        if (!this.hideIfSubmitted) {
            return;
        }

        const checkIfSubmittedForm = this.checkIfSubmittedForm.bind(this);
        this.storeUnsubscribe = this.store.mapStateToProps(this, (state: AppState) => {
            if (!this._isLoaded) {
                this._isLoaded = true;
                return { hasSubmittedForm: checkIfSubmittedForm(state.form.submittedFormIds) };
            }

            // If this isn't the first load do no change the value of the prop. We only want to display
            // the button on the user's next visit to the form. Otherwise we will hide any "thank you"
            // messages HubSpot displays after the submission.
            return { hasSubmittedForm: this.hasSubmittedForm };
        });
    }

    // Add an event listener to listen for a form submission and dispatch
    // that formId to be added to the user's preferences.
    @Listen("message", { target: "window" })
    onMessage(event: MessageEvent) {
        // Check to make sure we have the right event.
        if(event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormReady') {
            // Check that the form exists.
            const form = document.querySelector("#hubSpotInlineForm form");
            if (!form) {
                return;
            }

            // Add the form id to the the state store in local storage, so if the
            // user comes back we can hide the form if needed.
            const handler = this.addSubmittedFormId;
            const formId = this.formId;
            form.addEventListener("submit", function() {
                handler(formId);
            });
        }
    }

    // Once the component has loaded we will attach the form
    // to the form container, if neccessary.
    componentDidLoad() {
        const hsFormOpts: HubSpotFormOptions = {
            portalId: "4429525",
            css: "",
            formId: this.formId,
            cssClass: this.cssClass,
            goToWebinarWebinarKey: this.goToWebinarKey,
            target: "#" + this.formContainerId,
        };

        // Create the script element for loading the HubSpot form script.
        const hsFormScript = document.createElement("script");
        hsFormScript.src = "https://js.hsforms.net/forms/v2.js";
        document.body.appendChild(hsFormScript);

        // Once the script loads create the HubSpot form.
        hsFormScript.addEventListener("load", () => {
            const win = window as any;
            if (win.hbspt && win.hbspt.forms && typeof win.hbspt.forms.create === "function") {
                win.hbspt.forms.create(hsFormOpts);
            }
        });
    }

    componentDidUnload() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    renderWatchNowButton() {
        return [
            <a data-track={this.hiddenFormButtonText} class={this.hiddenFormButtonClass} href={this.hiddenFormButtonURL}>
                { this.hiddenFormButtonText }
            </a>
        ];
    }

    render() {
        return [
            this.hasSubmittedForm ? this.renderWatchNowButton() : <div id={this.formContainerId}></div>,
            <slot></slot>
        ];
    }

    private checkIfSubmittedForm(formIds: string[]): boolean {
        return formIds.indexOf(this.formId) > -1;
    }
}
