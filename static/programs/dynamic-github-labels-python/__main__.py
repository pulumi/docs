import pulumi
from pulumi import Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult, UpdateResult, ConfigureRequest
from typing import Optional
from github import Github, GithubObject

class GithubLabelArgs(object):
    owner: Input[str]
    repo: Input[str]
    name: Input[str]
    color: Input[str]
    description: Optional[Input[str]]
    def __init__(self, owner, repo, name, color, description=None):
        self.owner = owner
        self.repo = repo
        self.name = name
        self.color = color
        self.description = description

class GithubLabelProvider(ResourceProvider):
    auth: str
    def configure(self, req: ConfigureRequest):
        # Set a stack config variable named githubToken (e.g. pulumi config set githubToken <VALUE> --secret)
        self.auth = req.config.require("githubToken")

    def create(self, props):
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).create_label(
            name=props["name"],
            color=props["color"],
            description=props.get("description", GithubObject.NotSet))
        return CreateResult(l.name, {**props, **l.raw_data})
    def update(self, id, _olds, props):
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.edit(name=props["name"],
               color=props["color"],
               description=props.get("description", GithubObject.NotSet))
        return UpdateResult({**props, **l.raw_data})
    def delete(self, id, props):
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.delete()

class GithubLabel(Resource):
    name: Output[str]
    color: Output[str]
    url: Output[str]
    description: Output[str]
    def __init__(self, name, args: GithubLabelArgs, opts = None):
        full_args = {'url':None, 'description':None, 'name':None, 'color':None, **vars(args)}
        super().__init__(GithubLabelProvider(), name, full_args, opts)

label = GithubLabel("myLabel", GithubLabelArgs("my-org", "my-repo", "my-label", "d94f0b"))

pulumi.export("label_color", label.color)
pulumi.export("label_url", label.url)
