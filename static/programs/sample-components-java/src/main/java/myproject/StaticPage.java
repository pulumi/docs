package myproject;

import java.util.Map;

import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;
import com.pulumi.aws.s3.BucketPublicAccessBlock;
import com.pulumi.aws.s3.BucketPublicAccessBlockArgs;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketWebsiteConfiguration;
import com.pulumi.aws.s3.BucketWebsiteConfigurationArgs;
import com.pulumi.aws.s3.inputs.BucketWebsiteConfigurationIndexDocumentArgs;

import com.pulumi.core.Output;
import com.pulumi.core.Either;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.Import;

import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.resources.ResourceArgs;

class StaticPageArgs extends ResourceArgs {
    @Import(name = "indexContent", required = true)
    private Output<String> IndexContent;

    public Output<String> indexContent() {
        return this.IndexContent;
    }

    private StaticPageArgs() {
    }

    public StaticPageArgs(Output<String> indexContent) {
        this.IndexContent = indexContent;
    }
}

class StaticPage extends ComponentResource {
    @Export(name = "endpoint", refs = { String.class }, tree = "[0]")
    public final Output<String> endpoint;

    public StaticPage(String name, StaticPageArgs args, ComponentResourceOptions opts) {
        super("sample-components:index:StaticPage", name, null, opts);

        var bucket = new Bucket(
                String.format("%s-bucket", name),
                null,
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        var bucketWebsite = new BucketWebsiteConfiguration(
                String.format("%s-website", name),
                BucketWebsiteConfigurationArgs.builder()
                        .bucket(bucket.id())
                        .indexDocument(
                                BucketWebsiteConfigurationIndexDocumentArgs.builder()
                                        .suffix("index.html")
                                        .build())
                        .build(),
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        var bucketObject = new BucketObject(
                String.format("%s-index-object", name),
                BucketObjectArgs.builder()
                        .bucket(bucket.bucket())
                        .key("index.html")
                        .content(args.indexContent())
                        .contentType("text/html")
                        .build(),
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        var publicAccessBlock = new BucketPublicAccessBlock(
                String.format("%s-public-access-block", name),
                BucketPublicAccessBlockArgs.builder()
                        .bucket(bucket.id())
                        .blockPublicAcls(false)
                        .blockPublicPolicy(false)
                        .ignorePublicAcls(false)
                        .restrictPublicBuckets(false)
                        .build(),
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        var policyJson = bucket.arn().applyValue(bucketArn ->
            "{\n" +
            "  \"Version\": \"2012-10-17\",\n" +
            "  \"Statement\": [\n" +
            "    {\n" +
            "      \"Sid\": \"PublicReadGetObject\",\n" +
            "      \"Effect\": \"Allow\",\n" +
            "      \"Principal\": \"*\",\n" +
            "      \"Action\": \"s3:GetObject\",\n" +
            "      \"Resource\": \"" + bucketArn + "/*\"\n" +
            "    }\n" +
            "  ]\n" +
            "}"
        );

        var bucketPolicy = new BucketPolicy(
                String.format("%s-bucket-policy", name),
                BucketPolicyArgs.builder()
                        .bucket(bucket.id())
                        .policy(policyJson.applyValue(Either::ofLeft))
                        .build(),
                CustomResourceOptions.builder()
                        .parent(this)
                        .dependsOn(publicAccessBlock)
                        .build());

        this.endpoint = bucketWebsite.websiteEndpoint();

        this.registerOutputs(Map.of(
                "endpoint", bucketWebsite.websiteEndpoint()));
    }
}
