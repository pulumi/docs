package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("myBucket");

            var policyDocument = bucket.arn().applyValue(arn -> serializeJson(
                jsonObject(
                    jsonProperty("Version", "2012-10-17"),
                    jsonProperty("Statement", jsonArray(jsonObject(
                        jsonProperty("Effect", "Allow"),
                        jsonProperty("Action", jsonArray("s3:PutObject", "s3:PutObjectAcl")),
                        jsonProperty("Principal", jsonObject(
                            jsonProperty("Service", "lambda.amazonaws.com")
                        )),
                        jsonProperty("Resource", arn + "/*")
                    )))
                )
            ));

            var bucketPolicy = new BucketPolicy("myBucketPolicy", BucketPolicyArgs.builder()
                .bucket(bucket.id())
                .policy(policyDocument)
                .build());

            ctx.export("bucketName", bucket.id());
            ctx.export("bucketArn", bucket.arn());
        });
    }
}
