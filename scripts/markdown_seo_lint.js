const fs = require("fs");
const yaml = require("js-yaml");
const markdownlint = require("markdownlint");
const path = require("path");

const FRONT_MATTER_REGEX = /((^---\s*$[^]*?^---\s*$)|(^\+\+\+\s*$[^]*?^(\+\+\+|\.\.\.)\s*$))(\r\n|\r|\n|$)/m;

function checkPageTitle(title) {
    let error = null;
    if (!title) {
        error = "Missing page title";
    }else if (title.trim().length === 0) {
        error = "Page title is empty";
    }else if (title.trim().length > 60) {
        error = "Page title exceeds 60 characters";
    }
    return error;
}

function checkPageMetaDescription(meta) {
    let error = null;
    if (!meta) {
        error = "Missing meta description";
    }else if (meta.trim().length === 0) {
        error = "Meta description is empty";
    }else if (meta.trim().length < 50) {
        error = "Meta description is too short. Must be at least 50 characters";
    }else if (meta.trim().length > 160) {
        error = "Meta descripiton is too long. Must be shorter than 160 characters";
    }
    return error;
}

// Recursively generate a list of markdown files from a given
// list of paths.
function searchForMarkdown(paths, result) {
    // If the result arg does not exist we should create it.
    if (!result) {
        result = {
            files: [],
            frontMatter: {},
        }
    }
    // Grab the first file in the list and generate
    // its full path.
    const file = paths[0];
    const fullPath = path.resolve(__dirname, file);

    // Check if the path is a directory
    const isDirectory = fs.statSync(fullPath).isDirectory();

    // Get the file suffix so we can grab the markdown files.
    const fileParts = file.split(".");
    const fileSuffix = fileParts[fileParts.length - 1];

    // Ignore auto generated docs.
    if (file.indexOf("/content/docs/reference/pkg") > -1) {
        const remaining = paths.slice(1, paths.length);
        return searchForMarkdown(remaining, result);

    // If the path is a directory we want to add the contents of the directory
    // to the list.
    }else if (isDirectory) {
        const contents = fs.readdirSync(fullPath).map(function(file) {
            return fullPath + "/" + file;
        });
        paths[0] = contents;

        // Flatten the array.
        const newPaths = [].concat.apply([], paths);
        return searchForMarkdown(newPaths, result);

    // Else check if the file suffix is a markdown
    // and add it the resulting file list.
    }else {
        if (fileSuffix === "md") {
            try {
                const content = fs.readFileSync(fullPath, "utf8");
                const frontMatter = content.match(FRONT_MATTER_REGEX);
                const fContent = frontMatter[0].split("---").join("");
                const obj = yaml.load(fContent);
                result.frontMatter[fullPath] = {
                    error: null,
                    title: checkPageTitle(obj.title),
                    metaDescription: checkPageMetaDescription(obj.meta_desc),
                };
                result.files.push(fullPath);
            } catch(e) {
                result.frontMatter[fullPath] = {
                    error: e.message,
                };
                result.files.push(fullPath);
            }
        }

        // If there are remaining paths in the list, keep going.
        const remaining = paths.slice(1, paths.length);
        if (remaining.length > 0) {
            return searchForMarkdown(remaining, result);
        }
    }

    return result;
}

// Get a list of markdown files.
function getMarkdownFileList(parentPath) {
    const fullParentPath = path.resolve(__dirname, parentPath)
    const dirs = fs.readdirSync(fullParentPath).map(function(dir) {
        return parentPath + "/" + dir;
    });

    return searchForMarkdown(dirs);
}

const filesToLint = getMarkdownFileList("../content");

const opts = {
    files: filesToLint.files,
    config: {
        // Allow inline HTML.
        MD033: false,
        // Do not enforce line length.
        MD013: false,
        // Don't force language specification on code blocks.
        MD040: false,
        // Allow hard tabs.
        MD010: false,
        // Allow puncuation in headers.
        MD026: false,
        // Allow dollars signs in code blocks without values
        // immediately below the command.
        MD014: false,
        // Allow all code block styles in a file. Code block styles
        // are created equal and we shall not discriminate.
        MD046: false,
        // Allow indents on unordered lists to be 4 spaces instead of 2.
        MD007: { indent: 4 },
        // Allow duplicate heading content inside child headings.
        MD024: { siblings_only: true },
    },
};

const result = markdownlint.sync(opts);

// Get the total number of errors and build a collection
// of lint errors.
const errorsCount = [].concat.apply([], Object.values(result)).length;
const errors = Object.keys(result).map(function(key) {
    const lintErrors = result[key];
    const frontMatterErrors = filesToLint.frontMatter[key];

    if (frontMatterErrors.error) {
        lintErrors.push({
            lineNumber: "File Header",
            ruleDescription: frontMatterErrors.error,
        });
    }else {
        if (frontMatterErrors.title) {
            lintErrors.push({
                lineNumber: "File Header",
                ruleDescription: frontMatterErrors.title,
            });
        }
        if (frontMatterErrors.metaDescription) {
            lintErrors.push({
                lineNumber: "File Header",
                ruleDescription: frontMatterErrors.metaDescription,
            });
        }
    }

    if (lintErrors.length > 0) {
        return { path: key, errors: lintErrors };
    }else {
        return null;
    }
}).filter(function(item) { return item !== null; });

if (errors.length > 0) {
    console.log(`
Lint Results:
    - ${filesToLint.length} files parsed.
    - ${errorsCount} errors found.

ERRORS:

    ${
        errors.map(function(err) {
            let msg = err.path + ":\n";
            for (let i = 0; i < err.errors.length; i++) {
                const error = err.errors[i];
                msg += "Line " + error.lineNumber + ": " + error.ruleDescription;
                msg += error.errorDetail ? " [" + error.errorDetail + "].\n" : ".\n";
            }
            return msg;
        }).join("\n")
    }
    `);
    process.exit(1);
}else {
    console.log(`
Lint Results:
    - ${filesToLint.length} files parsed.
    - ${errorsCount} errors found.
    `);
    process.exit(0);
}
