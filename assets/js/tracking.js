/*
 * Function for registering tracking to a link. To add tracking to a link you
 * need to have an "id" attritube on the <a> element and the "track-click" attribute.
 *
 *   - ex. <a id="get-started-no-yaml" class="btn" href="/docs/get-started" track-click>GET STARTED</a>
 */
$(document).ready(function() {
    // Check if the analytics object and track function are available. If they are
    // not we do not even want to attempt to track anything.
    if (window && window.analytics && typeof window.analytics.track === "function") {

        // Find all the links with a "track-click" attribute.
        const links = $("a[data-tracking-id]");

        // Get the current date/time so we can track time from page load to user click.
        const now = new Date().getTime();

        function registerTracker(element) {
            // Create the tracking object.
            const trackingData = {
                // The id of the element.
                element_id: $(element).attr("data-tracking-id"),
                // The destination url of the link.
                destinationPath: $(element).attr("href"),
                // The current path.
                url: window.location.pathname,
                // The Google Analytic Event Values. These values are pushed into GA
                // specifically. More info: https://support.google.com/analytics/answer/1033068#Anatomy
                category: "User Interaction",
                label: $(element).attr("data-tracking-id"),
            }

            // Register a listener to the link to send data to Segment
            // when it has been clicked.
            $(element).on("click", function(e) {
                // The value is the time in seconds from page load to user action.
                trackingData.value = ((new Date().getTime()) - now) / 1000;
                window.analytics.track("link-click", trackingData);
            });
        }

        // Loop over the array of elements to register the click listeners.
        for (var i = 0; i < links.length; i++) {
            registerTracker(links[i]);
        }

        // Remove the event listeners when we navigate to a new page.
        $(window).on("unload", function() {
            for (var i = 0; i < links.length; i++) {
                $(link[i]).off("click");
            }
        });
    }
});
