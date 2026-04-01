import * as aws from "@pulumi/aws";

const zone = new aws.route53.Zone("zone", {
    name: "example.com",
});

const cert = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});

// Using apply to access nested output values
const certValidationApply = new aws.route53.Record("certValidationApply", {
    name: cert.domainValidationOptions.apply(
        domainValidationOptions => domainValidationOptions[0].resourceRecordName),
    type: cert.domainValidationOptions.apply(
        domainValidationOptions => domainValidationOptions[0].resourceRecordType),
    zoneId: zone.zoneId,
    ttl: 60,
    records: [
        cert.domainValidationOptions.apply(
            domainValidationOptions => domainValidationOptions[0].resourceRecordValue),
    ],
});

// Using lifting to access nested output values
const certValidationLifting = new aws.route53.Record("certValidationLifting", {
    name: cert.domainValidationOptions[0].resourceRecordName,
    type: cert.domainValidationOptions[0].resourceRecordType,
    zoneId: zone.zoneId,
    ttl: 60,
    records: [
        cert.domainValidationOptions[0].resourceRecordValue,
    ],
});
