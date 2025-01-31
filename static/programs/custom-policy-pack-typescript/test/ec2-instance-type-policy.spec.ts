import * as assert from "assert";
import { ec2InstanceTypeRestrictedPolicy, REQUIRED_INSTANCE_TYPE } from "../index";
import { runResourcePolicy, getEmptyArgs } from "./test-helpers";

describe("ec2-instance-type-restricted-policy", () => {
    it("should fail when it has no instanceType", () => {
        const args = getEmptyArgs();
        args.type = "aws.ec2.Instance";
        args.props.instanceType = "";
        assert.throws(() => {
            runResourcePolicy(ec2InstanceTypeRestrictedPolicy, args);
        });
    });
    it("should fail when it has the incorrect prefix", () => {
        const args = getEmptyArgs();
        args.type = "aws.ec2.Instance";
        args.props.instanceType = "t3.micro";
        assert.throws(() => {
            runResourcePolicy(ec2InstanceTypeRestrictedPolicy, args);
        });
    });
    it("should pass if it has the correct instance type", () => {
        const args = getEmptyArgs();
        args.type = "aws.ec2.Instance";
        args.props.instanceType = REQUIRED_INSTANCE_TYPE;
        assert.doesNotThrow(() => {
            runResourcePolicy(ec2InstanceTypeRestrictedPolicy, args);
        });
    });
});
