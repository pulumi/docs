import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.inputs.BucketPolicyPolicyArgs;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("myBucket");

            var bucketArn = bucket.arn();
            var policyDocument = bucketArn.apply(arn -> String.format("""
                {
                  "Version": "2012-10-17",
                  "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"Service": "lambda.amazonaws.com"},
                    "Action": ["s3:PutObject", "s3:PutObjectAcl"],
                    "Resource": "%s/*"
                  }]
                }""", arn));

            var bucketPolicy = new BucketPolicy("myBucketPolicy", BucketPolicyArgs.builder()
                .bucket(bucket.id())
                .policy(policyDocument)
                .build());

            ctx.export("bucketName", bucket.id());
            ctx.export("bucketArn", bucket.arn());
        });
    }
}
