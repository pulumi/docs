import { GreenhouseJobsList } from "./greenhouse-jobs-list";

describe("pulumi-greenhouse-jobs-list", () => {
    it("builds", () => {
        expect(new GreenhouseJobsList()).toBeTruthy();
    });
});
