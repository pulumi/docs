// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Minimal ambient declarations for the Node APIs the theme's unit tests use.
//
// The theme is pinned to TypeScript 3.9, which cannot *parse* the .d.ts syntax
// current @types/node ships (`override` members, and so on) — and skipLibCheck
// does not help, because those are syntax errors rather than type errors. So
// tsconfig.test.json sets "types": [] to turn off automatic @types inclusion,
// and this file supplies only what the tests actually touch.
//
// Bumping the theme's TypeScript would remove the need for this, but that
// compiler also builds the production bundle, so it is not a change to make in
// passing. Delete this file when it is upgraded.

declare const __dirname: string;

declare const require: {
    (id: string): any;
    resolve(id: string): string;
    cache: { [id: string]: any };
};

declare module "node:test" {
    export function test(name: string, fn: () => void | Promise<void>): void;
}

declare module "assert" {
    function ok(value: any, message?: string): void;
    function strictEqual(actual: any, expected: any, message?: string): void;
    function notStrictEqual(actual: any, expected: any, message?: string): void;
    function deepStrictEqual(actual: any, expected: any, message?: string): void;
    function match(value: string, regExp: RegExp, message?: string): void;
    function doesNotMatch(value: string, regExp: RegExp, message?: string): void;
}
