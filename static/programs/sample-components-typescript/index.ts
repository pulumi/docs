import * as pulumi from "@pulumi/pulumi";
import { StaticPage } from "./StaticPage";

const pageHTML = "<h1>I love Pulumi!</h1>";

const page = new StaticPage("my-static-page", {
    indexContent: pageHTML,
});

export const websiteURL = pulumi.interpolate`http://${page.endpoint}`;
