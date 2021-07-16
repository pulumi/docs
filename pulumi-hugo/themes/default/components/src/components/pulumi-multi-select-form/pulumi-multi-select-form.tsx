import { Component, Prop, State, Element, h } from "@stencil/core";

export interface MultiSelectFormItem {
    key: string | Date;
    hubspotFormId: string;
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

    // The currently selected item.
    @State()
    selectedItem: MultiSelectFormItem;

    @State()
    formSubmitted = false;

    // The window event listener used to handle submitting form data to Segment.
    private windowEventHandler: (this: Window, ev: MessageEvent) => any;

    // When the component loads we need to parse the items string.
    componentWillLoad() {
        if (this.defaultFormId !== "") {
            this.selectedItem = this.items.find((item) => item.hubspotFormId === this.defaultFormId);

            if (this.selectedItem) {
                return;
            }
        }

        this.selectedItem = this.items[0];
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
    }

    // When the select input changes we need to update the state accordingly.
    private handleSelectChange(hubspotFormId: string) {
        this.selectedItem = this.items.find((item) => item.hubspotFormId === hubspotFormId);
    }

    render() {
        const selectedFormId = this.selectedItem?.hubspotFormId;

        return (
            <div>
                { this.formSubmitted ? null :
                    <span>
                        <span class={this.labelClass || ""}>{ this.labelText }</span>
                        <select class={this.selectClass || ""} onInput={(event: any) => this.handleSelectChange(event.target.value)}>
                            {this.items.map((item) => {
                                const isSelected = item.hubspotFormId === selectedFormId;
                                return <option value={item.hubspotFormId} selected={isSelected}>{item.key}</option>;
                            })}
                        </select>
                    </span>
                }
                <pulumi-hubspot-form
                    key={selectedFormId}
                    form-id={selectedFormId}
                ></pulumi-hubspot-form>
            </div>
        );
    }
}
