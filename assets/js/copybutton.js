// When the DOM is ready, add copy buttons to code snippets.
$(function() {
    "use strict";

    // Used to "normalize" code snippet text that will be written to the clipboard.
    function normalizeText(lang, text) {
        if (!text) {
            return "";
        }

        // Replace all "\r\n" with "\n" to ensure consistent newlines.
        text = text.replace("\r\n", "\n");

        // Trim whitespace.
        text = text.trim();

        // For bash and shell code snippets:
        //   1. Strip any lines that are prefixed with "$ "
        //   2. Discard subsequent lines that don't start with "$ " (i.e. output)
        //   3. Combine multiple lines that start with "$ " into a single line, e.g.
        //      "$ mkdir mydir && mydir\n$ pulumi new typescript" =>
        //      "mkdir mydir && mydir && pulumi new typescript"
        if (lang === "bash" || lang === "shell" || lang === "sh") {
            var results = [];
            var lines = text.split("\n");
            for (var i = 0; i < lines.length; i++) {
                var line = lines[i].trim();

                // If the first line doesn't start with "$ ", break out of the loop to avoid any
                // further processing, so the whole thing is returned.
                if (i === 0 && !line.startsWith("$ ")) {
                    break;
                }

                // Skip empty lines and comments.
                if (line.length === 0 || line.startsWith("#")) {
                    continue;
                }

                // Include all initial lines that start with "$ " and discard subsequent lines after
                // a line is reached that doesn't start with "$ ".
                if (line.startsWith("$ ")) {
                    results.push(line.substring(2));
                } else {
                    break;
                }
            }

            // If we have results, combine into a single line, with commands separated by " && ".
            if (results.length > 0) {
                text = results.join(" && ");
            }
        }

        // If on Windows, ensure the appropriate line endings are applied.
        if (navigator.appVersion.indexOf("Win") !== -1) {
            text = text.replace("\n", "\r\n");
        }

        return text;
    }

    var buttonHtml =
        '<div class="copy-button-container">\n' +
        '    <button class="copy-button">\n' +
        '        <i class="far fa-copy copy text-xl" title="Copy code snippet"></i>\n' +
        '    </button>\n' +
        '    <span class="copy-button-tooltip">Copied!</span>\n'+
        '</div>';

    $(":not(.no-copy) > div.highlight")
        .addClass("relative")
        .append(buttonHtml)
        .on("click", "button.copy-button", function() {
            var $b = $(this);
            var $code = $b.parent().siblings("pre").children("code");

            // Get the lang and code.
            var lang = $code.attr("data-lang");
            var text = $code.text();

            // Write the text to the clipboard.
            var normalized = normalizeText(lang, text);
            if (normalized && normalized.length > 0) {
                clipboard.writeText(normalized);
            }

            // Remove focus from the button.
            $b.blur();

            // Show a "Copied!" tooltip for a second.
            var duration = 1000;
            var $tooltip = $b.siblings(".copy-button-tooltip").fadeIn();
            setTimeout(function() {
                $tooltip.fadeOut();
            }, duration);
        })
});
