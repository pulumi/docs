$(function () {
    $("#iac-pricing-select").on("click", function () {
        // show/hide prices by tab
        $(".esc-price").addClass("hidden");
        $(".iac-price").removeClass("hidden");

        // flip tab styles
        $('#esc-pricing-select').removeClass("border-blue-600 bg-gray-100");
        $('#esc-pricing-select').addClass("border-gray-300");
        $('#esc-pricing-select-text').removeClass("rainbow-text")
        $('#iac-pricing-select').addClass("border-blue-600 bg-gray-100");
        $('#iac-pricing-select-text').addClass("rainbow-text")
        
    });

    $("#esc-pricing-select").on("click", function () {
        // show/hide prices by tab
        $(".iac-price").addClass("hidden");
        $(".esc-price").removeClass("hidden");

        // flip tab styles
        $('#iac-pricing-select').removeClass("border-blue-600 bg-gray-100");
        $('#iac-pricing-select').addClass("border-gray-300");
        $('#iac-pricing-select-text').removeClass("rainbow-text")
        $('#esc-pricing-select').addClass("border-blue-600 bg-gray-100");
        $('#esc-pricing-select-text').addClass("rainbow-text")
    });

});