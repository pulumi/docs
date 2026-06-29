document.addEventListener("DOMContentLoaded", function () {
    var analyticsAvailable = window["analytics"] && window["analytics"].track && typeof window["analytics"].track === "function";

    var container = document.getElementById("docsFeedbackContainer");
    if (container) {
        container.classList.remove("hidden");
    }

    var longForm = document.getElementById("feedbackLongForm");
    // While open, the dialog is reparented to <body> so its fixed overlay escapes
    // any transformed/clipping ancestor in the sidebar. Remember where it lives so
    // closing can put it back.
    var longFormHome = longForm?.parentElement;
    var currentAnswer = "";

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

    function showSuccess(success) {
        document.getElementById("feedbackForm")?.classList.toggle("hidden", success);
        document.getElementById("feedbackSuccess")?.classList.toggle("hidden", !success);
    }

    // Toggle the required-comment error state: show/hide the message, red border, and
    // a red focus ring (swapped in for the default violet only while in the error state).
    function setCommentError(hasError) {
        var field = document.getElementById("feedbackAdditionalComments");
        document.getElementById("feedbackCommentsError")?.classList.toggle("hidden", !hasError);
        field?.classList.toggle("border-red-primary", hasError);
        field?.classList.toggle("focus:ring-red-primary", hasError);
        field?.classList.toggle("focus:ring-violet-primary", !hasError);
    }

    function openDialog(answer) {
        if (!longForm) {
            return;
        }
        currentAnswer = answer;
        showSuccess(false);
        longForm.classList.remove("hidden");
        document.body.appendChild(longForm);
        document.getElementById("feedbackAdditionalComments")?.focus();
    }

    function closeDialog() {
        if (!longForm) {
            return;
        }
        longForm.classList.add("hidden");
        if (longFormHome) {
            longFormHome.appendChild(longForm);
        }
        // Reset for the next time the dialog is opened.
        var comments = document.getElementById("feedbackAdditionalComments") as HTMLTextAreaElement;
        var email = document.getElementById("feedbackEmail") as HTMLInputElement;
        if (comments) {
            comments.value = "";
        }
        if (email) {
            email.value = "";
        }
        setCommentError(false);
        showSuccess(false);
    }

    ["docsFeedbackYes", "docsFeedbackNo"].forEach(function (key) {
        var answer = key === "docsFeedbackYes" ? "Yes" : "No";
        var btn = document.getElementById(key);
        if (btn) {
            btn.addEventListener("click", function () {
                openDialog(answer);
            });
        }
    });

    // Submit: a comment is required. If it's empty, surface the error and stop;
    // otherwise record the feedback and show the thank-you message in the dialog.
    document.getElementById("docsSubmitFeedback")?.addEventListener("click", function () {
        var commentsField = document.getElementById("feedbackAdditionalComments") as HTMLTextAreaElement;
        var comments = commentsField?.value?.trim() || "";
        var email = (document.getElementById("feedbackEmail") as HTMLInputElement)?.value?.trim() || "";

        if (!comments) {
            setCommentError(true);
            commentsField?.focus();
            return;
        }

        sendFeedbackToSegment(currentAnswer, comments, email);
        showSuccess(true);
    });

    // Clear the required-comment error as soon as the user starts typing.
    document.getElementById("feedbackAdditionalComments")?.addEventListener("input", function () {
        setCommentError(false);
    });

    // Close (cancel): record the yes/no vote, then return the widget to its
    // original state without showing the thank-you message.
    document.getElementById("docsCloseFeedbackLongForm")?.addEventListener("click", function () {
        sendFeedbackToSegment(currentAnswer, "", "");
        closeDialog();
    });

    // Done: dismiss the post-submit thank-you message.
    document.getElementById("docsDoneFeedback")?.addEventListener("click", function () {
        closeDialog();
    });

    // If the dialog is still on the form (not yet submitted) when the user
    // navigates away, record the vote so it isn't lost.
    window.addEventListener("beforeunload", function () {
        var dialogOpen = longForm && !longForm.classList.contains("hidden");
        var onForm = !document.getElementById("feedbackForm")?.classList.contains("hidden");
        if (dialogOpen && onForm && currentAnswer) {
            sendFeedbackToSegment(currentAnswer, "", "");
        }
    });
});
