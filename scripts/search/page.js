const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const cheerio = require("cheerio");
const rank = require("./rank");
const { spawn } = require('child_process');

module.exports = {

    // Return the top-level section the page belongs to. Note that these sections are used for
    // faceting (i.e., filtering the results returned by Algolia as well as how they appear in the
    // autocomplete UI), so changes to this code should be made extra care. (Any change made here
    // without an accompanying change to the UI will likely break the UI.)
    getTopLevelSection({ href }) {
        if (href.startsWith("/docs")) {
            return "Docs";
        } else if (href.startsWith("/blog")) {
            return "Blog";
        } else if (href.startsWith("/registry")) {
            return "Registry";
        } else if (href.startsWith("/tutorials")) {
            return "Tutorials";
        } else if (href.startsWith("/templates")) {
            return "Templates";
        } else if (href.startsWith("/resources")) {
            return "Resources";

        }
        return "General";
    },

    // Fetch a list of the explicit and implicit keywords associated with the page.
    async getKeywords(page) {
        if (page.href.startsWith("/docs/") || page.href.startsWith("/tutorials/")) {
            const pageContent = await this.getDOMContent(page);
            const content = pageContent.subheads.reduce((acc, curr) => acc + curr.content + " ", "");
            const extractedKeywords = await this.extractKeywords(page.title + " " + page.title + " " + (content || ""));
            // console.log("keywords", pageContent.subheads.map(subhead => subhead.keywords || []).flat() || []);
            console.log("keywords", extractedKeywords);
            return (page.params?.search?.keywords || [])
                .concat(rank.getImplicitKeywords(page))
                .concat(extractedKeywords)
                .concat(pageContent.subheads.map(subhead => subhead.keywords || []).flat() || []);
        }
        return (page.params?.search?.keywords || [])
            .concat(rank.getImplicitKeywords(page));
    },

    // Fetch a summary of any DOM content to use for the index. Things like H2s, their immediately
    // following paragraphs, and any of their explicitly provided keywords (as we also support this
    // also) are included.
    async getDOMContent({ href }) {
        // Assemble the local path to the file using its href.
        const filePath = path.join("public", href, "index.html");

        // Read the file and parse it into a DOM tree.
        const content = fs.readFileSync(filePath, "utf-8");
        
        // Parse with Cheerio, using htmlparser2.
        const $ = cheerio.load(content, {
            _useHtmlParser2: true,
            decodeEntities: true
        });
        
        const subheads = [];

        // Updated to include H2, H3, and H4 to expand search range.
        // If this becomes too noisy, reduce scope back to H2s only.
        $("main h2, main h3, main h4").each((index, element) => {
            const $h2 = $(element);
            const id = $h2.attr("id");

            // If a heading doesn't have an ID, it can't be linked to, so exclude it.
            if (!id) return;

            const title = $h2.text().trim();
            const keywords = $h2.attr("search.keywords");
            
            let content = "";
            let $next = $h2.next();
            if ($next.is("p")) {
                content = $next.text();
            }
            content = content.trim();

            subheads.push({
                title,
                anchor: id,
                keywords: keywords || [],
                content: content || "",
            });
        });

        return { subheads };
    },

    // Return the page's (explicit or implicit) ranking.
    getRank(page) {
        return rank.get(page);
    },

    // Return whether the specified page should be "boosted".
    isBoosted(page) {
        return rank.isImplicitlyBoosted(page) || rank.isExplicitlyBoosted(page) || undefined;
    },

    // Fetch a list of primary objects. These objects are generated directly from Hugo-rendered JSON.
    async getPrimaryObjects(hugoPageItems) {
        // Filter items first to avoid processing items we'll exclude anyway
        const filteredItems = hugoPageItems.filter(item => {
            const isDraft = !!item.params.draft;
            const isBlockedFromExternalSearch = item.block_external_search_index === true;
            const isMissingObjectID = item.objectID === "";
            const isZeroRanked = this.getRank(item) === 0;
            const isRedirect = (item.params.redirect_to && item.params.redirect_to !== "");

            return !(isDraft || isBlockedFromExternalSearch || isRedirect || isMissingObjectID || isZeroRanked);
        })
        // .filter(item => item.href.startsWith("/docs/") || item.href.startsWith("/tutorials/"))
        // .slice(0, 10);

        console.log("processing", filteredItems.length, "pages");

        // Process in batches of 12
        const batchSize = 9;
        const results = [];
        
        for (let i = 0; i < filteredItems.length; i += batchSize) {
            console.log("processing batch", i / batchSize + 1, "of", Math.ceil(filteredItems.length / batchSize));
            const batch = filteredItems.slice(i, i + batchSize);
            const batchResults = await Promise.all(batch.map(async item => {
                return {
                    objectID: this.getObjectID(item),
                    section: this.getTopLevelSection(item),
                    title: item.title,
                    h1: item.params.h1,
                    description: item.params.meta_desc,
                    href: item.href,
                    authors: item.params.authors,
                    tags: item.params.tags,
                    rank: this.getRank(item),
                    boosted: this.isBoosted(item),
                    keywords: await this.getKeywords(item),
                    ancestors: this.makeAncestorsList(item.ancestors),
                };
            }));
            results.push(...batchResults);
        }
        
        return results;
    },

    // Fetch a list of secondary objects. These are things like H2 headings (along with any
    // explicitly defined keywords, associated content, etc.) that we want to be findable in
    // addition to page titles, descriptions, and keywords.
    async getSecondaryObjects(sitePageObjects) {
        const secondaries = [];

        await sitePageObjects
            .filter(pageObject => !pageObject.href.match(/registry|pkg|blog/))
            .forEach(async pageObject => {
                const domContent = await this.getDOMContent(pageObject);
                const ancestors = pageObject.ancestors;

                if (domContent.subheads) {
                    domContent.subheads.forEach(subhead => {
                        const href = `${ pageObject.href }#${ subhead.anchor }`;

                        secondaries.push({
                            objectID: this.getObjectID({ href }),
                            section: pageObject.section,
                            ancestors: this.makeAncestorsList([ ...ancestors, pageObject.title ]),
                            title: subhead.title,
                            description: (subhead.content || "").substr(0, 200),
                            href,
                            keywords: [...(subhead.keywords || []), ...(pageObject.keywords || [])]
                        });
                    });
                }
        });

        return secondaries;
    },

    // Clean up (i.e., de-dupe, simplify, etc.) the items in a breadcrumb list.
    makeAncestorsList(rawList) {
        return [ ...new Set(rawList) ]
            .filter(s => s?.trim() !== "")
            .map(s => {
                if (s === "Pulumi Registry") {
                    return "Registry";
                }
                return s;
            });
    },

    // Every Algolia record requires a unique ID. Since every record should also have a unique URL,
    // we use the URL to generate the unique ID.
    //
    // If, at some point, we find that we need to have two records pointing to the same URL, we can
    // add another parameter to the list and hash both.
    getObjectID({ href }) {
        return crypto.createHash("md5").update(href).digest("hex");
    },

    async extractKeywords(text) {
        const venvPath = "/scripts/search/keywords/venv/bin/python";     
        
        const pythonPath = path.join(process.cwd(), venvPath);
        
        return new Promise((resolve, reject) => {
            const pythonProcess = spawn(pythonPath, [
                "scripts/search/keywords/keyword_gen.py",
                text
            ]);
    
            let result = '';
    
            pythonProcess.stdout.on("data", (data) => {
                result += data.toString();
            });
    
            pythonProcess.stderr.on("data", (data) => {
                console.error(`Error: ${data}`);
            });
    
            pythonProcess.on("close", (code) => {
                if (code !== 0) {
                    reject(new Error(`Process exited with code ${code}`));
                    return;
                }
                try {
                    const keywords = JSON.parse(result);
                    resolve(keywords);
                } catch (error) {
                    reject(error);
                }
            });
        });
    }
};
