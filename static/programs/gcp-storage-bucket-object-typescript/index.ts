import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const bucket = new gcp.storage.Bucket("bucket", {
    location: "US",
    forceDestroy: true,
});

const role = new gcp.projects.IAMCustomRole("role", {
    roleId: "bucketViewerRole",
    title: "Bucket Viewer Role",
    permissions: ["storage.objects.get", "storage.objects.list"],
    stage: "GA",
});

const bucketViewerRoleAssignment = new gcp.storage.BucketIAMMember("bucketViewerRoleAssignment", {
    bucket: bucket.name,
    role: role.name,
    member: "allAuthenticatedUsers",
});

const bucketName = bucket.name;
const roleName = role.roleId;

const bucketObject = new gcp.storage.BucketObject("bucketObject", {
    bucket: bucketName,
    content: pulumi.interpolate`My bucket role name is: ${roleName}`,
    contentType: "text/plain",
});

export const roleName1 = role.roleId;
export const bucketName1 = bucket.name;
