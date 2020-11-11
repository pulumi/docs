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

    // The labelClass defines the class for the label.
    @Prop()
    labelClass?: string;

    // The parsed sessions string.
    @State()
    webinarSessions: WebinarSessionItem[];

    // The currently selected session.
    @State()
    selectedSession: WebinarSessionItem;

    // When the form has been submitted we need to hide the form selector.
    @State()
    formSubmitted: boolean = false;

    // The window event listener used to handle submitting form data to Segment.
    private windowEventHandler: (this: Window, ev: MessageEvent) => any;

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
            const form = document.querySelector("form.hs-form") as HTMLFormElement;
            form.addEventListener("submit", this.handleFormSubmit.bind(this));
        }
    }

    // Set the formSubmitted to true when the form has been submitted.
    private handleFormSubmit() {
        this.formSubmitted = true;
    }

    // When the select input changes we need to update the state accordingly.
    private handleSelectChange(hubspotFormID: string) {
        this.selectedSession = this.webinarSessions.find((session) => session.hubspot_form_id === hubspotFormID);
    }

    render() {
        return (
            <div>
                { this.formSubmitted ? null :
                    <span>
                        <span class={this.labelClass || ""}>Pick a Session</span>
                        <select class={this.selectClass || ""} onInput={(event: any) => this.handleSelectChange(event.target.value)}>
                            {this.webinarSessions.map((session) => {
                                return <option value={session.hubspot_form_id}>{session.datetime}</option>;
                            })}
                        </select>
                    </span>
                }
                <pulumi-hubspot-form
                    key={this.selectedSession.hubspot_form_id}
                    form-id={this.selectedSession.hubspot_form_id}
                    go-to-webinar-key={this.selectedSession.gotowebinar_key}
                ></pulumi-hubspot-form>
            </div>
        );
    }

}
