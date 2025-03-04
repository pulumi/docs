const glob = require("glob");
const fs = require("fs");
const cheerio = require("cheerio");

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
        const $ = cheerio.load(fileContent);

        // Skip redirects.
        if ($("meta[http-equiv='refresh'][content*='0; url=']").length > 0) {
            return;
        }

        const main = $(".docs-main-content .docs-content");
        const html = main.html();

        if (html) {
            const title =  $("title").text();
            const h1 =  $("h1").text();
            const text = main.text();

            jsonOutput.push({
                path: path.replace("./public", ""),
                title,
                h1,
                main: {
                    innerHTML: html,
                    textContent: text,
                    markdown: service.turndown(html),
                },
            })
        };
    });

    return jsonOutput;
}

extractDocsContent()
    .catch(err => console.error(err))
    .then(docs => {
        fs.writeFileSync("./public/docs/content.json", JSON.stringify(docs, null, 4), "utf-8");
        console.log("✨ Done!");
    });
