package myproject;

import com.pulumi.Pulumi;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;
import com.pulumi.gcp.cloudrunv2.Service;
import com.pulumi.gcp.cloudrunv2.ServiceArgs;
import com.pulumi.gcp.cloudrunv2.inputs.ServiceTemplateArgs;
import com.pulumi.gcp.cloudrunv2.inputs.ServiceTemplateContainerArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Cloud Storage bucket using the GCP Classic provider.
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .location("US")
                .uniformBucketLevelAccess(true)
                .forceDestroy(true)
                .build());

            // Create a Cloud Run service.
            var service = new Service("my-service", ServiceArgs.builder()
                .location("us-central1")
                .deletionProtection(false)
                .template(ServiceTemplateArgs.builder()
                    .containers(ServiceTemplateContainerArgs.builder()
                        .image("us-docker.pkg.dev/cloudrun/container/hello")
                        .build())
                    .build())
                .build());

            ctx.export("bucketName", bucket.name());
            ctx.export("serviceUrl", service.uri());
        });
    }
}
