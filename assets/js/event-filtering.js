$(function() {
    var eventsElements = $(".event-tags span");
    var eventFilterParent = $("#eventFilter");

    // Check to see if the event elements exists.
    if (!eventsElements.length) {
        // Stop the script as there are no tags to filter.
        return;
    }
    if (!eventFilterParent.length) {
        // Stop the script because the event filter element does not exist.
        return;
    }

    var tags = [];

    /**
     * This function creates a checkbox from a given text string.
     * It will set the label and the value to whatever the input string is.
     *
     * @param {string} text The label and value of the checkbox
     */
    function createCheckbox(text) {
        var container = document.createElement("div");
        container.className = "my-2";

        var checkbox = document.createElement("input");
        checkbox.id = "checkbox-" + text;
        checkbox.type = "checkbox";
        checkbox.className = "mx-2 cursor-pointer";
        checkbox.value = text;

        var label = document.createElement("label");
        label.innerText = text;
        label.className = "cursor-pointer";
        label.setAttribute("for", checkbox.id);

        container.appendChild(checkbox);
        container.appendChild(label);

        return container;
    }

    // Loop through the tags and create a unique array of tag names and
    // append a checkbox to the event filter for each unique tag.
    for (var i = 0; i < eventsElements.length; i++) {
        var elem = eventsElements[i];

        // Grab the text of the element. We use the .text method because
        // it will grab the string value of the text.
        //
        // See: https://api.jquery.com/text/
        var text = $(elem).text();

        if (tags.indexOf(text) === -1) {
            tags.push(text);
            const input = createCheckbox(text);
            eventFilterParent.append(input);
        }
    }

    // This click handler will determine which checkboxes are selected
    // and then provide them to the filter event function to filter the events.
    $("#eventFilter input[type='checkbox']").on("click", function() {
        var inputs = $("input[type='checkbox']");
        var chosenInputs = [];

        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            var isChecked = $(input).prop("checked");
            if (isChecked) {
                chosenInputs.push($(input).val().toLowerCase());
            }
        }

        filterEventList(chosenInputs);
    });

    /**
     * This function checks to see if two arrays have any value in common. This
     * function can return false for arrays of objects becasue the objects
     * in each array can have different references.
     *
     * @param {*[]} arr1 An array of non object values
     * @param {*[]} arr2 An array of non object values
     */
    function checkForIntersection(arr1, arr2) {
        for (var i = 0; i < arr1.length; i++) {
            var val = arr1[i];
            if (arr2.indexOf(val) > -1) {
                return true;
            }
        }
        return false;
    }

    /**
     * This function will fitler the event list and hide/show specific items
     * based on the select checkboxes. If no checkboxes are selected we will show all
     * the events.
     *
     * @param {string[]} tags An array of tags that should appear in the event list.
     */
    function filterEventList(tags) {
        var events = $("#eventList li");
        var visibleEvents = 0;

        for (var i = 0; i < events.length; i++) {
            var event = $(events[i]);
            var dataEventType = event.attr("data-event-type").split(",");
            var shouldBeVisible = tags.length === 0 ? true : checkForIntersection(tags, dataEventType);

            if (shouldBeVisible) {
                visibleEvents += 1;
                event.removeClass("hidden");
            } else {
                event.addClass("hidden");
            }
        }
        if (visibleEvents === events.length) {
            $("#eventListHeading").text("All Upcoming Events")
        } else {
            $("#eventListHeading").text(visibleEvents + " Upcoming Events");
        }
    }
});
