const glob = require("glob");
const fs = require("fs");
const parser = require("node-html-parser");

async function findCodeBlocks() {
    const paths = glob.sync("./public/**/*.html", {
        ignore:[
            "./public/docs/reference/pkg/**/*",
            "./public/docs/cli/commands/**/*",
            "./public/docs/esc-cli/commands/**/*",
        ],
    });

    const allBlocks = [];

    paths.forEach(async path => {
        const fileContent = fs.readFileSync(path, "utf-8").toString();
        const doc = parser.parse(fileContent, { blockTextElements: { code: true }});

        const blocks = doc.querySelectorAll("pre > code").map(node => {
            const parentExample = node.closest("[data-program-path]");

            return {
                path,
                url: path.replace("./public/", "https://www.pulumi.com/"),
                language: node.getAttribute("data-lang"),
                example: parentExample ? parentExample.getAttribute("data-program-path"): undefined,
            };
        });

        allBlocks.push(...blocks);
    });

    return allBlocks;
}

findCodeBlocks()
    .catch(err => console.error(err))
    .then(blocks => {
        console.log("✨ Done!");

        const languages = [
            "javascript", "js",
            "typescript", "ts",
            "python", "py",
            "go",
            "csharp",
            "java",
            "yaml",
        ];

        // Only count languages we care about.
        blocks = blocks.filter(b => languages.includes(b.language));

        // Count up the tested ones.
        const testedBlocks = blocks.filter(block => !!block.example);

        console.log(`${blocks.length} code blocks found.`);
        console.log(`Of these, ${testedBlocks.length} (~${Math.ceil(testedBlocks.length / blocks.length * 100)}%) are covered by tests.`);
    });
