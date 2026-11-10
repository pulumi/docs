package main

import (
	"context"
	"fmt"
	"maps"
	"slices"
	"strings"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

const (
	componentType  = "example:storage:VersionedBucket"
	oldBucketType  = "aws:s3/bucketV2:BucketV2"
	bucketType     = "aws:s3/bucket:Bucket"
	versioningType = "aws:s3/bucketVersioningV2:BucketVersioningV2"
)

func stateString(state map[string]any, key string) (string, error) {
	value, ok := state[key].(string)
	if !ok || value == "" {
		return "", fmt.Errorf("state resource has missing or invalid %s", key)
	}
	return value, nil
}

func migrateBucketState(_ context.Context, args *pulumi.StateMigrationArgs) (*pulumi.StateMigrationResult, error) {
	if len(args.OldState) == 0 {
		return nil, nil
	}
	root := args.OldState[0]
	if root["type"] != componentType {
		return nil, fmt.Errorf("expected a VersionedBucket migration root")
	}

	// Find the bucket and versioning sidecar directly parented to this component.
	index, sidecarIndex := -1, -1
	for i, state := range args.OldState {
		if state["parent"] != root["urn"] {
			continue
		}
		switch state["type"] {
		case oldBucketType, bucketType:
			if index != -1 {
				return nil, fmt.Errorf("expected only one bucket")
			}
			index = i
		case versioningType:
			if sidecarIndex != -1 {
				return nil, fmt.Errorf("expected only one versioning sidecar")
			}
			sidecarIndex = i
		}
	}
	// Leave fresh or already-migrated state unchanged.
	if sidecarIndex == -1 && (index == -1 || args.OldState[index]["type"] == bucketType) {
		return nil, nil
	}
	if index == -1 || sidecarIndex == -1 || args.OldState[index]["type"] != oldBucketType {
		return nil, fmt.Errorf("expected BucketV2 and its versioning sidecar")
	}
	oldBucket, sidecar := args.OldState[index], args.OldState[sidecarIndex]
	// Both state entries must refer to the same physical bucket and provider.
	for _, key := range []string{"id", "provider"} {
		value, err := stateString(oldBucket, key)
		if err != nil {
			return nil, err
		}
		if sidecar[key] != value {
			return nil, fmt.Errorf("bucket and sidecar must have the same %s", key)
		}
	}
	// Only migrate the versioning configuration supported by this example.
	outputs, _ := sidecar["outputs"].(map[string]any)
	configuration, _ := outputs["versioningConfiguration"].(map[string]any)
	if configuration["status"] != "Enabled" || configuration["mfaDelete"] != "Disabled" {
		return nil, fmt.Errorf("this example requires enabled versioning without MFA delete")
	}
	sidecarURN, err := stateString(sidecar, "urn")
	if err != nil {
		return nil, err
	}

	// Copy the bucket state and change its logical type in both the URN and
	// type field, preserving its physical ID and other metadata.
	bucket := maps.Clone(args.OldState[index])
	oldURN, err := stateString(bucket, "urn")
	if err != nil {
		return nil, err
	}
	oldType := "$" + oldBucketType + "::"
	if !strings.Contains(oldURN, oldType) {
		return nil, fmt.Errorf("bucket URN does not match BucketV2")
	}
	newURN := strings.Replace(oldURN, oldType, "$"+bucketType+"::", 1)
	bucket["urn"], bucket["type"] = newURN, bucketType

	// Translate both saved inputs and observed outputs to the new schema.
	for _, field := range []string{"inputs", "outputs"} {
		oldProperties, ok := bucket[field].(map[string]any)
		if !ok {
			return nil, fmt.Errorf("expected bucket %s object", field)
		}
		properties := maps.Clone(oldProperties)
		delete(properties, "__pulumi_raw_state_delta")
		delete(properties, "versionings")
		// Populate the new bucket's inline versioning settings from the old
		// versioning sidecar, which managed this configuration before migration.
		properties["versioning"] = map[string]any{
			"enabled":   configuration["status"] == "Enabled",
			"mfaDelete": configuration["mfaDelete"] == "Enabled",
		}

		// BucketV2 uses plural singleton lists; Bucket uses singular objects.
		for plural, singular := range map[string]string{
			"loggings":                           "logging",
			"replicationConfigurations":          "replicationConfiguration",
			"serverSideEncryptionConfigurations": "serverSideEncryptionConfiguration",
			"websites":                           "website",
		} {
			value := properties[plural]
			delete(properties, plural)
			if value == nil {
				continue
			}
			blocks, ok := value.([]any)
			if !ok || len(blocks) > 1 {
				return nil, fmt.Errorf("expected at most one %s block", plural)
			}
			if len(blocks) == 1 {
				properties[singular] = blocks[0]
			}
		}
		bucket[field] = properties
	}

	// Preserve the rest of the subtree and remove the separate versioning entry.
	// Map both old URNs to the new bucket so Pulumi can rewrite references to them.
	newState := slices.Clone(args.OldState)
	newState[index] = bucket
	newState = slices.Delete(newState, sidecarIndex, sidecarIndex+1)
	return &pulumi.StateMigrationResult{
		NewState:   newState,
		Successors: map[string]string{oldURN: newURN, sidecarURN: newURN},
	}, nil
}
