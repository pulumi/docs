package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Bucket("my-bucket",
                                    BucketArgs.builder()
                                    .location("US")
                                    .build());
            ctx.export("bucketName", bucket.url());
        });
    }
}
