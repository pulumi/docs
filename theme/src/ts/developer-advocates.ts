$(function () {
    $("#upcoming-talks-select").on("click", function () {
        $("#upcoming-talks").removeClass("hidden");
        $("#past-talks").addClass("hidden");

        $("#upcoming-talks-select").addClass("is-selected");

        $("#past-talks-select").removeClass("is-selected");
    });

    $("#past-talks-select").on("click", function () {
        $("#upcoming-talks").addClass("hidden");
        $("#past-talks").removeClass("hidden");

        $("#upcoming-talks-select").removeClass("is-selected");

        $("#past-talks-select").addClass("is-selected");
    });

});