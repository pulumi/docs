import pulumi
from pulumi import Input, Output
from pulumi.dynamic import ResourceProvider, CreateResult, Resource
import requests
import os

class PulumiEnvironmentArgs:
    def __init__(self, org_name: str, environment_name: str):
        self.org_name = org_name
        self.environment_name = environment_name

class PulumiEnvironmentProviderArgs:
    def __init__(self, org_name: str, environment_name: str):
        self.org_name = org_name
        self.environment_name = environment_name

# Use user-specified API URL if provided. Otherwise, use default Pulumi cloud URL.
base_pulumi_api_url = os.getenv("PULUMI_CLOUD_API_URL", "https://api.pulumi.com")

base_pulumi_env_api_url = f"{base_pulumi_api_url}/api/environments"

# Set up the headers using the environment variable.
headers = {
    'Authorization': f"token {os.getenv('PULUMI_ACCESS_TOKEN')}",
    'Content-Type': 'application/json'
}

class PulumiEnvironmentProvider(ResourceProvider):
    def create(self, inputs: PulumiEnvironmentProviderArgs) -> CreateResult:

        create_env_url = f"{base_pulumi_env_api_url}/{inputs['org_name']}/{inputs['environment_name']}"

        env_id = "unassigned"
        response = requests.post(create_env_url, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            env_id = f"{inputs['org_name']}/{inputs['environment_name']}"
        else:
            print(f"ERROR: {response.status_code} - {response.text}")
            os._exit(10)

        env_outs = {"id": env_id, "envName": inputs['environment_name'], "orgName": inputs['org_name']}
        return CreateResult(id_=env_id, outs=env_outs)

    def delete(self, id: str, props):

        # The id provides the "org/environment-name" path for the environment
        delete_env_url = f"{base_pulumi_env_api_url}/{id}"

        response = requests.delete(delete_env_url, headers=headers)
        if response.status_code != 200:
            print(f"ERROR: {response.status_code} - {response.text}")
            os._exit(20)

class PulumiEnvironment(Resource):
    def __init__(self, name, args: PulumiEnvironmentArgs, opts=None):
        super().__init__(PulumiEnvironmentProvider(), name, vars(args), opts)

env = PulumiEnvironment("myEnvironment", PulumiEnvironmentArgs("my-org", "my-environment"))

pulumi.export("environment_id", env.id)
