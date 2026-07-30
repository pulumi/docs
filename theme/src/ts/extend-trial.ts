// /extend-trial/ confirmation swap: on a successful submission, hide the form
// card and show a confirmation recapping what was sent. Progressive enhancement
// — without JS the user still gets HubSpot's own inline thank-you message.
//
// DOM contract (rendered by layouts/page/extend-trial.html):
//   [data-extend-trial]                        root
//   [data-extend-trial-form]                   form card, hidden after submit
//   [data-extend-trial-confirmation]           confirmation card, `hidden` until submit
//   [data-extend-trial-value="<field name>"]   text node filled from the event's values map

interface HubSpotFormSubmittedDetail {
    formId: string;
    values: Record<string, string>;
}

document.addEventListener("DOMContentLoaded", () => {
    const root = document.querySelector<HTMLElement>("[data-extend-trial]");
    if (!root) {
        return;
    }

    const formCard = root.querySelector<HTMLElement>("[data-extend-trial-form]");
    const confirmation = root.querySelector<HTMLElement>("[data-extend-trial-confirmation]");
    if (!formCard || !confirmation) {
        return;
    }

    root.addEventListener("hubspotFormSubmitted", (event: CustomEvent<HubSpotFormSubmittedDetail>) => {
        const values = event.detail?.values || {};

        confirmation.querySelectorAll<HTMLElement>("[data-extend-trial-value]").forEach(node => {
            const value = values[node.dataset.extendTrialValue];
            if (value) {
                node.textContent = value;
            }
        });

        formCard.hidden = true;
        confirmation.hidden = false;
        confirmation.focus();
        confirmation.scrollIntoView({ behavior: "smooth", block: "start" });
    });
});
