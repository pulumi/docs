document.addEventListener("DOMContentLoaded", function () {
    const dialogId = "pricingTrialOptionsDialog";

    ["pricingStartTrial", "pricingStartTrialBottomCTA", "businessCriticalStartTrialButton", "enterpriseStartTrialButton", "teamStartTrialButton"].forEach(id => {
        document.getElementById(id)?.addEventListener("click", function () {
            document.getElementById(dialogId)?.classList.remove("hidden");
        });
    });

    document.getElementById("closePricingTrialOptionsDialog")?.addEventListener("click", function () {
        document.getElementById(dialogId)?.classList.add("hidden");
    });

    document.getElementById("startServiceTrial")?.addEventListener("click", function () {
        document.getElementById(dialogId)?.classList.add("hidden");
    });

    document.getElementById("startSelfHostedTrial")?.addEventListener("click", function () {
        document.getElementById(dialogId)?.classList.add("hidden");
    });
});
