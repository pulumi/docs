package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var bucket = new Bucket("bucket");

        var file = new BucketObject("bucket-object", BucketObjectArgs.builder()
            .bucket(bucket.id())
            .key("some-file.txt")
            .content("some-content")
            .build());

        var s3Url = Output.format("s3://%s/%s", bucket.bucket(), file.key());

        ctx.export("s3Url", s3Url);
    }
}
