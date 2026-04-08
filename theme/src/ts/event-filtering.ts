import { getQueryVariable } from "./util";

document.addEventListener("DOMContentLoaded", function () {
    function createCheckbox(text) {
        var filterValue = getQueryVariable("filter");

        var container = document.createElement("div");
        container.className = "my-2 uppercase flex items-center";

        var checkbox = document.createElement("input");
        checkbox.id = "checkbox-" + text;
        checkbox.type = "checkbox";
        checkbox.className = "mr-2 cursor-pointer";
        checkbox.value = text.toLowerCase();

        if (filterValue !== undefined) {
            var shouldBeChecked = filterValue.toLowerCase().split(",").indexOf(checkbox.value) > -1;
            if (shouldBeChecked) {
                checkbox.checked = true;
            }
        } else {
            checkbox.checked = true;
        }

        var label = document.createElement("label");
        label.innerText = text + "s";
        label.className = "cursor-pointer";
        label.setAttribute("for", checkbox.id);

        container.appendChild(checkbox);
        container.appendChild(label);

        return container;
    }

    function getFilterValuesAndFilterList() {
        var inputs = document.querySelectorAll<HTMLInputElement>("input[type='checkbox']");
        var chosenInputs = [];

        inputs.forEach(input => {
            if (input.checked) {
                chosenInputs.push(input.value);
            }
        });

        filterEventList(chosenInputs);
    }

    function checkForIntersection(arr1, arr2) {
        for (var i = 0; i < arr1.length; i++) {
            var val = arr1[i];
            if (arr2.indexOf(val) > -1) {
                return true;
            }
        }
        return false;
    }

    function filterEventList(tags) {
        var events = document.querySelectorAll("#event-list li");
        var visibleEvents = 0;

        events.forEach(event => {
            var dataEventType = event.getAttribute("data-event-type").split(",");
            var shouldBeVisible = tags.length === 0 ? true : checkForIntersection(tags, dataEventType);

            if (shouldBeVisible) {
                visibleEvents += 1;
                event.classList.remove("hidden");
            } else {
                event.classList.add("hidden");
            }
        });

        const heading = document.getElementById("event-list-heading");
        if (heading) {
            if (visibleEvents === events.length) {
                heading.textContent = "All Upcoming Events";
            } else {
                heading.textContent = visibleEvents + " Upcoming Events";
            }
        }
    }

    var eventsElements = document.querySelectorAll(".event-tags span");
    var eventFilterParent = document.getElementById("eventFilter");

    if (!eventsElements.length) {
        return;
    }
    if (!eventFilterParent) {
        return;
    }

    var tags = [];

    for (var i = 0; i < eventsElements.length; i++) {
        var text = eventsElements[i].textContent;

        if (tags.indexOf(text) === -1) {
            tags.push(text);
            const input = createCheckbox(text);
            eventFilterParent.appendChild(input);
        }
    }

    getFilterValuesAndFilterList();

    eventFilterParent.addEventListener("click", function (e) {
        if ((e.target as HTMLElement).matches("input[type='checkbox']")) {
            getFilterValuesAndFilterList();
        }
    });
});
