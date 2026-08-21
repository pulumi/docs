const LAMBDA_URL = "https://2pkfmebdylyd3lhmm3rbmoe2ly0exrbp.lambda-url.us-west-2.on.aws/";

function setSubmitting(button: Element | null, submitting: boolean) {
    if (!(button instanceof HTMLButtonElement)) {
        return;
    }
    button.disabled = submitting;
    button.textContent = submitting ? "Submitting..." : "Submit request";
}

function showStatus(status: Element | null, message: string, isError: boolean) {
    if (!(status instanceof HTMLElement)) {
        return;
    }
    status.textContent = message;
    status.classList.remove("hidden");
    status.classList.toggle("text-red-600", isError);
    status.classList.toggle("text-green-600", !isError);
}

function initSupportForm() {
    const form = document.querySelector("[data-support-form]");
    if (!(form instanceof HTMLFormElement)) {
        return;
    }

    const submitButton = form.querySelector("[data-support-submit]");
    const status = form.querySelector("[data-support-status]");

    form.addEventListener("submit", event => {
        event.preventDefault();

        const name = (form.elements.namedItem("name") as HTMLInputElement).value.trim();
        const email = (form.elements.namedItem("email") as HTMLInputElement).value.trim();
        const organization = (form.elements.namedItem("organization") as HTMLInputElement).value.trim();
        const details = (form.elements.namedItem("details") as HTMLTextAreaElement).value.trim();

        if (!name || !email || !organization || !details) {
            showStatus(status, "Please fill out all fields.", true);
            return;
        }

        setSubmitting(submitButton, true);

        fetch(LAMBDA_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                email,
                subject: `Support request from ${name} (${organization})`,
                message: `Name: ${name}\nPulumi organization: ${organization}\n\n${details}`,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Request failed with status ${response.status}`);
                }
                form.reset();
                showStatus(status, "Thanks! Your request has been submitted. We'll be in touch soon.", false);
                setSubmitting(submitButton, false);
            })
            .catch(() => {
                showStatus(status, "Something went wrong submitting your request. Please try again or email support@pulumi.com.", true);
                setSubmitting(submitButton, false);
            });
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSupportForm);
} else {
    initSupportForm();
}
