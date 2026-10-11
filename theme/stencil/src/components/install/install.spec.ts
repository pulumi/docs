import { Install } from "./install";

describe("pulumi-install", () => {
    it("builds", () => {
        expect(new Install()).toBeTruthy();
    });
});
