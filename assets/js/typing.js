(function($) {
    var spans = $(".typing span");
    var offset = 500 /* ms */;
    var delay = 150 /* ms */;

    // Wrap every character in a span to make it individually selectable.
    spans.each(function(i, span) {
        var chars = span.textContent.split("");

        $(span).html(chars.map(function(char) {
            return "<span class='char'>" + char + "</span>";
        }));
    });

    // Create an element to represent the cursor.
    var cursor = $("<span class='cursor'></span>");

    $(".char").map(function(i, el) {
        offset += Math.ceil(Math.random() * delay);

        // Position the cursor in relation to the character. If a line break is
        // encountered, show the cursor before the line break (as we pause for
        // line breaks); otherwise, show it after the character.
        setTimeout(function() {
            if (el.textContent === "\n") {
                $(el).css("opacity", 1).prepend(cursor);
            } else {
                $(el).css("opacity", 1).append(cursor);
            }
        }, offset);

        // Wait a bit at the end of each line, just to give the viewer a moment to note
        // what was expressed.
        if (el.textContent === "\n" || el.textContent === ";") {
            offset += 1000 /* ms */;
        }
    });
})(jQuery);
