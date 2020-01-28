$(function() {
    var eventsElements = $(".event-tags span");
    var eventFilterParent = $("#eventFilter");
    var tags = [];

    for (var i = 0; i < eventsElements.length; i++) {
        var elem = eventsElements[i];
        var text = $(elem).text();
        if (tags.indexOf(text) === -1) {
            tags.push(text);
            eventFilterParent.append(
                '<input type="checkbox" class="mx-2" value="' + text + '">' + text + '</p>'
            );
        }
    }

    $("input[type='checkbox']").on("click", function() {
        var inputs = $("input[type='checkbox']");
        var chosenInputs = [];

        for (var z = 0; z < inputs.length; z++) {
            var input = inputs[z];
            var isChecked = $(input).prop("checked");
            if (isChecked) {
                chosenInputs.push($(input).val().toLowerCase());
            }
        }

        filterEventList(chosenInputs);
    });

    /**
     *
     * @param {*[]} arr1 An array
     * @param {*[]} arr2 An array
     */
    function checkForIntersection(arr1, arr2) {
        for (var i = 0; i < arr1.length; i++) {
            var val = arr1[i];
            var hasIntersection = arr2.indexOf(val) > -1;
            if (hasIntersection) {
                return true;
            }
        }
        return false;
    }

    /**
     *
     * @param {string[]} tags An array of tags that should appear in the event list.
     */
    function filterEventList(tags) {
        var events = $("#eventList li");

        for (var i = 0; i < events.length; i++) {
            var event = $(events[i]);
            var dataEventType = event.attr("data-event-type").split(",");
            var shouldBeVisible = tags.length === 0 ? true : checkForIntersection(tags, dataEventType);

            if (shouldBeVisible) {
                event.removeClass("hidden");
            }else {
                event.addClass("hidden");
            }
        }
    }
});
