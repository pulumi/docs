$(function(){
    // Check that the analytics track function is available.
    var analyticsAvailable = window.analytics && window.analytics.track &&
                             (typeof window.analytics.track === "function");

    if (analyticsAvailable) {
        // Show the docs feedback container.
        $("#docsFeedbackContainer").removeClass("hidden");

        // For each of the button ids attach a click handler that shows
        // the additional comment section.
        ["#docsFeedbackYes", "#docsFeedbackNo"].forEach(function(key) {
            var answer = key === "#docsFeedbackYes" ? "Yes" : "No";
            $(key).on("click", function() {
                $("#feedbackLongForm").removeClass("hidden");

                // Show the additional comment section.
                showAdditionalCommentSection(answer);
            });
        });

        /**
         * Submit the documentation feedback to Segment.
         *
         * @param {string} answer The value of the button the user clicked when giving feedback.
         * @param {string} comments The value of the text area in the comment section. Defaults to an empty string
         * @param {string} email The value of the email input in the comment section. Defaults to an empty string
         */
        function sendFeedbackToSegment(answer, comments, email) {
            var trackingObj = {
                answer: answer,
                comments: comments || "",
                email: email || "",
                url: window.location.pathname,
                category: "Documentation Feedback",
                label: answer,
            };
            window.analytics.track("docs-feedback", trackingObj);
        }

        /**
         * Show the additional comments section and inject the user's feedback
         * answer into the submission click handler and form abandonment handler.
         *
         * @param {string} answer The value of the button the user clicked when giving feedback.
         */
        function showAdditionalCommentSection(answer) {
            // Add a click handler to the submit button.
            $("#docsSubmitFeedback").on("click", function() {
                // Grab the values of the comments and email inputs.
                var comments = $("#feedbackAdditionalComments").val().trim();
                var email = $("#feedbackEmail").val().trim();

                // Send to Segment.
                sendFeedbackToSegment(answer, comments, email);

                // Clear the form
                $("#feedbackAdditionalComments").val("");
                $("#feedbackEmail").val("");

                // Show the thank you section.
                $("#feedbackButtons").addClass("hidden");
                $("#feedbackLongForm").addClass("hidden");
                $("#feedbackThankYou").removeClass("hidden");
            });

            $("#docsCloseFeedbackLongForm").on("click", function() {
                // Send to Segment.
                sendFeedbackToSegment(answer, "", "");

                // Clear the form
                $("#feedbackAdditionalComments").val("");
                $("#feedbackEmail").val("");

                // Show the thank you section.
                $("#feedbackButtons").addClass("hidden");
                $("#feedbackLongForm").addClass("hidden");
                $("#feedbackThankYou").removeClass("hidden");
            });

            $(window).on("beforeunload", function() {
                // When page unloads send the answer if it has not already been sent.
                var feedbackSent = $("#feedbackLongForm").hasClass("hidden");
                if (!feedbackSent) {
                    sendFeedbackToSegment(answer, "", "");
                }
            });
        }
    }
});
