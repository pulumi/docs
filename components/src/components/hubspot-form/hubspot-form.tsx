import { Component, Prop, h } from '@stencil/core';
// import { Store, Unsubscribe } from "@stencil/redux";
// import { AppState } from "../../store/state";

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
  formContainerId = "hubSpotInlineForm";

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

    hsFormScript.addEventListener("load", () => {
      const win = window as any;
      if (win.hbspt && win.hbspt.forms && typeof win.hbspt.forms.create === "function") {
        win.hbspt.forms?.create(hsFormOpts);
      }
    });
  }

  render() {
    return [
      <div id={this.formContainerId}></div>,
      <slot></slot>
    ];
  }

}
