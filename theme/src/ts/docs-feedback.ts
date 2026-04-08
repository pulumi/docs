document.addEventListener("DOMContentLoaded", function () {
    var analyticsAvailable = window["analytics"] && window["analytics"].track && typeof window["analytics"].track === "function";

    var container = document.getElementById("docsFeedbackContainer");
    if (container) {
        container.classList.remove("hidden");
    }

    ["docsFeedbackYes", "docsFeedbackNo"].forEach(function (key) {
        var answer = key === "docsFeedbackYes" ? "Yes" : "No";
        var btn = document.getElementById(key);
        if (btn) {
            btn.addEventListener("click", function () {
                var longForm = document.getElementById("feedbackLongForm");
                if (longForm) {
                    longForm.classList.remove("hidden");
                }
                showAdditionalCommentSection(answer);
            });
        }
    });

    function sendFeedbackToSegment(answer, comments, email) {
        var trackingObj = {
            answer: answer,
            comments: comments || "",
            email: email || "",
            url: window.location.pathname,
            category: "Documentation Feedback",
            label: answer,
        };

        if (analyticsAvailable) {
            window["analytics"].track("docs-feedback", trackingObj);
        } else {
            console.log("Skipped call to analytics.track:", "docs-feedback", trackingObj);
        }
    }

    function showAdditionalCommentSection(answer) {
        var feedbackLongForm = document.getElementById("feedbackLongForm");
        var feedbackLongFormParent = feedbackLongForm?.parentElement;
        if (feedbackLongForm) {
            document.body.appendChild(feedbackLongForm);
        }

        var submitBtn = document.getElementById("docsSubmitFeedback");
        if (submitBtn) {
            submitBtn.addEventListener("click", function () {
                var comments = (document.getElementById("feedbackAdditionalComments") as HTMLTextAreaElement)?.value?.trim() || "";
                var email = (document.getElementById("feedbackEmail") as HTMLInputElement)?.value?.trim() || "";

                sendFeedbackToSegment(answer, comments, email);

                (document.getElementById("feedbackAdditionalComments") as HTMLTextAreaElement).value = "";
                (document.getElementById("feedbackEmail") as HTMLInputElement).value = "";

                document.getElementById("feedbackButtons")?.classList.add("hidden");
                document.getElementById("feedbackLongForm")?.classList.add("hidden");
                document.getElementById("feedbackThankYou")?.classList.remove("hidden");
            });
        }

        var closeBtn = document.getElementById("docsCloseFeedbackLongForm");
        if (closeBtn) {
            closeBtn.addEventListener("click", function () {
                sendFeedbackToSegment(answer, "", "");

                (document.getElementById("feedbackAdditionalComments") as HTMLTextAreaElement).value = "";
                (document.getElementById("feedbackEmail") as HTMLInputElement).value = "";

                document.getElementById("feedbackButtons")?.classList.add("hidden");
                document.getElementById("feedbackLongForm")?.classList.add("hidden");
                document.getElementById("feedbackThankYou")?.classList.remove("hidden");

                if (feedbackLongFormParent && feedbackLongForm) {
                    feedbackLongFormParent.appendChild(feedbackLongForm);
                }
            });
        }

        window.addEventListener("beforeunload", function () {
            var longForm = document.getElementById("feedbackLongForm");
            var feedbackSent = longForm?.classList.contains("hidden");
            if (!feedbackSent) {
                sendFeedbackToSegment(answer, "", "");
            }
        });
    }
});
