package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.aws.s3.BucketMetric;
import com.pulumi.aws.s3.BucketMetricArgs;
import com.pulumi.aws.s3.BucketNotification;
import com.pulumi.aws.s3.BucketNotificationArgs;
import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.aws.s3.BucketOwnershipControls;
import com.pulumi.aws.s3.BucketOwnershipControlsArgs;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;
import com.pulumi.aws.s3.BucketPublicAccessBlock;
import com.pulumi.aws.s3.BucketPublicAccessBlockArgs;
import com.pulumi.aws.s3.inputs.BucketOwnershipControlsRuleArgs;
import com.pulumi.resources.CustomResourceOptions;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("my-bucket", BucketArgs.builder().build());

            var ownershipControls = new BucketOwnershipControls("ownership-controls", BucketOwnershipControlsArgs.builder()
                .bucket(bucket.id())
                .rule(BucketOwnershipControlsRuleArgs.builder()
                    .objectOwnership("ObjectWriter")
                    .build())
                .build());

            var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", BucketPublicAccessBlockArgs.builder()
                .bucket(bucket.id())
                .blockPublicAcls(false)
                .build());

            var bucketMetric = new BucketMetric("my-bucket-metric", BucketMetricArgs.builder()
                .bucket(bucket.id())
                .build());

            var bucketNotification = new BucketNotification("my-bucket-notification", BucketNotificationArgs.builder()
                .bucket(bucket.id())
                .build());

            var bucketObject = new BucketObject("my-bucket-object", BucketObjectArgs.builder()
                .bucket(bucket.id())
                .content("hello world")
                .build(), CustomResourceOptions.builder()
                .dependsOn(publicAccessBlock, ownershipControls)
                .build());

            var bucketPolicy = new BucketPolicy("my-bucket-policy", BucketPolicyArgs.builder()
                .bucket(bucket.id())
                .policy(bucket.id().applyValue(App::publicReadPolicyForBucket))
                .build(), CustomResourceOptions.builder()
                .dependsOn(publicAccessBlock, ownershipControls)
                .build());
        });
    }

    private static String publicReadPolicyForBucket(String bucketName) {
        return String.format(serializeJson(
            jsonObject(
                jsonProperty("Version", "2012-10-17"),
                jsonProperty("Statement", jsonArray(jsonObject(
                    jsonProperty("Effect", "Allow"),
                    jsonProperty("Action", "s3:GetObject"),
                    jsonProperty("Principal", "*"),
                    jsonProperty("Resource", "arn:aws:s3:::%s/*")
                )))
            )), bucketName);
    }
}
