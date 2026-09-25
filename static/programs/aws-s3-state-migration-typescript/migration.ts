import type * as pulumi from "@pulumi/pulumi";

export const componentType = "example:storage:VersionedBucket";
const oldBucketType = "aws:s3/bucketV2:BucketV2";
const bucketType = "aws:s3/bucket:Bucket";
const versioningType = "aws:s3/bucketVersioningV2:BucketVersioningV2";

function stateString(state: Record<string, any>, key: string): string {
    const value = state[key];
    if (typeof value !== "string" || value === "") {
        throw new Error(`State resource has missing or invalid ${key}`);
    }
    return value;
}

export function migrateBucketState(args: pulumi.StateMigrationArgs): pulumi.StateMigrationResult | undefined {
    if (args.oldState.length === 0) {
        return undefined;
    }
    const root = args.oldState[0];
    if (root.type !== componentType) {
        throw new Error("Expected a VersionedBucket migration root");
    }

    // Find the bucket and versioning sidecar directly parented to this component.
    let index = -1;
    let sidecarIndex = -1;
    args.oldState.forEach((state, i) => {
        if (state.parent !== root.urn) {
            return;
        }
        if (state.type === oldBucketType || state.type === bucketType) {
            if (index !== -1) {
                throw new Error("Expected only one bucket");
            }
            index = i;
        } else if (state.type === versioningType) {
            if (sidecarIndex !== -1) {
                throw new Error("Expected only one versioning sidecar");
            }
            sidecarIndex = i;
        }
    });
    // Leave fresh or already-migrated state unchanged.
    if (sidecarIndex === -1 && (index === -1 || args.oldState[index].type === bucketType)) {
        return undefined;
    }
    if (index === -1 || sidecarIndex === -1 || args.oldState[index].type !== oldBucketType) {
        throw new Error("Expected BucketV2 and its versioning sidecar");
    }
    const oldBucket = args.oldState[index];
    const sidecar = args.oldState[sidecarIndex];
    // Both state entries must refer to the same physical bucket and provider.
    for (const key of ["id", "provider"]) {
        if (sidecar[key] !== stateString(oldBucket, key)) {
            throw new Error(`Bucket and sidecar must have the same ${key}`);
        }
    }
    // Only migrate the versioning configuration supported by this example.
    const configuration = sidecar.outputs?.versioningConfiguration;
    if (configuration?.status !== "Enabled" || configuration?.mfaDelete !== "Disabled") {
        throw new Error("This example requires enabled versioning without MFA delete");
    }
    const sidecarURN = stateString(sidecar, "urn");

    // Copy the bucket state and change its logical type in both the URN and
    // type field, preserving its physical ID and other metadata.
    const bucket = { ...oldBucket };
    const oldURN = stateString(bucket, "urn");
    const oldType = `$${oldBucketType}::`;
    if (!oldURN.includes(oldType)) {
        throw new Error("Bucket URN does not match BucketV2");
    }
    const newURN = oldURN.replace(oldType, `$${bucketType}::`);
    bucket.urn = newURN;
    bucket.type = bucketType;

    // Translate both saved inputs and observed outputs to the new schema.
    for (const field of ["inputs", "outputs"]) {
        const oldProperties = bucket[field];
        if (oldProperties === null || typeof oldProperties !== "object" || Array.isArray(oldProperties)) {
            throw new Error(`Expected bucket ${field} object`);
        }
        const properties = { ...oldProperties };
        delete properties.__pulumi_raw_state_delta;
        delete properties.versionings;
        // Populate the new bucket's inline versioning settings from the old
        // versioning sidecar, which managed this configuration before migration.
        properties.versioning = {
            enabled: configuration.status === "Enabled",
            mfaDelete: configuration.mfaDelete === "Enabled",
        };

        // BucketV2 uses plural singleton lists; Bucket uses singular objects.
        for (const [plural, singular] of Object.entries({
            loggings: "logging",
            replicationConfigurations: "replicationConfiguration",
            serverSideEncryptionConfigurations: "serverSideEncryptionConfiguration",
            websites: "website",
        })) {
            const blocks = properties[plural];
            delete properties[plural];
            if (blocks === undefined || blocks === null) {
                continue;
            }
            if (!Array.isArray(blocks) || blocks.length > 1) {
                throw new Error(`Expected at most one ${plural} block`);
            }
            if (blocks.length === 1) {
                properties[singular] = blocks[0];
            }
        }
        bucket[field] = properties;
    }

    // Preserve the rest of the subtree and remove the separate versioning entry.
    // Map both old URNs to the new bucket so Pulumi can rewrite references to them.
    const newState = args.oldState.slice();
    newState[index] = bucket;
    newState.splice(sidecarIndex, 1);
    return {
        newState,
        successors: { [oldURN]: newURN, [sidecarURN]: newURN },
    };
}
