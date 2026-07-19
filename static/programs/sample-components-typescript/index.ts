import * as pulumi from "@pulumi/pulumi";
import { StaticWebsite } from "./StaticWebsite";

const pageHTML = "<h1>I love Pulumi!</h1>";

const page = new StaticWebsite("my-static-website", {
    indexContent: pageHTML,
});

export const websiteURL = pulumi.interpolate`http://${page.endpoint}`;
