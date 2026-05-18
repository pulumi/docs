document.addEventListener("DOMContentLoaded", function () {
    const productTabs = ["iac-select", "esc-select", "insights-select"];
    const capabilityTabs = ["policies-select", "deployments-select", "neo-select", "management-select"];

    productTabs.forEach(tab => {
        document.getElementById(tab)?.addEventListener("click", function () {
            productTabs.forEach(id => {
                if (id !== tab) {
                    document.getElementById(id + "-content")?.classList.add("hidden");
                    document.getElementById(id)?.classList.remove("border-violet-primary");
                    document.getElementById(id + "-text")?.classList.remove("rainbow-text");
                }
            });
            document.getElementById(tab)?.classList.add("border-violet-primary");
            document.getElementById(tab + "-text")?.classList.add("rainbow-text");
            document.getElementById(tab + "-content")?.classList.remove("hidden");
        });
    });
    capabilityTabs.forEach(tab => {
        document.getElementById(tab)?.addEventListener("click", function () {
            capabilityTabs.forEach(id => {
                if (id !== tab) {
                    document.getElementById(id + "-content")?.classList.add("hidden");
                    document.getElementById(id)?.classList.remove("border-violet-primary");
                    document.getElementById(id + "-text")?.classList.remove("rainbow-text");
                }
            });
            document.getElementById(tab)?.classList.add("border-violet-primary");
            document.getElementById(tab + "-text")?.classList.add("rainbow-text");
            document.getElementById(tab + "-content")?.classList.remove("hidden");
        });
    });
});
