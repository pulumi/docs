// Test-only stand-in for the `uuid` package, which ships ESM-only and can't be
// parsed by jest's CJS runtime. Wired up via moduleNameMapper in stencil.config.ts.
export function v4(): string {
    return "00000000-0000-4000-8000-000000000000";
}
