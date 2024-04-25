import { Example } from "./example";

describe("pulumi-example", () => {
    it("builds", () => {
        expect(new Example()).toBeTruthy();
    });
});
