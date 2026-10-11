document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("upcoming-talks-select")?.addEventListener("click", function () {
        document.getElementById("upcoming-talks")?.classList.remove("hidden");
        document.getElementById("past-talks")?.classList.add("hidden");

        document.getElementById("upcoming-talks-select")?.classList.add("is-selected");
        document.getElementById("past-talks-select")?.classList.remove("is-selected");
    });

    document.getElementById("past-talks-select")?.addEventListener("click", function () {
        document.getElementById("upcoming-talks")?.classList.add("hidden");
        document.getElementById("past-talks")?.classList.remove("hidden");

        document.getElementById("upcoming-talks-select")?.classList.remove("is-selected");
        document.getElementById("past-talks-select")?.classList.add("is-selected");
    });
});
