import {LocalStorageService} from "./state";

(function (document) {
    var isTouchDevice = "ontouchstart" in document;

    if (!isTouchDevice) {
        document.querySelectorAll(".nav-header-items li a").forEach(a => {
            a.addEventListener("mouseenter", function (event) {
                var item = (event.target as HTMLElement).dataset.submenu;
                document.querySelectorAll<HTMLElement>(".submenu-item").forEach(el => el.style.display = "none");
                document.querySelectorAll<HTMLElement>(".submenu-item-" + item).forEach(el => el.style.display = "");
            });
        });

        document.querySelectorAll(".submenu").forEach(submenu => {
            submenu.addEventListener("mouseleave", function (event: MouseEvent) {
                if (event.relatedTarget !== document.querySelector("nav.nav-main")) {
                    document.querySelectorAll<HTMLElement>(".submenu-item").forEach(el => el.style.display = "none");
                }
            });
        });
    }

    (function () {
        let whyPulumiOpened = false;
        let learnOpened = false;

        document.getElementById("why-pulumi-menu-label")?.addEventListener("click", function() {
            const dropdown = document.getElementById("mobile-dropdown");
            if (whyPulumiOpened) {
                dropdown.scrollTo({ top: 0, behavior: "smooth" });
            } else {
                const menu = document.getElementById("why-pulumi-mobile-menu");
                if (menu && dropdown) {
                    dropdown.scrollTo({ top: (menu as HTMLElement).offsetTop - 115, behavior: "smooth" });
                }
            }
            whyPulumiOpened = !whyPulumiOpened;
        });

        document.getElementById("learn-menu-label")?.addEventListener("click", function() {
            const dropdown = document.getElementById("mobile-dropdown");
            if (learnOpened) {
                dropdown.scrollTo({ top: 0, behavior: "smooth" });
            } else {
                const menu = document.getElementById("learn-mobile-menu");
                if (menu && dropdown) {
                    dropdown.scrollTo({ top: (menu as HTMLElement).offsetTop - 115, behavior: "smooth" });
                }
            }
            learnOpened = !learnOpened;
        });
    })();

    const bannerState = new LocalStorageService("banner-state");
    const banner = document.getElementById("dismissable-banner");
    loadBannerState();

    function loadBannerState() {
        if (banner) {
            if (bannerState.getKey("dismissed") !== "true") {
                banner.style.display = "block";
            } else {
                banner.style.display = "none";
            }
        }
    }

    document.getElementById("dismiss-banner")?.addEventListener("click", function (e) {
        e.preventDefault();
        if (banner) {
            banner.style.display = "none";
        }
        bannerState.updateKey("dismissed", "true");
    });

})(document);
