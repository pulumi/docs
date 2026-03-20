document.addEventListener("DOMContentLoaded", function () {
    if (window && window["analytics"] && typeof window["analytics"].track === "function") {
        const links = document.querySelectorAll("a");
        const now = new Date().getTime();

        function registerTracker(element: HTMLAnchorElement, i: number) {
            if (!element) {
                return;
            }

            const dataTrack = element.getAttribute("data-track");
            const href = (element.getAttribute("href") || "").replace(/https?:\/\//g, "");
            const trackingDescription = dataTrack ? dataTrack : href.replace(/^#/, "anchor-").replace(/^\//, "").split("/").join("-");

            const currentPath = window.location.pathname === "/" ? "home" : window.location.pathname;
            const path = currentPath
                .split("/")
                .filter(function (segment) {
                    return segment !== "";
                })
                .map(function (segment) {
                    return segment;
                });

            const trackingId = path.concat(trackingDescription, String(i)).join("-");

            const trackingData = {
                element_id: trackingId,
                destinationPath: element.getAttribute("href"),
                url: window.location.pathname,
                category: "User Interaction",
                label: trackingId,
                value: undefined,
            };

            element.addEventListener("click", function () {
                trackingData.value = (new Date().getTime() - now) / 1000;
                window["analytics"].track("link-click", trackingData);
            });
        }

        for (var i = 0; i < links.length; i++) {
            registerTracker(links[i], i);
        }
    }
});
