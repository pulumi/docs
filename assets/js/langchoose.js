function getElemClasses(e) {
    return ($(e).attr("class") || "").split(/\s+/);
}

// selectLanguage will remember a given language as a preferred setting using a cookie and walk the DOM enabling
// all code tabs and snippets for this language, and disabling those for unselected languages.
function selectLanguage(lang) {
    $(function() {
        // Explicitly set `path` to `/` so the saved selection is available across all pages, and
        // set `max-age` to one year (31536000 is one year in seconds) so the saved selection does
        // not expire when the browser session ends.
        document.cookie = "pulumi_language=" + lang + "; max-age=31536000; path=/"

        // Change the active tab.
        var langTabs = 0;
        $("a.langtab").each(function (i, e) {
            langTabs++;
            if (e.innerText.toLowerCase() === lang) {
                $(e).addClass("is-active");
            } else {
                $(e).removeClass("is-active");
            }
        });

        // If and only if we found tabs, hide divs for the relevant languages.
        if (langTabs > 0) {
            // Highlighted code blocks:
            $("code").each(function (i, e) {
                var classes = getElemClasses(e);
                for (var i = 0; i < classes.length; i++) {
                    if (classes[i].startsWith("language-") && classes[i] !== "language-bash") {
                        var parents = $(e).parents("div.highlight");

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
                            (lang === "javascript" && classes[i] === "language-js")) {
                            parents.show();
                        } else {
                            parents.hide();
                        }
                        break;
                    }
                }
            });

            // Any explicit prologue elements:
            $("div,span").each(function (i, e) {
                var classes = getElemClasses(e);
                for (var i = 0; i < classes.length; i++) {
                    if (classes[i].startsWith("language-prologue-")) {
                        var next = $(e).next();
                        if (next) {
                            if (classes[i] === "language-prologue-"+lang) {
                                $(next).show();
                            } else {
                                $(next).hide();
                            }
                        }
                        break;
                    }
                }
            });
        }
    });
}

// The first time the DOM is finished loading, select the right language.  If no language is set as the preferred
// language yet, then JavaScript is chosen as the preferred language as a default.
$(function() {
    var tabLangsOnPage = {};
    $("a.langtab").each(function (i, e) {
        var lang = e.innerText.toLowerCase();

        // Save the languages we've seen.
        tabLangsOnPage[lang] = true;

        // For every language tab, inject a handler and make the correct one hidden.
        e.addEventListener("click", function() {
            selectLanguage(lang);
        });
    });

    var tabLangsOnPageKeys = Object.keys(tabLangsOnPage);

    // If we didn't find any lang tabs, there's nothing else to do.
    if (tabLangsOnPageKeys.length === 0) {
        return;
    }

    // Now select the right language based on whether there's a cookie, defaulting to JavaScript,
    // if it's among the tabs, otherwise falling back to the first lang we find.
    var langCookie = decodeURIComponent(
        document.cookie.replace(/(?:(?:^|.*;\s*)pulumi_language\s*\=\s*([^;]*).*$)|^.*$/, "$1"));

    if (langCookie && tabLangsOnPage.hasOwnProperty(langCookie)) {
        selectLanguage(langCookie);
    } else if (tabLangsOnPage.hasOwnProperty("javascript")) {
        selectLanguage("javascript");
    } else if (tabLangsOnPageKeys.length > 0) {
        selectLanguage(tabLangsOnPageKeys[0]);
    }
});
