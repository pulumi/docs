$(function () {
    $("#cloud-panel-products-select").on("click", function () {
        // show/hide prices by tab
        $(".cloud-panel-capabilities").addClass("hidden");
        $(".cloud-panel-products").removeClass("hidden");

        // flip tab styles
        $('#cloud-panel-capabilities-select').removeClass("border-blue-600 bg-violet-100");
        $('#cloud-panel-capabilities-select').addClass("border-gray-300");
        $('#cloud-panel-capabilities-select-text').removeClass("rainbow-text")
        $('#cloud-panel-products-select').addClass("border-blue-600 bg-violet-100");
        $('#cloud-panel-products-select-text').addClass("rainbow-text")

    });

    $("#cloud-panel-capabilities-select").on("click", function () {
        // show/hide prices by tab
        $(".cloud-panel-products").addClass("hidden");
        $(".cloud-panel-capabilities").removeClass("hidden");

        // flip tab styles
        $('#cloud-panel-products-select').removeClass("border-blue-600 bg-violet-100");
        $('#cloud-panel-products-select').addClass("border-gray-300");
        $('#cloud-panel-products-select-text').removeClass("rainbow-text")
        $('#cloud-panel-capabilities-select').addClass("border-blue-600 bg-violet-100");
        $('#cloud-panel-capabilities-select-text').addClass("rainbow-text")
    });

});