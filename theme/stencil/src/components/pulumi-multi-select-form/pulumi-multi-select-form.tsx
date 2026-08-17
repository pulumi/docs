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

    // The items to choose between.
    @Prop()
    items: MultiSelectFormItem[] = [];

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The text to be displayed as the label for the selector.
    @Prop()
    labelText: string;

    // The form to pre-select when rendered. Blank falls back to the first item.
    @Prop()
    defaultFormId: string = "";

    // Optional LinkedIn conversion ID to fire on form submission.
    @Prop()
    linkedinConversionId?: number;

    // The currently selected item. Defaults to the first, so the page lands on a
    // usable form; a ?form= deep link overrides it.
    @State()
    selectedItem: MultiSelectFormItem | undefined;

    @State()
    formSubmitted = false;

    // What the visitor had typed into the form they're switching away from, so
    // changing your mind about why you're writing in doesn't cost you the message
    // you already wrote. Handed to the incoming form, which fills only the fields
    // it finds empty.
    @State()
    carriedValues: Record<string, string> = {};

    // The window event listener used to handle submitting form data to Segment.
    private windowEventHandler: (this: Window, ev: MessageEvent) => any;

    // Groups the radios. A page only ever renders one of these, so a constant
    // name is enough.
    private static readonly radioGroupName = "multi-select-form-choice";

    componentWillLoad() {
        if (this.defaultFormId !== "") {
            this.selectedItem = this.items.find(item => item.hubspotFormId === this.defaultFormId);
        }

        // Falls through to the first item when there's no deep link, and also when
        // a ?form= names a key we don't have.
        if (!this.selectedItem) {
            this.selectedItem = this.items[0];
        }
    }

    // After the form submits we should hide the chooser.
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

    // When the choice changes we need to update the state accordingly, capturing
    // the outgoing form's values first — switching swaps the embedded form out
    // entirely, so anything typed is gone once the state changes.
    private async handleChoiceChange(hubspotFormId: string) {
        this.carriedValues = await this.captureCarryOverValues();
        this.selectedItem = this.items.find(item => item.hubspotFormId === hubspotFormId);
    }

    private async captureCarryOverValues(): Promise<Record<string, string>> {
        const form = this.el.querySelector("pulumi-hubspot-form") as HTMLPulumiHubspotFormElement;

        // No form to read: either nothing has been chosen yet, or the current
        // choice is one of the CTA-only options. Keep what was captured last so a
        // detour through the support option doesn't discard it.
        if (!form || typeof form.getCarryOverValues !== "function") {
            return this.carriedValues;
        }

        const values = await form.getCarryOverValues();

        // Merged into what's already carried rather than replacing it. The forms
        // don't all ask for the same things, so a message typed on one of them has
        // to survive a detour through one that never had a message field.
        const carried: Record<string, string> = { ...this.carriedValues };

        Object.keys(values).forEach(name => {
            // Present but emptied: the visitor cleared it, so drop it. A field this
            // form doesn't have simply isn't in `values`, and keeps whatever an
            // earlier form carried in.
            if (values[name]) {
                carried[name] = values[name];
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
                        {/*
                            A div with role="radiogroup", NOT a <fieldset>: this renders
                            inside the page's `.hs-form` wrapper, and _hubspot.scss gates
                            its "newer HubSpot editor, no fieldset" field-chrome branch on
                            `:not(:has(fieldset))`. A fieldset here would flip that branch
                            off and leave the embedded form below with browser-default
                            inputs.
                        */}
                        <div role="radiogroup" aria-label={this.labelText} class="grid grid-cols-1 lg:grid-cols-4 gap-3">
                            {this.items.map(item => (
                                // The card is the affordance, so the radio itself is
                                // sr-only — still focusable and arrow-navigable, with the
                                // focus treatment drawn on the card via has-[:focus-visible].
                                // That treatment is the FORM-CONTROL one, not the button
                                // one: violet-800 border plus a 2px inset ring of the same
                                // color, merging into one edge ($form-focus-ring in
                                // shared/_forms.scss). Keep it in step with that token.
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
                    // Stands in for the submit button of the form the other choices
                    // render, so it matches it: _hubspot.scss extends the HubSpot
                    // submit input with .btn-primary .btn-lg.
                    <div class="mt-8"><a class="btn btn-primary btn-lg" href={this.selectedItem.cta.url}>{this.selectedItem.cta.label}</a></div>
                ) : (
                    <pulumi-hubspot-form key={selectedFormId} form-id={selectedFormId} carryOverValues={this.carriedValues}></pulumi-hubspot-form>
                )}
            </div>
        );
    }
}
