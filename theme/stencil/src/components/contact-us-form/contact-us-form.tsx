import { Component, Prop, State, h } from "@stencil/core";
import { MultiSelectFormItem } from "../pulumi-multi-select-form/pulumi-multi-select-form";
import { getQueryVariable } from "../../util/util";

interface ContactUsCta {
    label: string;
    url: string;
}

interface ContactUsItem {
    key: string;
    label?: string;
    hubspot_form_id: string;
    cta?: ContactUsCta;
    qualifier?: string;
}

@Component({
    tag: "pulumi-contact-us-form",
    styleUrl: "contact-us-form.css",
    shadow: false,
})
export class ContactUsForm {
    // The JSON string of the sessions.
    @Prop()
    items: string;

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The parsed and transformed session string.
    @State()
    parsedItems: MultiSelectFormItem[];

    @State()
    defaultFormId: string = "";

    componentWillLoad() {
        this.parsedItems = JSON.parse(this.items).map((item: ContactUsItem) => {
            return {
                key: item.key,
                label: item.label ? item.label : item.key.charAt(0).toUpperCase() + item.key.slice(1),
                hubspotFormId: item.hubspot_form_id,
                cta: item.cta,
                qualifier: item.qualifier
            };
        });

        const formQueryParam = getQueryVariable("form");
        if (formQueryParam) {
            const selectedForm = this.parsedItems.find(item => (item.key as string).toLowerCase() === formQueryParam.toLowerCase());

            if (selectedForm) {
                this.defaultFormId = selectedForm.hubspotFormId;
                return;
            }
        }
    }

    render() {
        return (
            <pulumi-multi-select-form
                items={this.parsedItems}
                labelClass={this.labelClass}
                labelText="What can we help you with?"
                defaultFormId={this.defaultFormId}
                linkedinConversionId={24927132}
            />
        );
    }
}
