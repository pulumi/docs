import { onPageEvent } from "./navigation";

onPageEvent("load", () => {
    const pathTocHeaderMap = {
        "/docs/get-started/": "get-started-with-pulumi-toc-header",
        "/docs/": "intro-toc-header",
        "/docs/using-pulumi/": "user-guides-toc-header",
        "/docs/concepts/": "reference-toc-header",
        "/docs/support/": "support-toc-header",
        "/docs/using-pulumi/adopting-pulumi/converters/": "converters-toc-header",
    };

    Object.keys(pathTocHeaderMap).map(key => {
        const headerElement = document.getElementById(pathTocHeaderMap[key]);
        if (headerElement) {
            headerElement.classList.remove("active");
            if (document.location.pathname === key) {
                const container = document.getElementById("left-nav");
                headerElement.classList.add("active");
                container.scrollTop = headerElement.offsetTop - 100;
            }
        }
    });
});
