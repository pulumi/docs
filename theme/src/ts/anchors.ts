import { onPageEvent } from "./navigation";

onPageEvent("load", () => {
    const anchors = window["anchors"];

    function isAnchorable() {
        for (let key of ["docs", "tutorials", "blog", "authors", "tags", "registry"]) {
            if (document.location.pathname.startsWith(`/${key}/`)) {
                return true;
            }
        }
        return false;
    }

    if (anchors && isAnchorable()) {
        anchors.add("h1:not(.no-anchor), h2:not(.no-anchor), h3:not(.no-anchor), h4:not(.no-anchor), h5:not(.no-anchor), h6:not(.no-anchor)");
    }
});
