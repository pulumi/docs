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

    @Prop()
    items: MultiSelectFormItem[] = [];

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The text to be displayed as the label for the selector.
    @Prop()
    labelText: string;

    @Prop()
    defaultFormId: string = "";

    // Optional LinkedIn conversion ID to fire on form submission.
    @Prop()
    linkedinConversionId?: number;

    @State()
    selectedItem: MultiSelectFormItem | undefined;

    @State()
    formSubmitted = false;

    @State()
    carriedValues: Record<string, string> = {};

    // The window event listener used to handle submitting form data to Segment.
    private windowEventHandler: (this: Window, ev: MessageEvent) => any;

    private static readonly radioGroupName = "multi-select-form-choice";

    componentWillLoad() {
        if (this.defaultFormId !== "") {
            this.selectedItem = this.items.find(item => item.hubspotFormId === this.defaultFormId);
        }
        if (!this.selectedItem) {
            this.selectedItem = this.items[0];
        }
    }

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

    private async handleChoiceChange(hubspotFormId: string) {
        this.carriedValues = await this.captureCarryOverValues();
        this.selectedItem = this.items.find(item => item.hubspotFormId === hubspotFormId);
    }

    private async captureCarryOverValues(): Promise<Record<string, string>> {
        const form = this.el.querySelector("pulumi-hubspot-form") as HTMLPulumiHubspotFormElement;
        if (!form?.getCarryOverValues) {
            return this.carriedValues;
        }

        const values = await form.getCarryOverValues();
        // Merged rather than replaced: the forms don't all share fields, so a message
        // has to survive a detour through one that lacks a message field.
        const carried: Record<string, string> = { ...this.carriedValues };

        Object.entries(values).forEach(([name, value]) => {
            if (value) {
                carried[name] = value;
            } else {
                delete carried[name];
            }
        });

        return carried;
    }

    render() {
        const selectedFormId = this.selectedItem?.hubspotFormId || "";

        return (
            <div>
                {this.formSubmitted ? null : (
                    <div>
                        <span class={this.labelClass || ""}>{this.labelText}</span>
                        {/* Not a <fieldset>: one here disables the `:not(:has(fieldset))` branch in _hubspot.scss that styles the embedded form's fields. */}
                        <div role="radiogroup" aria-label={this.labelText} class="grid grid-cols-1 lg:grid-cols-4 gap-3">
                            {this.items.map(item => (
                                <label class="card card-hover flex items-center justify-center p-3 m-0 text-center text-sm font-normal has-[:checked]:border-violet-primary has-[:checked]:bg-violet-50 has-[:checked]:text-violet-primary has-[:focus-visible]:border-violet-800 has-[:focus-visible]:inset-ring-2 has-[:focus-visible]:inset-ring-violet-800">
                                    <input
                                        type="radio"
                                        class="sr-only"
                                        name={PulumiMultiSelectForm.radioGroupName}
                                        value={item.hubspotFormId}
                                        checked={item.hubspotFormId === selectedFormId}
                                        onInput={(event: any) => this.handleChoiceChange(event.target.value)}
                                    />
                                    <span>{item.label ? item.label : item.key}</span>
                                </label>
                            ))}
                        </div>
                    </div>
                )}
                {!this.selectedItem ? null : this.selectedItem.cta ? (
                    <div class="mt-8"><a class="btn btn-primary btn-lg" href={this.selectedItem.cta.url}>{this.selectedItem.cta.label}</a></div>
                ) : (
                    <pulumi-hubspot-form key={selectedFormId} form-id={selectedFormId} form-name={String(this.selectedItem.key)} carryOverValues={this.carriedValues}></pulumi-hubspot-form>
                )}
            </div>
        );
    }
}
