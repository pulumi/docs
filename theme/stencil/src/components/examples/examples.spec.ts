import { Examples } from "./examples";

describe("pulumi-examples", () => {
    it("builds", () => {
        expect(new Examples()).toBeTruthy();
    });
});
