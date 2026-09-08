// Unit tests for scripts/fetch-package-schema.js. Run with `make test-unit`.
//
// The two things worth testing here are the two things that fail silently in production:
// the JSON pointer/type resolution that decides whether a row links to another section or
// flattens to "object", and the Go struct scanner, whose job is to notice that it has lost
// its place rather than quietly drop properties off a published reference page.

const test = require("node:test");
const assert = require("node:assert");

const {
    SchemaDocsError,
    buildCore,
    buildLanguage,
    describeGoType,
    describeType,
    normalizeDescription,
    parseGoStruct,
    resolvePointer,
    toProse,
} = require("./fetch-package-schema.js");

const SOURCE = { repo: "pulumi/pulumi", path: "p.json", version: "v1.0.0", url: "https://example.invalid" };

// A miniature metaschema with the shapes that matter: a $defs entry, composition via
// allOf, a titled oneOf branch, and an inline sub-schema that only a pointer can name.
const METASCHEMA = {
    type: "object",
    required: ["name"],
    properties: {
        name: { description: "Name is the name of the thing", type: "string" },
        meta: {
            description: "Format metadata.",
            type: "object",
            properties: { moduleFormat: { description: "A regex.", type: "string" } },
        },
        resources: {
            description: "The resources.",
            type: "object",
            additionalProperties: { $ref: "#/$defs/resourceSpec" },
        },
        tags: { description: "Tags", type: "array", items: { $ref: "#/$defs/tagSpec" } },
    },
    $defs: {
        objectTypeSpec: {
            description: "Describes an object type",
            properties: { properties: { description: "The properties.", type: "object" } },
        },
        resourceSpec: {
            description: "Describes a resource.",
            allOf: [{ $ref: "#/$defs/objectTypeSpec" }],
            properties: {
                isComponent: { description: "Indicates whether it is a component.", type: "boolean" },
                mode: { description: "The mode.", type: "string", enum: ["a", "b"] },
            },
        },
        tagSpec: { type: "object", additionalProperties: { type: "string" } },
        typeSpec: {
            description: "A type reference.",
            properties: { plain: { description: "Plain is a marker.", type: "boolean" } },
            oneOf: [
                {
                    title: "Union Type",
                    description: "A union.",
                    properties: {
                        items: false,
                        discriminator: {
                            type: "object",
                            properties: {
                                propertyName: { description: "PropertyName is the name.", type: "string" },
                            },
                            required: ["propertyName"],
                        },
                    },
                },
            ],
        },
    },
};

const OVERRIDES = {
    core: {
        types: [
            { pointer: "#", id: "package", title: "Package" },
            { pointer: "#/properties/meta", id: "metadata", title: "Metadata" },
            { pointer: "#/$defs/objectTypeSpec", id: "objecttype", title: "ObjectType" },
            { pointer: "#/$defs/resourceSpec", id: "resource", title: "Resource" },
            { pointer: "#/$defs/typeSpec", id: "type", title: "Type" },
            {
                pointer: "#/$defs/typeSpec/oneOf/title:Union Type/properties/discriminator",
                id: "discriminator",
                title: "Discriminator",
            },
        ],
    },
};

const index = new Map([
    ["#/$defs/resourceSpec", { id: "resource", title: "Resource" }],
    ["#/properties/meta", { id: "metadata", title: "Metadata" }],
]);

const describe = (node, pointer = "#/x") => describeType(node, pointer, index, METASCHEMA, new Set());

test("describeType renders primitives as themselves", () => {
    assert.deepStrictEqual(describe({ type: "string" }), { text: "string" });
    assert.deepStrictEqual(describe({ type: "boolean" }), { text: "boolean" });
    assert.deepStrictEqual(describe({}), { text: "any" });
});

test("describeType links a $ref to a documented type", () => {
    assert.deepStrictEqual(describe({ $ref: "#/$defs/resourceSpec" }), {
        text: "Resource",
        href: "#resource",
    });
});

test("describeType inlines a $ref to an undocumented $def rather than dangling a link", () => {
    // tagSpec is a map of strings and has no section of its own, so a row that uses it
    // should say what it is instead of linking to nothing.
    assert.deepStrictEqual(describe({ $ref: "#/$defs/tagSpec" }), { text: "map[string]" });
});

test("describeType names arrays and maps after their element type", () => {
    assert.deepStrictEqual(describe({ type: "array", items: { $ref: "#/$defs/resourceSpec" } }), {
        text: "array[Resource]",
        href: "#resource",
    });
    assert.deepStrictEqual(
        describe({ type: "object", additionalProperties: { $ref: "#/$defs/resourceSpec" } }),
        { text: "map[Resource]", href: "#resource" },
    );
    assert.deepStrictEqual(describe({ type: "object", additionalProperties: { type: "string" } }), {
        text: "map[string]",
    });
});

test("describeType links an inline sub-schema addressed by pointer", () => {
    // The metaschema never gives `meta` a $defs entry, so its pointer is the only handle
    // the Metadata section has. Losing this is how #metadata would silently become
    // "object".
    assert.deepStrictEqual(describe(METASCHEMA.properties.meta, "#/properties/meta"), {
        text: "Metadata",
        href: "#metadata",
    });
});

test("describeType follows a single-member allOf", () => {
    assert.deepStrictEqual(describe({ type: "object", allOf: [{ $ref: "#/$defs/resourceSpec" }] }), {
        text: "Resource",
        href: "#resource",
    });
});

test("describeType keeps every link in a union of documented types", () => {
    const result = describe({
        anyOf: [{ $ref: "#/$defs/resourceSpec" }, { $ref: "#/properties/meta" }],
    });
    assert.strictEqual(result.text, "Resource | Metadata");
    assert.deepStrictEqual(
        result.parts.map(p => p.href),
        ["#resource", "#metadata"],
    );
});

test("describeType leaves a union of primitives unlinked", () => {
    const result = describe({ oneOf: [{ type: "string" }, { type: "boolean" }] });
    assert.strictEqual(result.text, "string | boolean");
    assert.strictEqual(result.parts, undefined);
});

test("resolvePointer selects a oneOf branch by title, not by position", () => {
    const node = resolvePointer(METASCHEMA, "#/$defs/typeSpec/oneOf/title:Union Type");
    assert.strictEqual(node.description, "A union.");
});

test("resolvePointer fails loudly on a pointer that no longer resolves", () => {
    assert.throws(() => resolvePointer(METASCHEMA, "#/$defs/gone"), SchemaDocsError);
    assert.throws(
        () => resolvePointer(METASCHEMA, "#/$defs/typeSpec/oneOf/title:Nope"),
        /no member titled "Nope"/,
    );
});

test("normalizeDescription drops the Go doc-comment opener", () => {
    assert.strictEqual(
        normalizeDescription("PropertyName is the name of the property", "propertyName"),
        "The name of the property.",
    );
    assert.strictEqual(normalizeDescription("Plain is a marker.", "plain"), "A marker.");
    // A description that merely starts with a similar word is left alone.
    assert.strictEqual(normalizeDescription("The type of the object", "type"), "The type of the object.");
});

test("buildCore produces linked, ordered types with inheritance and variants", () => {
    const core = buildCore(METASCHEMA, OVERRIDES, SOURCE);

    assert.deepStrictEqual(
        core.types.map(t => t.id),
        ["package", "metadata", "objecttype", "resource", "type", "discriminator"],
    );

    const pkg = core.types[0];
    assert.strictEqual(pkg.properties.find(p => p.name === "name").required, true);
    assert.strictEqual(pkg.properties.find(p => p.name === "meta").type.href, "#metadata");
    assert.strictEqual(pkg.properties.find(p => p.name === "resources").type.text, "map[Resource]");

    const resource = core.types.find(t => t.id === "resource");
    assert.deepStrictEqual(resource.inherits, [{ title: "ObjectType", href: "#objecttype" }]);
    // Inherited properties belong to the parent's section, not repeated here.
    assert.deepStrictEqual(
        resource.properties.map(p => p.name),
        ["isComponent", "mode"],
    );
    assert.deepStrictEqual(resource.properties.find(p => p.name === "mode").values, ["a", "b"]);

    const type = core.types.find(t => t.id === "type");
    assert.deepStrictEqual(
        type.variants.map(v => v.title),
        ["Union Type"],
    );
    // `items: false` is a constraint saying the property must be absent, not a property.
    assert.deepStrictEqual(
        type.variants[0].properties.map(p => p.name),
        ["discriminator"],
    );
});

test("buildCore rejects an override that no longer matches anything upstream", () => {
    const stale = {
        core: {
            ...OVERRIDES.core,
            descriptions: { "package.thisIsGone": "wishful thinking" },
        },
    };
    assert.throws(() => buildCore(METASCHEMA, stale, SOURCE), /package\.thisIsGone/);
});

test("buildCore rejects a duplicate pointer", () => {
    const dupe = { core: { types: [...OVERRIDES.core.types, OVERRIDES.core.types[0]] } };
    assert.throws(() => buildCore(METASCHEMA, dupe, SOURCE), /declares "#" twice/);
});

// ---------------------------------------------------------------------------
// Go struct scanner
// ---------------------------------------------------------------------------

const GO = `package nodejs

// NodePackageInfo holds stuff.
type NodePackageInfo struct {
	// Custom name for the NPM package.
	PackageName string \`json:"packageName,omitempty"\`
	// PackageDescription is the description for the NPM package.
	PackageDescription string \`json:"packageDescription,omitempty"\`
	// Deprecated: This flag no longer does anything.
	UsesIOClasses bool \`json:"usesIOClasses,omitempty"\`
	// Always written.
	Required []string \`json:"required"\`
	Internal string \`json:"-"\`
	compiled bool
	// If enabled, a pyproject.toml file will be generated.
	PyProject struct {
		Enabled bool \`json:"enabled,omitempty"\`
	} \`json:"pyproject,omitempty"\`
	// Specifies what types are used.
	// Allowed values are the following:
	// - "classes": Args classes only
	// - "classes-and-dicts": TypedDicts as well
	InputTypes string \`json:"inputTypes,omitempty"\`

	// This comment is detached from the field below it by a blank line, which is how Go
	// says the two are unrelated.

	Orphan string \`json:"orphan,omitempty"\`
}

func other() {}
`;

test("parseGoStruct reads names, types, and requiredness from the JSON tags", () => {
    const properties = parseGoStruct(GO, "NodePackageInfo", "test");
    const byName = Object.fromEntries(properties.map(p => [p.name, p]));

    assert.deepStrictEqual(
        properties.map(p => p.name),
        ["packageName", "packageDescription", "usesIOClasses", "required", "pyproject", "inputTypes", "orphan"],
    );
    assert.strictEqual(byName.packageName.type.text, "string");
    assert.strictEqual(byName.packageName.required, false);
    // No omitempty means the field is always serialized.
    assert.strictEqual(byName.required.required, true);
    assert.strictEqual(byName.required.type.text, "array[string]");
});

test("parseGoStruct skips fields that never reach the wire", () => {
    const names = parseGoStruct(GO, "NodePackageInfo", "test").map(p => p.name);
    assert.ok(!names.includes("Internal"), "json:\"-\" fields are not schema fields");
    assert.ok(!names.includes("compiled"), "unexported fields are not schema fields");
});

test("parseGoStruct documents an anonymous struct field as an object", () => {
    const pyproject = parseGoStruct(GO, "NodePackageInfo", "test").find(p => p.name === "pyproject");
    assert.strictEqual(pyproject.type.text, "object");
    assert.strictEqual(pyproject.description, "If enabled, a pyproject.toml file will be generated.");
});

test("parseGoStruct marks and unwraps a deprecated field", () => {
    const [, , usesIOClasses] = parseGoStruct(GO, "NodePackageInfo", "test");
    assert.strictEqual(usesIOClasses.deprecated, true);
    assert.strictEqual(usesIOClasses.description, "This flag no longer does anything.");
});

test("parseGoStruct honors the blank line that detaches a Go doc comment", () => {
    const orphan = parseGoStruct(GO, "NodePackageInfo", "test").find(p => p.name === "orphan");
    assert.strictEqual(orphan.description, "");
});

test("parseGoStruct throws rather than skip a line it cannot classify", () => {
    // The failure this guards against is silent: a scanner that shrugs at an unfamiliar
    // line drops real properties off a published page and nothing notices.
    const broken = "type X struct {\n\tSomething entirely unexpected here\n}\n";
    assert.throws(() => parseGoStruct(broken, "X", "test"), /cannot parse line 2 of X/);
});

test("parseGoStruct throws when the struct is gone", () => {
    assert.throws(() => parseGoStruct(GO, "RenamedUpstream", "test"), /no "type RenamedUpstream struct \{"/);
});

test("parseGoStruct throws when a struct yields no properties at all", () => {
    assert.throws(() => parseGoStruct("type X struct {\n}\n", "X", "test"), /cannot be right/);
});

test("toProse keeps a Markdown list instead of flattening it into a sentence", () => {
    const inputTypes = parseGoStruct(GO, "NodePackageInfo", "test").find(p => p.name === "inputTypes");
    assert.strictEqual(
        inputTypes.description,
        'Specifies what types are used. Allowed values are the following:\n\n' +
            '- "classes": Args classes only\n- "classes-and-dicts": TypedDicts as well',
    );
});

test("toProse drops the field's own name from the front of its comment", () => {
    assert.strictEqual(
        toProse(["PackageDescription is the description for the NPM package"], "PackageDescription"),
        "The description for the NPM package.",
    );
});

test("describeGoType maps Go types onto the schema's vocabulary", () => {
    assert.strictEqual(describeGoType("bool").text, "boolean");
    assert.strictEqual(describeGoType("int").text, "integer");
    assert.strictEqual(describeGoType("map[string]string").text, "map[string]");
    assert.strictEqual(describeGoType("[]string").text, "array[string]");
    assert.strictEqual(describeGoType("*string").text, "string");
    assert.strictEqual(describeGoType("someInternalType").text, "object");
});

// ---------------------------------------------------------------------------
// Language assembly
// ---------------------------------------------------------------------------

const LANGUAGE = { id: "go", label: "Go", schemaKey: "go", choosable: "go" };

test("buildLanguage applies description overrides and drops excluded properties", () => {
    const sources = { packagelanguage: parseGoStruct(GO, "NodePackageInfo", "test") };
    const overrides = {
        language: {
            descriptions: { "packagelanguage.go.orphan": "Prose upstream does not have." },
            exclude: ["packagelanguage.go.usesIOClasses"],
        },
    };

    const built = buildLanguage(LANGUAGE, sources, overrides, SOURCE);
    const names = built.sections.packagelanguage.properties.map(p => p.name);

    assert.ok(!names.includes("usesIOClasses"));
    assert.strictEqual(
        built.sections.packagelanguage.properties.find(p => p.name === "orphan").description,
        "Prose upstream does not have.",
    );
    assert.strictEqual(built.schemaKey, "go");
});

test("buildLanguage rejects an override aimed at a property that is gone", () => {
    const sources = { packagelanguage: parseGoStruct(GO, "NodePackageInfo", "test") };
    const overrides = { language: { exclude: ["packagelanguage.go.longSinceRenamed"] } };
    assert.throws(() => buildLanguage(LANGUAGE, sources, overrides, SOURCE), /longSinceRenamed/);
});

test("buildLanguage ignores overrides belonging to another language", () => {
    const sources = { packagelanguage: parseGoStruct(GO, "NodePackageInfo", "test") };
    const overrides = { language: { descriptions: { "packagelanguage.java.basePackage": "..." } } };
    assert.doesNotThrow(() => buildLanguage(LANGUAGE, sources, overrides, SOURCE));
});
