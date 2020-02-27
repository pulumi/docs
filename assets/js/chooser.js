function getElemClasses(e) {
    return ($(e).attr("class") || "").split(/\s+/);
}

// selectChoice will remember a given choice -- such as language or operating system -- as a preferred setting using
// a cookie and walk the DOM enabling all code tabs and snippets for that choice, and disabling those for others.
function selectChoice(kind, choice, extra) {
    // Explicitly set `path` to `/` so the saved selection is available across all pages, and
    // set `max-age` to one year (31536000 is one year in seconds) so the saved selection does
    // not expire when the browser session ends.
    document.cookie = "pulumi_" + kind + "=" + choice + "; max-age=31536000; path=/"

    // Change the active tab.
    var choiceTabs = 0;
    $("a." + kind + "-tab").each(function (i, e) {
        choiceTabs++;

        var $e = $(e);
        var currentTabChoice = $e.attr("data-choice") || e.innerText.toLowerCase();
        if (currentTabChoice === choice) {
            $e.addClass("is-active");
        } else {
            $e.removeClass("is-active");
        }
    });

    // If and only if we found tabs, show and hide divs for the relevant choices.
    if (choiceTabs > 0) {
        $("div,span").each(function (i, e) {
            var classes = getElemClasses(e);
            for (var i = 0; i < classes.length; i++) {
                if (classes[i].startsWith(kind + "-prologue-")) {
                    var next = $(e).next();
                    if (next) {
                        if (classes[i] === kind + "-prologue-" + choice) {
                            $(next).show();
                        } else {
                            $(next).hide();
                        }
                    }
                    break;
                }
            }
        });

        if (extra) {
            extra();
        }
    }
}

// selectLanguage chooses a language.
function selectLanguage(lang) {
    selectChoice("language", lang, function() {
        var shellLanguages = ["bat", "batch", "batchfile", "powershell", "posh", "pwsh", "bash", "sh", "shell", "zsh"].map(
            function(l) {
                return "language-" + l;
            }
        );
        // In addition to the basic showing/hiding, highlight the right code blocks:
        $("code").each(function (i, e) {
            var classes = getElemClasses(e);
            for (var i = 0; i < classes.length; i++) {
                if (classes[i].startsWith("language-") && shellLanguages.indexOf(classes[i]) === -1) {
                    var parents = $(e).parents("div.highlight");
                    if (!parents.length) {
                        parents = $(e).parents("span.highlight");
                    }

                    // Our Node reference docs contain examples written in TypeScript, and
                    // don't currently have JavaScript examples above.
                    // Ensure these TypeScript examples are always visible, even when
                    // JavaScript is the selected language.
                    if (lang === "javascript" &&
                        (classes[i] === "language-typescript" || classes[i] === "language-ts")) {
                        // If the previous element doesn't have a highlight, show it.
                        var prev = parents.prev();
                        if (prev && !prev.hasClass("highlight")) {
                            parents.show();
                            break;
                        }
                    }

                    if (classes[i] === "language-"+lang ||
                        (lang === "typescript" && classes[i] === "language-ts") ||
                        (lang === "javascript" && classes[i] === "language-js") ||
                        (lang === "visualbasic" && classes[i] === "language-vb")) {
                        parents.show();
                    } else {
                        parents.hide();
                    }
                    break;
                }
            }
        });
    });
}

// selectOs chooses an operating system.
function selectOs(os) {
    selectChoice("os", os);
}

// selectCloud chooses a cloud provider.
function selectCloud(cloud) {
    selectChoice("cloud", cloud);
}

// selectCloud chooses a kubernetes language syntax.
function selectK8sLang(syntax) {
    selectChoice("k8s-language", syntax);
}

// Hides and shows choices based on previous preferences.
function hideShowChoices(kind, selector, defaultChoice) {
    var tabsOnPage = {};
    $("a." + kind + "-tab").each(function (i, e) {
        var choice = $(e).attr("data-choice") || e.innerText.toLowerCase();

        // Save the languages we've seen.
        tabsOnPage[choice] = true;

        // For every language tab, inject a handler and make the correct one hidden.
        e.addEventListener("click", function() {

            // Choosing a tab currently affects the selection state of all of the other
            // tabs on the page, which can cause unpredictable reflows, so we note the
            // current position of the clicked element relative to the upper edge of the
            // viewport, do the selection, then scroll to the same relative location once
            // the reflow is complete.
            var el = $(this).get(0);
            var distanctFromViewportTop = el.getBoundingClientRect().top;

            selector(choice, e);

            requestAnimationFrame(function() {
                window.scroll(0, el.offsetTop - distanctFromViewportTop);
            });
        });
    });

    var tabsOnPageKeys = Object.keys(tabsOnPage);

    // If we didn't find any tabs, there's nothing else to do.
    if (tabsOnPageKeys.length === 0) {
        return;
    }

    // Now select the right choice based on whether there's a cookie, defaulting as appropriate.
    var choiceCookie = decodeURIComponent(
        document.cookie.replace(new RegExp("(?:(?:^|.*;\\s*)pulumi_" + kind + "\\=\\s*([^;]*).*$)|^.*$"), "$1"));
    if (choiceCookie && tabsOnPage.hasOwnProperty(choiceCookie)) {
        selector(choiceCookie);
    } else if (defaultChoice && tabsOnPage.hasOwnProperty(defaultChoice)) {
        selector(defaultChoice);
    } else if (tabsOnPageKeys.length > 0) {
        selector(tabsOnPageKeys[0]);
    }
}

// The first time the DOM is finished loading, select the right language and OS.
$(document).on("rendered", function() {

    // If a query param's been provided for a tab category, honor that.
    ["language", "os", "cloud", "k8s-language"].forEach(function(kind) {
        var val = getQueryVariable(kind);
        if (val) {
            selectChoice(kind, val);
        }
    });

    // If no language is chosen yet, default to TypeScript.
    hideShowChoices("language", selectLanguage, "typescript");

    // If no OS is chosen yet, do our best to detect it using the browser.
    var defaultOsChoice;
    if (navigator.appVersion.indexOf("Win") !== -1) {
        defaultOsChoice = "windows";
    } else if (navigator.appVersion.indexOf("Mac") !== -1) {
        defaultOsChoice = "macos";
    } else if (navigator.appVersion.indexOf("Linux") !== -1) {
        defaultOsChoice = "linux";
    }
    hideShowChoices("os", selectOs, defaultOsChoice);
    hideShowChoices("cloud", selectCloud, "aws");
    hideShowChoices("k8s-language", selectK8sLang, "typescript");
});
