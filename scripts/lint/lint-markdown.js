const fs = require("fs");
const zlib = require("zlib");
const yaml = require("js-yaml");
const { lint: markdownlint, readConfig } = require("markdownlint/sync");
const path = require("path");
const markdownIt = require("markdown-it");

// BEHAVIOR SWITCH: Set to false to use old behavior, true for new behavior
const USE_NEW_FRONTMATTER_VALIDATION = true;

/**
 * Allowed blog post category ids, loaded once from the single source of truth
 * at data/blog_categories.yaml. See that file's header for the rules.
 */
const BLOG_CATEGORIES = (function () {
    try {
        const p = path.resolve(__dirname, "../../data/blog_categories.yaml");
        const doc = yaml.load(fs.readFileSync(p, "utf8"));
        return (doc.categories || []).map(c => c.id);
    } catch (e) {
        console.warn(`Warning: could not load blog categories: ${e.message}`);
        return [];
    }
})();

/**
 * Allowed case-study industry ids, loaded once from the single source of truth
 * at data/case_study_industries.yaml. See that file's header for the rules.
 */
const CASE_STUDY_INDUSTRIES = (function () {
    try {
        const p = path.resolve(__dirname, "../../data/case_study_industries.yaml");
        const doc = yaml.load(fs.readFileSync(p, "utf8"));
        return (doc.industries || []).map(i => i.id);
    } catch (e) {
        console.warn(`Warning: could not load case-study industries: ${e.message}`);
        return [];
    }
})();

/**
 * The Pulumi Cloud editions and the feature availability matrix, loaded once
 * from the single source of truth at data/pulumi_pricing.yaml. See that file's
 * header for the rules.
 *
 * The `available_from` + `availability` expansion below mirrors the one in
 * layouts/partials/pricing/data.html. It is duplicated rather than shared
 * because the two run in different languages, and the repo splits data
 * validation by consumer: structural invariants belong to the template that
 * renders the file, frontmatter-facing invariants belong here so authors fail
 * in `make lint` (~2s, and it gates the build) instead of in a full Hugo build.
 *
 * Shape: { editions: [id], names: {id: name}, features: {id: minEdition},
 *          duplicates: [id], yamlBooleans: [{line, value, text}],
 *          loadError: string|null }. A feature's minimum edition is the first
 * edition with a truthy cell, or its `requires:` when set. `loadError` is set
 * when the file didn't parse: the checks that read this vocabulary stand down,
 * and the run reports the data file itself instead (see pricingDataErrors).
 */
const PRICING = (function () {
    const empty = { editions: [], names: {}, features: {}, duplicates: [], yamlBooleans: [], loadError: null };
    try {
        const p = path.resolve(__dirname, "../../data/pulumi_pricing.yaml");
        const raw = fs.readFileSync(p, "utf8");

        // YAML 1.1 parses `no`, `yes`, `on`, `off`, `y`, and `n` as booleans, so
        // an author writing `enterprise: No` to mean the *word* "No" silently
        // gets `false` and the cell renders as a dash. By parse time the two are
        // indistinguishable from a deliberate `false`, so catch it in the source
        // text: quote the string, or write `true`/`false` if you meant the bool.
        const yamlBooleans = [];
        raw.split("\n").forEach(function (line, i) {
            const m = line.match(/^\s+[a-z0-9-]+:\s*(y|n|yes|no|on|off)\s*$/i);
            if (m) {
                yamlBooleans.push({ line: i + 1, value: m[1], text: line.trim() });
            }
        });

        const doc = yaml.load(raw);
        const editions = (doc.editions || []).map(e => e.id);
        const names = {};
        (doc.editions || []).forEach(e => (names[e.id] = e.name));
        const features = {};
        const duplicates = [];
        for (const cat of doc.categories || []) {
            for (const f of cat.features || []) {
                if (Object.prototype.hasOwnProperty.call(features, f.id)) {
                    duplicates.push(f.id);
                }
                const from = f.available_from ? editions.indexOf(f.available_from) : -1;
                let min = null;
                editions.forEach(function (id, i) {
                    let v = from >= 0 && i >= from;
                    // A stranded key (`enterprise:` with nothing after it) parses
                    // as null, which Hugo's `ne $o nil` treats as no override at
                    // all. Match that, or lint and the build disagree about the
                    // feature's minimum edition and the "fail in lint first"
                    // contract inverts.
                    if (f.availability && f.availability[id] !== undefined && f.availability[id] !== null) {
                        v = f.availability[id];
                    }
                    if (v && min === null) {
                        min = id;
                    }
                });
                features[f.id] = f.requires || min;
            }
        }
        return { editions, names, features, duplicates, yamlBooleans, loadError: null };
    } catch (e) {
        // Don't warn and carry on with empty vocabularies: that makes every
        // marked page and changelog entry fail with "not an edition id... Use
        // one of: " and an empty list, burying the one real problem. Report the
        // data file itself instead, and skip the checks that read it.
        return Object.assign({}, empty, { loadError: e.message });
    }
})();

/**
 * Feature ids a marker may name: everything except the ones that resolve to the
 * lowest edition, which gates nothing.
 */
const MARKABLE_FEATURES = Object.keys(PRICING.features)
    .filter(id => PRICING.features[id] && PRICING.features[id] !== PRICING.editions[0])
    .sort();

/**
 * Defined blog series slugs, loaded once from data/blog_series.yml. Used to
 * enforce that every series member is wired up consistently (see
 * checkSeriesConsistency).
 */
const BLOG_SERIES_SLUGS = (function () {
    try {
        const p = path.resolve(__dirname, "../../data/blog_series.yml");
        const doc = yaml.load(fs.readFileSync(p, "utf8"));
        return new Set((doc.series || []).map(s => s.slug).filter(Boolean));
    } catch (e) {
        console.warn(`Warning: could not load blog series: ${e.message}`);
        return new Set();
    }
})();

/**
 * REGEX for grabbing the front matter of a Hugo markdown file. Example:
 *
 *     ---
 *     ...props
 *     ---
 */
const FRONT_MATTER_REGEX = /((^---\s*$[^]*?^---\s*$)|(^\+\+\+\s*$[^]*?^(\+\+\+|\.\.\.)\s*$))(\r\n|\r|\n|$)/m;
const AUTO_GENERATED_HEADING_REGEX = /###### Auto generated by ([a-z0-9]\w+)[/]([a-z0-9]\w+) on ([0-9]+)-([a-zA-z]\w+)-([0-9]\w+)/g;

/**
 * Validates if a title exists, has length, and does not have a length over 60 characters.
 * More info: https://moz.com/learn/seo/title-tag
 *
 * @param {string} title The title tag value for a given page.
 */
function checkPageTitle(title, allowLongTitle) {
    if (allowLongTitle) {
        return null;
    }

    if (!title) {
        return "Missing page title";
    } else if (typeof title === "string") {
        const titleLength = title.trim().length;
        if (titleLength === 0) {
            return "Page title is empty";
        } else if (titleLength > 70) {
            return "Page title exceeds 60 characters";
        }
    } else {
        return "Page title is not a valid string";
    }
    return null;
}

/**
 * Validates that a meta description exists, has length, is not too short,
 * and is not too long.
 * More info: https://moz.com/learn/seo/meta-description
 *
 * @param {string} meta The meta description for a given page
 */
function checkPageMetaDescription(meta) {
    if (!meta) {
        return "Missing meta description";
    } else if (typeof meta === "string") {
        const metaLength = meta.trim().length;
        if (metaLength === 0) {
            return "Meta description is empty";
        } else if (metaLength < 50) {
            return "Meta description is too short. Must be at least 50 characters";
        } else if (metaLength > 160) {
            return "Meta description is too long. Must be shorter than 160 characters";
        }
    } else {
        return "Meta description is not a valid string";
    }
    return null;
}

/**
 * checkMetaImage validates that all meta images are png files in order ensure
 * compatibility when shared on social media platforms.
 *
 * @param {string} image The meta image file for a given page
 */
function checkMetaImage(image) {
    if (!image) {
        return null;
    }

    const regex = /\.([0-9a-z]+)(?:[\?#]|$)/i;
    const extension = regex.exec(image)[1];
    if (extension !== "png") {
        return `Meta image, '${image}', must be a png file.`;
    }

    return null;
}

/** Canonical blog feature image dimensions, matching the blog-feature-image templates. */
const FEATURE_IMAGE_WIDTH = 1884;
const FEATURE_IMAGE_HEIGHT = 1256;

/**
 * Reads the intrinsic pixel dimensions from a PNG or JPEG file by inspecting its
 * header bytes — no image library required. Returns { width, height } or null if
 * the file can't be read or isn't a recognized PNG/JPEG.
 *
 * @param {string} file Absolute path to the image file.
 * @returns {{width: number, height: number}|null}
 */
function imageDimensions(file) {
    let buf;
    try {
        buf = fs.readFileSync(file);
    } catch (e) {
        return null;
    }

    // PNG: 8-byte signature (\x89PNG...), then the IHDR chunk whose width/height
    // are big-endian uint32s at byte offsets 16 and 20.
    if (buf.length >= 24 && buf.readUInt32BE(0) === 0x89504e47) {
        return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
    }

    // JPEG: starts with FFD8; scan the marker segments for a Start-Of-Frame
    // (SOF0-SOF15, excluding the non-frame C4/C8/CC markers), which carries the
    // image height and width as big-endian uint16s.
    if (buf.length >= 4 && buf[0] === 0xff && buf[1] === 0xd8) {
        let offset = 2;
        while (offset + 9 < buf.length) {
            if (buf[offset] !== 0xff) {
                offset++;
                continue;
            }
            const marker = buf[offset + 1];
            if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc) {
                return { height: buf.readUInt16BE(offset + 5), width: buf.readUInt16BE(offset + 7) };
            }
            offset += 2 + buf.readUInt16BE(offset + 2);
        }
    }

    return null;
}

/**
 * checkFeatureImageDimensions enforces that a blog post's `feature_image` is a
 * template-sized 1884x1256 image. The blog-feature-image skill only ever renders
 * templates at this size (and designer-supplied images are expected to match it),
 * so an off-size image is a strong signal it's AI-generated slop rather than a
 * template render or a real designer image. Only blog posts carry a fixed-size
 * feature image, and only post-local (relative) paths are checked; shared/legacy
 * absolute paths (/images/...) are out of scope.
 *
 * @param {string} featureImage The `feature_image` front-matter value.
 * @param {string} fullPath Absolute path to the markdown file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkFeatureImageDimensions(featureImage, fullPath) {
    if (!featureImage || typeof featureImage !== "string" || fullPath.indexOf("/content/blog/") === -1) {
        return null;
    }
    if (featureImage.startsWith("/") || /^https?:/i.test(featureImage)) {
        return null;
    }

    const imgPath = path.join(path.dirname(fullPath), featureImage);
    if (!fs.existsSync(imgPath)) {
        return `Feature image '${featureImage}' was not found next to the post.`;
    }

    const size = imageDimensions(imgPath);
    if (!size) {
        return `Feature image '${featureImage}' could not be read as a PNG/JPEG; render it with the /blog-feature-image skill.`;
    }
    if (size.width !== FEATURE_IMAGE_WIDTH || size.height !== FEATURE_IMAGE_HEIGHT) {
        return `Feature image '${featureImage}' is ${size.width}x${size.height}, but blog feature images must be ${FEATURE_IMAGE_WIDTH}x${FEATURE_IMAGE_HEIGHT}. Render it with the /blog-feature-image skill or use a designer-supplied image (never AI-generated).`;
    }

    return null;
}

/** Canonical blog feature image background color (the templates' backdrop). */
const FEATURE_IMAGE_BG = { r: 0x23, g: 0x1f, b: 0x33 };

/** PNG Paeth predictor, used to reverse filter type 4. */
function paethPredictor(a, b, c) {
    const p = a + b - c;
    const pa = Math.abs(p - a);
    const pb = Math.abs(p - b);
    const pc = Math.abs(p - c);
    if (pa <= pb && pa <= pc) return a;
    if (pb <= pc) return b;
    return c;
}

/**
 * Decodes an 8-bit, non-interlaced PNG and returns its four corner pixels as
 * {r,g,b}, ordered [top-left, top-right, bottom-left, bottom-right]. Uses only
 * Node's built-in zlib — no image dependency. Returns null for anything it can't
 * safely decode (non-PNG, 16-bit, interlaced, unknown/paletteless color type),
 * so callers skip the check rather than raising a false positive.
 *
 * @param {string} file Absolute path to a PNG file.
 * @returns {{r:number,g:number,b:number}[]|null}
 */
function pngCornerColors(file) {
    let buf;
    try {
        buf = fs.readFileSync(file);
    } catch (e) {
        return null;
    }
    if (buf.length < 33 || buf.readUInt32BE(0) !== 0x89504e47) {
        return null; // Not a PNG.
    }

    const width = buf.readUInt32BE(16);
    const height = buf.readUInt32BE(20);
    const bitDepth = buf[24];
    const colorType = buf[25];
    const interlace = buf[28];
    const channels = { 0: 1, 2: 3, 3: 1, 4: 2, 6: 4 }[colorType];
    if (bitDepth !== 8 || interlace !== 0 || !channels || width < 1 || height < 1) {
        return null;
    }

    // Walk the chunk stream: concatenate IDAT payloads and grab the palette.
    let offset = 8;
    const idatParts = [];
    let palette = null;
    while (offset + 8 <= buf.length) {
        const length = buf.readUInt32BE(offset);
        const type = buf.toString("ascii", offset + 4, offset + 8);
        const dataStart = offset + 8;
        if (type === "IDAT") {
            idatParts.push(buf.subarray(dataStart, dataStart + length));
        } else if (type === "PLTE") {
            palette = buf.subarray(dataStart, dataStart + length);
        } else if (type === "IEND") {
            break;
        }
        offset = dataStart + length + 4; // Skip the chunk data and its 4-byte CRC.
    }
    if (idatParts.length === 0 || (colorType === 3 && !palette)) {
        return null;
    }

    let raw;
    try {
        raw = zlib.inflateSync(Buffer.concat(idatParts));
    } catch (e) {
        return null;
    }

    const stride = width * channels;
    if (raw.length < (stride + 1) * height) {
        return null; // Truncated/unexpected data.
    }

    // Reverse the per-scanline filters into a contiguous raster. Every row must be
    // un-filtered because filters can reference the pixel directly above.
    const out = Buffer.alloc(stride * height);
    for (let y = 0; y < height; y++) {
        const filter = raw[y * (stride + 1)];
        const inStart = y * (stride + 1) + 1;
        const outStart = y * stride;
        const prevStart = outStart - stride;
        for (let x = 0; x < stride; x++) {
            const rawByte = raw[inStart + x];
            const left = x >= channels ? out[outStart + x - channels] : 0;
            const up = y > 0 ? out[prevStart + x] : 0;
            const upLeft = y > 0 && x >= channels ? out[prevStart + x - channels] : 0;
            let value;
            switch (filter) {
                case 0:
                    value = rawByte;
                    break;
                case 1:
                    value = rawByte + left;
                    break;
                case 2:
                    value = rawByte + up;
                    break;
                case 3:
                    value = rawByte + ((left + up) >> 1);
                    break;
                case 4:
                    value = rawByte + paethPredictor(left, up, upLeft);
                    break;
                default:
                    return null; // Unknown filter type.
            }
            out[outStart + x] = value & 0xff;
        }
    }

    function pixel(x, y) {
        const i = y * stride + x * channels;
        if (colorType === 3) {
            const idx = out[i] * 3;
            return { r: palette[idx], g: palette[idx + 1], b: palette[idx + 2] };
        }
        if (colorType === 0 || colorType === 4) {
            return { r: out[i], g: out[i], b: out[i] };
        }
        return { r: out[i], g: out[i + 1], b: out[i + 2] };
    }

    return [pixel(0, 0), pixel(width - 1, 0), pixel(0, height - 1), pixel(width - 1, height - 1)];
}

/**
 * checkFeatureImageBackground enforces that a blog post's `feature_image` uses
 * the canonical #231F33 backdrop by sampling the four corners (every template
 * renders a flat #231F33 background, so an off-color corner means the file was
 * not rendered from a template). Scope matches checkFeatureImageDimensions:
 * blog posts only, post-local paths only. Non-PNG/undecodable files are skipped
 * (the dimension check remains the size guard).
 *
 * @param {string} featureImage The `feature_image` front-matter value.
 * @param {string} fullPath Absolute path to the markdown file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkFeatureImageBackground(featureImage, fullPath) {
    if (!featureImage || typeof featureImage !== "string" || fullPath.indexOf("/content/blog/") === -1) {
        return null;
    }
    if (featureImage.startsWith("/") || /^https?:/i.test(featureImage)) {
        return null;
    }

    const imgPath = path.join(path.dirname(fullPath), featureImage);
    if (!fs.existsSync(imgPath)) {
        return null; // checkFeatureImageDimensions already reports a missing file.
    }

    const corners = pngCornerColors(imgPath);
    if (!corners) {
        return null; // Not a decodable PNG; leave sizing to the dimension check.
    }

    const { r, g, b } = FEATURE_IMAGE_BG;
    const offColor = corners.find(c => c.r !== r || c.g !== g || c.b !== b);
    if (offColor) {
        const toHex = c => "#" + [c.r, c.g, c.b].map(n => n.toString(16).padStart(2, "0")).join("").toUpperCase();
        return `Feature image '${featureImage}' has a ${toHex(offColor)} background, but blog feature images must be #231F33. Render it with the /blog-feature-image skill or use a designer-supplied image (never AI-generated).`;
    }

    return null;
}

/**
 * PNG Software tag written by the blog-feature-image renderer
 * (compose_meta_image.py). This string is a shared constant between the renderer
 * and this allowlist — keep the two in sync if it ever changes.
 */
const FEATURE_IMAGE_SOFTWARE = "pulumi-blog-feature-image";

/**
 * Reads a PNG's `tEXt` Software value straight from the file bytes — no decode
 * library. Returns the string, or null when there's no tEXtSoftware chunk.
 *
 * @param {Buffer} buf The raw PNG file contents.
 * @returns {string|null}
 */
function readPngSoftware(buf) {
    const match = /tEXtSoftware\x00([ -~]*)/.exec(buf.toString("latin1"));
    return match ? match[1] : null;
}

/**
 * checkFeatureImageSoftware enforces that a blog post's `feature_image` was
 * produced by the approved pipeline, using an allowlist on the PNG Software tag
 * rather than a denylist (so a new bad generator fails by default). Allowed:
 * "Figma" (designer exports), our renderer's stamp, or no tag at all (legacy
 * skill output — Pillow wrote no Software tag before the stamp was added). Any
 * other stamp (Matplotlib, PIL, DALL·E, Midjourney, etc.) fails. Scope matches
 * the other feature-image checks: blog posts, post-local PNG paths only.
 *
 * @param {string} featureImage The `feature_image` front-matter value.
 * @param {string} fullPath Absolute path to the markdown file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkFeatureImageSoftware(featureImage, fullPath) {
    if (!featureImage || typeof featureImage !== "string" || fullPath.indexOf("/content/blog/") === -1) {
        return null;
    }
    if (featureImage.startsWith("/") || /^https?:/i.test(featureImage)) {
        return null;
    }

    const imgPath = path.join(path.dirname(fullPath), featureImage);
    if (!fs.existsSync(imgPath)) {
        return null; // checkFeatureImageDimensions already reports a missing file.
    }

    let buf;
    try {
        buf = fs.readFileSync(imgPath);
    } catch (e) {
        return null;
    }
    if (buf.length < 8 || buf.readUInt32BE(0) !== 0x89504e47) {
        return null; // Not a PNG; leave format/sizing to the other checks.
    }

    // Allowlist: Figma exports, our renderer's stamp, or no tag (legacy renders).
    const software = readPngSoftware(buf);
    if (software === null || software === "Figma" || software === FEATURE_IMAGE_SOFTWARE) {
        return null;
    }

    return `Feature image '${featureImage}' was produced by '${software}', which is not an approved source. Render it with the /blog-feature-image skill or use a designer-supplied (Figma) image (never AI-generated).`;
}

/**
 * Every C2PA (content-credentials) manifest embeds a JUMBF superbox whose
 * description box carries the ASCII label `jumdc2pa\0` — the same 9 bytes in a
 * JPEG APP11 segment or a PNG chunk, so one needle covers both formats.
 */
const C2PA_MARKER = "jumdc2pa\x00";

/**
 * checkFeatureImageC2pa fails a blog post's `feature_image` that carries a C2PA
 * content-credentials manifest. AI image generators (Google, OpenAI, Adobe
 * Firefly) sign their output with C2PA precisely to mark it as AI-generated,
 * and neither of our approved sources emits it — compose_meta_image.py writes
 * plain Pillow PNGs and Figma exports carry no manifest — so any C2PA marker
 * means the file did not come from an approved pipeline. This closes the gap
 * the other checks leave: a generated image resized to 1884x1256 with a
 * template-colored backdrop and no PNG Software tag would otherwise pass.
 * Scope matches the other feature-image checks: blog posts, post-local paths.
 *
 * @param {string} featureImage The `feature_image` front-matter value.
 * @param {string} fullPath Absolute path to the markdown file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkFeatureImageC2pa(featureImage, fullPath) {
    if (!featureImage || typeof featureImage !== "string" || fullPath.indexOf("/content/blog/") === -1) {
        return null;
    }
    if (featureImage.startsWith("/") || /^https?:/i.test(featureImage)) {
        return null;
    }

    const imgPath = path.join(path.dirname(fullPath), featureImage);
    if (!fs.existsSync(imgPath)) {
        return null; // checkFeatureImageDimensions already reports a missing file.
    }

    let buf;
    try {
        buf = fs.readFileSync(imgPath);
    } catch (e) {
        return null;
    }

    if (buf.toString("latin1").indexOf(C2PA_MARKER) !== -1) {
        return `Feature image '${featureImage}' carries a C2PA content-credentials manifest, which marks it as AI-generated output. Render it with the /blog-feature-image skill or use a designer-supplied (Figma) image (never AI-generated).`;
    }

    return null;
}

/**
 * checkBlogCategory validates the `category:` front matter on blog posts against
 * the closed set in data/blog_categories.yaml. It applies ONLY to individual
 * blog posts (content/blog/<slug>/index.md), not section pages (_index.md), tag
 * pages, or non-blog content.
 *
 * Category is REQUIRED and SINGULAR: every post must declare exactly one
 * `category:` scalar value from the allowed set. Use `general` (the default)
 * for posts that don't clearly fit a specific kind. A list value, a missing
 * value, or a value outside the set is an error. (The legacy plural `categories`
 * field is no longer accepted.)
 *
 * @param {string} category The `category` front matter value.
 * @param {*} legacyCategories The legacy `categories` front matter value, if any.
 * @param {string} fullPath The absolute path of the file being linted.
 */
function checkBlogCategory(category, legacyCategories, fullPath) {
    const isBlogPost =
        fullPath.includes("/content/blog/") && path.basename(fullPath) === "index.md";
    if (!isBlogPost) {
        return null;
    }

    if (typeof legacyCategories !== "undefined") {
        return "Blog post uses the legacy 'categories' field. Use a singular 'category:' scalar instead (e.g. 'category: general'). See data/blog_categories.yaml.";
    }
    if (Array.isArray(category)) {
        return "Blog post 'category' must be a single scalar value, not a list (e.g. 'category: general'). See data/blog_categories.yaml.";
    }
    if (!category) {
        return "Blog post is missing a required 'category' value. Add exactly one category from data/blog_categories.yaml (use 'general' if it doesn't fit a specific kind).";
    }
    if (!BLOG_CATEGORIES.includes(category)) {
        return `Invalid blog category value: '${category}'. Allowed: ${BLOG_CATEGORIES.join(", ")}. See data/blog_categories.yaml.`;
    }

    return null;
}

/**
 * checkCaseStudyIndustry validates the `industry:` front matter on case studies
 * against the closed set in data/case_study_industries.yaml. It applies ONLY to
 * individual case-study pages (content/case-studies/<slug>.md), not the section
 * index (_index.md) or any other content.
 *
 * Industry is REQUIRED and SINGULAR: every case study declares exactly one
 * `industry:` scalar value from the allowed set — a customer belongs to one
 * vertical. A list value, a missing value, or a value outside the set is an
 * error. `industry` is a dedicated Hugo taxonomy (see config.yml), so any value
 * generates a public term page at /case-studies/industry/<slug>/; a typo would
 * silently ship an orphan URL, which this guard prevents.
 *
 * @param {*} industry The `industry` front matter value.
 * @param {string} fullPath The absolute path of the file being linted.
 */
function checkCaseStudyIndustry(industry, fullPath) {
    const isCaseStudy =
        fullPath.includes("/content/case-studies/") && path.basename(fullPath) !== "_index.md";
    if (!isCaseStudy) {
        return null;
    }

    if (Array.isArray(industry)) {
        return "Case study 'industry' must be a single scalar value, not a list (e.g. 'industry: security'). See data/case_study_industries.yaml.";
    }
    if (!industry) {
        return "Case study is missing a required 'industry' value. Add exactly one industry from data/case_study_industries.yaml.";
    }
    if (!CASE_STUDY_INDUSTRIES.includes(industry)) {
        return `Invalid case-study industry value: '${industry}'. Allowed: ${CASE_STUDY_INDUSTRIES.join(", ")}. See data/case_study_industries.yaml.`;
    }

    return null;
}

/**
 * checkCaseStudyLogoTile validates the optional logo-tile front matter on case
 * studies, rendered by layouts/partials/case-studies/card.html (see its header
 * comment for what each field does):
 *   - logo_bg_color: a hex color ("#RRGGBB" or "#RGB")
 *   - logo_style: "white" or "dark", lowercase
 *   - logo_size: "lg"
 * All are optional; this guard rejects present-but-malformed values, which
 * would otherwise ship silently — the template compares exactly, so e.g.
 * `logo_style: White` just renders the logo in its original colors, and a bad
 * hex paints no tile background at all.
 *
 * @param {*} obj The parsed front matter object.
 * @param {string} fullPath The absolute path of the file being linted.
 */
function checkCaseStudyLogoTile(obj, fullPath) {
    const isCaseStudy =
        fullPath.includes("/content/case-studies/") && path.basename(fullPath) !== "_index.md";
    if (!isCaseStudy) {
        return null;
    }

    const errors = [];
    if (obj.logo_bg_color !== undefined && !/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/.test(String(obj.logo_bg_color))) {
        errors.push(
            `Invalid 'logo_bg_color' value: '${obj.logo_bg_color}'. Use a quoted hex color like "#0052CC".`,
        );
    }
    if (obj.logo_style !== undefined && !["white", "dark"].includes(obj.logo_style)) {
        errors.push(
            `Invalid 'logo_style' value: '${obj.logo_style}'. Allowed: white, dark (lowercase), or omit to render the logo in its original colors.`,
        );
    }
    if (obj.logo_size !== undefined && obj.logo_size !== "lg") {
        errors.push(
            `Invalid 'logo_size' value: '${obj.logo_size}'. Allowed: lg, or omit for the default size.`,
        );
    }

    return errors.length > 0 ? errors.join(" ") : null;
}

/**
 * checkSeriesConsistency enforces that a blog post's series wiring is correct.
 *
 * Series membership is driven solely by the `series: <slug>` key:
 *   - single.html renders the "In This Series" sidebar, finding siblings via
 *     `where .Params.series`.
 *   - the dedicated `series` taxonomy generates the landing page at
 *     /blog/series/<slug>/ (see layouts/taxonomy/series.html + config.yml).
 * The slug must name a series defined in data/blog_series.yml (any value
 * generates a public term page, so a typo would ship a junk URL) and must NOT
 * also appear in `tags`: that was the old workaround for manufacturing a landing
 * page under the `tags` taxonomy, and it now only produces a stray
 * /blog/tag/<slug>/ page and surfaces the slug as a topical tag pill. Applies
 * only to blog posts (content/blog/<slug>/index.md).
 *
 * @param {*} series The `series` front matter value.
 * @param {*} tags The `tags` front matter value.
 * @param {string} fullPath The absolute path of the file being linted.
 */
function checkSeriesConsistency(series, tags, fullPath) {
    const isBlogPost =
        fullPath.includes("/content/blog/") && path.basename(fullPath) === "index.md";
    if (!isBlogPost || BLOG_SERIES_SLUGS.size === 0) {
        return null;
    }

    const tagList = Array.isArray(tags) ? tags : typeof tags === "string" ? [tags] : [];

    if (Array.isArray(series)) {
        return "Blog post 'series' must be a single scalar value (the series slug), not a list. See data/blog_series.yml.";
    }

    // Every `series:` value mints a public, indexable /blog/series/<value>/ term
    // page, so it must name a defined series — a typo would silently ship a bare
    // fallback listing at a junk URL.
    if (series && !BLOG_SERIES_SLUGS.has(series)) {
        return `Blog post has 'series: ${series}', which is not a defined blog series. Every series value generates a public /blog/series/ page, so it must match a slug in data/blog_series.yml — fix the typo, or add the series to the data file.`;
    }

    // A defined series slug must not be used as a tag; the `series` taxonomy owns
    // the landing page now, keyed off the `series:` front matter.
    for (const t of tagList) {
        if (BLOG_SERIES_SLUGS.has(t)) {
            const addKey = series === t ? "" : ` and add 'series: ${t}'`;
            return `Blog post is tagged '${t}', a defined blog series. Series now live in their own taxonomy at /blog/series/${t}/ (driven by the 'series:' key), so the slug must not be a tag. Remove '${t}' from tags${addKey}. See data/blog_series.yml.`;
        }
    }

    return null;
}

/**
 * Approximates Hugo's `anchorize` well enough to detect two session labels that
 * would collide into the same anchor (and so the same DOM key): lowercase, spaces
 * to hyphens, drop anything that isn't a word character or a hyphen.
 *
 * @param {string} value The label to anchorize.
 * @returns {string} The anchorized form.
 */
function anchorizeLabel(value) {
    return String(value)
        .trim()
        .toLowerCase()
        .replace(/\s+/g, "-")
        .replace(/[^a-z0-9_-]/g, "");
}

/**
 * Parses a front matter datetime into a Date. js-yaml resolves an unquoted ISO
 * timestamp to a Date and leaves a quoted one a string, so handle both. Returns
 * null when the value is missing or unparseable.
 *
 * @param {*} value The raw front matter value.
 * @returns {Date|null} The parsed date, or null.
 */
function parseDateTime(value) {
    if (value instanceof Date) {
        return isNaN(value.getTime()) ? null : value;
    }
    if (typeof value !== "string" || value.trim() === "") {
        return null;
    }
    const parsed = new Date(value);
    return isNaN(parsed.getTime()) ? null : parsed;
}

/**
 * checkEventSessions validates the optional `sessions:` front matter on event
 * pages (content/events/<slug>/index.md). An event offered on more than one date
 * — an Americas slot and an EMEA slot, say — is one page with a `sessions:`
 * array rather than two near-identical bundles; see the archetype and
 * layouts/partials/events/sessions.html.
 *
 * What's enforced, and why each one would otherwise ship silently broken:
 *   - every session needs a parseable `sortable_date`; a session without one
 *     sorts to the front of every list with a zero date
 *   - with more than one session, each needs a `label`, and no two may anchorize
 *     to the same key — the label is the tab, the badge, and the deep-link anchor,
 *     so a collision makes two sessions share one panel
 *   - a gated event needs a `form.hubspot_form_id` per session, since the
 *     top-level form no longer applies
 *   - the top-level `form:` must be gone when sessions are present, so there's no
 *     ambiguity about which form a session renders
 *   - the top-level `sortable_date` must equal the earliest session's; it stays
 *     the event's own date for sorting, schema.org, and the social card, and
 *     drifting from the sessions makes the event sort to a date it doesn't run on
 *
 * Reusing one HubSpot form id across sessions is warned about rather than
 * rejected: the page renders two <pulumi-hubspot-form> instances and they filter
 * HubSpot's window messages by form id, so identical ids make the two forms react
 * to each other's events.
 *
 * @param {*} obj The parsed front matter object.
 * @param {string} fullPath The absolute path of the file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkEventSessions(obj, fullPath) {
    const normalized = fullPath.replace(/\\/g, "/");
    const isEvent =
        normalized.includes("/content/events/") && path.basename(normalized) === "index.md";
    if (!isEvent || obj.sessions === undefined) {
        return null;
    }

    if (!Array.isArray(obj.sessions) || obj.sessions.length === 0) {
        return "Event 'sessions' must be a non-empty YAML array, one entry per date the event runs. Remove the key entirely for an event that runs once. See archetypes/event/index.md.";
    }

    const errors = [];
    const sessions = obj.sessions;
    const multi = sessions.length > 1;

    if (obj.form !== undefined) {
        errors.push(
            "Event has both a top-level 'form:' and 'sessions:'. Move the form into each session so there's no question which one renders, and delete the top-level key.",
        );
    }

    const dates = [];
    const anchors = new Map();
    const formIds = new Map();

    sessions.forEach(function (session, i) {
        const at = `sessions[${i}]`;
        if (!session || typeof session !== "object" || Array.isArray(session)) {
            errors.push(`${at} must be a mapping with at least a 'sortable_date'.`);
            return;
        }

        const date = parseDateTime(session.sortable_date);
        if (!date) {
            errors.push(
                `${at} is missing a valid 'sortable_date' (RFC 3339, e.g. 2026-09-16T09:00:00.000-07:00).`,
            );
        } else {
            dates.push(date);
        }

        const label = typeof session.label === "string" ? session.label.trim() : "";
        if (multi && !label) {
            errors.push(
                `${at} is missing a 'label'. With more than one session the label is the tab, the badge, and the deep-link anchor (e.g. 'label: EMEA').`,
            );
        } else if (multi) {
            const anchor = anchorizeLabel(label);
            if (!anchor) {
                errors.push(`${at} has a 'label' with no letters or digits ('${label}'), which anchorizes to nothing.`);
            } else if (anchors.has(anchor)) {
                errors.push(
                    `${at} label '${label}' collides with '${anchors.get(anchor)}' (both anchorize to '${anchor}'), so the two sessions would share one tab and one panel.`,
                );
            } else {
                anchors.set(anchor, label);
            }
        }

        const hubspotFormId = session.form && session.form.hubspot_form_id;
        if (obj.gated === true && !hubspotFormId) {
            errors.push(
                `${at} is missing 'form.hubspot_form_id'. A gated event needs a registration form per session.`,
            );
        } else if (hubspotFormId) {
            if (formIds.has(hubspotFormId)) {
                console.warn(
                    `Warning: ${normalized}: ${at} reuses the HubSpot form id '${hubspotFormId}' from ${formIds.get(hubspotFormId)}. Both forms render on the page and filter HubSpot's events by form id, so they will react to each other. Give each session its own form.`,
                );
            } else {
                formIds.set(hubspotFormId, at);
            }
        }
    });

    const topDate = parseDateTime(obj.sortable_date);
    if (!topDate) {
        errors.push(
            "Event is missing a valid top-level 'sortable_date'. It stays required alongside 'sessions' and must equal the earliest session's date.",
        );
    } else if (dates.length > 0) {
        const earliest = dates.reduce(function (a, b) {
            return a < b ? a : b;
        });
        if (topDate.getTime() !== earliest.getTime()) {
            errors.push(
                `Event's top-level 'sortable_date' (${topDate.toISOString()}) must equal the earliest session's date (${earliest.toISOString()}). It's what sorts the event, dates its schema.org entry, and stamps its social card.`,
            );
        }
    }

    return errors.length > 0 ? errors.join(" ") : null;
}

/**
 * Normalizes a front matter `date:` value to a YYYY-MM-DD string. js-yaml parses
 * an unquoted ISO date into a Date, while a quoted one stays a string, so handle
 * both. Returns null if the value is missing or unparseable.
 *
 * @param {Date|string|undefined} date The raw front matter date value.
 * @returns {string|null} The date as YYYY-MM-DD, or null.
 */
function normalizeDate(date) {
    if (!date) {
        return null;
    }
    if (date instanceof Date) {
        return date.toISOString().slice(0, 10);
    }
    const match = String(date).trim().match(/^\d{4}-\d{2}-\d{2}/);
    return match ? match[0] : null;
}

/**
 * checkChangelogFilename enforces the naming convention for individual changelog
 * entries under content/releases/changelog/: files must be named
 * `YYYY-MM-DD-<slug>.md`, and the date prefix must match the front matter
 * `date:` so the two never drift. Applies only to entry pages, not the section
 * `_index.md`. See archetypes/changelog.md and the /new-changelog skill.
 *
 * @param {Date|string|undefined} date The front matter date value.
 * @param {string} fullPath The absolute path of the file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkChangelogFilename(date, fullPath) {
    const normalized = fullPath.replace(/\\/g, "/");
    const isChangelogEntry =
        normalized.includes("/content/releases/changelog/") &&
        path.basename(normalized) !== "_index.md";
    if (!isChangelogEntry) {
        return null;
    }

    const filename = path.basename(normalized);
    const match = filename.match(/^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$/);
    if (!match) {
        return "Changelog entry filenames must be date-prefixed and lowercase-hyphenated, as 'YYYY-MM-DD-slug.md' (e.g. 2026-07-11-universal-search.md). See archetypes/changelog.md or run /new-changelog.";
    }

    // The filename date prefix must agree with the front matter `date:`.
    const prefix = match[1];
    const fmDate = normalizeDate(date);
    if (fmDate && fmDate !== prefix) {
        return `Changelog entry filename date prefix '${prefix}' does not match front matter 'date: ${fmDate}'. Rename the file or fix the date so they agree.`;
    }

    return null;
}

/**
 * checkChangelogEditions validates the optional `editions:` front matter on
 * individual changelog entries: it must be a YAML array of edition ids from
 * data/pulumi_pricing.yaml. Templates look the ids up to render the display
 * name, so an entry writes `business-critical` and the badge reads "Business
 * Critical". Authors list every edition the feature is available in; since a
 * lower edition implies the ones above it, that means the lowest applicable
 * edition and all editions above it — checked here as a contiguous suffix of
 * the edition list, not just set membership. Applies only to entry pages, not
 * the section `_index.md`.
 *
 * The legacy `tiers:` array and singular `tier:` scalar are both rejected:
 * "tier" is not a word the product uses, and the old list carried a `Free`
 * value for an edition that doesn't exist (the free edition is Individual).
 *
 * @param {*} editions The front matter `editions` value.
 * @param {*} tiers The front matter `tiers` value (legacy; rejected if present).
 * @param {*} tier The front matter `tier` value (legacy; rejected if present).
 * @param {string} fullPath The absolute path of the file being linted.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkChangelogEditions(editions, tiers, tier, fullPath) {
    const normalized = fullPath.replace(/\\/g, "/");
    const isChangelogEntry =
        normalized.includes("/content/releases/changelog/") &&
        path.basename(normalized) !== "_index.md";
    // Without the pricing data there is no vocabulary to check against, and
    // guessing produces "use one of: " with an empty list on every entry. The
    // run already carries one finding about the data file (pricingDataErrors).
    if (!isChangelogEntry || PRICING.loadError) {
        return null;
    }

    if (tier !== undefined || tiers !== undefined) {
        const old = tier !== undefined ? "tier:" : "tiers:";
        return `Changelog \`${old}\` has been replaced by \`editions:\`, a YAML array of edition ids (e.g. \`editions:\` then \`    - enterprise\`). List every edition the feature is available in — the lowest applicable edition and all editions above it. Ids come from data/pulumi_pricing.yaml: ${PRICING.editions.join(", ")}.`;
    }
    if (editions === undefined) {
        return null;
    }
    if (!Array.isArray(editions)) {
        return "Changelog `editions:` must be a YAML array (e.g. `editions:` then `    - enterprise`), not a single value.";
    }
    const invalid = editions.filter(function (e) {
        return !PRICING.editions.includes(e);
    });
    if (invalid.length > 0) {
        const quoted = invalid
            .map(function (e) {
                return "'" + e + "'";
            })
            .join(", ");
        return "Changelog `editions:` value(s) " + quoted + " not allowed. Use an edition id from data/pulumi_pricing.yaml: " + PRICING.editions.join(", ") + ". Templates render the display name from the id, so write 'business-critical', not 'Business Critical'.";
    }
    if (editions.length === 0) {
        return "Changelog `editions:` is empty. List every edition the feature is available in — the lowest applicable edition and all editions above it — or drop the key.";
    }
    // A lower edition implies the ones above it, so a valid list is a contiguous
    // suffix of PRICING.editions. `editions: [enterprise]` on its own lints as
    // three valid ids but renders a badge that tells Business Critical readers
    // the feature isn't theirs.
    const listed = PRICING.editions.filter(function (e) {
        return editions.includes(e);
    });
    const expected = PRICING.editions.slice(PRICING.editions.indexOf(listed[0]));
    if (listed.length !== expected.length) {
        const missing = expected.filter(function (e) {
            return !listed.includes(e);
        });
        return (
            "Changelog `editions:` lists " +
            listed.join(", ") +
            " but not " +
            missing.join(", ") +
            ". A lower edition implies the ones above it, so list the lowest applicable edition and every edition above it: " +
            expected.join(", ") +
            "."
        );
    }
    return null;
}

/**
 * Explains why one marker value is wrong, shared by the front matter key and the
 * shortcode argument since they name the same vocabulary.
 *
 * A marker names a FEATURE, not an edition:
 *
 *   pulumi_cloud_feature: rbac
 *   {{< pulumi-cloud "rbac" />}}
 *
 * The edition the callout states is derived from that feature's row in
 * data/pulumi_pricing.yaml, so a feature that moves editions updates /pricing/
 * and every page marked with it in one edit.
 *
 * We only mark what a reader has to buy, so there is no value meaning "Cloud but
 * ungated" — such a page carries no marker at all. `true`, `false`, and any
 * feature available on the lowest edition are therefore all rejected.
 *
 * @param {*} value The authored marker value.
 * @param {string} label How to refer to it in the message.
 * @returns {string|null} An error message, or null when valid.
 */
function pulumiCloudValueError(value, label) {
    if (typeof value === "boolean") {
        return `Invalid ${label} value: ${value}. Name the feature (for example 'rbac' or 'audit-logs'), or drop the key — an ungated page carries no marker. See data/pulumi_pricing.yaml.`;
    }
    // A bare `pulumi_cloud_feature:` parses as null, and nothing stops an author
    // writing a number. Normalize before the string comparisons below, which would
    // otherwise throw a TypeError that the caller's try/catch turns into an
    // unhelpful message.
    const id = value === null || value === undefined ? "" : String(value);
    if (!id) {
        return `Empty ${label} value. Name the feature (for example 'rbac' or 'audit-logs'), or drop the key — an ungated page carries no marker. See data/pulumi_pricing.yaml.`;
    }
    if (PRICING.editions.includes(id)) {
        return `Invalid ${label} value: '${id}'. That's an edition id, not a feature id — markers name the feature and the edition is derived from data/pulumi_pricing.yaml. Features on the ${PRICING.names[id] || id} edition include: ${MARKABLE_FEATURES.filter(f => PRICING.features[f] === id)
            .slice(0, 5)
            .join(", ")}.`;
    }
    if (PRICING.features[id] !== undefined && !MARKABLE_FEATURES.includes(id)) {
        return `Invalid ${label} value: '${id}'. That feature is available on the ${PRICING.names[PRICING.editions[0]]} edition, which gates nothing — drop the marker, or set 'requires:' on it in data/pulumi_pricing.yaml if its lowest column is really a limited variant.`;
    }
    if (!MARKABLE_FEATURES.includes(id)) {
        const near = MARKABLE_FEATURES.filter(f => f.includes(id) || id.includes(f));
        const hint = near.length > 0 ? ` Did you mean: ${near.join(", ")}?` : ` Add it to data/pulumi_pricing.yaml — with 'hidden: true' if it isn't a marketed line item on /pricing/.`;
        return `Invalid ${label} value: '${id}'. Not a feature id in data/pulumi_pricing.yaml.${hint}`;
    }
    return null;
}

/**
 * checkPulumiCloudFeature validates the optional `pulumi_cloud_feature:` front
 * matter, which marks a whole page as documenting a Pulumi Cloud feature that
 * needs a paid edition. Markers are set per page; there is no inheritance. Where
 * only part of a page is a Cloud feature, use the {{< pulumi-cloud >}} shortcode
 * instead (checkPulumiCloudShortcode below).
 *
 * The key names the feature because the value does: `pulumi_cloud: rbac` reads
 * as an assertion about Pulumi Cloud, when what it says is which feature the
 * page documents. It is not `cloud_feature` either — on a site that documents
 * AWS, Azure, and GCP, "cloud feature" reads as a PROVIDER feature.
 *
 * @param {*} feature The front matter `pulumi_cloud_feature` value.
 * @param {*} legacy The front matter `pulumi_cloud` value (renamed; rejected).
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkPulumiCloudFeature(feature, legacy) {
    // `pulumi_cloud:` was this key's name while the value was an edition id.
    // Hugo ignores an unknown front matter key, so without this the page would
    // just quietly render no marker. Droppable once the rename has settled.
    if (legacy !== undefined) {
        return "`pulumi_cloud:` is now `pulumi_cloud_feature:`, and its value is a feature id rather than an edition (e.g. `pulumi_cloud_feature: rbac`). The edition the callout states is derived from that feature in data/pulumi_pricing.yaml.";
    }
    if (feature === undefined || PRICING.loadError) {
        return null;
    }
    return pulumiCloudValueError(feature, "'pulumi_cloud_feature'");
}

/**
 * Matches any {{< pulumi-cloud ... >}} opening tag and captures whatever stands
 * between the shortcode name and the closing delimiter, quotes and all. The
 * argument isn't captured directly because the forms that need catching are the
 * ones that *aren't* a quoted positional: a named param (`feature="rbac"`) makes
 * Hugo's `.Get 0` nil, and an unquoted id works in Hugo but used to slip past a
 * regex that required the quote.
 *
 * The no-argument form means "Pulumi Cloud, all editions" and is deliberately
 * allowed, as is the block form with inner prose. The closing `{{< /pulumi-cloud >}}`
 * doesn't match, because the slash isn't whitespace.
 */
const PULUMI_CLOUD_SHORTCODE_REGEX = /\{\{[<%]\s*pulumi-cloud(\s[^}]*?)?\s*\/?\s*[>%]\}\}/g;

/**
 * checkPulumiCloudShortcode validates the argument of every
 * {{< pulumi-cloud "<feature>" />}} in a page body against the same vocabulary
 * as the front matter key. Hugo already fails the build on a bad value, but a
 * full build is minutes and `make lint` is seconds — and lint runs first.
 *
 * @param {string} content The full file contents, front matter included.
 * @returns {string|null} An error message, or null when valid/not applicable.
 */
function checkPulumiCloudShortcode(content) {
    if (PRICING.loadError) {
        return null;
    }
    const messages = [];
    let match;
    PULUMI_CLOUD_SHORTCODE_REGEX.lastIndex = 0;
    while ((match = PULUMI_CLOUD_SHORTCODE_REGEX.exec(content)) !== null) {
        const args = (match[1] || "").trim();
        if (args === "") {
            continue;
        }
        let err;
        if (args.includes("=")) {
            // The {{% notes type="warning" %}} convention makes this an easy
            // mistake, and a named param leaves `.Get 0` nil — the callout then
            // claims the feature is available on every edition.
            err = `Invalid {{< pulumi-cloud >}} argument: '${args}'. Named parameters aren't supported — write the feature id positionally, as {{< pulumi-cloud "rbac" />}}.`;
        } else {
            err = pulumiCloudValueError(args.replace(/^"(.*)"$/, "$1"), "{{< pulumi-cloud >}}");
        }
        if (err && !messages.includes(err)) {
            messages.push(err);
        }
    }
    return messages.length > 0 ? messages.join(" ") : null;
}

/**
 * Asset directories under content/releases/changelog/ whose files must be
 * date-prefixed, mirroring the entry-filename convention (checkChangelogFilename)
 * so the shared folders don't turn into an undated jumble.
 */
const CHANGELOG_ASSET_DIRS = [
    "../../content/releases/changelog/images",
    "../../content/releases/changelog/videos",
];

/** Date-prefixed, lowercase-hyphenated asset filename, e.g. 2026-07-11-foo.png. */
const CHANGELOG_ASSET_NAME_REGEX = /^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.[a-z0-9]+$/;

/**
 * Scans the changelog asset directories and returns an error group for every
 * file whose name isn't date-prefixed as YYYY-MM-DD-<slug>.<ext>. Hidden files
 * (e.g. .DS_Store, .gitkeep) are ignored. Missing directories yield no errors.
 * The shape matches groupLintErrorOutput's output so results merge cleanly.
 *
 * @returns {{path: string, errors: Object[]}[]} One error group per bad file.
 */
function checkChangelogAssets() {
    const errors = [];

    function walk(dir) {
        let entries;
        try {
            entries = fs.readdirSync(dir, { withFileTypes: true });
        } catch (e) {
            return; // Directory doesn't exist; nothing to check.
        }
        entries.forEach(function (entry) {
            const full = path.join(dir, entry.name);
            if (entry.isDirectory()) {
                walk(full);
                return;
            }
            if (entry.name.startsWith(".")) {
                return;
            }
            if (!CHANGELOG_ASSET_NAME_REGEX.test(entry.name)) {
                errors.push({
                    path: full,
                    errors: [
                        {
                            lineNumber: "Filename",
                            ruleDescription:
                                "Changelog asset filenames must be date-prefixed and lowercase-hyphenated, as 'YYYY-MM-DD-slug.ext' (e.g. 2026-07-11-universal-search.png). Rename the file and update its references.",
                        },
                    ],
                });
            }
        });
    }

    CHANGELOG_ASSET_DIRS.forEach(function (rel) {
        walk(path.resolve(__dirname, rel));
    });
    return errors;
}

/**
 * The Stencil chooser component, which is the single source of truth for which
 * chooser types exist and which option keys each one accepts. The lint check
 * below parses this file rather than duplicating its lists into a data file, so
 * the guard can't drift out of sync with the component it's guarding.
 */
const CHOOSER_COMPONENT_PATH = path.resolve(__dirname, "../../theme/stencil/src/components/chooser/chooser.tsx");

/**
 * Option tokens that both chooser shortcodes rewrite before handing them to the
 * component (layouts/shortcodes/{chooser,choosable}.html), and which therefore
 * won't appear as keys in chooser.tsx.
 */
const CHOOSER_OPTION_ALIASES = ["nodejs"];

/** Matches a chooser/choosable shortcode call, capturing its raw argument list. */
const CHOOSER_SHORTCODE_REGEX = /\{\{[<%]\s*(chooser|choosable)\s+([^\n%>}]*?)\s*\/?\s*[%>]\}\}/g;

/**
 * Parses chooser.tsx into { types, optionsByType }: the set of valid chooser
 * types (from the ChooserType union) and, for each type whose options we can
 * resolve, the set of valid option keys (by following mapOptions' switch to the
 * corresponding supported* list).
 *
 * Throws if the file can't be parsed into a non-empty type list. Failing loudly
 * is deliberate: a silently-empty registry would turn this guard into a no-op,
 * which is the exact failure mode it exists to prevent.
 *
 * @returns {{types: string[], optionsByType: Object<string, string[]>}}
 */
const parseChooserRegistry = (function () {
    let cached;

    return function () {
        if (cached) {
            return cached;
        }

        const src = fs.readFileSync(CHOOSER_COMPONENT_PATH, "utf8");

        // export type ChooserType = "language" | "os" | ...;
        const union = src.match(/export type ChooserType\s*=\s*([^;]+);/);
        const types = union ? [...union[1].matchAll(/"([^"]+)"/g)].map(m => m[1]) : [];
        if (types.length === 0) {
            throw new Error(`Could not parse the ChooserType union from ${CHOOSER_COMPONENT_PATH}. ` + `If the component was refactored, update parseChooserRegistry in this file to match.`);
        }

        // case "language": options = this.supportedLanguages;
        const typeToList = {};
        for (const m of src.matchAll(/case\s+"([^"]+)":\s*options\s*=\s*this\.(\w+);/g)) {
            typeToList[m[1]] = m[2];
        }

        // private supportedLanguages: SupportedLanguage[] = [ { key: "typescript", ... }, ... ];
        const listKeys = {};
        for (const m of src.matchAll(/private\s+(\w+):\s*\w+\[\]\s*=\s*\[([\s\S]*?)\n {4}\];/g)) {
            listKeys[m[1]] = [...m[2].matchAll(/key:\s*"([^"]+)"/g)].map(k => k[1]);
        }

        const optionsByType = {};
        types.forEach(function (type) {
            const keys = listKeys[typeToList[type]];
            if (keys && keys.length > 0) {
                optionsByType[type] = keys;
            }
        });

        // Fail loudly here for the same reason the union parse does above: an
        // unresolved type leaves the option-key check with nothing to compare
        // against, so it quietly passes everything. A regex that stops matching
        // (a reformat moving the closing `];`, a renamed supported* list, a
        // restructured mapOptions switch) would otherwise disable half the guard.
        types.forEach(function (type) {
            if (!optionsByType[type]) {
                const listName = typeToList[type];
                const where = listName ? `(list: ${listName})` : "(no matching case in mapOptions)";
                throw new Error(
                    `Could not parse option keys for chooser type '${type}' ${where} from ${CHOOSER_COMPONENT_PATH}. ` +
                        `If the component was refactored, update parseChooserRegistry in this file to match.`,
                );
            }
        });

        cached = { types, optionsByType };
        return cached;
    };
})();

/**
 * Recursively collects markdown files under a directory, applying the same
 * exclusions as the front-matter walk (auto-generated reference and registry
 * pages, which are produced elsewhere).
 *
 * The chooser check needs its own walk rather than reusing searchForMarkdown's
 * file list, because that list omits pages the front-matter checks skip
 * (auto-generated, noindex, redirect passthroughs) -- and a chooser renders on
 * those pages just the same.
 *
 * @param {string} dir Absolute path to walk.
 * @returns {string[]} Absolute paths of the markdown files found.
 */
function listMarkdownFiles(dir) {
    const found = [];

    function walk(current) {
        let entries;
        try {
            entries = fs.readdirSync(current, { withFileTypes: true });
        } catch (e) {
            return;
        }
        entries.forEach(function (entry) {
            const full = path.join(current, entry.name);
            if (entry.isDirectory()) {
                walk(full);
            } else if (entry.name.endsWith(".md")) {
                if (full.indexOf("/content/docs/reference/pkg") > -1 || full.indexOf("/content/registry") > -1) {
                    return;
                }
                found.push(full);
            }
        });
    }

    walk(dir);
    return found;
}

/**
 * Validates every chooser/choosable shortcode call in the given markdown files.
 *
 * An unrecognized chooser type, or an option key the type doesn't define, fails
 * silently at runtime: the component matches no options, renders zero tabs, and
 * -- because a choosable only reveals itself when its value matches the current
 * selection -- hides all of the content it wraps. A page can therefore lose
 * every code block it has while still building, linting and rendering "fine".
 * That shipped once already (tf-tool, PR #20001, invisible for four weeks), so
 * it's a hard error here.
 *
 * @param {string[]} files Absolute paths of markdown files to check.
 * @returns {{path: string, errors: Object[]}[]} One error group per bad file.
 */
function checkChooserShortcodes(files) {
    const { types, optionsByType } = parseChooserRegistry();
    const groups = [];

    files.forEach(function (fullPath) {
        let content;
        try {
            content = fs.readFileSync(fullPath, "utf8");
        } catch (e) {
            return; // Unreadable files are surfaced by the front-matter checks.
        }

        if (content.indexOf("chooser") === -1 && content.indexOf("choosable") === -1) {
            return; // Fast path: the vast majority of files have neither.
        }

        const errors = [];

        for (const match of content.matchAll(CHOOSER_SHORTCODE_REGEX)) {
            const [full, shortcode, rawArgs] = match;
            const args = (rawArgs.match(/"[^"]*"|\S+/g) || []).map(a => a.replace(/^"|"$/g, ""));
            const lineNumber = content.slice(0, match.index).split("\n").length;

            const type = args[0];
            if (!type) {
                continue; // The shortcode itself errors on missing arguments.
            }

            if (!types.includes(type)) {
                errors.push({
                    lineNumber: lineNumber,
                    ruleDescription:
                        `Unknown chooser type '${type}' in ${shortcode} shortcode. Valid types are: ` +
                        `${types.join(", ")}. An unrecognized type renders no tabs AND hides all of the ` +
                        `content it wraps, so the page silently loses it. Either use a valid type or add ` +
                        `'${type}' to the chooser component (theme/stencil/src/components/chooser/chooser.tsx ` +
                        `plus the store slice in theme/stencil/src/store/)`,
                    errorDetail: full.trim(),
                });
                continue;
            }

            // The second positional argument is the option list (chooser) or the
            // value(s) to match (choosable). A third argument, if present, is the
            // mode, which the shortcodes validate themselves.
            const valid = optionsByType[type];
            if (!valid || !args[1]) {
                continue;
            }

            const unknown = args[1]
                .split(",")
                .map(o => o.trim())
                .filter(o => o.length > 0 && !valid.includes(o) && !CHOOSER_OPTION_ALIASES.includes(o));

            if (unknown.length > 0) {
                errors.push({
                    lineNumber: lineNumber,
                    ruleDescription:
                        `Unknown '${type}' option${unknown.length > 1 ? "s" : ""} ${unknown.map(o => `'${o}'`).join(", ")} ` +
                        `in ${shortcode} shortcode. Valid options for '${type}' are: ${valid.join(", ")}. ` +
                        `An unrecognized option is silently dropped, which can leave the chooser with no ` +
                        `tabs and its content hidden`,
                    errorDetail: full.trim(),
                });
            }
        }

        if (errors.length > 0) {
            groups.push({ path: fullPath, errors: errors });
        }
    });

    return groups;
}

/**
 * Builds an array of markdown files to lint and checks each file's front matter
 * for formatting errors.
 *
 * @param {string[]} paths An array of paths to search for markdown files.
 * @param {Object} [result] The result object returned after finishing searching.
 * @returns {Object} The markdown file paths to search and an error object for the files front matter.
 */
function searchForMarkdown(paths) {
    var result = {
        files: [], // list of file paths
        frontMatter: {}, // file path => { error: string } | { title: string, metaDescription: string }
    };

    while (paths.length > 0) {
        // Grab the first file in the list and generate
        // its full path.
        const file = paths.shift();
        const fullPath = path.resolve(__dirname, file);

        // Check if the path is a directory
        const isDirectory = fs.statSync(fullPath).isDirectory();

        // Get the file suffix so we can grab the markdown files.
        const fileParts = file.split(".");
        const fileSuffix = fileParts[fileParts.length - 1];

        // Ignore auto generated docs and registry pages (handled in the registry repo).
        if (file.indexOf("/content/docs/reference/pkg") > -1 || file.indexOf("/content/registry") > -1) {
            continue;
        }

        // If the path is a directory we want to add the contents of the directory
        // to the list.
        if (isDirectory) {
            fs.readdirSync(fullPath).forEach(function (file) {
                paths.push(fullPath + "/" + file);
            });
            continue;
        }

        // Else check if the file suffix is a markdown
        // and add it the resulting file list.
        if (fileSuffix !== "md") {
            continue;
        }

        try {
            // Read the file contents so we can grab the file header.
            const content = fs.readFileSync(fullPath, "utf8");

            // Grab the file header.
            const frontMatter = content.match(FRONT_MATTER_REGEX);

            // Remove the dash blocks around the file header.
            const fContent = frontMatter[0].split("---").join("");

            // Read the yaml.
            const obj = yaml.load(fContent);

            // If the page is auto generated, a redirect, or not indexed do not parse the front matter.
            const autoGenerated = obj.no_edit_this_page === true || content.match(AUTO_GENERATED_HEADING_REGEX);
            const redirectPassthrough = typeof obj.redirect_to === "string";
            const noIndex = obj.block_external_search_index === true;
            const allowLongTitle = !!obj.allow_long_title;

            // Use behavior switch to control front matter validation logic
            const shouldCheckFrontMatter = USE_NEW_FRONTMATTER_VALIDATION
                ? (!autoGenerated && !redirectPassthrough && !noIndex) // New behavior: always check front matter
                : (!autoGenerated && !redirectPassthrough && !noIndex && !allowLongTitle); // Old behavior: skip if allowLongTitle

            if (shouldCheckFrontMatter) {
                // Build the front matter error object and add the file path.
                result.frontMatter[fullPath] = {
                    error: null,
                    title: checkPageTitle(obj.title, allowLongTitle),
                    metaDescription: checkPageMetaDescription(obj.meta_desc),
                    metaImage: checkMetaImage(obj.meta_image),
                    featureImageDimensions: checkFeatureImageDimensions(obj.feature_image, fullPath),
                    featureImageBackground: checkFeatureImageBackground(obj.feature_image, fullPath),
                    featureImageSoftware: checkFeatureImageSoftware(obj.feature_image, fullPath),
                    featureImageC2pa: checkFeatureImageC2pa(obj.feature_image, fullPath),
                    blogCategory: checkBlogCategory(obj.category, obj.categories, fullPath),
                    caseStudyIndustry: checkCaseStudyIndustry(obj.industry, fullPath),
                    caseStudyLogoTile: checkCaseStudyLogoTile(obj, fullPath),
                    seriesConsistency: checkSeriesConsistency(obj.series, obj.tags, fullPath),
                    eventSessions: checkEventSessions(obj, fullPath),
                    changelogFilename: checkChangelogFilename(obj.date, fullPath),
                    changelogEditions: checkChangelogEditions(obj.editions, obj.tiers, obj.tier, fullPath),
                    pulumiCloudFeature: checkPulumiCloudFeature(obj.pulumi_cloud_feature, obj.pulumi_cloud),
                    pulumiCloudShortcode: checkPulumiCloudShortcode(content),
                };
                result.files.push(fullPath);
            }
        } catch (e) {
            // Include the error message in the front matter error object
            // so we can display it to the user.
            result.frontMatter[fullPath] = {
                error: e.message,
            };
            result.files.push(fullPath);
        }
    }
    return result;
}

/**
 * Builds an array of markdown files to search through from a
 * given path.
 *
 * @param {string} parentPath The path to search for markdown files
 */
function getMarkdownFiles(parentPath) {
    const fullParentPath = path.resolve(__dirname, parentPath);
    const dirs = fs.readdirSync(fullParentPath).map(function (dir) {
        return path.join(parentPath, dir);
    });

    return searchForMarkdown(dirs);
}

/**
 * Finds the appropriate .markdownlint.json config file for a given file path
 * by walking up the directory tree.
 *
 * @param {string} filePath The absolute path to the markdown file
 * @returns {Object} The configuration object for this file
 */
function getConfigForFile(filePath) {
    const baseConfigPath = path.resolve(__dirname, "../../.markdownlint-base.json");
    let currentDir = path.dirname(filePath);
    const rootDir = path.resolve(__dirname, "../..");

    // Walk up the directory tree looking for .markdownlint.json
    while (currentDir.startsWith(rootDir)) {
        const configPath = path.join(currentDir, ".markdownlint.json");

        if (fs.existsSync(configPath)) {
            try {
                return readConfig(configPath);
            } catch (e) {
                console.warn(`Warning: Failed to read config at ${configPath}: ${e.message}`);
            }
        }

        // Move up one directory
        const parentDir = path.dirname(currentDir);
        if (parentDir === currentDir) {
            break;
        }
        currentDir = parentDir;
    }

    // Fallback to base config
    if (fs.existsSync(baseConfigPath)) {
        return readConfig(baseConfigPath);
    }

    // If no config files exist, return null (will use default hardcoded config)
    return null;
}

/**
 * Groups the result of linting a file for markdown errors.
 *
 * @param {Object} result Results of lint errors. See: https://github.com/DavidAnson/markdownlint#usage
 * @return {Object} An object containing the file path and lint errors.
 * @return {string} result.path The full path of the linted file.
 * @return {Object[]} result.errors An array of error objects. Same as the result param.
 */
function groupLintErrorOutput(result) {
    // Grab the keys of the result object.
    const keys = Object.keys(result);

    // Map over the key array so we can combine front matter errors
    // with the markdown lint errors.
    const combinedErrors = keys.map(function (key) {
        // Get the lint and front matter errors.
        const lintErrors = result[key];
        const frontMatterErrors = filesToLint.frontMatter[key];

        // If the front matter error check threw an error add it to the lint
        // error array. Else add title and meta descriptoins if they exist.
        if (frontMatterErrors.error) {
            lintErrors.push({
                lineNumber: "File Header",
                ruleDescription: frontMatterErrors.error,
            });
        } else {
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
            if (frontMatterErrors.metaImage) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.metaImage,
                });
            }
            if (frontMatterErrors.featureImageDimensions) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.featureImageDimensions,
                });
            }
            if (frontMatterErrors.featureImageBackground) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.featureImageBackground,
                });
            }
            if (frontMatterErrors.featureImageSoftware) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.featureImageSoftware,
                });
            }
            if (frontMatterErrors.featureImageC2pa) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.featureImageC2pa,
                });
            }
            if (frontMatterErrors.blogCategory) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.blogCategory,
                });
            }
            if (frontMatterErrors.caseStudyIndustry) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.caseStudyIndustry,
                });
            }
            if (frontMatterErrors.caseStudyLogoTile) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.caseStudyLogoTile,
                });
            }
            if (frontMatterErrors.seriesConsistency) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.seriesConsistency,
                });
            }
            if (frontMatterErrors.eventSessions) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.eventSessions,
                });
            }
            if (frontMatterErrors.changelogFilename) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.changelogFilename,
                });
            }
            if (frontMatterErrors.changelogEditions) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.changelogEditions,
                });
            }
            if (frontMatterErrors.pulumiCloudFeature) {
                lintErrors.push({
                    lineNumber: "File Header",
                    ruleDescription: frontMatterErrors.pulumiCloudFeature,
                });
            }
            if (frontMatterErrors.pulumiCloudShortcode) {
                lintErrors.push({
                    lineNumber: "Body",
                    ruleDescription: frontMatterErrors.pulumiCloudShortcode,
                });
            }
        }

        if (lintErrors.length > 0) {
            return { path: key, errors: lintErrors };
        }
        return null;
    });

    // Filter out all null values from the combined result array.
    const filteredErrors = combinedErrors.filter(function (err) {
        return err !== null;
    });
    return filteredErrors;
}

// Get files from command line arguments (for lint-staged) or scan all files (for CI)
const filesFromArgs = process.argv.slice(2).filter(arg => !arg.startsWith('--'));
let filesToLint;

if (filesFromArgs.length > 0) {
    // When specific files are provided (from lint-staged), process only those files
    filesToLint = searchForMarkdown(filesFromArgs.map(f => path.resolve(process.cwd(), f)));
} else {
    // When no files are provided, scan all markdown files (CI behavior)
    filesToLint = getMarkdownFiles(`../../content`);
}

/**
 * Custom rule for checking Hugo relrefs
 */
const customRules = [
    {
        names: ["relref"],
        description: "Hugo relrefs are no longer supported. Use standard [Markdown](/links) instead",
        tags: ["hugo-relref"],
        function: (params, onError) => {
            params.tokens
                .filter(token => {
                    return token.type === "inline";
                })
                .forEach(inline => {
                    const line = inline.content;
                    if (line.match(/{{<[ ]?relref ".+"[ ]?>}}/)) {
                        onError({
                            lineNumber: inline.lineNumber,
                        });
                    }
                });
        },
    },
];

// Lint markdown files with per-directory configs
// Group files by their config to minimize repeated linting calls
const filesByConfig = {};

filesToLint.files.forEach(file => {
    const config = getConfigForFile(file);
    const configKey = JSON.stringify(config);

    if (!filesByConfig[configKey]) {
        filesByConfig[configKey] = {
            config: config,
            files: []
        };
    }

    filesByConfig[configKey].files.push(file);
});

// Lint each group of files with their shared config
let result = {};

Object.values(filesByConfig).forEach(group => {
    const opts = {
        files: group.files,
        markdownItFactory: () => markdownIt(),
        config: group.config,
        customRules: customRules,
    };

    const groupResult = markdownlint(opts);

    // Merge results
    result = { ...result, ...groupResult };
});

// Group the lint errors by file.
const errors = groupLintErrorOutput(result);

// Changelog assets (images/videos) aren't markdown, so the walk above never
// sees them. Enforce their date-prefix naming during the full CI scan; skip it
// when linting an explicit file list (lint-staged) to avoid surfacing errors
// for files the caller didn't touch.
if (filesFromArgs.length === 0) {
    checkChangelogAssets().forEach(function (assetError) {
        errors.push(assetError);
    });
}

// Feature ids in data/pulumi_pricing.yaml are global, so a duplicate is one
// finding about the data file, not a finding about every page that happens to
// reference it. Report it once per run. (Hugo raises the same error at build
// time; this just surfaces it seconds earlier.)
//
// A file that doesn't parse at all is the same kind of finding, and it comes
// first: the marker and changelog-edition checks read this file, so they stand
// down (returning null) until it loads. Reporting it here is what keeps a merge
// conflict marker from blaming every page in the repo.
const pricingDataErrors = PRICING.loadError
    ? [
        {
            lineNumber: "Data",
            ruleDescription: `Could not load data/pulumi_pricing.yaml: ${PRICING.loadError}. Every Pulumi Cloud marker and changelog \`editions:\` check reads this file, so they were skipped for this run — fix the file and lint again.`,
        },
    ]
    : PRICING.duplicates
        .map(function (id) {
            return {
                lineNumber: "Data",
                ruleDescription: `Duplicate feature id '${id}'. Ids are unique across every category — prefix the newer one with its product (for example 'esc-${id}').`,
            };
        })
        .concat(
            PRICING.yamlBooleans.map(function (b) {
                return {
                    lineNumber: b.line,
                    ruleDescription: `'${b.text}' — YAML 1.1 parses '${b.value}' as a boolean, so this cell becomes ${/^(y|yes|on)$/i.test(b.value) ? "true" : "false"} and renders as a ${/^(y|yes|on)$/i.test(b.value) ? "check mark" : "dash"}, not the word. Quote it ("${b.value}") if you meant the text, or write true/false if you meant the boolean.`,
                };
            })
        );
if (pricingDataErrors.length > 0) {
    errors.push({ path: "data/pulumi_pricing.yaml", errors: pricingDataErrors });
}

// Chooser/choosable shortcode calls live in the body rather than the front
// matter, so they get their own pass over the same scope the caller asked for.
const chooserScope =
    filesFromArgs.length > 0
        ? filesFromArgs.map(f => path.resolve(process.cwd(), f)).filter(f => f.endsWith(".md"))
        : listMarkdownFiles(path.resolve(__dirname, "../../content"));

checkChooserShortcodes(chooserScope).forEach(function (chooserError) {
    errors.push(chooserError);
});

// Get the total number of errors.
const errorsArray = errors.map(function (err) {
    return err.errors;
});
const errorsCount = [].concat.apply([], errorsArray).length;

// Create the error output string.
const errorOutput = errors
    .map(function (err) {
        let msg = err.path + ":\n";
        for (let i = 0; i < err.errors.length; i++) {
            const error = err.errors[i];
            msg += "Line " + error.lineNumber + ": " + error.ruleDescription;
            msg += error.errorDetail ? " [" + error.errorDetail + "].\n" : ".\n";
        }
        return msg;
    })
    .join("\n");

// If there are errors output the error string and exit
// the program with an error.
if (errors.length > 0) {
    console.log(`
Markdown Lint Results:
    - ${filesToLint.files.length} files parsed.
    - ${errorsCount} errors found.

Errors:

${errorOutput}
    `);

    const noError = process.argv.indexOf("--no-error") > -1;
    process.exit(noError ? 0 : 1);
}

console.log(`
Markdown Lint Results:
    - ${filesToLint.files.length} files parsed.
    - ${errorsCount} errors found.
`);
process.exit(0);
