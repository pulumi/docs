import { Component, Prop, State, h } from '@stencil/core';

interface WebinarSessionItem {
    datetime: string;
    hubspot_form_id: string;
    gotowebinar_key: string;
}

@Component({
    tag: 'pulumi-webinar-form-select',
    styleUrl: 'webinar-form-select.scss',
    shadow: false
})
export class WebinarFormSelect {
    // The JSON string of the sessions.
    @Prop()
    sessions: string;

    // The class for the select input.
    @Prop()
    selectClass?: string;

    // The parsed sessions string.
    @State()
    webinarSessions: WebinarSessionItem[];

    // The currently selected session.
    @State()
    selectedSession: WebinarSessionItem;

    // When the component loads we need to parse the session strings and turn the datetime
    // into a human friendly format.
    componentWillLoad() {
        const parsedSessions = JSON.parse(this.sessions).map((session: WebinarSessionItem) => {
            const sessionDate = new Date(session.datetime);
            const options = {
                timeZoneName: "short",
                weekday: 'short',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: "numeric",
                minute: "2-digit"
              };
            return { ...session, datetime: sessionDate.toLocaleString(undefined, options) };
        });

        // Set the initial state.
        this.webinarSessions = parsedSessions;
        this.selectedSession = parsedSessions[0];
    }

    // When the select input changes we need to update the state accordingly.
    handleSelectChange(hubspotFormID: string) {
        this.selectedSession = this.webinarSessions.find((session) => session.hubspot_form_id === hubspotFormID);
    }

    render() {
        return (
            <div>
                <span>Pick a Session</span>
                <select class={this.selectClass || ""} onInput={(event: any) => this.handleSelectChange(event.target.value)}>
                    {this.webinarSessions.map((session) => {
                        return <option value={session.hubspot_form_id}>{session.datetime}</option>;
                    })}
                </select>
                <pulumi-hubspot-form
                    key={this.selectedSession.hubspot_form_id}
                    form-id={this.selectedSession.hubspot_form_id}
                    go-to-webinar-key={this.selectedSession.gotowebinar_key}
                ></pulumi-hubspot-form>
            </div>
        );
    }

}
