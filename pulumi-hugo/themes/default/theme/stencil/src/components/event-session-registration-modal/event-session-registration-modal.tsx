import { Host, Component, Prop, State, Watch, Element, h } from "@stencil/core";

export interface EventSessionInfo {
    hubspot_form_id: string;
    title: string;
    description: string;
}

export type EventSessionRegistrationModalContent = "session-select" | "form";
export type SubmittedFormValues = Record<string, string>;

@Component({
    tag: "event-session-registration-modal",
    styleUrl: "event-session-registration-modal.scss",
    shadow: false,
})
export class EventSessionRegistrationModal {
    @Element()
    el: HTMLElement;

    @Prop()
    buttonClass: string;

    @Prop()
    buttonText: string;

    @Prop()
    modalTitle: string;

    @Prop()
    eventSessions: string;

    @Prop()
    redirectUrl = "/pulumi-up/thank-you/";

    private parsedEventSessions: EventSessionInfo[];

    @State()
    isModalOpen: boolean = false;

    @State()
    displayingContent: EventSessionRegistrationModalContent = "session-select";

    @State()
    selectedSessions: string[] = [];

    @State()
    processingFormSubmissions = false;

    @State()
    formProcessor: HTMLDivElement = undefined;

    @State()
    error: string | undefined = undefined;

    @State()
    submittedFormValues: SubmittedFormValues = {};

    @Watch("eventSessions")
    private handleEventSessionInfo(newEventSessions: string) {
        this.parsedEventSessions = JSON.parse(newEventSessions);
    }

    componentWillLoad() {
        this.handleEventSessionInfo(this.eventSessions);
    }

    componentDidLoad() {
        window.addEventListener("message", this.onMessage);
    }

    disconnectedCallback() {
        window.removeEventListener("message", this.onMessage);
    }

    private onMessage = (event: MessageEvent) => {
        // Ignore any non-HubSpot-form-related events and if the modal isn't open.
        if ((event.data?.type !== "hsFormCallback") || (!this.isModalOpen)) {
            return;
        }

        const eventName: string = event.data.eventName;
        if ((eventName === "onFormReady") && this.processingFormSubmissions) {
            this.handleFormSubmissions();
        }

        if (eventName === "onFormSubmit") {
            const formInputs = this.el.querySelectorAll("form input") as NodeListOf<HTMLInputElement>;
            const newSubmittedFormValues: SubmittedFormValues = {};
            formInputs.forEach((input) => {
                if (input.type !== "checkbox") {
                    newSubmittedFormValues[input.name] = input.value;
                }
            });
            this.submittedFormValues = newSubmittedFormValues;

            setTimeout(() => {
                this.selectedSessions = [ ...this.selectedSessions.slice(1) ];
                this.processingFormSubmissions = true;

                if (this.selectedSessions.length === 0) {
                    window.location.href = this.redirectUrl;
                }
            }, 500);
        }
    }

    private handleButtonClick = (e: Event) => {
        e.preventDefault();
        this.isModalOpen = true;
        document.querySelector("body").className += " disable-scroll";
    }

    private handleCloseModal = (e: Event) => {
        e.preventDefault();
        this.isModalOpen = false;
        this.displayingContent = "session-select";
        this.selectedSessions = [];
        document.querySelector("body").className = document.querySelector("body").className.replace("disable-scroll", "");
    }

    private handleSessionSelection = (formId: string) => {
        const formIdIndex = this.selectedSessions.indexOf(formId);
        if (formIdIndex === -1) {
            this.selectedSessions.push(formId);
        } else {
            this.selectedSessions.splice(formIdIndex, 1);
        }
    }

    private handleGotToSessionSelect = (e: Event) => {
        e.preventDefault();
        this.displayingContent = "session-select";
    }

    private handleGoToForm(e: Event, content: EventSessionRegistrationModalContent) {
        e.preventDefault();

        if (this.selectedSessions.length === 0) {
            this.error = "You must select at least one of the above options.";
            return;
        }

        this.displayingContent = content;
        this.error = undefined;
    }

    private handleFormSubmissions() {
        if (this.selectedSessions.length === 0) {
            window.location.href = this.redirectUrl;
            return;
        }

        // Check the code of conduct checkbox as it has to have already been checked
        // to reach this point.
        const cocCheckbox = this.el.querySelectorAll("form input[type='checkbox']") as NodeListOf<HTMLInputElement>;
        cocCheckbox[1].click();

        setTimeout(() => {
            const submittedFormValueKeys = Object.keys(this.submittedFormValues);
            if (submittedFormValueKeys.length > 0) {
                for (let i = 0; i < submittedFormValueKeys.length; i++) {
                    const formValueKey = submittedFormValueKeys[i];
                    if (formValueKey === "") {
                        continue;
                    }

                    const formInput = this.el.querySelector(`form input[name="${ formValueKey }"]`) as HTMLInputElement;
                    formInput.value = this.submittedFormValues[formValueKey];
                    formInput.dispatchEvent(new Event("change"));
                }
            }
        }, 500);

        setTimeout(() => {
            const formSubmitButton = this.el.querySelector("form input[type='submit']") as HTMLInputElement;
            formSubmitButton.click();
        }, 500);
    }

    private renderSessionSelectionItem(info: EventSessionInfo) {
        const isChecked = this.selectedSessions.indexOf(info.hubspot_form_id) > -1;

        return(
            <li>
                <label class="session-selection-item">
                    <div class="checkbox-container">
                        <input type="checkbox" id={info.title} name={info.title} onChange={() => this.handleSessionSelection(info.hubspot_form_id)} checked={isChecked} />
                        <span class="checkmark"></span>
                    </div>
                    <div class="checkbox-label">
                        <h6>{ info.title }</h6>
                        <p>{ info.description }</p>
                    </div>
                </label>
            </li>
        );
    }

    private renderSessionSelectContent() {
        return [
            <div class="session-select-container">
                <p>
                    Please select all the options you'd like to register for:
                </p>

                <ul class="session-select-list">
                    { this.parsedEventSessions.map((session) => this.renderSessionSelectionItem(session)) }
                </ul>
            </div>,

            <div class="next-button-container">
                <a href="#" class={ `${this.buttonClass} modal-button` } onClick={(e: Event) => this.handleGoToForm(e, "form")}>
                    Next
                </a>
                { this.error ? <p class="error-message">{ this.error }</p> : null}
            </div>,
        ];
    }

    private renderForm(formId: string) {
        if (!this.processingFormSubmissions) {
            return(
                <div class="registration-form-container">
                    <a href="#" onClick={this.handleGotToSessionSelect}>&larr; Go back to select sessions.</a>
                    <div class="registration-form">
                        <pulumi-hubspot-form
                            formId={ this.selectedSessions[0] }
                        >
                        </pulumi-hubspot-form>
                    </div>
                </div>
            );
        }

        return(
            <div>
                <h4>
                    <i class="fas fa-spinner fa-spin"></i>
                </h4>
                <div class="invisible" ref={(el: HTMLDivElement) => this.formProcessor = el}>
                    <pulumi-hubspot-form
                        key={ formId }
                        formId={ formId }
                    >
                    </pulumi-hubspot-form>
                </div>
            </div>
        );
    }

    private renderContent() {
        console.log("rendering content");
        switch (this.displayingContent) {
            case "session-select":
                return this.renderSessionSelectContent();
            case "form":
                console.log("rendering form");
                return this.renderForm(this.selectedSessions[0]);
        }
    }

    private renderModal() {
        return(
            <div class="event-session-modal-container">
                <div class="modal-container">
                    <div class="modal">
                        <div class="title-container">
                            <div class="title-text">
                                <h4>{ this.modalTitle }</h4>
                            </div>

                            <div class="close-icon">
                                <i class="fa fa-times" onClick={this.handleCloseModal}></i>
                            </div>
                        </div>

                        { this.renderContent() }
                    </div>
                </div>
            </div>
        );
    }

    render() {
        return (
            <Host>
                <div>
                    <div>
                        <a class={this.buttonClass} href="#" onClick={this.handleButtonClick}>{ this.buttonText }</a>
                    </div>

                    { this.isModalOpen ? this.renderModal() : null }
                </div>
            </Host>
        );
    }

}
