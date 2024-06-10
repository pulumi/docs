const glob = require("glob");
const fs = require("fs");
const parser = require("node-html-parser");

const TurndownService = require("turndown");

const service = new TurndownService({
    codeBlockStyle: "fenced",
    linkStyle: "inlined",
});

async function extractDocsContent() {
    console.log("Generating docs JSON...")

    const paths = glob.sync("./public/{docs,templates,learn}/**/*.html", { ignore:[ "./public/docs/reference/pkg/**/*" ] });
    const jsonOutput = [];

    paths.forEach(async path => {
        const fileContent = fs.readFileSync(path, "utf-8").toString();
        const doc = parser.parse(fileContent);

        // Skip redirects.
        if (doc.querySelector("meta[http-equiv='refresh'][content*='0; url=']")) {
            return;
        }

        const main = doc.querySelector(".docs-main-content .docs-content");

        if (main && main.textContent) {
            jsonOutput.push({
                path: path.replace("./public", ""),
                title: doc.querySelector("title").textContent,
                h1: doc.querySelector("h1").textContent,
                main: {
                    innerHTML: main.innerHTML,
                    textContent: main.textContent,
                    markdown: service.turndown(main.innerHTML),
                },
            })
        }
    });

    return jsonOutput;
}

extractDocsContent()
    .catch(err => console.error(err))
    .then(docs => {
        fs.writeFileSync("./public/docs/content.json", JSON.stringify(docs, null, 4), "utf-8");
        console.log("✨ Done!");
    });
