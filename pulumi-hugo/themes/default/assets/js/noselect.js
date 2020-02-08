$(function() {
    // Make the prompt inside command line code snippets unselectable.
    function noselect(langs, pattern) {
        var replaceWith = '<span class="no-select">$1</span>';
        var selector = langs.map(function(lang) {
            return ".highlight .chroma .language-" + lang;
        }).join(", ");

        $(selector).each(function() {
            var $el = $(this);
            $el.html($el.html().replace(pattern, replaceWith));
        });
    }

    noselect(["bash", "sh", "shell", "zsh"], /([ |\t]*\$ )/mig);
    noselect(["bat", "batch", "batchfile", "powershell", "posh", "pwsh"], /([ |\t]*<span class="p">&gt;<\/span> )/mig);
});
