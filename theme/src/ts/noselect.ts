document.addEventListener("DOMContentLoaded", function () {
    function noselect(langs, pattern) {
        var replaceWith = '<span class="no-select">$1</span>';
        var selector = langs
            .map(function (lang) {
                return ".highlight .chroma .language-" + lang;
            })
            .join(", ");

        document.querySelectorAll(selector).forEach(el => {
            el.innerHTML = el.innerHTML.replace(pattern, replaceWith);
        });
    }

    noselect(["bash", "sh", "shell", "zsh"], /([ |\t]*\$ )/gim);
    noselect(["bat", "batch", "batchfile", "powershell", "posh", "pwsh"], /([ |\t]*<span class="p">&gt;<\/span> )/gim);
});
