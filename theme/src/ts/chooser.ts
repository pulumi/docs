import { getQueryVariable } from "./util";

function getElemClasses(e: Element) {
    return (e.getAttribute("class") || "").split(/\s+/);
}

function selectChoice(kind, choice, extra?) {
    document.cookie = "pulumi_" + kind + "=" + choice + "; max-age=31536000; path=/";

    var choiceTabs = 0;
    document.querySelectorAll<HTMLElement>("a." + kind + "-tab").forEach(e => {
        choiceTabs++;

        var currentTabChoice = e.getAttribute("data-choice") || e.innerText.toLowerCase();
        if (currentTabChoice === choice) {
            e.classList.add("is-active");
        } else {
            e.classList.remove("is-active");
        }
    });

    if (choiceTabs > 0) {
        document.querySelectorAll<HTMLElement>("div,span").forEach(e => {
            var classes = getElemClasses(e);
            for (var i = 0; i < classes.length; i++) {
                if (classes[i].startsWith(kind + "-prologue-")) {
                    var next = e.nextElementSibling as HTMLElement;
                    if (next) {
                        if (classes[i] === kind + "-prologue-" + choice) {
                            next.style.display = "";
                        } else {
                            next.style.display = "none";
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

function selectLanguage(lang) {
    selectChoice("language", lang, function () {
        var shellLanguages = ["bat", "batch", "batchfile", "powershell", "posh", "pwsh", "bash", "sh", "shell", "zsh", "diff"].map(function (l) {
            return "language-" + l;
        });
        document.querySelectorAll<HTMLElement>("code").forEach(e => {
            var classes = getElemClasses(e);
            for (var i = 0; i < classes.length; i++) {
                if (classes[i].startsWith("language-") && shellLanguages.indexOf(classes[i]) === -1) {
                    let parents = e.closest("div.highlight") || e.closest("span.highlight");

                    if (lang === "javascript" && (classes[i] === "language-typescript" || classes[i] === "language-ts")) {
                        var prev = (parents as HTMLElement)?.previousElementSibling;
                        if (prev && !prev.classList.contains("highlight")) {
                            (parents as HTMLElement).style.display = "";
                            break;
                        }
                    }

                    if (parents) {
                        if (
                            classes[i] === "language-" + lang ||
                            (lang === "typescript" && classes[i] === "language-ts") ||
                            (lang === "javascript" && classes[i] === "language-js") ||
                            (lang === "visualbasic" && classes[i] === "language-vb")
                        ) {
                            (parents as HTMLElement).style.display = "";
                        } else {
                            (parents as HTMLElement).style.display = "none";
                        }
                    }
                    break;
                }
            }
        });
    });
}

function selectOs(os) {
    selectChoice("os", os);
}

function selectCloud(cloud) {
    selectChoice("cloud", cloud);
}

function selectK8sLang(syntax) {
    selectChoice("k8s-language", syntax);
}

function hideShowChoices(kind, selector, defaultChoice) {
    var tabsOnPage = {};
    document.querySelectorAll<HTMLElement>("a." + kind + "-tab").forEach(e => {
        var choice = e.getAttribute("data-choice") || e.innerText.toLowerCase();

        tabsOnPage[choice] = true;

        e.addEventListener("click", function () {
            var distanctFromViewportTop = e.getBoundingClientRect().top;

            selector(choice, e);

            requestAnimationFrame(function () {
                window.scroll(0, e.offsetTop - distanctFromViewportTop);
            });
        });
    });

    var tabsOnPageKeys = Object.keys(tabsOnPage);

    if (tabsOnPageKeys.length === 0) {
        return;
    }

    var choiceCookie = decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;\\s*)pulumi_" + kind + "\\=\\s*([^;]*).*$)|^.*$"), "$1"));
    if (choiceCookie && tabsOnPage.hasOwnProperty(choiceCookie)) {
        selector(choiceCookie);
    } else if (defaultChoice && tabsOnPage.hasOwnProperty(defaultChoice)) {
        selector(defaultChoice);
    } else if (tabsOnPageKeys.length > 0) {
        selector(tabsOnPageKeys[0]);
    }
}

document.addEventListener("rendered", function () {
    ["language", "os", "cloud", "k8s-language", "input-kind"].forEach(function (kind) {
        var val = getQueryVariable(kind);
        if (val) {
            selectChoice(kind, val);
        }
    });

    hideShowChoices("language", selectLanguage, "typescript");

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
