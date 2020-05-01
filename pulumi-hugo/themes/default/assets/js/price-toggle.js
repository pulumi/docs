// The first time the DOM is finished loading, wire up billing period listeners.
$(document).on("rendered", function() {
    // If there's a billing period element on the page, wire up a change listener
    // so we can toggle the various pricing elements between annual/monthly.
    $("#billing-period").each(function (i, e) {
        e.addEventListener("change", function(ev) {
            if (ev && ev.target && ev.target.checked) {
                $(".billing-price-monthly").each(function (i, p) { $(p).hide(); });
                $(".billing-price-annually").each(function (i, p) { $(p).show(); });
            } else {
                $(".billing-price-monthly").each(function (i, p) { $(p).show(); });
                $(".billing-price-annually").each(function (i, p) { $(p).hide(); });
            }
        });
    });
});
