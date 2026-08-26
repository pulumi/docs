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

// Mirrors EMAIL_PATTERN in infrastructure/support-form/validation.ts, including
// the separator characters excluded there.
const EMAIL_PATTERN = /^[^\s@<>",;]+@[^\s@<>",;]+\.[^\s@<>",;]+$/;
const ORGANIZATION_PATTERN = /^[a-zA-Z0-9][a-zA-Z0-9-_]*$/;
// Mirrors LIMITS.organization in infrastructure/support-form/validation.ts.
// Duplicated rather than shared because the two live in different build
// systems; the server is authoritative, so drift costs a round trip, not
// correctness — except if this one is ever the SMALLER of the two, which would
// hard-block a value the API would have accepted.
const ORGANIZATION_MAX = 40;

// The rest of LIMITS, mirrored for the same reason and with the same caveat:
// the server is authoritative, these only save a round trip. Without them a
// value that arrived by prefill or by paste past the maxlength sailed through
// to a 422.
const EMAIL_MAX = 254;
const NAME_MAX = 200;
const SUBJECT_MAX = 200;
const DESCRIPTION_MAX = 20000;
const DESCRIPTION_MIN = 10;

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
    // One pattern, matching the server's. As two, the schemeless branch did not
    // allow www., so "www.app.pulumi.com/my-org" reduced to the host name and
    // was then hard-blocked by ORGANIZATION_PATTERN -- exactly the
    // client-stricter-than-the-API failure the note above warns about.
    value = value.replace(/^(https?:\/\/)?(www\.)?app\.pulumi\.com\//i, "");
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
// the control. Returns whether the value was applied.
function setControlValue(input: FormControl, value: string): boolean {
    if (input instanceof HTMLSelectElement) {
        if (!Array.from(input.options).some(option => option.value === value)) {
            return false;
        }
    } else if (input.value) {
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
            if (value.length > EMAIL_MAX || !EMAIL_PATTERN.test(value)) {
                return "Enter a valid email address.";
            }
            return null;
        },
        name: value => {
            if (!value) {
                return "Enter your full name.";
            }
            return value.length > NAME_MAX ? `Keep your name to ${NAME_MAX} characters or fewer.` : null;
        },
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
            if (select instanceof HTMLSelectElement) {
                return Array.from(select.options).some(option => option.value === value)
                    ? null
                    : "Choose a priority.";
            }
            // Not a <select> — someone changed the layout. Fall back to
            // "non-empty" rather than passing anything through: the server's
            // closed enum is still authoritative, but silently accepting any
            // string here would cost the user a round trip to find that out.
            return value ? null : "Choose a priority.";
        },
        subject: value => {
            if (!value) {
                return "Enter a subject.";
            }
            return value.length > SUBJECT_MAX ? `Keep the subject to ${SUBJECT_MAX} characters or fewer.` : null;
        },
        description: value => {
            if (value.length < DESCRIPTION_MIN) {
                return "Describe the issue in at least a few words.";
            }
            return value.length > DESCRIPTION_MAX
                ? `Keep the description to ${DESCRIPTION_MAX.toLocaleString()} characters or fewer.`
                : null;
        },
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
    const counterUpdates: Array<() => void> = [];
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
            counter.textContent =
                remaining === 1 ? "1 character left" : `${remaining.toLocaleString()} characters left`;
        };
        target.addEventListener("input", update);
        update();
        // Re-run after the draft restore and the query-string prefill below,
        // which set values without firing `input`. Without it a restored 19,000
        // character description shows a hidden counter still reading the full
        // limit until the next keystroke.
        counterUpdates.push(update);
    });

    // Draft persistence: a failed submit (or an accidental navigation) never
    // loses the user's entries. sessionStorage access can throw (private
    // windows, blocked storage) — degrade to no persistence.
    const draftFields = ["email", "name", "organization", "priority", "subject", "description"];

    // Fields the user has actually interacted with. The draft holds only these,
    // which is what lets the query-param prefill below tell a real choice from a
    // default: a <select> always reports a value, so saving every field would
    // put priority: "normal" in the draft after a single keystroke elsewhere,
    // and a stale default would then outrank an explicit ?priority= in the URL.
    // Saving only touched fields also means "differs from the default" never has
    // to stand in for "the user chose it" — the two are not the same, and a user
    // who deliberately picks the default is entitled to have that stick.
    const touched = new Set<string>();

    const fieldById: Record<string, string> = {};
    for (const field of Object.keys(FIELD_IDS)) {
        fieldById[FIELD_IDS[field]] = field;
    }

    function markTouched(event: Event): void {
        const target = event.target as HTMLElement | null;
        const field = target && target.id ? fieldById[target.id] : undefined;
        if (field) {
            touched.add(field);
        }
    }

    // `change` as well as `input`, because a <select> fires only the former in
    // some browsers when navigated by keyboard.
    form.addEventListener("input", markTouched);
    form.addEventListener("change", markTouched);

    function saveDraft(): void {
        try {
            const draft: Record<string, string> = {};
            for (const field of draftFields) {
                if (!touched.has(field)) {
                    continue;
                }
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

    // Returns the fields recovered from the draft. Everything in a draft was
    // touched by the user, so these are choices, and the prefill must not
    // overwrite them. They are also re-marked as touched so the next save keeps
    // them rather than dropping what was just restored.
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
                if (input && typeof draft[field] === "string" && draft[field]) {
                    // Only a value that was actually applied counts as restored.
                    // A stale draft can name an option the page no longer
                    // renders (priority: "high"); treating that as restored
                    // would suppress the ?priority= prefill in favour of a value
                    // the control never took, so a visitor following an urgent
                    // link would file a normal ticket.
                    if (setControlValue(input, draft[field])) {
                        restored.add(field);
                        touched.add(field);
                    }
                }
            }
        } catch (e) {
            // Ignore unreadable drafts.
        }
        return restored;
    }

    let draftTimer: number | undefined;

    function clearDraft(): void {
        // Cancel the pending save first. saveDraft is debounced by 500ms, so a
        // submit that lands inside that window would otherwise have the timer
        // fire after the key was removed and write the draft straight back --
        // leaving a filed request sitting in the form on the next visit, ready
        // to be submitted twice.
        window.clearTimeout(draftTimer);
        try {
            sessionStorage.removeItem(DRAFT_KEY);
        } catch (e) {
            // Ignore.
        }
    }

    function scheduleSave(): void {
        window.clearTimeout(draftTimer);
        draftTimer = window.setTimeout(saveDraft, 500);
    }

    // Both events, for the same reason markTouched listens to both: a <select>
    // is not guaranteed to fire `input`, so debouncing on `input` alone means a
    // visitor who changes only the priority — touching nothing else — never has
    // that choice written to the draft, and loses it on a failed submit.
    form.addEventListener("input", scheduleSave);
    form.addEventListener("change", scheduleSave);

    const restoredFields = restoreDraft();

    // Query-param prefill, e.g. /support/new/?priority=urgent&subject=CLI+crash.
    // A recovered draft is the user's own work, so it wins over the URL.
    const params = new URLSearchParams(window.location.search);
    for (const field of ["priority", "subject", "email", "name", "organization"]) {
        const value = params.get(field);
        const input = control(field);
        if (value && input && !restoredFields.has(field)) {
            // Normalized on the way in for the same reason the blur handler
            // does it: a prefilled console URL would otherwise sit in the field
            // looking like it failed to work until the user touched it.
            setControlValue(input, field === "organization" ? normalizeOrganization(value) : value);
        }
    }

    // Both of the above set values without firing `input`, so the counters have
    // to be told.
    counterUpdates.forEach(update => update());

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
        // Clear the controls before hiding the card. The draft is already gone,
        // but browsers restore form state themselves when the user comes Back
        // to this history entry -- so without this they would land on a fully
        // repopulated form, with nothing on screen saying the request was
        // already filed, one click away from a duplicate ticket.
        form.reset();
        formCard.hidden = true;
        confirmation.hidden = false;
        confirmation.focus();
        confirmation.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    // In-flight guard. setBusy disables the submit button, and a browser will
    // not implicitly submit through a disabled default button, so this is
    // belt-and-braces -- but the cost of being wrong is a duplicate support
    // ticket, and the button is not the only thing that can raise a submit
    // event. Kept separate from setBusy so the two cannot drift.
    let submitting = false;

    form.addEventListener("submit", async event => {
        event.preventDefault();

        if (submitting) {
            return;
        }

        banner.hidden = true;

        if (!validateAll()) {
            firstInvalidControl()?.focus();
            return;
        }

        const payload = buildPayload();
        submitting = true;
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
            submitting = false;
            const hadFocus = document.activeElement === submitButton || document.activeElement === document.body;
            setBusy(false);
            // Disabling the button blurred it, which drops focus to <body> and
            // makes a keyboard user tab from the top of the document to retry.
            // Only reclaimed if focus had not moved somewhere deliberate --
            // the 422 path focuses the first invalid control, and that wins.
            if (hadFocus && document.activeElement === document.body) {
                submitButton.focus();
            }
        }
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
