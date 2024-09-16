$(function () {
    const productTabs = ["iac-select", "esc-select", "insights-select"];
    const capabilityTabs = ["crossguard-select", "deployments-select", "copilot-select", "management-select"];

    productTabs.forEach(tab => {
        $(`#${tab}`).on("click", function () {
            // hide all others
            productTabs.forEach(id => {
                if (id !== tab) {
                    $(`#${id}-content`).addClass("hidden");
                    $(`#${id}`).removeClass("border-blue-600 bg-violet-100");
                    $(`#${id}-text`).removeClass("rainbow-text");
                }
            });
            $(`#${tab}`).addClass("border-blue-600 bg-violet-100");
            $(`#${tab}-text`).addClass("rainbow-text")
            $(`#${tab}-content`).removeClass("hidden")
        });
    });
    capabilityTabs.forEach(tab => {
        $(`#${tab}`).on("click", function () {
            // hide all others
            capabilityTabs.forEach(id => {
                if (id !== tab) {
                    $(`#${id}-content`).addClass("hidden");
                    $(`#${id}`).removeClass("border-blue-600 bg-violet-100");
                    $(`#${id}-text`).removeClass("rainbow-text");
                }
            });
            $(`#${tab}`).addClass("border-blue-600 bg-violet-100");
            $(`#${tab}-text`).addClass("rainbow-text")
            $(`#${tab}-content`).removeClass("hidden")
        });
    });
});