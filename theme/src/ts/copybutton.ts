("use strict");

function normalizeText(lang, text) {
    if (!text) {
        return "";
    }

    text = text.replace("\r\n", "\n");
    text = text.trim();

    var prompt;
    var comment;
    var trailingCommentRE;
    var trailingContinuationChar;
    var combinator;
    switch (lang) {
        case "bash":
        case "sh":
        case "shell":
        case "zsh":
            prompt = "$ ";
            comment = "#";
            trailingCommentRE = /\s+#.*$/m;
            trailingContinuationChar = "\\";
            combinator = " && ";
            break;

        case "bat":
        case "batch":
        case "batchfile":
            prompt = "> ";
            comment = "::";
            trailingCommentRE = /\s+::.*$/m;
            trailingContinuationChar = "^";
            combinator = " && ";
            break;

        case "powershell":
        case "posh":
        case "pwsh":
            prompt = "> ";
            comment = "#";
            trailingCommentRE = /\s+#.*$/m;
            trailingContinuationChar = "`";
            combinator = "; ";
            break;
    }
    if (prompt) {
        var results = [];
        var lines = text.split("\n");
        var priorLineContinued = false;
        for (var i = 0; i < lines.length; i++) {
            var line = lines[i].trim();

            if (i === 0 && !line.startsWith(prompt)) {
                break;
            }

            if (line.length === 0 || line.startsWith(comment)) {
                priorLineContinued = false;
                continue;
            }

            if (line.startsWith(prompt) || priorLineContinued) {
                line = line.replace(trailingCommentRE, "");

                var wasContinued = priorLineContinued;
                if (line.endsWith(trailingContinuationChar)) {
                    priorLineContinued = true;
                    line = line.substring(0, line.length - trailingContinuationChar.length);
                } else {
                    priorLineContinued = false;
                }

                if (wasContinued) {
                    results.push(results.pop() + line);
                } else {
                    results.push(line.substring(2));
                }
            } else {
                break;
            }
        }

        if (results.length > 0) {
            text = results.join(combinator);
        }
    }

    if (navigator.appVersion.indexOf("Win") !== -1) {
        text = text.replace("\n", "\r\n");
    }

    return text;
}

function addCopyButton(container: HTMLElement) {
    var tooltipText = "Copy";
    var buttonHtml =
        '<div class="copy-button-container">' +
        "    <pulumi-tooltip>" +
        '        <button class="copy-button"><i class="far fa-copy copy"></i></button>' +
        '        <span slot="content">' +
        tooltipText +
        "</span>" +
        "    </pulumi-tooltip>" +
        "</div>";

    container.insertAdjacentHTML("beforeend", buttonHtml);
    container.addEventListener("click", function (event) {
        const target = event.target as HTMLElement;
        const btn = target.closest("button.copy-button") as HTMLElement;
        if (!btn) return;

        const tooltipEl = btn.closest("pulumi-tooltip") as any;
        const copyButtonContainer = tooltipEl?.closest(".copy-button-container");
        const pre = copyButtonContainer?.parentElement?.querySelector("pre");
        const code = pre?.querySelector("code");

        if (!code) return;

        var lang = code.getAttribute("data-lang");
        var text = code.textContent;

        var normalized = normalizeText(lang, text);
        if (normalized && normalized.length > 0) {
            navigator.clipboard.writeText(normalized).catch(() => {});
        }

        btn.blur();

        var tooltipContent = tooltipEl?.querySelector("[slot='content']");

        if (tooltipContent) {
            tooltipContent.textContent = "Copied!";
        }
        if (tooltipEl?.show) {
            tooltipEl.show().then(() => {
                setTimeout(function () {
                    if (tooltipEl?.hide) {
                        tooltipEl.hide().then(() => {
                            if (tooltipContent) tooltipContent.textContent = tooltipText;
                        });
                    }
                }, 1000);
            });
        }

        const analytics = (window as any).analytics;
        const analyticsAvailable = analytics && analytics.track && typeof analytics.track === "function";
        var codeBlockName = code.getAttribute("data-track");

        if (analyticsAvailable && codeBlockName) {
            const trackData = {
                codeBlockName: codeBlockName
            };
            analytics.track("copy-code-block", trackData);
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll<HTMLElement>(":not(.no-copy) > div.highlight").forEach(el => {
        addCopyButton(el);
    });
});
