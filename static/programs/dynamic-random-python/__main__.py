from pulumi import ResourceOptions
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Optional
import binascii
import os
import pulumi

class RandomProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_=binascii.b2a_hex(os.urandom(16)), outs={})

class Random(Resource):
    def __init__(self, name: str, opts: Optional[ResourceOptions] = None):
        super().__init__(RandomProvider(), name, {}, opts)

random = Random("myRandom")

pulumi.export("random_id", random.id)
