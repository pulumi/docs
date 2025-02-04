import * as path from 'path';
import { findMarkdownFiles, FinderMode } from './find-markdown';

// Types for markdownlint
type Token = {
    type: string;
    content: string;
    lineNumber: number;
};

type RuleParams = {
    name?: string;
    tokens: Token[];
    lines?: string[];
};

interface LintError {
    lineNumber: string | number;
    ruleDescription: string;
    errorDetail?: string;
}

type RuleOnError = (error: Partial<LintError>) => void;

type Rule = {
    names: string[];
    description: string;
    tags: string[];
    function: (params: RuleParams, onError: RuleOnError) => void;
};

type Options = {
    files: string[];
    config: Record<string, any>;
    customRules: Rule[];
};

// Import markdownlint with require to handle its CommonJS format
// eslint-disable-next-line @typescript-eslint/no-var-requires
const markdownlint = require('markdownlint');

interface LintResult {
    path: string;
    errors: LintError[];
}

/**
 * Groups the result of linting a file for markdown errors.
 */
function groupLintErrorOutput(result: Record<string, LintError[]>): LintResult[] {
    return Object.entries(result)
        .map(([key, lintErrors]) => {
            if (lintErrors.length > 0) {
                return { path: key, errors: lintErrors };
            }
            return null;
        })
        .filter((err): err is LintResult => err !== null);
}

import { debug } from './utils';

// Get mode from command line args, defaulting to 'standard'
const mode = (process.argv[2] as FinderMode) || 'git';
debug('Running in mode:', mode);

// Get markdown files to lint
debug('Finding markdown files...');
const files = findMarkdownFiles(path.resolve(__dirname, '../../content'), mode, [
    '/content/docs/reference/pkg',
    '/content/registry'
]).map(file => file.path);

// Output file list for comparison
// console.log('\nTS version files:');
// const sortedFiles = files.map(f => f.replace(path.resolve(__dirname, '../../content/'), '')).sort();
// sortedFiles.forEach(f => console.log(f));

/**
 * The config options for lint markdown files. All rules
 * are enabled by default. The config object lets us customize
 * what rules we enforce and how we enforce them.
 *
 * See: https://github.com/DavidAnson/markdownlint
 */
const opts: Options = {
    files,
    config: {
        // Allow inline HTML
        MD033: false,
        // Do not enforce line length
        MD013: false,
        // Don't force language specification on code blocks
        MD040: false,
        // Allow hard tabs
        MD010: false,
        // Allow punctuation in headers
        MD026: false,
        // Allow dollars signs in code blocks without values
        // immediately below the command
        MD014: false,
        // Allow all code block styles in a file
        MD046: false,
        // Allow indents on unordered lists to be 4 spaces instead of 2
        'MD007/ul-indent': { indent: 4 },
        // Allow duplicate headings
        MD024: false,
        // Allow headings to be indented
        MD023: false,
        // Allow blank lines in blockquotes
        MD028: false,
        // Allow indentation in unordered lists
        // Note: This is set again to override the previous MD007
        MD007: false,
        // Allow bare URLs
        MD034: false,
        // Allow bold/italicized paragraphs
        MD036: false,
        // Allow multiple consecutive blank lines
        MD012: false,
        // Allow inconsistent bullet styles
        MD004: false,
        // Allow lists without surrounding blank lines
        MD032: false,
        // Allow lists to start at beginning of line
        MD030: false,
        // Allow trailing spaces
        MD009: false,
        // Allow inconsistent heading levels
        MD001: false,
        // Allow indented bullet lists
        MD006: false,
    },
    customRules: [
        {
            names: ['relref'],
            description: 'Hugo relrefs are no longer supported. Use standard [Markdown](/links) instead',
            tags: ['hugo-relref'],
            function(params: RuleParams, onError: RuleOnError) {
                params.tokens
                    .filter(token => token.type === 'inline')
                    .forEach(inline => {
                        if (inline.content.match(/{{<[ ]?relref ".+"[ ]?>}}/)) {
                            onError({
                                lineNumber: inline.lineNumber,
                            });
                        }
                    });
            },
        },
    ]
};

// Lint the markdown files
const result = markdownlint.sync(opts);

// Group the lint errors by file
const errors = groupLintErrorOutput(result);

// Get the total number of errors
const errorsArray = errors.map(err => err.errors);
const errorsCount = ([] as LintError[]).concat(...errorsArray).length;

// Create the error output string
const errorOutput = errors
    .map(err => {
        let msg = err.path + ':\n';
        for (let i = 0; i < err.errors.length; i++) {
            const error = err.errors[i];
            msg += 'Line ' + error.lineNumber + ': ' + error.ruleDescription;
            msg += error.errorDetail ? ' [' + error.errorDetail + '].\n' : '.\n';
        }
        return msg;
    })
    .join('\n');

// If there are errors output the error string and exit
// the program with an error
if (errors.length > 0) {
    console.log(`
Markdown Lint Results:
    - ${files.length} files parsed.
    - ${errorsCount} errors found.

Errors:

${errorOutput}
    `);

    const noError = process.argv.indexOf('--no-error') > -1;
    process.exit(noError ? 0 : 1);
}

console.log(`
Markdown Lint Results:
    - ${files.length} files parsed.
    - ${errorsCount} errors found.
`);
process.exit(0);
