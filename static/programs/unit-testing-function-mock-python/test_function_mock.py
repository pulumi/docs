import runpy
import unittest

import pulumi


class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        if args.token == "aws:ec2/getAmi:getAmi":
            return {
                "id": "ami-0eb1f3cdeeb8eed2a",
                "architecture": "x86_64",
            }
        return {}


class TestingWithMocks(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        pulumi.runtime.set_mocks(
            MyMocks(),
            preview=False,
        )
        # Run the program fresh for each test *after* setting the mocks.
        program = runpy.run_path("__main__.py")
        self.server = program["server"]

    @pulumi.runtime.test
    def test_server_uses_looked_up_ami(self):
        def check_ami(args):
            urn, ami = args
            self.assertEqual(
                ami, "ami-0eb1f3cdeeb8eed2a", f"unexpected AMI on server {urn}"
            )

        return pulumi.Output.all(self.server.urn, self.server.ami).apply(check_ami)
