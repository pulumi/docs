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
        const buttons = $("a[track-click]");

        function registerTracker(element) {

            // Create the tracking object.
            const trackingData = {
                // The id of the element.
                id: $(element).attr("id"),
                // The destination url of the link.
                destinationPath: $(element).attr("href"),
                // The current path.
                url: window.location.pathname,
            }

            // Register a listener to the link to send data to Segment
            // when it has been clicked.
            $(element).on("click", function(e) {
                window.analytics.track("link-click", trackingData);
            });

        }

        // Loop over the array of elements to register the click listeners.
        for (var i = 0; i < buttons.length; i++) {
            registerTracker(buttons[i]);
        }
    }

});