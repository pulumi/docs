// /support/new/ — the support-request form. Client-side validation, data-entry
// conveniences, and the JSON submit to the same-origin /api/support endpoint
// (a Lambda behind CloudFront; see infrastructure/supportForm.ts).
//
// The validation rules here MIRROR the server's (infrastructure/support-form/
// validation.ts) for immediate feedback, but the server is authoritative: a
// 422 response carries per-field messages that are mapped back onto the form
// exactly like local errors.
//
// DOM contract (rendered by layouts/page/support-new.html):
//   [data-support-form-root]              page root; module no-ops if absent
//   [data-support-form-card]              form card, hidden after success
//   [data-support-form]                   the <form>
//   [data-support-form-banner]            generic (non-field) error banner
//   [data-support-form-submit]            submit button (data-label/data-busy-label)
//   [data-support-form-counter="<id>"]    character counter for the control #<id>
//   [data-support-form-confirmation]      confirmation card, hidden until success
//   [data-support-form-value="<field>"]   confirmation recap value slots
//   Each control has id support-<field>, with a sibling #<id>-error paragraph.
//
// Graceful degradation: on PR-preview buckets and `make serve` there is no
// /api/support origin, so the POST fails or returns S3's XML error — either
// way the banner shows and the sessionStorage draft keeps the user's entries.

const ENDPOINT = "/api/support";
const DRAFT_KEY = "pulumi-support-form-draft";

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const ORGANIZATION_PATTERN = /^[a-zA-Z0-9][a-zA-Z0-9-_]*$/;
// Mirrors LIMITS.organization in infrastructure/support-form/validation.ts.
// Duplicated rather than shared because the two live in different build
// systems; the server is authoritative, so drift costs a round trip, not
// correctness — except if this one is ever the SMALLER of the two, which would
// hard-block a value the API would have accepted.
const ORGANIZATION_MAX = 40;

// Field keys are the API payload keys; ids are the DOM ids in the layout.
const FIELD_IDS: Record<string, string> = {
    email: "support-email",
    name: "support-name",
    organization: "support-organization",
    priority: "support-priority",
    subject: "support-subject",
    description: "support-description",
};

type FormControl = HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement;

// Strips a pasted console URL down to the bare organization name. Mirrors
// normalizeOrganization in infrastructure/support-form/validation.ts.
function normalizeOrganization(raw: string): string {
    let value = raw.trim();
    value = value.replace(/^https?:\/\/(www\.)?app\.pulumi\.com\//i, "");
    value = value.replace(/^app\.pulumi\.com\//i, "");
    value = value.replace(/^\/+/, "");
    const slash = value.indexOf("/");
    if (slash !== -1) {
        value = value.slice(0, slash);
    }
    return value.trim();
}

// Fills a control without clobbering what the user already typed.
//
// A <select> always reports a value (its first option is selected by default),
// so the emptiness guard that protects the text inputs would skip it every
// time — which is why both the draft restore and the ?priority= prefill used to
// silently do nothing. Selects are matched against their own options instead,
// which doubles as validation: a bogus value is ignored rather than blanking
// the control. Returns whether this call actually changed the control.
function setControlValue(input: FormControl, value: string): boolean {
    if (input instanceof HTMLSelectElement) {
        if (!Array.from(input.options).some(option => option.value === value)) {
            return false;
        }
    } else if (input.value) {
        return false;
    }
    // Reports false when the control already held this value, so a caller can
    // tell "the user chose this" from "it was already the default". A <select>
    // is always in the draft (it always has a value, so saveDraft always stores
    // it), and treating that as a deliberate choice would let a stale default
    // silently outrank an explicit ?priority= in the URL.
    if (input.value === value) {
        return false;
    }
    input.value = value;
    return true;
}

function init() {
    const root = document.querySelector<HTMLElement>("[data-support-form-root]");
    if (!root) {
        return;
    }
    const formNode = root.querySelector<HTMLFormElement>("[data-support-form]");
    const formCardNode = root.querySelector<HTMLElement>("[data-support-form-card]");
    const confirmationNode = root.querySelector<HTMLElement>("[data-support-form-confirmation]");
    const bannerNode = root.querySelector<HTMLElement>("[data-support-form-banner]");
    const submitButtonNode = root.querySelector<HTMLButtonElement>("[data-support-form-submit]");
    if (!formNode || !formCardNode || !confirmationNode || !bannerNode || !submitButtonNode) {
        return;
    }
    // Re-bind after the guard so the narrowed (non-null) types flow into the
    // nested function declarations below.
    const form = formNode;
    const formCard = formCardNode;
    const confirmation = confirmationNode;
    const banner = bannerNode;
    const submitButton = submitButtonNode;

    const control = (field: string): FormControl | null =>
        form.querySelector<FormControl>(`#${FIELD_IDS[field]}`);

    // --- Per-field error plumbing -----------------------------------------

    const errorElement = (field: string): HTMLElement | null =>
        form.querySelector<HTMLElement>(`#${FIELD_IDS[field]}-error`);

    function setError(field: string, message: string): void {
        const input = control(field);
        const error = errorElement(field);
        if (input) {
            input.setAttribute("aria-invalid", "true");
        }
        if (error) {
            error.textContent = message;
            error.hidden = false;
        }
    }

    function clearError(field: string): void {
        const input = control(field);
        const error = errorElement(field);
        if (input) {
            input.removeAttribute("aria-invalid");
        }
        if (error) {
            error.textContent = "";
            error.hidden = true;
        }
    }

    function firstInvalidControl(): FormControl | null {
        return form.querySelector<FormControl>('[aria-invalid="true"]');
    }

    // --- Validation (mirrors the server's rules) --------------------------

    // Each validator returns an error message or null. Values arrive trimmed.
    const validators: Record<string, (value: string) => string | null> = {
        email: value => {
            if (!value) {
                return "Enter your email address.";
            }
            if (value.length > 254 || !EMAIL_PATTERN.test(value)) {
                return "Enter a valid email address.";
            }
            return null;
        },
        name: value => (value ? null : "Enter your full name."),
        organization: value => {
            if (!value) {
                return "Enter your Pulumi organization name.";
            }
            const normalized = normalizeOrganization(value);
            if (normalized.length > ORGANIZATION_MAX) {
                return `Keep the organization name to ${ORGANIZATION_MAX} characters or fewer.`;
            }
            if (!ORGANIZATION_PATTERN.test(normalized)) {
                return "Enter just the organization name from https://app.pulumi.com/PULUMI_ORG_NAME (letters, numbers, hyphens, and underscores).";
            }
            return null;
        },
        // Checked against the options the layout actually rendered, rather than
        // a hardcoded copy of the enum. A third place to keep in sync would go
        // stale the first time someone adds a priority to the front matter, and
        // the failure is nasty: the new option would be permanently
        // unsubmittable with no server round trip to explain why.
        priority: value => {
            const select = control("priority");
            if (!(select instanceof HTMLSelectElement)) {
                return null;
            }
            return Array.from(select.options).some(option => option.value === value)
                ? null
                : "Choose a priority.";
        },
        subject: value => (value ? null : "Enter a subject."),
        description: value =>
            value.length >= 10 ? null : "Describe the issue in at least a few words.",
    };

    function validateField(field: string): boolean {
        const input = control(field);
        if (!input) {
            return true;
        }
        const message = validators[field](input.value.trim());
        if (message) {
            setError(field, message);
            return false;
        }
        clearError(field);
        return true;
    }

    function validateAll(): boolean {
        let ok = true;
        for (const field of Object.keys(validators)) {
            // Validate every field so all errors show at once, not just the first.
            ok = validateField(field) && ok;
        }
        return ok;
    }

    // --- Data-entry conveniences ------------------------------------------

    // Organization: strip a pasted console URL down to the org name.
    const organizationInput = control("organization");
    if (organizationInput) {
        organizationInput.addEventListener("blur", () => {
            organizationInput.value = normalizeOrganization(organizationInput.value);
        });
    }

    // Character counters for long fields, shown once the user nears the limit.
    root.querySelectorAll<HTMLElement>("[data-support-form-counter]").forEach(counter => {
        const target = document.getElementById(counter.dataset.supportFormCounter || "") as FormControl | null;
        if (!target) {
            return;
        }
        const max = Number(target.getAttribute("maxlength"));
        if (!max) {
            return;
        }
        const update = () => {
            const remaining = max - target.value.length;
            counter.hidden = remaining > max * 0.1;
            counter.textContent = `${remaining.toLocaleString()} characters left`;
        };
        target.addEventListener("input", update);
        update();
    });

    // Draft persistence: a failed submit (or an accidental navigation) never
    // loses the user's entries. sessionStorage access can throw (private
    // windows, blocked storage) — degrade to no persistence.
    const draftFields = ["email", "name", "organization", "priority", "subject", "description"];

    function saveDraft(): void {
        try {
            const draft: Record<string, string> = {};
            for (const field of draftFields) {
                const input = control(field);
                if (input && input.value) {
                    draft[field] = input.value;
                }
            }
            sessionStorage.setItem(DRAFT_KEY, JSON.stringify(draft));
        } catch (e) {
            // Storage unavailable; drafts just don't persist.
        }
    }

    // Returns the fields the draft actually changed, so the query-param prefill
    // below doesn't overwrite the user's own recovered work. A field whose draft
    // value merely matched what was already there isn't in the set — that's a
    // default, not a choice.
    function restoreDraft(): Set<string> {
        const restored = new Set<string>();
        try {
            const raw = sessionStorage.getItem(DRAFT_KEY);
            if (!raw) {
                return restored;
            }
            const draft = JSON.parse(raw) as Record<string, string>;
            for (const field of draftFields) {
                const input = control(field);
                if (input && typeof draft[field] === "string" && setControlValue(input, draft[field])) {
                    restored.add(field);
                }
            }
        } catch (e) {
            // Ignore unreadable drafts.
        }
        return restored;
    }

    function clearDraft(): void {
        try {
            sessionStorage.removeItem(DRAFT_KEY);
        } catch (e) {
            // Ignore.
        }
    }

    let draftTimer: number | undefined;
    form.addEventListener("input", () => {
        window.clearTimeout(draftTimer);
        draftTimer = window.setTimeout(saveDraft, 500);
    });

    const restoredFields = restoreDraft();

    // Query-param prefill, e.g. /support/new/?priority=urgent&subject=CLI+crash.
    // A recovered draft is the user's own work, so it wins over the URL.
    const params = new URLSearchParams(window.location.search);
    for (const field of ["priority", "subject", "email", "organization"]) {
        const value = params.get(field);
        const input = control(field);
        if (value && input && !restoredFields.has(field)) {
            setControlValue(input, value);
        }
    }

    // Errors clear as the user fixes the field.
    for (const field of Object.keys(validators)) {
        const input = control(field);
        if (!input) {
            continue;
        }
        input.addEventListener("input", () => clearError(field));
        input.addEventListener("blur", () => {
            if (input.value.trim()) {
                validateField(field);
            }
        });
    }

    // --- Submit -----------------------------------------------------------

    function setBusy(busy: boolean): void {
        submitButton.disabled = busy;
        submitButton.setAttribute("aria-busy", String(busy));
        const label = busy ? submitButton.dataset.busyLabel : submitButton.dataset.label;
        if (label) {
            submitButton.textContent = label;
        }
    }

    function buildPayload(): Record<string, unknown> {
        const value = (field: string) => (control(field)?.value || "").trim();
        const payload: Record<string, unknown> = {
            email: value("email"),
            name: value("name"),
            organization: normalizeOrganization(value("organization")),
            priority: value("priority"),
            subject: value("subject"),
            description: value("description"),
        };
        // Honeypot travels with the payload so the server can drop bot fills.
        const honeypot = form.querySelector<HTMLInputElement>("#support-website");
        if (honeypot && honeypot.value) {
            payload.website = honeypot.value;
        }
        return payload;
    }

    function showConfirmation(payload: Record<string, unknown>): void {
        confirmation.querySelectorAll<HTMLElement>("[data-support-form-value]").forEach(node => {
            const value = payload[node.dataset.supportFormValue || ""];
            if (typeof value === "string" && value) {
                node.textContent = value;
            }
        });
        formCard.hidden = true;
        confirmation.hidden = false;
        confirmation.focus();
        confirmation.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    form.addEventListener("submit", async event => {
        event.preventDefault();
        banner.hidden = true;

        if (!validateAll()) {
            firstInvalidControl()?.focus();
            return;
        }

        const payload = buildPayload();
        setBusy(true);
        try {
            const response = await fetch(ENDPOINT, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            let body: any = null;
            try {
                body = await response.json();
            } catch (e) {
                // Non-JSON response (e.g. an S3 error page on preview
                // environments without the API) — treated as a failure below.
            }

            if (response.ok && body && body.ok) {
                clearDraft();
                showConfirmation(payload);
                (window as any).analytics?.track?.("form-submission", {
                    form_id: "support-request",
                    priority: payload.priority,
                });
                return;
            }

            if (response.status === 422 && body && body.fields) {
                for (const field of Object.keys(body.fields)) {
                    if (FIELD_IDS[field]) {
                        setError(field, String(body.fields[field]));
                    } else {
                        banner.hidden = false;
                    }
                }
                firstInvalidControl()?.focus();
                if (firstInvalidControl() === null) {
                    banner.hidden = false;
                }
                return;
            }

            banner.hidden = false;
        } catch (e) {
            // Network failure — the draft is saved; the user can retry.
            banner.hidden = false;
        } finally {
            setBusy(false);
        }
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
