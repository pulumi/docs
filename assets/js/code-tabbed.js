(function($) {
    var languageItem = 1;

    var languageInterval = window.setInterval(function() {
        showLanguageItem(languageItem);
        languageItem++;

        if (languageItem > 3) {
            languageItem = 0;
        }
    }, 5000);

    showLanguageItem(0);

    $(".code-tabbed-tab").click(function() {
        clearInterval(languageInterval);

        var i = $(".code-tabbed-tab").index(this);
        showLanguageItem(i);
    });

    function showLanguageItem(i) {

        $(".code-tabbed-content")
            .scrollTop(0)
            .scrollLeft(0);

        $(".code-tabbed-tab")
            .removeClass("active")
            .eq(i)
            .addClass("active");

        $(".code-tabbed-content-item")
            .removeClass("active")
            .eq(i)
            .addClass("active");
    }
})(jQuery);
