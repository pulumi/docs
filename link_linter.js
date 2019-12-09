const parse = require("node-html-parser");
const fs = require('fs');
const path = require('path');
const { expect } = require("chai");

function fetchFilePaths(files, result = []) {
    const file = files[0];
    const filePath = path.resolve(__dirname, file);
    const fstat = fs.statSync(filePath);
    const fileParts = file.split(".");
    const fileSuffix = fileParts[fileParts.length - 1];

    if (fstat.isDirectory()) {
        const dirFiles = fs.readdirSync(filePath).map(function(file) {
            return filePath + "/" + file;
        });
        files[0] = dirFiles;
        const combinedFiles = [].concat.apply([], files);
        return fetchFilePaths(combinedFiles, result);
    }else {
        if (fileSuffix.toLowerCase() === "html") {
            result.push(filePath);
        }
        const remainingFiles = files.slice(1, files.length);
        if (remainingFiles.length > 0) {
            return fetchFilePaths(remainingFiles, result);
        }
    }
    return result;
}

function buildFileList(directoryPath) {
    const files = fs.readdirSync(path.resolve(__dirname, directoryPath)).map(function(file) {
        return directoryPath + "/" + file;
    });

    return fetchFilePaths(files, []);
}

function validateTrackingLink(link) {
    return {
        tagName: link.tagName === "a",
        id: link.id,
        trackingAttr: link.rawAttrs.indexOf("track-click") > -1,
    };
};

const filesToLint = buildFileList("./layouts");

describe("Tracking Link Linting", function() {

    for (let i = 0; i < filesToLint.length; i++) {
        const fileToLint = filesToLint[i];

        describe(fileToLint, function() {

            const html = fs.readFileSync(fileToLint, "utf8");
            const parsedHtml = parse.parse(html);
            const links = parsedHtml.querySelectorAll("a").map(validateTrackingLink);

            for (let i = 0; i < links.length; i++) {
                const link = links[i];

                it(`should validate link for ${link.id}`, function(){
                    const validLink = link;
                    validLink.id = validLink.id && validLink.id.length > 0;
                    expect(link.tagName).to.equal(true);
                    expect(link.trackingAttr).to.equal(true);
                });

            }

        });

    }

});
