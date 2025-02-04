import * as assert from "assert";
import { s3ProductPrefixPolicy, REQUIRED_S3_PREFIX } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("s3-product-prefix-policy", () => {
    it("should fail when it has no prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.BucketV2";
        args.props.bucketPrefix = "";
        assert.throws(() => {
            runResourcePolicy(s3ProductPrefixPolicy, args);
        });
    });
    it("should fail when it has the incorrect prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.BucketV2";
        args.props.bucketPrefix = "somethingiswrong-";
        assert.throws(() => {
            runResourcePolicy(s3ProductPrefixPolicy, args);
        });
    });
    it("should pass if it has the correct prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.BucketV2";
        args.props.bucketPrefix = REQUIRED_S3_PREFIX;
        assert.doesNotThrow(() => {
            runResourcePolicy(s3ProductPrefixPolicy, args);
        });
    });
});
