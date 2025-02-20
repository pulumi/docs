import * as fs from "fs";
import * as path from "path";
import * as crypto from "crypto";
import * as cheerio from "cheerio";
import * as rank from "./rank";

    // Return the top-level section the page belongs to. Note that these sections are used for
    // faceting (i.e., filtering the results returned by Algolia as well as how they appear in the
    // autocomplete UI), so changes to this code should be made extra care. (Any change made here
    // without an accompanying change to the UI will likely break the UI.)
    export function getTopLevelSection({ href }) {
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
    }

    // Fetch a list of the explicit and implicit keywords associated with the page.
    export function getKeywords(page) {
        return (page.params?.search?.keywords || []).concat(rank.getImplicitKeywords(page));
    }

    // Fetch a summary of any DOM content to use for the index. Things like H2s, their immediately
    // following paragraphs, and any of their explicitly provided keywords (as we also support this
    // also) are included.
    export function getDOMContent({ href }) {
        // Assemble the local path to the file using its href.
        const filePath = path.join("public", href, "index.html");

        // Read the file and parse it into a DOM tree.
        const content = fs.readFileSync(filePath, "utf-8");
        
        // Parse with Cheerio, using htmlparser2.
        const $ = cheerio.load(content, {
            _useHtmlParser2: true,
            decodeEntities: true
        } as any /* We are using a hidden option: _useHtmlParser2: https://github.com/cheeriojs/cheerio/discussions/1271 */);
        
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
                keywords: keywords || undefined,
                content: content || undefined,
            });
        });

        return { subheads };
    }

    // Return the page's (explicit or implicit) ranking.
    export function getRank(page) {
        return rank.get(page);
    }

    // Return whether the specified page should be "boosted".
    export function isBoosted(page) {
        return rank.isImplicitlyBoosted(page) || rank.isExplicitlyBoosted(page) || undefined;
    }

    // Fetch a list of primary objects. These objects are generated directly from Hugo-rendered JSON.
    export function getPrimaryObjects(hugoPageItems) {
        return hugoPageItems

            // Exclude drafts, pages blocked from external search listings, those missing object IDs
            // (as this means they probably aren't actual Hugo pages), and those with explicit
            // rankings of zero.
            .filter(item => {
                const isDraft = !!item.params.draft;
                const isBlockedFromExternalSearch = item.block_external_search_index === true;
                const isMissingObjectID = item.objectID === "";
                const isZeroRanked = getRank(item) === 0;
                const isRedirect = (item.params.redirect_to && item.params.redirect_to !== "");

                if (isDraft || isBlockedFromExternalSearch || isRedirect || isMissingObjectID || isZeroRanked) {
                    return false;
                }

                return true;
            })

            // Convert Hugo page items into Algolia index objects.
            .map(item => {
                return {
                    objectID: getObjectID(item),
                    section: getTopLevelSection(item),
                    title: item.title,
                    h1: item.params.h1,
                    description: item.params.meta_desc,
                    href: item.href,
                    authors: item.params.authors,
                    tags: item.params.tags,
                    rank: getRank(item),
                    boosted: isBoosted(item),
                    keywords: getKeywords(item),
                    ancestors: makeAncestorsList(item.ancestors),
                };
            });
    }

    // Fetch a list of secondary objects. These are things like H2 headings (along with any
    // explicitly defined keywords, associated content, etc.) that we want to be findable in
    // addition to page titles, descriptions, and keywords.
    export function getSecondaryObjects(sitePageObjects) {
        const secondaries = [];

        sitePageObjects
            .filter(pageObject => !pageObject.href.match(/registry|pkg|blog/))
            .forEach(pageObject => {
                const domContent = getDOMContent(pageObject);
                const ancestors = pageObject.ancestors;

                if (domContent.subheads) {
                    domContent.subheads.forEach(subhead => {
                        const href = `${ pageObject.href }#${ subhead.anchor }`;

                        secondaries.push({
                            objectID: getObjectID({ href }),
                            section: pageObject.section,
                            ancestors: makeAncestorsList([ ...ancestors, pageObject.title ]),
                            title: subhead.title,
                            description: (subhead.content || "").substr(0, 200),
                            href,
                            keywords: subhead.keywords || undefined,
                        });
                    });
                }
        });

        return secondaries;
    }

// Clean up (i.e., de-dupe, simplify, etc.) the items in a breadcrumb list.
export function makeAncestorsList(rawList: string[]) {
    return Array.from(new Set(rawList).values())
        .filter(s => s?.trim() !== "")
        .map(s => {
            if (s === "Pulumi Registry") {
                return "Registry";
            }
            return s;
        });
}

// Every Algolia record requires a unique ID. Since every record should also have a unique URL,
// we use the URL to generate the unique ID.
//
// If, at some point, we find that we need to have two records pointing to the same URL, we can
// add another parameter to the list and hash both.
export function getObjectID({ href }) {
    return crypto.createHash("md5").update(href).digest("hex");
}
