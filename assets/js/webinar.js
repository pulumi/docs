/**
 *
 * @param {string} date The string value of the date to localize.
 */
function localizeDateTime(date) {
    var localeDate = new Date(date.getAttribute("data-datetime"));
    var options = { timeZoneName: "short", weekday: 'short', year: 'numeric', month: 'long', day: 'numeric', hour: "numeric", minute: "2-digit" };
    return localeDate.toLocaleString(undefined, options);
}

/**
 * This function parses the cookie string and returns an object of the current cookies.
 */
function parseCookie() {
    return document.cookie.split(";").reduce(function(obj, cookie) {
        var index = cookie.indexOf("=");
        var key = cookie.substring(0, index).trim();
        var value = cookie.substring(index + 1).trim();
        obj[key] = value;
        return obj;
    }, {});
}

/**
 * This function parses the UTM cookie and returns and object of the cookie.
 *
 * @param {string} utmCookieString The value of the '__utmzz' cookie. Values are separated by '|'.
 */
function parseUTMCookie(utmCookieString) {
    return (utmCookieString || "").split("|").reduce(function(obj, utm) {
        var parts = utm.split("=");
        obj[parts[0]] = parts[1];
        return obj;
    }, {});
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

    // Check that the analytics track function is available.
    var analyticsAvailable = window.analytics && window.analytics.track &&
                             (typeof window.analytics.track === "function");

    if (webinarDetails && analyticsAvailable) {
        // Parse the cookie and grab the UTM cookie values.
        var cookies = parseCookie();
        var utmCookie = parseUTMCookie(cookies["__utmzz"]);

        // Listen for the HubSpot form to be loaded.
        window.addEventListener('message', event => {
            if(event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormReady') {
                var form = $(".hbspt-form form");
                console.log(form);

                // Send an analytics event with the UTM values when the form is submitted.
                form.submit(function() {
                    var submissionData = {
                        formId: form.attr("data-form-id"),
                        email: $(".hbspt-form form input[name='email']").val(),
                        utmCampaign: utmCookie.utmccn || "(not set)",
                        utmSource: utmCookie.utmcsr || "(direct)",
                        utmMedium: utmCookie.utmcmd || "(none)",
                    };

                    window.analytics.track("form-submission", submissionData);
                });
            }
        });
    }
});
