import { Component, Prop, State, h } from "@stencil/core";
import { MultiSelectFormItem } from "../pulumi-multi-select-form/pulumi-multi-select-form";
import { getQueryVariable } from "../../util/util";

interface WebinarSessionItem {
    datetime: string;
    hubspot_form_id: string;
}

@Component({
    tag: "pulumi-webinar-form-select",
    styleUrl: "webinar-form-select.scss",
    shadow: false
})
export class WebinarFormSelect {
    // The JSON string of the sessions.
    @Prop()
    sessions: string;

    // The class for the select input.
    @Prop()
    selectClass?: string;

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The parsed and transformed session string.
    @State()
    parsedSessions: MultiSelectFormItem[];

    @State()
    defaultFormId: string = "";

    // When the component loads we need to parse the session strings and turn the datetime
    // into a human friendly format.
    componentWillLoad() {
        this.parsedSessions = this.transformSessionData(JSON.parse(this.sessions));

        // Set the selector value if the `date` query parameter is set.
        const dateQueryParam = getQueryVariable("date");
        if (dateQueryParam) {
            const queryParamDate = new Date(dateQueryParam);
            if (isNaN(queryParamDate.getTime())) {
                return;
            }

            const selectedSession = this.parsedSessions.find((session) => {
                const sessionDate = new Date(session.key);
                return sessionDate.getFullYear() === queryParamDate.getFullYear() &&
                       sessionDate.getMonth() === queryParamDate.getMonth() &&
                       sessionDate.getDate() === queryParamDate.getDate();
            });

            if (selectedSession) {
                this.defaultFormId = selectedSession.hubspotFormId;
            }
        }
    }

    public transformSessionData(sessions: WebinarSessionItem[]): MultiSelectFormItem[] {
        return sessions.map((session: WebinarSessionItem) => {
            const sessionDate = new Date(session.datetime);

            const options: Intl.DateTimeFormatOptions = {
                timeZoneName: "short",
                weekday: "short",
                year: "numeric",
                month: "long",
                day: 'numeric',
                hour: "numeric",
                minute: "2-digit"
            };
            return { hubspotFormId: session.hubspot_form_id, key: sessionDate.toLocaleString(undefined, options)};
        });
    }

    render() {
        return (
            <pulumi-multi-select-form
                items={this.parsedSessions}
                selectClass={this.selectClass}
                labelClass={this.labelClass}
                labelText="Pick A Session"
                defaultFormId={this.defaultFormId}
            />
        );
    }

}
