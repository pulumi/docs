$(function () {
    $("#iac-pricing-select").on("click", function () {
        // show/hide prices by tab
        $(".esc-price").addClass("hidden");
        $(".iac-price").removeClass("hidden");

        // flip tab styles
        $('#esc-pricing-select').removeClass("border-b-4 border-blue-600 rainbow-text");
        $('#iac-pricing-select').addClass("border-b-4 border-blue-600 rainbow-text");

        
    });

    $("#esc-pricing-select").on("click", function () {
        // show/hide prices by tab
        $(".iac-price").addClass("hidden");
        $(".esc-price").removeClass("hidden");

        // flip tab styles
        $('#iac-pricing-select').removeClass("border-b-4 border-blue-600 rainbow-text");
        $('#esc-pricing-select').addClass("border-b-4 border-blue-600 rainbow-text");
    });

});