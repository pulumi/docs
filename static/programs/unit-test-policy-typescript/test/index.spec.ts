import * as assert from "assert";
import * as policy from "@pulumi/policy";
import { rdsStorageEncryptionPolicy } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("rds-storage-encryption-policy", () => {
    it("should pass when storage encryption is enabled", () => {
        const args = getEmptyArgs();
        args.type = "aws:rds/instance:Instance";
        args.props.storageEncrypted = true;
        assert.doesNotThrow(() => {
            runResourcePolicy(rdsStorageEncryptionPolicy, args);
        });
    });

    it("should fail when storage encryption is not enabled", () => {
        const args = getEmptyArgs();
        args.type = "aws:rds/instance:Instance";
        args.props.storageEncrypted = false;
        assert.throws(() => {
            runResourcePolicy(rdsStorageEncryptionPolicy, args);
        });
    });

    it("should pass when the instance is tagged as non-production data", () => {
        const args = getEmptyArgs();
        args.type = "aws:rds/instance:Instance";
        args.props.storageEncrypted = false;
        args.props.tags = { "data-classification": "non-production" };
        assert.doesNotThrow(() => {
            runResourcePolicy(rdsStorageEncryptionPolicy, args);
        });
    });
});
