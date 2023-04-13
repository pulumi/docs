import { getQueryVariable } from "./util";

$(document).on("rendered", function () {
    $("#pulumi-ai pulumi-ai")
        .attr("prompt", () => {
            return getQueryVariable("prompt");
        })
        .attr("language", () => {
            return getQueryVariable("language");
        });
})
