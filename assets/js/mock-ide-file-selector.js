$(function() {
    console.log("file selector starting...");
    var codeBlockIds = ["terraformComparePython","terraformCompareGo","terraformCompareCSharp","terraformCompareTypeScript"];

    /**
     *
     * @param {string} blockId The id of the code block to show.
     */
    function displayCodeBlock(blockId) {
        for(var i = 0; i < codeBlockIds.length; i++) {
            var codeBlockId = codeBlockIds[i];

            if (codeBlockId === blockId) {
                $("#" + codeBlockId + " .compare-code-block").removeClass("hidden");
                $("#" + codeBlockId + " a").removeClass("file-not-active");
            } else {
                $("#" + codeBlockId + " .compare-code-block").addClass("hidden");
                $("#" + codeBlockId + " a").addClass("file-not-active");
            }
        }
    }

    function registerClickHandlers() {
        for(var i = 0; i < codeBlockIds.length; i ++) {
            var clickId = "#" + codeBlockIds[i] + " a";

            $(clickId).on("click", function(e) {
                e.preventDefault();
                console.log(this.parentElement.id);
                displayCodeBlock(this.parentElement.id);
            });
        }
    }

    registerClickHandlers();
})
