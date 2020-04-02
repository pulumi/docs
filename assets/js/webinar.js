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

    if (webinarListings) {
        var tabs = [ "liveWebinarTab", "onDemandWebinarTab", "pulumiTVWebinarTab" ];
        tabs.forEach(function(tab) {
            var tabMap = {
                "liveWebinarTab": "liveWebinarsList",
                "onDemandWebinarTab": "onDemandWebinarsList",
                "pulumiTVWebinarTab": "pulumiTVWebinarsList"
            };

            $("#" + tab).on("click", function(e) {
                e.preventDefault();
                var listIds = Object.keys(tabMap);
                for (var i = 0; i < listIds.length; i++) {
                    var idKey = listIds[i];
                    $("#" + idKey).removeClass("text-blue-700").addClass("text-gray-500").addClass("hover:text-blue-800");
                    $("#" + tabMap[idKey]).addClass("hidden");
                }

                var listId = tabMap[tab];
                $("#" + listId).removeClass("hidden");
                $(this).removeClass("text-gray-500").removeClass("hover:text-blue-800").addClass("text-blue-700");
            });
        });
    }
});
