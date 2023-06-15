const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const jsdom = require("jsdom");
const rank = require("./rank");

const { JSDOM } = jsdom;

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
        } else if (href.startsWith("/templates")) {
            return "Templates";
        } else if (href.startsWith("/resources")) {
            return "Resources";
        }
        return "General";
    },

    // Fetch a list of the explicit and implicit keywords associated with the page.
    getKeywords(page) {
        return (page.params?.search?.keywords || []).concat(rank.getImplicitKeywords(page));
    },

    // Fetch a summary of any DOM content to use for the index. Things like H2s, their immediately
    // following paragraphs, and any of their explicitly provided keywords (as we also support this
    // also) are included.
    getDOMContent({ href }) {

        // Assemble the local path to the file using its href.
        const filePath = path.join("public", href, "index.html");

        // Read the file and parse it into a DOM tree.
        const content = fs.readFileSync(filePath, "utf-8");
        const { document } = new JSDOM(content).window;
        const subheads = [];

        // For now, only bother with H2s, as the noise level goes way up with H3s.
        [2].forEach(level => {
            const headings = document.querySelectorAll(`main h${level}`);
            headings.forEach(h => {

                // If a heading doesn't have an ID, it can't be linked to, so exclude it.
                if (!h.getAttribute("id")) {
                    return;
                }

                subheads.push(
                    {
                        title : h.textContent,
                        anchor: h.getAttribute("id") || undefined,
                        keywords: h.getAttribute("search.keywords") || undefined,
                        content: h.nextElementSibling?.nodeName === "P" ? h.nextElementSibling.textContent : undefined,
                    },
                );
            });
        })

        return {
            subheads,
        };
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
    getPrimaryObjects(hugoPageItems) {
        return hugoPageItems

            // Exclude drafts, pages blocked from external search listings, those missing object IDs
            // (as this means they probably aren't actual Hugo pages), and those with explicit
            // rankings of zero.
            .filter(item => {
                const isDraft = !!item.params.draft;
                const isBlockedFromExternalSearch = item.block_external_search_index === true;
                const isMissingObjectID = item.objectID === "";
                const isZeroRanked = this.getRank(item) === 0;
                const isRedirect = (item.params.redirect_to && item.params.redirect_to !== "");

                if (isDraft || isBlockedFromExternalSearch || isRedirect || isMissingObjectID || isZeroRanked) {
                    return false;
                }

                return true;
            })

            // Convert Hugo page items into Algolia index objects.
            .map(item => {
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
                    keywords: this.getKeywords(item),
                    ancestors: this.makeAncestorsList(item.ancestors),
                };
            });
    },

    // Fetch a list of secondary objects. These are things like H2 headings (along with any
    // explicitly defined keywords, associated content, etc.) that we want to be findable in
    // addition to page titles, descriptions, and keywords.
    getSecondaryObjects(sitePageObjects) {
        const secondaries = [];

        sitePageObjects
            .filter(pageObject => !pageObject.href.match(/registry|pkg|blog/))
            .forEach(pageObject => {
                const domContent = this.getDOMContent(pageObject);
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
                            keywords: subhead.keywords || undefined,
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
    }
};
