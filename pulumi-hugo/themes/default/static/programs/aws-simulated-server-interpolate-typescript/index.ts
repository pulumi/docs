import * as pulumi from "@pulumi/pulumi";
import { Output } from "@pulumi/pulumi";

// Simulated web server resource
const webServer = pulumi.output({
    hostName: "www.mywebserver.com",
    port: "8080",
});

// concat takes a list of args and concatenates all of them into a single output:
const url1: Output<string> = pulumi.concat("http://", webServer.hostName, ":", webServer.port, "/");

// interpolate takes a JavaScript "template literal" and expands outputs correctly:
const url2: Output<string> = pulumi.interpolate`http://${webServer.hostName}:${webServer.port}/`;

export const serverUrl1 = url1;
export const serverUrl2 = url2;
