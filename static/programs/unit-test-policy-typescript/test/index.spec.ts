import * as assert from "assert";
import * as policy from "@pulumi/policy";
import { s3BucketPrefixPolicy } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("s3-bucket-prefix-policy", () => {
    it("should pass when bucket has correct prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        args.props.bucketPrefix = "mycompany-data";
        assert.doesNotThrow(() => {
            runResourcePolicy(s3BucketPrefixPolicy, args);
        });
    });

    it("should fail when bucket has wrong prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        args.props.bucketPrefix = "wrongprefix-data";
        assert.throws(() => {
            runResourcePolicy(s3BucketPrefixPolicy, args);
        });
    });

    it("should fail when bucket has no prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        args.props.bucketPrefix = "";
        assert.throws(() => {
            runResourcePolicy(s3BucketPrefixPolicy, args);
        });
    });
});
