$(function() {
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
                $("#" + codeBlockId + "Selector").removeClass("file-not-active");
            } else {
                $("#" + codeBlockId + " .compare-code-block").addClass("hidden");
                $("#" + codeBlockId + "Selector").addClass("file-not-active");
            }
        }
    }

    function handleFileSelectorClick(blockId) {
        return function(e) {
            e.preventDefault();
            displayCodeBlock(blockId);
        }
    }

    function registerClickHandlers() {
        for(var i = 0; i < codeBlockIds.length; i ++) {
            var clickId = "#" + codeBlockIds[i] + "Selector";
            var blockId = codeBlockIds[i];

            $(clickId).on("click", handleFileSelectorClick(blockId));
        }
    }

    registerClickHandlers();
})
