/**
 *
 * @param {string} date The string value of the date to localize.
 */
function localizeDateTime(date) {
    var localeDate = new Date(date.getAttribute("data-datetime"));
    var options = { timeZoneName: "short" };
    return localeDate.toLocaleString(undefined, options);
}

$(function() {
    var webinarListings = $("#webinarListings")[0];
    var webinarDetails = $("#webinarLandingPage")[0];

    if (webinarListings || webinarDetails) {
        var dates = document.querySelectorAll(".webinar-datetime span");

        for (var i = 0; i < dates.length; i++) {
            var date = dates[i];
            date.innerText = localizeDateTime(date);
        }
    }
});
