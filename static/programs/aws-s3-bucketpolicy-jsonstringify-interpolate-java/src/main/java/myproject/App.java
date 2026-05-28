package myproject;

import static com.pulumi.codegen.internal.Serialization.*;

import com.pulumi.Pulumi;
import com.pulumi.core.Either;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an S3 bucket.
            var bucket = new Bucket("my-bucket");

            // Build the policy document, appending "/*" to the bucket ARN so the
            // statement targets individual objects rather than the bucket itself.
            var policyDocument = bucket.arn().applyValue(arn -> serializeJson(
                jsonObject(
                    jsonProperty("Version", "2012-10-17"),
                    jsonProperty("Statement", jsonArray(jsonObject(
                        jsonProperty("Effect", "Allow"),
                        jsonProperty("Principal", "*"),
                        jsonProperty("Action", "s3:GetObject"),
                        jsonProperty("Resource", arn + "/*")
                    )))
                )
            ));

            // Create an S3 bucket policy that grants read access to all objects in the bucket.
            var policy = new BucketPolicy("my-bucket-policy", BucketPolicyArgs.builder()
                .bucket(bucket.id())
                .policy(policyDocument.applyValue(Either::ofLeft))
                .build());

            // Export the name of the bucket.
            ctx.export("bucketName", bucket.id());
        });
    }
}
