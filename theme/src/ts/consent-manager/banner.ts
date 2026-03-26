import { ConsentManagerConfig, Destination } from "./types";
import { categorizeDestinations } from "./categories";

export function renderBanner(
    config: ConsentManagerConfig,
    onAcceptAll: () => void,
    onDenyAll: () => void,
    onManage: () => void,
): HTMLElement {
    const wrapper = document.createElement("div");

    const content = document.createElement("div");
    content.style.padding = "16px";

    const text = document.createElement("p");
    text.textContent = config.bannerText + " ";
    const link = document.createElement("a");
    link.href = config.privacyPolicyUrl;
    link.target = "_blank";
    link.textContent = "Privacy Policy";
    text.appendChild(link);
    text.appendChild(document.createTextNode("."));
    content.appendChild(text);

    const actions = document.createElement("div");
    actions.className = "consent-actions";

    const manageBtn = document.createElement("button");
    manageBtn.type = "button";
    manageBtn.className = "consent-btn consent-btn-secondary";
    manageBtn.textContent = "Manage cookies";
    manageBtn.addEventListener("click", onManage);

    const rejectBtn = document.createElement("button");
    rejectBtn.type = "button";
    rejectBtn.className = "consent-btn consent-btn-secondary";
    rejectBtn.textContent = "Reject All";
    rejectBtn.addEventListener("click", onDenyAll);

    const acceptBtn = document.createElement("button");
    acceptBtn.type = "button";
    acceptBtn.className = "consent-btn consent-btn-accept";
    acceptBtn.textContent = "Accept All";
    acceptBtn.addEventListener("click", onAcceptAll);

    actions.appendChild(manageBtn);
    actions.appendChild(rejectBtn);
    actions.appendChild(acceptBtn);
    content.appendChild(actions);

    wrapper.appendChild(content);
    return wrapper;
}

export function renderPreferencesDialog(
    config: ConsentManagerConfig,
    destinations: Destination[],
    currentPreferences: Record<string, boolean>,
    onSave: (prefs: Record<string, boolean>) => void,
    onCancel: () => void,
): HTMLElement {
    const categories = categorizeDestinations(destinations);

    const categoryState: Record<string, boolean> = {};
    for (const cat of categories) {
        if (!cat.toggleable) continue;
        categoryState[cat.key] = cat.tools.every((d) => currentPreferences[d.id] !== false);
    }

    const overlay = document.createElement("div");
    overlay.className = "consent-dialog-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", config.preferencesDialogTitle);

    const dialog = document.createElement("div");
    dialog.className = "consent-dialog";

    const header = document.createElement("div");
    header.className = "consent-dialog-header";
    const title = document.createElement("h2");
    title.textContent = config.preferencesDialogTitle;
    const closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.className = "consent-dialog-close";
    closeBtn.textContent = "\u00d7";
    closeBtn.setAttribute("aria-label", "Close");
    closeBtn.addEventListener("click", onCancel);
    header.appendChild(title);
    header.appendChild(closeBtn);
    dialog.appendChild(header);

    const desc = document.createElement("p");
    desc.className = "consent-dialog-desc";
    desc.textContent = config.preferencesDialogContent;
    dialog.appendChild(desc);

    const table = document.createElement("table");
    table.className = "consent-dialog-table";

    const thead = document.createElement("thead");
    const headRow = document.createElement("tr");
    for (const label of ["Allow", "Category", "Purpose", "Tools"]) {
        const th = document.createElement("th");
        th.textContent = label;
        headRow.appendChild(th);
    }
    thead.appendChild(headRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");

    for (const cat of categories) {
        const row = document.createElement("tr");

        const allowCell = document.createElement("td");
        allowCell.className = "consent-table-allow";
        if (cat.toggleable) {
            const yesLabel = document.createElement("label");
            const yesRadio = document.createElement("input");
            yesRadio.type = "radio";
            yesRadio.name = `consent-${cat.key}`;
            yesRadio.checked = categoryState[cat.key] !== false;
            yesLabel.appendChild(yesRadio);
            yesLabel.appendChild(document.createTextNode(" Yes"));

            const noLabel = document.createElement("label");
            const noRadio = document.createElement("input");
            noRadio.type = "radio";
            noRadio.name = `consent-${cat.key}`;
            noRadio.checked = categoryState[cat.key] === false;
            noLabel.appendChild(noRadio);
            noLabel.appendChild(document.createTextNode(" No"));

            yesRadio.addEventListener("change", () => {
                categoryState[cat.key] = true;
            });
            noRadio.addEventListener("change", () => {
                categoryState[cat.key] = false;
            });

            allowCell.appendChild(yesLabel);
            allowCell.appendChild(noLabel);
        } else {
            const na = document.createElement("span");
            na.className = "consent-table-na";
            na.textContent = "N/A";
            allowCell.appendChild(na);
        }
        row.appendChild(allowCell);

        const catCell = document.createElement("td");
        catCell.className = "consent-table-category";
        catCell.textContent = cat.name;
        row.appendChild(catCell);

        const purposeCell = document.createElement("td");
        purposeCell.className = "consent-table-purpose";
        purposeCell.textContent = cat.description;
        row.appendChild(purposeCell);

        const toolsCell = document.createElement("td");
        toolsCell.className = "consent-table-tools";
        toolsCell.textContent = cat.tools.map((d) => d.name).join(", ");
        row.appendChild(toolsCell);

        tbody.appendChild(row);
    }

    table.appendChild(tbody);
    dialog.appendChild(table);

    const buttons = document.createElement("div");
    buttons.className = "consent-dialog-buttons";

    const cancelBtn = document.createElement("button");
    cancelBtn.type = "button";
    cancelBtn.className = "consent-btn consent-btn-secondary";
    cancelBtn.textContent = "Cancel";
    cancelBtn.addEventListener("click", onCancel);

    const saveBtn = document.createElement("button");
    saveBtn.type = "button";
    saveBtn.className = "consent-btn consent-btn-accept";
    saveBtn.textContent = "Save";
    saveBtn.addEventListener("click", () => {
        const prefs: Record<string, boolean> = {};
        for (const cat of categories) {
            if (!cat.toggleable) continue;
            const allowed = categoryState[cat.key];
            for (const dest of cat.tools) {
                prefs[dest.id] = allowed;
            }
        }
        onSave(prefs);
    });

    buttons.appendChild(cancelBtn);
    buttons.appendChild(saveBtn);
    dialog.appendChild(buttons);

    overlay.appendChild(dialog);
    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) onCancel();
    });

    overlay.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            onCancel();
            return;
        }
        if (e.key === "Tab") {
            const focusable = dialog.querySelectorAll<HTMLElement>(
                'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
            );
            if (focusable.length === 0) return;
            const first = focusable[0];
            const last = focusable[focusable.length - 1];
            if (e.shiftKey && document.activeElement === first) {
                e.preventDefault();
                last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
                e.preventDefault();
                first.focus();
            }
        }
    });

    requestAnimationFrame(() => {
        const firstFocusable = dialog.querySelector<HTMLElement>(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
        );
        firstFocusable?.focus();
    });

    return overlay;
}
