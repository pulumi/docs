$(function () {
    // If the button is selected from any entry point, open the dialog.
    $("#pricingStartTrial").on("click", function () {
        $("#pricingTrialOptionsDialog").removeClass("hidden");
    });

    $("#pricingStartTrialBottomCTA").on("click", function () {
        $("#pricingTrialOptionsDialog").removeClass("hidden");
    });

    $("#businessCriticalStartTrialButton").on("click", function () {
        $("#pricingTrialOptionsDialog").removeClass("hidden");
    });

    $("#enterpriseStartTrialButton").on("click", function () {
        $("#pricingTrialOptionsDialog").removeClass("hidden");
    });

    $("#teamStartTrialButton").on("click", function () {
        $("#pricingTrialOptionsDialog").removeClass("hidden");
    });

    // If the close button in the dialog is selected, hide the dialog.
    $("#closePricingTrialOptionsDialog").on("click", function () {
        $("#pricingTrialOptionsDialog").addClass("hidden");
    });

    // If either link in the dialog is followed, hide the dialog.
    $("#startServiceTrial").on("click", function () {
        $("#pricingTrialOptionsDialog").addClass("hidden");
    });

    $("#startSelfHostedTrial").on("click", function () {
        $("#pricingTrialOptionsDialog").addClass("hidden");
    });
});
