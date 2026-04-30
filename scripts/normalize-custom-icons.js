#!/usr/bin/env node
/**
 * Normalize Figma-exported custom icons from _inbox/ into assets/icons/custom/.
 *
 * Source: assets/icons/custom/_inbox/<FolderName>/Format=Outline, Weight=<X>.svg
 * Output: assets/icons/custom/<slug>.svg          (regular)
 *         assets/icons/custom/<slug>-bold.svg     (bold)
 *         assets/icons/custom/<slug>-duotone.svg  (duotone)
 *
 * Normalization applied to each SVG:
 *   - Remove width/height attributes from <svg>
 *   - Set fill="currentColor" on <svg>
 *   - Strip fill="#..." from individual <path> elements
 *   - Tag duotone secondary paths (opacity="0.2") with class="duotone-secondary"
 *   - Tag duotone primary paths with class="duotone-primary"
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const INBOX = path.join(ROOT, "assets/icons/custom/_inbox");
const OUT = path.join(ROOT, "assets/icons/custom");

// Folder-name → output slug mapping
const ICON_MAP = {
    PulumiNeo: "pulumi-neo",
    PulumiInfrastructureCode: "pulumi-iac",
    PulumiInsightsGovernance: "pulumi-insights",
    PulumiInternalDeveloperPlatform: "pulumi-idp",
    PulumiSecretsConfig: "pulumi-secrets",
};

// Weight → Figma filename suffix → output filename suffix
const WEIGHTS = [
    { figma: "Regular", suffix: "" },
    { figma: "Bold", suffix: "-bold" },
    { figma: "Fill", suffix: "-fill" },
    { figma: "Duotone", suffix: "-duotone" },
];

function normalizeSvg(content, isDuotone) {
    // Remove XML declaration if present
    content = content.replace(/<\?xml[^?]*\?>\s*/g, "");

    // Strip width and height from the <svg> opening tag
    content = content.replace(/<svg([^>]*)>/, (_, attrs) => {
        attrs = attrs.replace(/\s+width="[^"]*"/, "");
        attrs = attrs.replace(/\s+height="[^"]*"/, "");
        // Replace fill="none" (or any fill value) on svg with fill="currentColor"
        if (/\bfill=/.test(attrs)) {
            attrs = attrs.replace(/\bfill="[^"]*"/, 'fill="currentColor"');
        } else {
            attrs += ' fill="currentColor"';
        }
        return `<svg${attrs}>`;
    });

    if (isDuotone) {
        // Tag secondary (opacity="0.2") paths
        content = content.replace(
            /<path([^>]*)\bopacity="0\.2"([^>]*)>/g,
            (match, before, after) => {
                const attrs = (before + after)
                    .replace(/\bfill="[^"]*"/g, "")
                    .replace(/\bstroke="[^"]*"/g, "")
                    .trim();
                return `<path class="duotone-secondary" ${attrs}>`;
            }
        );
        // Tag primary paths (those without opacity="0.2")
        content = content.replace(
            /<path(?![^>]*\bclass=)([^>]*)>/g,
            (match, attrs) => {
                const cleaned = attrs
                    .replace(/\bfill="[^"]*"/g, "")
                    .replace(/\bstroke="[^"]*"/g, "")
                    .trim();
                return `<path class="duotone-primary" ${cleaned}>`;
            }
        );
    } else {
        // Regular / bold: just strip hard-coded fill/stroke on paths
        content = content.replace(
            /<path([^>]*)>/g,
            (match, attrs) => {
                const cleaned = attrs
                    .replace(/\bfill="[^"]*"/g, "")
                    .replace(/\bstroke="[^"]*"/g, "")
                    .trim();
                return `<path ${cleaned}>`;
            }
        );
    }

    // Collapse any double spaces introduced by replacements
    content = content.replace(/ {2,}/g, " ");
    // Ensure trailing newline
    return content.trimEnd() + "\n";
}

let written = 0;
let errors = 0;

for (const [folder, slug] of Object.entries(ICON_MAP)) {
    const srcDir = path.join(INBOX, folder);
    if (!fs.existsSync(srcDir)) {
        console.error(`MISSING: ${srcDir}`);
        errors++;
        continue;
    }

    for (const { figma, suffix } of WEIGHTS) {
        const srcFile = path.join(srcDir, `Format=Outline, Weight=${figma}.svg`);
        if (!fs.existsSync(srcFile)) {
            console.error(`MISSING: ${srcFile}`);
            errors++;
            continue;
        }

        const raw = fs.readFileSync(srcFile, "utf8");
        const normalized = normalizeSvg(raw, figma === "Duotone");
        const outFile = path.join(OUT, `${slug}${suffix}.svg`);
        fs.writeFileSync(outFile, normalized);
        console.log(`  wrote  ${path.relative(ROOT, outFile)}`);
        written++;
    }
}

console.log(`\n${written} files written, ${errors} errors.`);
if (errors > 0) process.exit(1);
