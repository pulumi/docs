function initCodeSnippets() {
    const containers = document.querySelectorAll<HTMLElement>(".code-snippets-container");

    containers.forEach((container) => {
        const trigger = container.querySelector<HTMLButtonElement>(".code-snippets-dropdown-trigger");
        const menu = container.querySelector<HTMLElement>(".code-snippets-dropdown-menu");
        const items = container.querySelectorAll<HTMLElement>(".code-snippets-dropdown-item");
        const panels = container.querySelectorAll<HTMLElement>(".code-snippets-panel");
        const labelEl = container.querySelector<HTMLElement>(".code-snippets-dropdown-label");
        const titleEl = container.querySelector<HTMLElement>(".code-snippets-title");
        const defaultTitle = titleEl?.dataset.defaultTitle ?? "";

        if (!trigger || !menu) return;

        function openMenu() {
            menu!.classList.add("open");
            trigger!.setAttribute("aria-expanded", "true");
            container.querySelector<HTMLElement>(".code-snippets-dropdown")?.setAttribute("aria-expanded", "true");
            const activeItem = menu!.querySelector<HTMLElement>(".code-snippets-dropdown-item.active");
            activeItem?.focus();
        }

        function closeMenu() {
            menu!.classList.remove("open");
            trigger!.setAttribute("aria-expanded", "false");
            container.querySelector<HTMLElement>(".code-snippets-dropdown")?.setAttribute("aria-expanded", "false");
        }

        function selectLanguage(item: HTMLElement) {
            const language = item.dataset.language;
            const label = item.dataset.label ?? language ?? "";
            const snippetTitle = item.dataset.snippetTitle ?? "";

            items.forEach((i) => {
                i.classList.toggle("active", i === item);
                i.setAttribute("aria-selected", i === item ? "true" : "false");
            });

            panels.forEach((panel) => {
                const isActive = panel.dataset.language === language;
                panel.classList.toggle("active", isActive);
                if (isActive) {
                    panel.removeAttribute("aria-hidden");
                } else {
                    panel.setAttribute("aria-hidden", "true");
                }
            });

            if (labelEl) labelEl.textContent = label;

            if (titleEl) {
                titleEl.textContent = snippetTitle || defaultTitle;
            }

            closeMenu();
            trigger!.focus();
        }

        trigger.addEventListener("click", () => {
            if (menu.classList.contains("open")) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        items.forEach((item) => {
            item.addEventListener("click", () => selectLanguage(item));

            item.addEventListener("keydown", (e: KeyboardEvent) => {
                const allItems = Array.from(items);
                const idx = allItems.indexOf(item);

                if (e.key === "ArrowDown") {
                    e.preventDefault();
                    allItems[(idx + 1) % allItems.length]?.focus();
                } else if (e.key === "ArrowUp") {
                    e.preventDefault();
                    allItems[(idx - 1 + allItems.length) % allItems.length]?.focus();
                } else if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    selectLanguage(item);
                } else if (e.key === "Escape") {
                    e.preventDefault();
                    closeMenu();
                    trigger!.focus();
                } else if (e.key === "Tab") {
                    closeMenu();
                }
            });
        });

        trigger.addEventListener("keydown", (e: KeyboardEvent) => {
            if (e.key === "ArrowDown" || e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                openMenu();
            } else if (e.key === "Escape") {
                closeMenu();
            }
        });

        document.addEventListener("click", (e: MouseEvent) => {
            if (!container.contains(e.target as Node)) {
                closeMenu();
            }
        });

        document.addEventListener("keydown", (e: KeyboardEvent) => {
            if (e.key === "Escape" && menu.classList.contains("open")) {
                closeMenu();
                trigger!.focus();
            }
        });
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCodeSnippets);
} else {
    initCodeSnippets();
}
