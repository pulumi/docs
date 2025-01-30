import * as assert from "assert";
import * as policy from "@pulumi/policy";
import { s3NoPublicReadPolicy } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("s3-no-public-read-policy", () => {
    it("should fail when public-read is set", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        args.props.acl = "public-read";
        assert.throws(() => {
            runResourcePolicy(s3NoPublicReadPolicy, args);
        });
    });

    it("should fail when public-read-write is set", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        args.props.acl = "public-read-write";
        assert.throws(() => {
            runResourcePolicy(s3NoPublicReadPolicy, args);
        });
    });
    it("should pass if neither public-read or public-read-write are set", () => {
        const args = getEmptyArgs();
        args.type = "aws.s3.Bucket";
        assert.doesNotThrow(() => {
            runResourcePolicy(s3NoPublicReadPolicy, args);
        });
    });
});
