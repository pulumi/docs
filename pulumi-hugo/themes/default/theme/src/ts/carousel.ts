(function ($) {
    // The home-page carousel. Items cycle every four seconds. Clicking a label stops the
    // cycling and shows the selected item.

    var carouselItem = 1;

    var carouselInterval = window.setInterval(function () {
        showCarouselItem(carouselItem);
        carouselItem++;

        if (carouselItem > 2) {
            carouselItem = 0;
        }
    }, 11000);

    showCarouselItem(0);

    $(".carousel-item-label").click(function () {
        clearInterval(carouselInterval);

        var i = $(".carousel-item-label").index(this);
        showCarouselItem(i);
    });

    function showCarouselItem(i) {
        // On some pages we might want to show all the carousel animations at
        // once, so if this element is available we show everything and return.
        if ($(".carousel-always-visible").length) {
            showIDE();
            showCLI();
            showConsole();
            return;
        }

        if ($(".carousel-always-visible-cli-only").length) {
            showCLIOnly();
            return;
        }

        $(".carousel-item").css("opacity", 0).css("pointer-events", "none").eq(i).css("opacity", 1).css("pointer-events", "auto");

        $(".carousel-item-description").css("opacity", 0).css("pointer-events", "none").eq(i).css("opacity", 1).css("pointer-events", "auto");

        $(".carousel-item-label")
            .removeClass("border-purple-700")
            .removeClass("text-purple-700")
            .removeClass("hover:text-purple-700")
            .addClass("text-purple-200")
            .addClass("hover:text-purple-300")
            .eq(i)
            .addClass("border-purple-700")
            .addClass("text-purple-700")
            .addClass("hover:text-purple-700");

        if (i === 0) {
            showIDE();
        } else if (i === 1) {
            showCLI();
        } else if (i === 2) {
            showConsole();
        }
    }

    function showIDE() {
        // Hide the windows.
        $(".menu").css("opacity", 0);

        // Restore the selection state of the first menu.
        $(".menu").find(".row").removeClass("bg-gray-600").eq(0).addClass("bg-gray-600");

        // Start typing. On completion, show the menus.
        startTyping(0, function () {
            $(".menu").each(function (i, el) {
                var delay = parseInt($(el).attr("data-delay")) || 0;

                // Animate the selection indicator of the first menu when it's shown.
                if (i === 0) {
                    setTimeout(function () {
                        $(el).find(".row").removeClass("bg-gray-600").eq(1).addClass("bg-gray-600");
                    }, 600);
                }

                setTimeout(function () {
                    $(el).css("opacity", 1);
                }, delay);
            });
        });
    }

    function showCLI() {
        startTyping(1);
        showLines(1);
    }

    function showCLIOnly() {
        startTyping(0);
        showLines(0);
    }

    function showConsole() {
        var tabs = $("#carousel-console .tab");

        tabs.css("opacity", 0).eq(0).css("opacity", 1);

        setTimeout(function () {
            tabs.eq(0).css("opacity", 0);
            tabs.eq(1).css("opacity", 1);
        }, 5000);
    }

    function startTyping(i, onComplete?) {
        var spans = $(".carousel-item").eq(i).find(".line.typed span");
        var offset = 500; /* ms */
        var delay = 75; /* ms */

        // Wrap every character in a span to make it individually selectable.
        spans.each(function (i, span) {
            var chars = span.textContent.split("");

            $(span)
                .addClass("typing")
                .html(
                    chars
                        .map(char => {
                            return "<span class='char'>" + char + "</span>";
                        })
                        .join("")
                        .toString(),
                );
        });

        // Create an element to represent the cursor.
        var cursor = $("<span class='cursor'></span>");

        var chars = $(".carousel-item").eq(i).find(".char");
        chars.map(function (j, el) {
            offset += Math.ceil(Math.random() * delay);

            // Position the cursor in relation to the character. If a line break is
            // encountered, show the cursor before the line break (as we pause for
            // line breaks); otherwise, show it after the character.
            setTimeout(function () {
                if (el.textContent === "\n") {
                    $(el).css("opacity", 1).prepend(cursor);
                } else {
                    $(el).css("opacity", 1).append(cursor);
                }

                // If we've reached end of the input in the current view, remove the cursor.
                if (j === chars.length - 1) {
                    setTimeout(function () {
                        cursor.remove();

                        if (typeof onComplete === "function") {
                            onComplete();
                        }
                    }, 600);
                }
            }, offset);

            // Wait a bit at the end of each line, just to give the viewer a moment to note
            // what was expressed.
            if (el.textContent === "\n" || el.textContent === ";") {
                offset += 1000 /* ms */;
            }
        });
    }

    function showLines(i) {
        var lines = $(".carousel-item").eq(i).find(".line.full");
        lines.css("opacity", 0);
        var offset = 2000; /* ms */
        var delay = 75; /* ms */

        lines.each(function (i, el) {
            var d = parseInt($(el).attr("data-delay")) || delay;
            offset += Math.ceil(Math.random() * d);

            setTimeout(function () {
                $(el).css("opacity", 1);
            }, offset);
        });
    }
})(jQuery);
