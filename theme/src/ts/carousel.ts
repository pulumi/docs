(function () {
    var carouselItem = 1;

    var carouselInterval = window.setInterval(function () {
        showCarouselItem(carouselItem);
        carouselItem++;

        if (carouselItem > 2) {
            carouselItem = 0;
        }
    }, 11000);

    showCarouselItem(0);

    document.querySelectorAll(".carousel-item-label").forEach((label, index) => {
        label.addEventListener("click", function () {
            clearInterval(carouselInterval);
            showCarouselItem(index);
        });
    });

    function showCarouselItem(i) {
        if (document.querySelector(".carousel-always-visible")) {
            showIDE();
            showCLI();
            showConsole();
            return;
        }

        if (document.querySelector(".carousel-always-visible-cli-only")) {
            showCLIOnly();
            return;
        }

        document.querySelectorAll<HTMLElement>(".carousel-item").forEach((el, idx) => {
            el.style.opacity = idx === i ? "1" : "0";
            el.style.pointerEvents = idx === i ? "auto" : "none";
        });

        document.querySelectorAll<HTMLElement>(".carousel-item-description").forEach((el, idx) => {
            el.style.opacity = idx === i ? "1" : "0";
            el.style.pointerEvents = idx === i ? "auto" : "none";
        });

        document.querySelectorAll(".carousel-item-label").forEach((el, idx) => {
            el.classList.remove("border-purple-700", "text-purple-700", "hover:text-purple-700");
            el.classList.add("text-purple-200", "hover:text-purple-300");
            if (idx === i) {
                el.classList.add("border-purple-700", "text-purple-700", "hover:text-purple-700");
                el.classList.remove("text-purple-200", "hover:text-purple-300");
            }
        });

        if (i === 0) {
            showIDE();
        } else if (i === 1) {
            showCLI();
        } else if (i === 2) {
            showConsole();
        }
    }

    function showIDE() {
        document.querySelectorAll<HTMLElement>(".menu").forEach(el => el.style.opacity = "0");
        const menus = document.querySelectorAll<HTMLElement>(".menu");
        menus.forEach(el => {
            el.querySelectorAll(".row").forEach(row => row.classList.remove("bg-gray-600"));
            const firstRow = el.querySelector(".row");
            if (firstRow) firstRow.classList.add("bg-gray-600");
        });

        startTyping(0, function () {
            menus.forEach((el, idx) => {
                var delay = parseInt(el.getAttribute("data-delay")) || 0;

                if (idx === 0) {
                    setTimeout(function () {
                        el.querySelectorAll(".row").forEach(row => row.classList.remove("bg-gray-600"));
                        const secondRow = el.querySelectorAll(".row")[1];
                        if (secondRow) secondRow.classList.add("bg-gray-600");
                    }, 600);
                }

                setTimeout(function () {
                    el.style.opacity = "1";
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
        const tabs = document.querySelectorAll<HTMLElement>("#carousel-console .tab");

        tabs.forEach(tab => tab.style.opacity = "0");
        if (tabs[0]) tabs[0].style.opacity = "1";

        setTimeout(function () {
            if (tabs[0]) tabs[0].style.opacity = "0";
            if (tabs[1]) tabs[1].style.opacity = "1";
        }, 5000);
    }

    function startTyping(i, onComplete?) {
        const carouselItems = document.querySelectorAll(".carousel-item");
        const item = carouselItems[i];
        if (!item) return;

        const spans = item.querySelectorAll(".line.typed span");
        var offset = 500;
        var delay = 75;

        spans.forEach(span => {
            var chars = span.textContent.split("");
            span.classList.add("typing");
            span.innerHTML = chars.map(char => "<span class='char'>" + char + "</span>").join("");
        });

        var cursor = document.createElement("span");
        cursor.className = "cursor";

        const charEls = item.querySelectorAll<HTMLElement>(".char");
        charEls.forEach((el, j) => {
            offset += Math.ceil(Math.random() * delay);

            setTimeout(function () {
                if (el.textContent === "\n") {
                    el.style.opacity = "1";
                    el.insertBefore(cursor, el.firstChild);
                } else {
                    el.style.opacity = "1";
                    el.appendChild(cursor);
                }

                if (j === charEls.length - 1) {
                    setTimeout(function () {
                        cursor.remove();
                        if (typeof onComplete === "function") {
                            onComplete();
                        }
                    }, 600);
                }
            }, offset);

            if (el.textContent === "\n" || el.textContent === ";") {
                offset += 1000;
            }
        });
    }

    function showLines(i) {
        const carouselItems = document.querySelectorAll(".carousel-item");
        const item = carouselItems[i];
        if (!item) return;

        const lines = item.querySelectorAll<HTMLElement>(".line.full");
        lines.forEach(el => el.style.opacity = "0");
        var offset = 2000;
        var delay = 75;

        lines.forEach(el => {
            var d = parseInt(el.getAttribute("data-delay")) || delay;
            offset += Math.ceil(Math.random() * d);

            setTimeout(function () {
                el.style.opacity = "1";
            }, offset);
        });
    }
})();
