const fs = require("fs");
const Beasties = require("beasties");

const pages = ["public/index.html"];

async function inlineCriticalCSS() {
    const beasties = new Beasties({
        path: "public/",
        preload: "swap",
        reduceInlineStyles: true,
        pruneSource: false,
    });

    for (const page of pages) {
        if (!fs.existsSync(page)) {
            console.warn(`Skipping ${page} (not found)`);
            continue;
        }

        const html = fs.readFileSync(page, "utf-8");
        const inlined = await beasties.process(html);
        fs.writeFileSync(page, inlined);
        console.log(`Inlined critical CSS: ${page}`);
    }
}

inlineCriticalCSS().catch((err) => {
    console.error("Failed to inline critical CSS:", err);
    process.exit(1);
});
