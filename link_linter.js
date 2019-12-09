const parse = require("node-html-parser");
const fs = require('fs');
const path = require('path');
const { expect } = require("chai");

/**
 * Recursively search for html files and add them to the result list.
 *
 * @param {string[]} files A list of files to search through.
 * @param {string[]} result A list of complete file paths to html files.
 */
function fetchFilePaths(files, result = []) {
    // Grab the first file in the list and build its full path.
    const file = files[0];
    const filePath = path.resolve(__dirname, file);

    // Get the "stat" for the file to check if it is a directory.
    const fstat = fs.statSync(filePath);

    // Split the file string to capture the file suffix.
    const fileParts = file.split(".");
    const fileSuffix = fileParts[fileParts.length - 1];

    // If the file is a directory, check the contents of the directory.
    if (fstat.isDirectory()) {
        const dirFiles = fs.readdirSync(filePath).map(function(file) {
            return filePath + "/" + file;
        });
        files[0] = dirFiles;

        // Add the contents of the directory to the original file list.
        const combinedFiles = [].concat.apply([], files);
        return fetchFilePaths(combinedFiles, result);
    }else {
        // If the file has a "html" suffix add it the result list.
        if (fileSuffix.toLowerCase() === "html") {
            result.push(filePath);
        }
        const remainingFiles = files.slice(1, files.length);

        // If there are files remaining check them.
        if (remainingFiles.length > 0) {
            return fetchFilePaths(remainingFiles, result);
        }
    }

    // Return the resulting list of html files.
    return result;
}

/**
 * Grab the initial list of files in the defined directory and pass them
 * to recursive function to build the file list.
 *
 * @param {string} directoryPath The path relative to the script where the files that need to be checked live.
*/
function buildFileList(directoryPath) {
    const files = fs.readdirSync(path.resolve(__dirname, directoryPath)).map(function(file) {
        return directoryPath + "/" + file;
    });

    return fetchFilePaths(files, []);
}

/**
 * Convert an element from the HTML parse result to a validation object
 * for our tests.
 *
 * @param {object} link An HTML <a> element.
 */
function validateTrackingLink(link) {
    // Return an objec that checks the element is a link and the
    // track-click attribute is present.
    return {
        id: link.id,
        tagName: link.tagName === "a",
        trackingAttr: link.rawAttrs.indexOf("track-click") > -1,
    };
};

// Build a list of files to lint from the layouts directory.
const filesToLint = buildFileList("./layouts");

describe("Tracking Link Linting", function() {

    for (let i = 0; i < filesToLint.length; i++) {
        const fileToLint = filesToLint[i];

        // Run a test suite for each file to check. Each file has its own describe block
        // for organizational purposes.
        describe(fileToLint, function() {

            // Read the html file and parse its contents.
            const html = fs.readFileSync(fileToLint, "utf8");
            const parsedHtml = parse.parse(html);

            // Find all the a tags and convert the result to validation objects.
            const links = parsedHtml.querySelectorAll("a").map(validateTrackingLink);

            for (let i = 0; i < links.length; i++) {
                const link = links[i];

                it(`should validate link for ${link.id}`, function(){
                    const validLink = link;

                    // Check to make sure the id exists and has length.
                    validLink.id = validLink.id && validLink.id.trim().length > 0;

                    // Check the tag and trackingAttr are valid.
                    expect(link.tagName).to.equal(true);
                    expect(link.trackingAttr).to.equal(true);
                });
            }
        });
    }
});
