import * as assert from "assert";
import { allAwsResourcesMustHaveTagsPolicy } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("all-resources-must-have-tags-policy", () => {
    it("should fail when it has no tags", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.BucketV2";
        args.props.tags = {};
        assert.throws(() => {
            runResourcePolicy(allAwsResourcesMustHaveTagsPolicy, args);
        });
    });
    it("should pass it has at least one tag", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.BucketV2";
        args.props.tags = {
            Name: "test",
        };
        assert.doesNotThrow(() => {
            runResourcePolicy(allAwsResourcesMustHaveTagsPolicy, args);
        });
    });
});
