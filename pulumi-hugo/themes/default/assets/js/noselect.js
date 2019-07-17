$(function() {
    // Make "$ " inside bash and shell code snippets unselectable.
    var pattern = /([ |\t]*\$ )/mig;
    var replaceWith = '<span class="no-select">$1</span>';
    $(".highlight .chroma .language-bash, .highlight .chroma .language-shell, .highlight .chroma .language-sh").each(function() {
        $(this).html($(this).html().replace(pattern, replaceWith));
    });
});
