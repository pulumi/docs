import * as pulumi from "@pulumi/pulumi";
import { Octokit } from "@octokit/rest";

export interface LabelResourceInputs {
    owner: pulumi.Input<string>;
    repo: pulumi.Input<string>;
    name: pulumi.Input<string>;
    color: pulumi.Input<string>;
    description?: pulumi.Input<string>;
}

interface LabelInputs {
    owner: string;
    repo: string;
    name: string;
    color: string;
    description?: string;
}

class githubLabelProvider implements pulumi.dynamic.ResourceProvider {
    private auth: string = "";

    async configure(req: pulumi.dynamic.ConfigureRequest): Promise<void> {
        // Set a stack config variable named githubToken (e.g. pulumi config set githubToken <VALUE> --secret)
        this.auth = req.config.require("githubToken");
    }
    async create(inputs: LabelInputs) {
        const octokit = new Octokit({ auth: this.auth });
        const label = await octokit.issues.createLabel({
            owner: inputs.owner,
            repo: inputs.repo,
            name: inputs.name,
            color: inputs.color,
        });
        return { id: label.data.id.toString(), outs: label.data };
    }
    async update(id: string, olds: LabelInputs, news: LabelInputs) {
        const octokit = new Octokit({ auth: this.auth });
        const label = await octokit.issues.updateLabel({
            owner: news.owner,
            repo: news.repo,
            current_name: olds.name,
            name: news.name,
            color: news.color,
        });
        return { outs: label.data };
    }
    async delete(id: string, props: LabelInputs) {
        const octokit = new Octokit({ auth: this.auth });
        await octokit.issues.deleteLabel({ owner: props.owner, repo: props.repo, name: props.name });
    }
}

export class Label extends pulumi.dynamic.Resource {
    constructor(name: string, args: LabelResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(new githubLabelProvider(), name, args, opts);
    }
}

const label = new Label("myLabel", {
    owner: "my-org",
    repo: "my-repo",
    name: "my-label",
    color: "d94f0b",
});

export const labelColor = label.color;
export const labelUrl = label.url;
