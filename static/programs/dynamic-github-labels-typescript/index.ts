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
    // check runs before any other method and validates the user's inputs.
    async check(olds: LabelInputs, news: LabelInputs): Promise<pulumi.dynamic.CheckResult> {
        const failures: pulumi.dynamic.CheckFailure[] = [];
        // GitHub label colors are six hexadecimal digits with no leading "#".
        if (!/^[0-9a-fA-F]{6}$/.test(news.color)) {
            failures.push({
                property: "color",
                reason: `invalid color "${news.color}": expected six hexadecimal digits with no leading "#"`,
            });
        }
        return { inputs: news, failures };
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
    // diff reports whether the resource needs to change. GitHub labels can be
    // updated in place, so a change never forces a replacement.
    async diff(id: string, olds: LabelInputs, news: LabelInputs): Promise<pulumi.dynamic.DiffResult> {
        const changed =
            olds.name !== news.name ||
            olds.color !== news.color ||
            olds.description !== news.description;
        return { changes: changed };
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
    declare readonly color: pulumi.Output<string>;
    declare readonly url: pulumi.Output<string>;

    constructor(name: string, args: LabelResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(new githubLabelProvider(), name, { color: undefined, url: undefined, ...args }, opts);
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
