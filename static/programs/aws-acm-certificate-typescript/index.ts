import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
