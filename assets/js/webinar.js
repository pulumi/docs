/**
 *
 * @param {string} date The string value of the date to localize.
 */
function localizeDateTime(date) {
    var localeDate = new Date(date.getAttribute("data-datetime"));
    var options = { timeZoneName: "short", weekday: 'short', year: 'numeric', month: 'long', day: 'numeric', hour: "numeric", minute: "2-digit" };
    return localeDate.toLocaleString(undefined, options);
}

$(function() {
    var webinarDetails = $("#webinarLandingPage")[0];

    if (webinarDetails) {
        var dates = document.querySelectorAll(".webinar-datetime span");

        for (var i = 0; i < dates.length; i++) {
            var date = dates[i];
            date.innerText = localizeDateTime(date);
        }
    }
});
