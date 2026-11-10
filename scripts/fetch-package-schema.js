#!/usr/bin/env node
// Generates the Pulumi package schema reference at
// /docs/iac/guides/building-extending/packages/schema/ from the upstream sources that
// actually define the schema, and writes it to data/package_schema/*.json -- the source
// of truth for layouts/shortcodes/package-schema.html.
//
// There are two kinds of source, because the schema has two kinds of author:
//
//   core       pkg/codegen/schema/pulumi.json in pulumi/pulumi. This is the Pulumi
//              Package Metaschema: a JSON Schema document that is //go:embed-ed into
//              every pulumi binary and validated against verbatim by `pulumi schema
//              check`. If it disagrees with this page, the page is wrong.
//
//   language   the *PackageInfo / *PropertyInfo / *ResourceInfo / *ObjectInfo Go structs
//              each language's code generator unmarshals its slice of the schema's
//              `language` map into. The metaschema has its own *LanguageSpec $defs, but
//              they are a stale subset -- its goLanguageSpec lists four properties where
//              GoPackageInfo has fifteen -- so the structs are what we read.
//
// Those sources live in three repos that release on their own cadences, so this script
// runs once per repo and writes only that repo's files:
//
//   node scripts/fetch-package-schema.js --repo pulumi        --version 3.261.0
//   node scripts/fetch-package-schema.js --repo pulumi-dotnet --version 3.0.0
//   node scripts/fetch-package-schema.js --repo pulumi-java   --version 1.11.0
//
// Each invocation is driven by a GitHub workflow of its own, fired by that repo's
// release (.github/workflows/package-schema-docs{,-dotnet,-java}.yml). Files are fetched
// one at a time from raw.githubusercontent.com at the release tag: no checkout, no Go
// toolchain, no auth. That means this script needs only network access, so unlike
// scripts/fetch-esc-schemas.sh it is safe to run locally without a token -- but it is
// still not part of `make ensure`, because the committed output is what the site builds
// from and a build should never depend on GitHub being reachable.
//
// What gets documented, what each type is called, and which anchor it gets are editorial
// decisions, and they live in data/package_schema_overrides.yaml. Read that file's header
// before changing anything here.

const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const OVERRIDES = path.join(ROOT, "data", "package_schema_overrides.yaml");
const OUTPUT_DIR = path.join(ROOT, "data", "package_schema");
const RAW = "https://raw.githubusercontent.com";

// Where each documented thing comes from. Structural, not editorial: adding a language
// or moving an upstream file is a change here; renaming a section or rewording a
// description is a change in data/package_schema_overrides.yaml.
//
// `schemaKey` is the key the language occupies in a schema's `language` map, which is
// what a package author actually types. `choosable` is the value the page's language
// chooser switches on -- deliberately "typescript" rather than "javascript,typescript",
// since the site does not offer JavaScript as a docs tab.
const REPOS = {
    pulumi: {
        metaschema: { file: "pkg/codegen/schema/pulumi.json", output: "core" },
        languages: [
            {
                id: "typescript",
                label: "TypeScript",
                schemaKey: "nodejs",
                choosable: "typescript",
                structs: {
                    packagelanguage: { file: "pkg/codegen/nodejs/importer.go", struct: "NodePackageInfo" },
                    objecttypelanguage: { file: "pkg/codegen/nodejs/importer.go", struct: "NodeObjectInfo" },
                },
            },
            {
                id: "python",
                label: "Python",
                schemaKey: "python",
                choosable: "python",
                structs: {
                    packagelanguage: { file: "pkg/codegen/python/importer.go", struct: "PackageInfo" },
                    propertylanguage: { file: "pkg/codegen/python/importer.go", struct: "PropertyInfo" },
                },
            },
            {
                id: "go",
                label: "Go",
                schemaKey: "go",
                choosable: "go",
                structs: {
                    packagelanguage: { file: "pkg/codegen/go/importer.go", struct: "GoPackageInfo" },
                },
            },
        ],
    },
    "pulumi-dotnet": {
        languages: [
            {
                id: "csharp",
                label: "C#",
                schemaKey: "csharp",
                choosable: "csharp",
                structs: {
                    packagelanguage: {
                        file: "pulumi-language-dotnet/codegen/importer.go",
                        struct: "CSharpPackageInfo",
                    },
                    propertylanguage: {
                        file: "pulumi-language-dotnet/codegen/importer.go",
                        struct: "CSharpPropertyInfo",
                    },
                    resourcelanguage: {
                        file: "pulumi-language-dotnet/codegen/importer.go",
                        struct: "CSharpResourceInfo",
                    },
                },
            },
        ],
    },
    "pulumi-java": {
        languages: [
            {
                id: "java",
                label: "Java",
                schemaKey: "java",
                choosable: "java",
                structs: {
                    packagelanguage: { file: "pkg/codegen/java/package_info.go", struct: "PackageInfo" },
                    propertylanguage: { file: "pkg/codegen/java/importer.go", struct: "PropertyInfo" },
                },
            },
        ],
    },
};

// A struct that parses to fewer properties than this almost certainly means the scanner
// lost its place rather than that upstream deleted everything. Cheap insurance against a
// silently gutted reference page; raise a floor if a struct legitimately grows past it.
const MIN_PROPERTIES = 1;

class SchemaDocsError extends Error {}

function fail(message) {
    throw new SchemaDocsError(message);
}

// ---------------------------------------------------------------------------
// JSON pointers
// ---------------------------------------------------------------------------

// Resolve a JSON pointer, with one extension: a segment written `title:<value>` selects
// the member of an array whose `title` equals <value>. The metaschema hides two
// documented types inside `oneOf` lists (Discriminator inside typeSpec's Union Type
// branch), and addressing those by array index would silently point at the wrong branch
// the day upstream reorders the list.
function resolvePointer(root, pointer) {
    if (!pointer.startsWith("#")) {
        fail(`pointer "${pointer}" must start with "#"`);
    }

    let node = root;
    const segments = pointer
        .slice(1)
        .split("/")
        .filter(s => s.length > 0)
        .map(s => s.replace(/~1/g, "/").replace(/~0/g, "~"));

    for (const [i, segment] of segments.entries()) {
        const here = `#/${segments.slice(0, i + 1).join("/")}`;

        if (segment.startsWith("title:")) {
            const wanted = segment.slice("title:".length);
            if (!Array.isArray(node)) {
                fail(`pointer "${pointer}": "${segment}" selects by title, but ${here} is not an array`);
            }
            const found = node.find(member => member && member.title === wanted);
            if (!found) {
                const titles = node.map(m => (m && m.title) || "(untitled)").join(", ");
                fail(`pointer "${pointer}": no member titled "${wanted}" (found: ${titles})`);
            }
            node = found;
            continue;
        }

        if (node === null || typeof node !== "object" || !(segment in node)) {
            fail(`pointer "${pointer}" does not resolve: nothing at ${here}`);
        }
        node = node[segment];
    }

    return node;
}

// ---------------------------------------------------------------------------
// Metaschema -> documented types
// ---------------------------------------------------------------------------

// JSON Schema's primitive names are already the names the docs use, so the display type
// of a primitive is the primitive.
const PRIMITIVES = new Set(["boolean", "integer", "number", "string", "null"]);

// The metaschema's descriptions are written for readers, but a handful still open in Go's
// doc-comment voice ("PropertyName is the name of the property...") because they were
// copied across from schema.go, and their line wrapping is an artifact of the JSON file
// rather than intended structure.
function normalizeDescription(text, propertyName) {
    let out = String(text || "")
        .split(/\n{2,}/)
        .map(paragraph => paragraph.replace(/\s+/g, " ").trim())
        .filter(Boolean)
        .join("\n\n");

    out = dropLeadingIdentifier(out, propertyName);
    if (out && !/[.!?)]$/.test(out)) {
        out += ".";
    }
    return out;
}

// Go's doc-comment convention is to open with the identifier ("PropertyName is the name
// of..."), and both the Go structs and a handful of metaschema descriptions copied from
// them do it. In a reference row it reads as a leak from the source -- which is exactly
// what the hand-written version of this page was criticized for -- and the row is already
// labelled with the name. So drop it, along with the copula it was the subject of.
function dropLeadingIdentifier(text, name) {
    if (!name || !new RegExp(`^${name}\\s`, "i").test(text)) {
        return text;
    }
    let out = text.slice(name.length + 1).replace(/^(?:is|are|was|were)\s+/i, "");
    return out.charAt(0).toUpperCase() + out.slice(1);
}

// A `$ref`, an `items`, or an `additionalProperties` may point at something this page
// documents as a type of its own, in which case the row should link to it rather than
// flatten it to "object". Documented types are addressed by JSON pointer, not by `$ref`:
// most of them (Alias, EnumValue, Default, Metadata) are inline sub-schemas the
// metaschema never gave a `$defs` entry, so a pointer is the only handle they have.
// Omitting an absent href rather than setting it undefined keeps the committed JSON free
// of keys that mean nothing, so a diff only ever shows a real change.
function typeRef(text, href) {
    return href ? { text, href } : { text };
}

function describeType(node, pointer, index, root, seen) {
    const declared = index.get(pointer);
    if (declared) {
        return { text: declared.title, href: `#${declared.id}` };
    }

    if (node === true || node === undefined || node === null) {
        return { text: "any" };
    }

    if (node.$ref) {
        const target = index.get(node.$ref);
        if (target) {
            return { text: target.title, href: `#${target.id}` };
        }
        // An undocumented $def (token, schemaStringMap): inline it rather than dangle a
        // link to a section that does not exist.
        if (seen.has(node.$ref)) {
            return { text: "any" };
        }
        seen.add(node.$ref);
        return describeType(resolvePointer(root, node.$ref), node.$ref, index, root, seen);
    }

    // `allOf` at the property level is how the metaschema says "this is that type" when
    // it also wants to attach a description of its own.
    if (node.allOf && node.allOf.length === 1 && !node.properties) {
        return describeType(node.allOf[0], `${pointer}/allOf/0`, index, root, seen);
    }

    if (node.const !== undefined) {
        return { text: JSON.stringify(node.const) };
    }

    if (Array.isArray(node.type)) {
        return { text: node.type.join(" | ") };
    }

    if (node.type === "array") {
        const item = describeType(node.items, `${pointer}/items`, index, root, seen);
        return typeRef(`array[${item.text}]`, item.href);
    }

    if (node.type === "object") {
        if (node.additionalProperties && typeof node.additionalProperties === "object") {
            const value = describeType(
                node.additionalProperties,
                `${pointer}/additionalProperties`,
                index,
                root,
                seen,
            );
            return typeRef(`map[${value.text}]`, value.href);
        }
        return { text: "object" };
    }

    // A union of alternatives. When more than one alternative is a documented type, a
    // single href cannot express it, so the row carries the pieces and the template links
    // each one.
    const union = node.oneOf || node.anyOf;
    if (union) {
        const key = node.oneOf ? "oneOf" : "anyOf";
        const parts = union.map((member, i) =>
            describeType(member, `${pointer}/${key}/${i}`, index, root, seen),
        );
        const unique = [];
        for (const part of parts) {
            if (!unique.some(p => p.text === part.text)) {
                unique.push(part);
            }
        }
        const text = unique.map(p => p.text).join(" | ");
        if (unique.filter(p => p.href).length > 1) {
            return { text, parts: unique };
        }
        return typeRef(text, unique.length === 1 ? unique[0].href : undefined);
    }

    if (typeof node.type === "string" && PRIMITIVES.has(node.type)) {
        return { text: node.type };
    }

    return { text: "any" };
}

// A `oneOf` branch expresses "this property must not be present" as `false`. Those are
// constraints, not properties, and documenting them as rows would be nonsense.
function ownProperties(node) {
    const props = node.properties || {};
    return Object.entries(props).filter(([, schema]) => schema !== false && schema !== undefined);
}

function buildProperties(node, pointer, index, root, ctx) {
    const required = new Set(node.required || []);

    return ownProperties(node).map(([name, schema]) => {
        const key = `${ctx.typeId}.${name}`;
        ctx.seenKeys.add(key);

        const property = {
            name,
            type:
                ctx.typesDisplay[key] ||
                describeType(schema, `${pointer}/properties/${name}`, index, root, new Set()),
            required: required.has(name),
            description: ctx.descriptions[key]
                ? ctx.descriptions[key].trim()
                : normalizeDescription(schema.description, name),
        };

        // Enumerated values are the one JSON Schema constraint worth surfacing: they tell
        // an author what they are allowed to type. Patterns (the semver regex, for one)
        // are noise at this size.
        const values = schema.enum || (schema.items && schema.items.enum);
        if (values) {
            property.values = values.map(v => String(v));
        }

        return property;
    });
}

function buildInherits(node, index) {
    if (!node.allOf) {
        return [];
    }
    return node.allOf.map(member => {
        const declared = member.$ref && index.get(member.$ref);
        if (!declared) {
            fail(
                `a type composes ${JSON.stringify(member)} with allOf, but that is not a documented ` +
                    `type. Add it to core.types in data/package_schema_overrides.yaml.`,
            );
        }
        return { title: declared.title, href: `#${declared.id}` };
    });
}

function buildVariants(node, pointer, index, root, ctx) {
    if (!node.oneOf) {
        return [];
    }

    return node.oneOf.map((member, i) => {
        const declared = member.$ref && index.get(member.$ref);
        if (declared) {
            return { title: declared.title, ref: { text: declared.title, href: `#${declared.id}` } };
        }

        // Title-addressed, matching how data/package_schema_overrides.yaml points into
        // these branches, so both survive a reordering upstream.
        const here = member.title
            ? `${pointer}/oneOf/title:${member.title}`
            : `${pointer}/oneOf/${i}`;

        return {
            title: member.title || `Form ${i + 1}`,
            description: normalizeDescription(member.description),
            inherits: buildInherits(member, index),
            properties: buildProperties(member, here, index, root, ctx),
        };
    });
}

function buildCore(metaschema, overrides, source) {
    const declared = overrides.core && overrides.core.types;
    if (!Array.isArray(declared) || declared.length === 0) {
        fail("data/package_schema_overrides.yaml declares no core.types");
    }

    // Pointer -> {id, title}, built first so a property can link to a type declared later
    // in the list.
    const index = new Map();
    for (const entry of declared) {
        for (const field of ["pointer", "id", "title"]) {
            if (!entry[field]) {
                fail(`every core.types entry needs a "${field}": ${JSON.stringify(entry)}`);
            }
        }
        if (index.has(entry.pointer)) {
            fail(`core.types declares "${entry.pointer}" twice`);
        }
        index.set(entry.pointer, { id: entry.id, title: entry.title });
    }

    const descriptions = (overrides.core && overrides.core.descriptions) || {};
    const typesDisplay = (overrides.core && overrides.core.types_display) || {};
    const ctx = { descriptions, typesDisplay, seenKeys: new Set(), typeId: null };

    const types = declared.map(entry => {
        const node = resolvePointer(metaschema, entry.pointer);
        ctx.typeId = entry.id;

        return {
            id: entry.id,
            title: entry.title,
            description: entry.description
                ? entry.description.trim()
                : normalizeDescription(node.description),
            inherits: buildInherits(node, index),
            properties: buildProperties(node, entry.pointer, index, metaschema, ctx),
            variants: buildVariants(node, entry.pointer, index, metaschema, ctx),
        };
    });

    assertOverridesUsed("core", { descriptions, types_display: typesDisplay }, ctx.seenKeys);

    return { source, generated: today(), types };
}
// ---------------------------------------------------------------------------
// Go structs -> documented properties
// ---------------------------------------------------------------------------

const GO_TYPES = {
    string: "string",
    bool: "boolean",
    int: "integer",
    int32: "integer",
    int64: "integer",
    float64: "number",
    "[]string": "array[string]",
    "map[string]string": "map[string]",
    "map[string]bool": "map[boolean]",
    "map[string][]string": "map[array[string]]",
};

function describeGoType(goType) {
    if (GO_TYPES[goType]) {
        return { text: GO_TYPES[goType] };
    }
    if (goType.startsWith("[]")) {
        return { text: `array[${describeGoType(goType.slice(2)).text}]` };
    }
    const map = goType.match(/^map\[string\](.+)$/);
    if (map) {
        return { text: `map[${describeGoType(map[1]).text}]` };
    }
    if (goType.startsWith("*")) {
        return describeGoType(goType.slice(1));
    }
    return { text: "object" };
}

const LIST_ITEM = /^\s*(?:[-*]\s|\d+[.)]\s)/;

// Turn a Go doc comment into docs prose. Descriptions are rendered as Markdown, so a
// comment that lays out its allowed values as a dash list has to keep its line breaks
// (and gain the blank line Markdown needs before a list) rather than be flattened into
// one run-on sentence.
function toProse(lines, fieldName) {
    const out = [];
    let inList = false;

    for (const line of lines) {
        if (LIST_ITEM.test(line)) {
            out.push((inList ? "\n" : "\n\n") + line.trim());
            inList = true;
        } else if (out.length === 0) {
            out.push(line.trim());
        } else {
            out.push((inList ? "\n\n" : " ") + line.trim());
            inList = false;
        }
    }

    let text = dropLeadingIdentifier(out.join("").trim(), fieldName);

    if (text && !inList && !/[.!?)]$/.test(text)) {
        text += ".";
    }
    return text;
}
const GO_FIELD = /^\s*([A-Za-z_]\w*)\s+(\S+)\s+`([^`]*)`\s*(?:\/\/.*)?$/;
const GO_UNTAGGED_FIELD = /^\s*([A-Za-z_]\w*)\s+(\S+)\s*(?:\/\/.*)?$/;
const GO_INLINE_STRUCT = /^\s*([A-Za-z_]\w*)\s+struct\s*\{\s*$/;
const GO_COMMENT = /^\s*\/\/ ?(.*)$/;

// A deliberately strict scanner. It throws on any line inside the struct body it cannot
// classify rather than skipping it, so an upstream refactor fails the workflow loudly
// instead of quietly deleting rows from a published reference page.
function parseGoStruct(source, structName, where) {
    const lines = source.split("\n");
    const start = lines.findIndex(line => new RegExp(`^type ${structName} struct \\{\\s*$`).test(line));
    if (start === -1) {
        fail(`${where}: no "type ${structName} struct {" found. Did it move or get renamed upstream?`);
    }

    const properties = [];
    let doc = [];

    const emit = (fieldName, goType, tag) => {
        const pending = doc;
        doc = [];

        // An unexported field is never serialized, so it is not part of the schema an
        // author writes -- and neither is one tagged `json:"-"`. An exported field with no
        // tag at all is: encoding/json serializes it under its Go name.
        if (fieldName[0] !== fieldName[0].toUpperCase()) {
            return;
        }
        const json = tag === null ? null : tag.match(/json:"([^",]*)/);
        const name = tag === null ? fieldName : json && json[1];
        if (!name || name === "-") {
            return;
        }

        // Only the first paragraph: several of these comments continue into worked
        // examples and indented code, which belong in prose, not in a property row.
        const paragraph = [];
        for (const line of pending) {
            if (line.trim() === "") {
                break;
            }
            paragraph.push(line);
        }

        const deprecated = /^\s*deprecated:/i.test(paragraph[0] || "");
        if (deprecated) {
            paragraph[0] = paragraph[0].replace(/^\s*Deprecated:\s*/i, "");
        }

        properties.push({
            name,
            type: describeGoType(goType),
            required: tag === null || !tag.includes("omitempty"),
            description: toProse(paragraph, fieldName),
            deprecated,
        });
    };

    for (let i = start + 1; i < lines.length; i++) {
        const line = lines[i];

        if (/^\}\s*$/.test(line)) {
            if (properties.length < MIN_PROPERTIES) {
                fail(`${where}: ${structName} parsed to ${properties.length} properties, which cannot be right`);
            }
            return properties;
        }

        if (/^\s*$/.test(line)) {
            // A blank line breaks a Go doc comment's association with the field below it.
            doc = [];
            continue;
        }

        const comment = line.match(GO_COMMENT);
        if (comment) {
            doc.push(comment[1]);
            continue;
        }

        // An anonymous struct field spans several lines. Its inner shape is an
        // implementation detail of one language's importer rather than something an
        // author writes out, so it is documented as an object and skipped over.
        const inline = line.match(GO_INLINE_STRUCT);
        if (inline) {
            let depth = 1;
            let tag = null;
            let j = i;
            while (++j < lines.length) {
                if (/\{\s*$/.test(lines[j])) {
                    depth++;
                } else if (/^\s*\}/.test(lines[j]) && --depth === 0) {
                    const close = lines[j].match(/^\s*\}\s+`([^`]*)`\s*$/);
                    if (!close) {
                        fail(`${where}: anonymous struct ${inline[1]} in ${structName} has no JSON tag`);
                    }
                    tag = close[1];
                    break;
                }
            }
            if (tag === null) {
                fail(`${where}: anonymous struct ${inline[1]} in ${structName} is never closed`);
            }
            i = j;
            emit(inline[1], "struct", tag);
            continue;
        }

        const field = line.match(GO_FIELD);
        if (field) {
            emit(field[1], field[2], field[3]);
            continue;
        }

        const untagged = line.match(GO_UNTAGGED_FIELD);
        if (untagged) {
            emit(untagged[1], untagged[2], null);
            continue;
        }

        fail(`${where}: cannot parse line ${i + 1} of ${structName}: ${JSON.stringify(line)}`);
    }

    fail(`${where}: ${structName} has no closing brace`);
    return properties; // unreachable; keeps the return type honest
}

function buildLanguage(language, sources, overrides, source) {
    const spec = overrides.language || {};
    const descriptions = spec.descriptions || {};
    const excluded = new Set(spec.exclude || []);
    const seenKeys = new Set();

    const sections = {};
    for (const [sectionId, parsed] of Object.entries(sources)) {
        const properties = [];
        for (const property of parsed) {
            const key = `${sectionId}.${language.id}.${property.name}`;
            seenKeys.add(key);
            if (excluded.has(key)) {
                continue;
            }
            if (descriptions[key]) {
                property.description = descriptions[key].trim();
            }
            properties.push(property);
        }
        sections[sectionId] = { properties };
    }

    assertOverridesUsed(`language (${language.id})`, { descriptions, exclude: spec.exclude }, seenKeys, language.id);

    return {
        language: language.id,
        label: language.label,
        schemaKey: language.schemaKey,
        choosable: language.choosable,
        source,
        generated: today(),
        sections,
    };
}

// ---------------------------------------------------------------------------
// Guards
// ---------------------------------------------------------------------------

// The editorial layer is supposed to shrink as upstream fills its own gaps. An override
// that no longer matches anything is either a typo or a leftover, and both are worth a
// failed job: the first hides a description that never reaches the page, the second
// leaves us maintaining prose nobody reads.
function assertOverridesUsed(scope, overrides, seenKeys, languageFilter) {
    const stale = [];

    const applies = key => !languageFilter || key.split(".")[1] === languageFilter;

    for (const key of Object.keys(overrides.descriptions || {})) {
        if (applies(key) && !seenKeys.has(key)) {
            stale.push(`descriptions: ${key}`);
        }
    }
    for (const key of overrides.exclude || []) {
        if (applies(key) && !seenKeys.has(key)) {
            stale.push(`exclude: ${key}`);
        }
    }
    for (const key of Object.keys(overrides.types_display || {})) {
        if (!seenKeys.has(key)) {
            stale.push(`types_display: ${key}`);
        }
    }

    if (stale.length > 0) {
        fail(
            `these ${scope} overrides in data/package_schema_overrides.yaml no longer match anything ` +
                `upstream:\n  ${stale.join("\n  ")}\n` +
                `Either the property was renamed, or upstream now documents it and the override can go.`,
        );
    }
}

// ---------------------------------------------------------------------------
// Plumbing
// ---------------------------------------------------------------------------

function today() {
    return new Date().toISOString().slice(0, 10);
}

async function fetchFile(repo, version, file) {
    const url = `${RAW}/pulumi/${repo}/v${version}/${file}`;
    const response = await fetch(url);
    if (!response.ok) {
        fail(`GET ${url} returned ${response.status} ${response.statusText}`);
    }
    return response.text();
}

// Sorted keys and a trailing newline, so a release that changed nothing this page
// documents produces a byte-identical file and therefore no pull request.
function writeJson(name, value) {
    const stable = JSON.stringify(value, (_, v) => {
        if (v && typeof v === "object" && !Array.isArray(v)) {
            return Object.fromEntries(Object.keys(v).sort().map(k => [k, v[k]]));
        }
        return v;
    }, 2);

    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    const file = path.join(OUTPUT_DIR, `${name}.json`);
    fs.writeFileSync(file, stable + "\n");
    return path.relative(ROOT, file);
}

function parseArgs(argv) {
    const args = {};
    for (let i = 0; i < argv.length; i += 2) {
        if (!argv[i].startsWith("--") || argv[i + 1] === undefined) {
            fail(`usage: fetch-package-schema.js --repo <${Object.keys(REPOS).join("|")}> --version <x.y.z>`);
        }
        args[argv[i].slice(2)] = argv[i + 1];
    }
    return args;
}

async function main() {
    const args = parseArgs(process.argv.slice(2));
    const repo = args.repo;
    const version = (args.version || "").replace(/^v/, "");

    if (!REPOS[repo]) {
        fail(`unknown --repo "${repo}". Expected one of: ${Object.keys(REPOS).join(", ")}`);
    }
    if (!/^\d+\.\d+\.\d+/.test(version)) {
        fail(`--version must be a release version like 3.261.0, got "${args.version}"`);
    }

    const yaml = require("js-yaml");
    const overrides = yaml.load(fs.readFileSync(OVERRIDES, "utf8"));
    const config = REPOS[repo];
    const written = [];

    if (config.metaschema) {
        const file = config.metaschema.file;
        const raw = await fetchFile(repo, version, file);
        const source = {
            repo: `pulumi/${repo}`,
            path: file,
            version: `v${version}`,
            url: `https://github.com/pulumi/${repo}/blob/v${version}/${file}`,
        };
        written.push(writeJson(config.metaschema.output, buildCore(JSON.parse(raw), overrides, source)));
    }

    for (const language of config.languages || []) {
        const files = new Map();
        const sources = {};

        for (const [sectionId, spec] of Object.entries(language.structs)) {
            if (!files.has(spec.file)) {
                files.set(spec.file, await fetchFile(repo, version, spec.file));
            }
            sources[sectionId] = parseGoStruct(
                files.get(spec.file),
                spec.struct,
                `pulumi/${repo}@v${version} ${spec.file}`,
            );
        }

        const source = {
            repo: `pulumi/${repo}`,
            paths: [...files.keys()].sort(),
            version: `v${version}`,
            url: `https://github.com/pulumi/${repo}/tree/v${version}`,
        };
        written.push(writeJson(`language_${language.id}`, buildLanguage(language, sources, overrides, source)));
    }

    console.log(`Wrote ${written.length} file(s) from pulumi/${repo}@v${version}:`);
    written.forEach(f => console.log(`  ${f}`));
}

if (require.main === module) {
    main().catch(e => {
        console.error(e instanceof SchemaDocsError ? `error: ${e.message}` : e);
        process.exit(1);
    });
}

module.exports = {
    REPOS,
    SchemaDocsError,
    buildCore,
    buildLanguage,
    describeGoType,
    describeType,
    normalizeDescription,
    parseGoStruct,
    resolvePointer,
    toProse,
};
