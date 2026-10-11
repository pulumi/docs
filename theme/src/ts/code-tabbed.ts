(function () {
    var languageItem = 1;

    var languageInterval = window.setInterval(function () {
        showLanguageItem(languageItem);
        languageItem++;

        if (languageItem > 3) {
            languageItem = 0;
        }
    }, 5000);

    showLanguageItem(0);

    document.querySelectorAll(".code-tabbed-tab").forEach((tab, index) => {
        tab.addEventListener("click", function () {
            clearInterval(languageInterval);
            showLanguageItem(index);
        });
    });

    function showLanguageItem(i) {
        document.querySelectorAll(".code-tabbed-content").forEach((el: HTMLElement) => {
            el.scrollTop = 0;
            el.scrollLeft = 0;
        });

        document.querySelectorAll(".code-tabbed-tab").forEach((el, idx) => {
            el.classList.toggle("active", idx === i);
        });

        document.querySelectorAll(".code-tabbed-content-item").forEach((el, idx) => {
            el.classList.toggle("active", idx === i);
        });
    }
})();
