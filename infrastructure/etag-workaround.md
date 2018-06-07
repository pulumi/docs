# ETag Workaround

Bash commands for working around
[pulumi/pulumi #1449](https://github.com/pulumi/pulumi/issues/1449).

```bash
# Get current stack checkpoint, and make a copy.
pulumi stack export > before.json
cp before.json after.json

# Print all CDNs in it.
cat before.json | jq '.deployment.resources[] | select(.type | contains("aws:cloudfront/distribution:Distribution")) | "URN=\( .urn ) - CDN_ID=\( .id ) - CUR_ETAG=\( .outputs.etag )"'

# Get the *NEW* current ETag.
aws cloudfront get-distribution --id $CDN_ID | grep -i etag

# Update the value(s)
export CUR_ETAG="... from jq command output ..."
export NEW_ETAG="... from aws command output ..."
sed -i -e "s/${CUR_ETAG}/${NEW_ETAG}/g" after.json

# Confirm only the ETag values have changed.
diff -c before.json after.json

# Import the fixed stack checkpoint.
pulumi stack import < after.json
```
