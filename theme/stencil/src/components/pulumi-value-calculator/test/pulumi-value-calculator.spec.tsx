import { PulumiValueCalculator } from "../pulumi-value-calculator";

describe("pulumi-value-calculator", () => {
    it("builds", () => {
        expect(new PulumiValueCalculator()).toBeTruthy();
    });
});
