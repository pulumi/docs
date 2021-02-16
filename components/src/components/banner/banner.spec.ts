import { Banner } from './banner';

describe("pulumi-banner", () => {
    it("builds", () => {
        expect(new Banner()).toBeTruthy();
    });
});
