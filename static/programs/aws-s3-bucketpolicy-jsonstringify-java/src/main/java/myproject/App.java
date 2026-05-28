package myproject;

import static com.pulumi.codegen.internal.Serialization.*;

import com.pulumi.Pulumi;
import com.pulumi.core.Either;
import com.pulumi.core.Output;
import com.pulumi.aws.AwsFunctions;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Get the account ID of the current user as a Pulumi output.
            var accountID = AwsFunctions.getCallerIdentity().applyValue(identity -> identity.accountId());

            // Create an S3 bucket.
            var bucket = new Bucket("my-bucket");

            // Build the policy document, waiting for the account ID and bucket ARN to resolve.
            var policyDocument = Output.tuple(accountID, bucket.arn()).applyValue(t -> serializeJson(
                jsonObject(
                    jsonProperty("Version", "2012-10-17"),
                    jsonProperty("Statement", jsonArray(jsonObject(
                        jsonProperty("Effect", "Allow"),
                        jsonProperty("Principal", jsonObject(
                            jsonProperty("AWS", "arn:aws:iam::" + t.t1 + ":root")
                        )),
                        jsonProperty("Action", "s3:ListBucket"),
                        jsonProperty("Resource", t.t2)
                    )))
                )
            ));

            // Create an S3 bucket policy allowing anyone in the account to list the contents of the bucket.
            var policy = new BucketPolicy("my-bucket-policy", BucketPolicyArgs.builder()
                .bucket(bucket.id())
                .policy(policyDocument.applyValue(Either::ofLeft))
                .build());

            // Export the name of the bucket.
            ctx.export("bucketName", bucket.id());
        });
    }
}
