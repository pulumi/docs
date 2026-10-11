// NOTE: These tests do not run in CI. `make test` only runs the example-program tests,
// and the pull-request workflow never invokes `stencil test`. Run them by hand when
// touching this component or the store:
//
//     cd theme/stencil && yarn install
//     npx stencil test --e2e -- src/components/choosable/choosable.e2e.ts
//
import { newE2EPage } from "@stencil/core/testing";

describe("pulumi-choosable", () => {
    it("renders", async () => {
        const page = await newE2EPage();
        await page.setContent("<pulumi-choosable></pulumi-choosable>");

        const element = await page.find("pulumi-choosable");
        expect(element).toHaveClass("hydrated");
    });

    // The block shortcode wraps each choosable in a bare <div>; a "toggle set" is a run
    // of those adjacent wrapper divs. These helpers build that structure and read back
    // which choosables ended up active (their rendered inner <div> carries .active).
    const setOf = (langs: string[], selection: string) =>
        langs.map(l => `<div><pulumi-choosable type="language" values="${l}" selection="${selection}"></pulumi-choosable></div>`).join("\n");

    const activeLangs = async (page): Promise<string[]> => {
        const choosables = await page.findAll("pulumi-choosable");
        const active: string[] = [];
        for (const c of choosables) {
            const inner = await c.find("div");
            if (inner && (await inner.getAttribute("class"))?.includes("active")) {
                active.push(await c.getAttribute("values"));
            }
        }
        return active;
    };

    it("shows the matching choosable when the selection is offered", async () => {
        const page = await newE2EPage();
        await page.setContent(setOf(["typescript", "python", "go"], "python"));
        expect(await activeLangs(page)).toEqual(["python"]);
    });

    it("falls back to the first member when the selection is not offered (headless HCL)", async () => {
        const page = await newE2EPage();
        await page.setContent(setOf(["typescript", "python", "go"], "hcl"));
        // HCL is offered by none of the three, so the first (typescript) shows itself
        // instead of the reader seeing an empty gap.
        expect(await activeLangs(page)).toEqual(["typescript"]);
    });

    it("does not fall back for a group that deliberately omits a language the page offers elsewhere", async () => {
        const page = await newE2EPage();
        // Mirrors apply.md: a run of per-language asides with no Java member, on a page
        // that serves Java readers elsewhere. The partial group must stay hidden -- blank
        // is correct -- rather than show a Java reader its TypeScript member.
        await page.setContent(
            setOf(["typescript", "python", "go", "csharp"], "java") +
                `<h2>A heading breaks the run</h2>` +
                setOf(["typescript", "python", "go", "csharp", "java"], "java"),
        );
        expect(await activeLangs(page)).toEqual(["java"]);
    });

    it("does not fall back across a boundary between two separate toggle sets", async () => {
        const page = await newE2EPage();
        await page.setContent(
            setOf(["typescript", "python"], "hcl") +
                `<h2>A heading breaks the run</h2>` +
                setOf(["go", "csharp"], "hcl"),
        );
        // Each set falls back independently to its own first member.
        expect(await activeLangs(page)).toEqual(["typescript", "go"]);
    });

    it("does not fall back for a lone single-language aside", async () => {
        const page = await newE2EPage();
        // A standalone TypeScript-only note is intentionally hidden on other languages.
        await page.setContent(setOf(["typescript"], "hcl"));
        expect(await activeLangs(page)).toEqual([]);
    });

    it("leaves choosables inside a chooser to the chooser's own fallback", async () => {
        const page = await newE2EPage();
        await page.setContent(
            `<pulumi-chooser type="language" options="typescript,python">
                <div><pulumi-choosable type="language" values="typescript" selection="hcl"></pulumi-choosable></div>
                <div><pulumi-choosable type="language" values="python" selection="hcl"></pulumi-choosable></div>
            </pulumi-chooser>`,
        );
        // The headless fallback must not fire here; with no chooser selection applied in
        // this isolated test, neither child is active.
        expect(await activeLangs(page)).toEqual([]);
    });
});
