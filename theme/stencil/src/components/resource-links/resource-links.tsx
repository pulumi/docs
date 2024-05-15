import { Component, Prop, State, h } from "@stencil/core";
// import { resources } from "./resources";

// Scroll to top button.
@Component({
    tag: "pulumi-resource-links",
    shadow: false,
})
export class ResourceLinks {
    @Prop()
    packageName: string;

    @Prop()
    moduleName: string;

    @Prop()
    resourceName: string;

    @State()
    related: [];

    componentWillLoad() {
        // Fetch JSON file containing resource link information.
        fetch("https://www.pulumi.com/uploads/related-resources/2022-12-19.json")
        .then(resp => resp.json())
        .then((response) => {
            const relatedResources = response;
            if (relatedResources) {
                const pkg = this.packageName.toLowerCase();
                const module = this.moduleName.toLowerCase();
                const typ = this.resourceName.toLowerCase();

                // Look up related links for this resource.
                this.related = relatedResources[pkg] ? relatedResources[pkg][module] ? relatedResources[pkg][module][typ] : undefined : undefined;

            }
        })
        .catch(err => console.error(err));
    }

    render() {
        // relatedResources will be set once the response returns and state is updated,
        // so return empty div until then.
        if (!this.related) {
            return <div></div>
        }
        const pkg = this.packageName.toLowerCase();
        return (
            <div class="container">
                <hr class="mr-5"/>
                <div class="heading">Related Resources</div>
                    {
                        this.related.map((typ: string) => {
                            // Parse out the module and resource from the related resource.
                            // We are currently only linking to resources related in the
                            // same package.
                            const parts = typ.split("/");
                            let module = parts.slice(0, parts.length-1).join("/");
                            const resource = parts[parts.length-1];
                            const rellink = `/registry/packages/${pkg}/api-docs/${module.toLowerCase()}/${resource.toLowerCase()}/`;
                            return <div class="links"><a href={rellink}>{`${module}`}.{`${resource}`}</a></div>
                        })
                    }
            </div>
        );
    }
}
