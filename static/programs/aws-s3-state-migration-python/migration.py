from typing import Any

import pulumi

COMPONENT_TYPE = "example:storage:VersionedBucket"
OLD_BUCKET_TYPE = "aws:s3/bucketV2:BucketV2"
BUCKET_TYPE = "aws:s3/bucket:Bucket"
VERSIONING_TYPE = "aws:s3/bucketVersioningV2:BucketVersioningV2"


def state_string(state: dict[str, Any], key: str) -> str:
    value = state.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"State resource has missing or invalid {key}")
    return value


def migrate_bucket_state(
    args: pulumi.StateMigrationArgs,
) -> pulumi.StateMigrationResult | None:
    if not args.old_state:
        return None
    root = args.old_state[0]
    if root.get("type") != COMPONENT_TYPE:
        raise ValueError("Expected a VersionedBucket migration root")

    # Find the bucket and versioning sidecar directly parented to this component.
    index, sidecar_index = -1, -1
    for i, state in enumerate(args.old_state):
        if state.get("parent") != root.get("urn"):
            continue
        if state.get("type") in (OLD_BUCKET_TYPE, BUCKET_TYPE):
            if index != -1:
                raise ValueError("Expected only one bucket")
            index = i
        elif state.get("type") == VERSIONING_TYPE:
            if sidecar_index != -1:
                raise ValueError("Expected only one versioning sidecar")
            sidecar_index = i
    # Leave fresh or already-migrated state unchanged.
    if sidecar_index == -1 and (
        index == -1 or args.old_state[index].get("type") == BUCKET_TYPE
    ):
        return None
    if index == -1 or sidecar_index == -1 or args.old_state[index].get("type") != OLD_BUCKET_TYPE:
        raise ValueError("Expected BucketV2 and its versioning sidecar")
    old_bucket, sidecar = args.old_state[index], args.old_state[sidecar_index]

    # Both state entries must refer to the same physical bucket and provider.
    for key in ("id", "provider"):
        if sidecar.get(key) != state_string(old_bucket, key):
            raise ValueError(f"Bucket and sidecar must have the same {key}")
    # Only migrate the versioning configuration supported by this example.
    outputs = sidecar.get("outputs")
    configuration = outputs.get("versioningConfiguration") if isinstance(outputs, dict) else None
    if (
        not isinstance(configuration, dict)
        or configuration.get("status") != "Enabled"
        or configuration.get("mfaDelete") != "Disabled"
    ):
        raise ValueError("This example requires enabled versioning without MFA delete")
    sidecar_urn = state_string(sidecar, "urn")

    # Copy the bucket state and change its logical type in both the URN and
    # type field, preserving its physical ID and other metadata.
    bucket = dict(old_bucket)
    old_urn = state_string(bucket, "urn")
    old_type = f"${OLD_BUCKET_TYPE}::"
    if old_type not in old_urn:
        raise ValueError("Bucket URN does not match BucketV2")
    new_urn = old_urn.replace(old_type, f"${BUCKET_TYPE}::", 1)
    bucket["urn"], bucket["type"] = new_urn, BUCKET_TYPE

    # Translate both saved inputs and observed outputs to the new schema.
    for field in ("inputs", "outputs"):
        old_properties = bucket.get(field)
        if not isinstance(old_properties, dict):
            raise ValueError(f"Expected bucket {field} object")
        properties = dict(old_properties)
        properties.pop("__pulumi_raw_state_delta", None)
        properties.pop("versionings", None)
        # Populate the new bucket's inline versioning settings from the old
        # versioning sidecar, which managed this configuration before migration.
        properties["versioning"] = {
            "enabled": configuration["status"] == "Enabled",
            "mfaDelete": configuration["mfaDelete"] == "Enabled",
        }

        # BucketV2 uses plural singleton lists; Bucket uses singular objects.
        for plural, singular in {
            "loggings": "logging",
            "replicationConfigurations": "replicationConfiguration",
            "serverSideEncryptionConfigurations": "serverSideEncryptionConfiguration",
            "websites": "website",
        }.items():
            blocks = properties.pop(plural, None)
            if blocks is None:
                continue
            if not isinstance(blocks, list) or len(blocks) > 1:
                raise ValueError(f"Expected at most one {plural} block")
            if blocks:
                properties[singular] = blocks[0]
        bucket[field] = properties

    # Preserve the rest of the subtree and remove the separate versioning entry.
    # Map both old URNs to the new bucket so Pulumi can rewrite references to them.
    new_state = list(args.old_state)
    new_state[index] = bucket
    del new_state[sidecar_index]
    return pulumi.StateMigrationResult(
        new_state=new_state,
        successors={old_urn: new_urn, sidecar_urn: new_urn},
    )
