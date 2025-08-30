package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.s3.Bucket;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("my-bucket");
            ctx.export("bucketName", bucket.bucket());
        });
    }
}
