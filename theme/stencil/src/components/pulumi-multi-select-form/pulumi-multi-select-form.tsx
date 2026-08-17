import { Component, Prop, State, Element, h } from "@stencil/core";

interface MultiSelectFormCta {
    label: string;
    url: string;
}

export interface MultiSelectFormItem {
    key: string | Date;
    label?: string;
    hubspotFormId: string;
    cta?: MultiSelectFormCta;
}

@Component({
    tag: "pulumi-multi-select-form",
    styleUrl: "pulumi-multi-select-form.css",
    shadow: false,
})
export class PulumiMultiSelectForm {
    @Element()
    el: Element;

    // The JSON string of the items for the selector.
    @Prop()
    items: MultiSelectFormItem[] = [];

    // The class for the select input.
    @Prop()
    selectClass?: string;

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The text to be displayed as the label for the selector.
    @Prop()
    labelText: string;

    // The default key for the selector to set to when rendered. If the key
    // is blank then the first item in the array will be selected.
    @Prop()
    defaultFormId: string = "";

    // Optional LinkedIn conversion ID to fire on form submission.
    @Prop()
    linkedinConversionId?: number;

    // The currently selected item. Left undefined until the visitor makes a
    // choice (or arrives via a ?form= deep link that pre-selects one), so the
    // embedded HubSpot form's extra fields stay hidden until they're relevant.
    @State()
    selectedItem: MultiSelectFormItem | undefined;

    @State()
    formSubmitted = false;

    // The window event listener used to handle submitting form data to Segment.
    private windowEventHandler: (this: Window, ev: MessageEvent) => any;

    // When the component loads we need to parse the items string.
    componentWillLoad() {
        if (this.defaultFormId !== "") {
            this.selectedItem = this.items.find(item => item.hubspotFormId === this.defaultFormId);
        }
    }

    // After the form submits we should hide the session selector.
    componentDidLoad() {
        this.windowEventHandler = this.handleWindowMessage.bind(this);
        window.addEventListener("message", this.windowEventHandler);
    }

    disconnectedCallback() {
        window.removeEventListener("message", this.windowEventHandler);
    }

    // Handle an incoming window message.
    private handleWindowMessage(event: MessageEvent) {
        if (event.data.type === "hsFormCallback" && event.data.eventName === "onFormReady") {
            const form = this.el.querySelector("form.hs-form") as HTMLFormElement;
            form.addEventListener("submit", this.handleFormSubmit.bind(this));
        }
    }

    // Set the formSubmitted to true when the form has been submitted.
    private handleFormSubmit() {
        this.formSubmitted = true;

        // Fire LinkedIn conversion tracking if a conversion ID is set.
        if (this.linkedinConversionId && typeof (window as any).lintrk === "function") {
            (window as any).lintrk("track", { conversion_id: this.linkedinConversionId });
        }
    }

    // When the select input changes we need to update the state accordingly.
    // An empty value means the visitor is back on the unselected placeholder,
    // so collapse back to the not-yet-chosen state rather than crashing on a
    // missing item.
    private handleSelectChange(hubspotFormId: string) {
        this.selectedItem = hubspotFormId ? this.items.find(item => item.hubspotFormId === hubspotFormId) : undefined;
    }

    render() {
        const selectedFormId = this.selectedItem?.hubspotFormId || "";

        return (
            <div>
                {this.formSubmitted ? null : (
                    <span>
                        <span class={this.labelClass || ""}>{this.labelText}</span>
                        <select class={this.selectClass || ""} onInput={(event: any) => this.handleSelectChange(event.target.value)}>
                            <option value="" selected={!selectedFormId} disabled hidden>
                                Please select
                            </option>
                            {this.items.map(item => {
                                const isSelected = item.hubspotFormId === selectedFormId;
                                return (
                                    <option value={item.hubspotFormId} selected={isSelected}>
                                        {item.label ? item.label : item.key}
                                    </option>
                                );
                            })}
                        </select>
                    </span>
                )}
                {!this.selectedItem ? null : this.selectedItem.cta ? (
                    <div class="mt-8"><a class="btn btn-secondary" href={this.selectedItem.cta.url}>{this.selectedItem.cta.label}</a></div>
                ) : (
                    <pulumi-hubspot-form key={selectedFormId} form-id={selectedFormId}></pulumi-hubspot-form>
                )}
            </div>
        );
    }
}
