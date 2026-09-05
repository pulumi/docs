import * as pulumi from "@pulumi/pulumi";
import "mocha";

pulumi.runtime.setMocks({
    newResource: function(args: pulumi.runtime.MockResourceArgs): {id: string, state: any} {
        return {
            id: args.name + "_id",
            state: args.inputs,
        };
    },
    call: function(args: pulumi.runtime.MockCallArgs) {
        switch (args.token) {
            case "aws:ec2/getAmi:getAmi":
                return {
                    id: "ami-0eb1f3cdeeb8eed2a",
                    architecture: "x86_64",
                };
            default:
                return args.inputs;
        }
    },
}, "project", "stack", false); // Project and stack names, plus dryRun; the names show up in mocked URNs.

describe("Infrastructure", function() {
    let infra: typeof import("../index");

    before(async function() {
        // It's important to import the program _after_ the mocks are defined.
        infra = await import("../index");
    });

    describe("#server", function() {
        it("must use the AMI returned by the getAmi lookup", function(done) {
            pulumi.all([infra.server.urn, infra.server.ami]).apply(([urn, ami]) => {
                if (ami !== "ami-0eb1f3cdeeb8eed2a") {
                    done(new Error(`Unexpected AMI ${ami} on server ${urn}`));
                } else {
                    done();
                }
            });
        });
    });
});
