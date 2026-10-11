package myproject;

import java.util.List;

import com.pulumi.Pulumi;
import com.pulumi.core.Either;
import com.pulumi.core.Output;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
import com.pulumi.aws.acm.Certificate;
import com.pulumi.aws.acm.CertificateArgs;
import com.pulumi.aws.acm.CertificateValidation;
import com.pulumi.aws.acm.CertificateValidationArgs;
import com.pulumi.aws.apigateway.BasePathMapping;
import com.pulumi.aws.apigateway.BasePathMappingArgs;
import com.pulumi.aws.apigateway.DomainName;
import com.pulumi.aws.apigateway.DomainNameArgs;
import com.pulumi.aws.route53.Record;
import com.pulumi.aws.route53.RecordArgs;
import com.pulumi.aws.route53.Route53Functions;
import com.pulumi.aws.route53.inputs.GetZoneArgs;
import com.pulumi.aws.route53.inputs.RecordAliasArgs;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var hostedZoneName = "example.com";
            var domainName = String.format("myapp.%s", hostedZoneName);

            var zone = Route53Functions.getZone(GetZoneArgs.builder()
                .name(hostedZoneName)
                .build());

            var usEast1 = new Provider("us-east-1", ProviderArgs.builder()
                .region("us-east-1")
                .build());

            var certificate = new Certificate("cert", CertificateArgs.builder()
                .domainName(domainName)
                .validationMethod("DNS")
                .build(), CustomResourceOptions.builder()
                    .provider(usEast1)
                    .build());

            var validationOption = certificate.domainValidationOptions().applyValue(o -> o.get(0));
            var validationRecord = new Record("certificate-validation-record", RecordArgs.builder()
                .name(validationOption.apply(o -> Output.of(o.resourceRecordName().get())))
                .type(validationOption.apply(o -> Output.of(Either.ofLeft(o.resourceRecordType().get()))))
                .zoneId(zone.applyValue(z -> z.zoneId()))
                .records(validationOption.applyValue(o -> List.of(o.resourceRecordValue().get())))
                .ttl(60)
                .build());

            var validation = new CertificateValidation("certificate-validation", CertificateValidationArgs.builder()
                .certificateArn(certificate.arn())
                .validationRecordFqdns(validationRecord.fqdn().applyValue(fqdn -> List.of(fqdn)))
                .build(), CustomResourceOptions.builder()
                    .provider(usEast1)
                    .build());

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .localPath("www")
                    .build()
                })
            .build());

            var gatewayDomainName = new DomainName("gateway-domain-name", DomainNameArgs.builder()
                .certificateArn(certificate.arn())
                .domainName(domainName)
                .build(), CustomResourceOptions.builder()
                    .dependsOn(List.of(validation))
                    .build());

            var gatewayDNSRecord = new Record("gateway-dns-record", RecordArgs.builder()
                .zoneId(zone.applyValue(z -> z.zoneId()))
                .type("A")
                .name(domainName)
                .aliases(RecordAliasArgs.builder()
                    .name(gatewayDomainName.cloudfrontDomainName())
                    .zoneId(gatewayDomainName.cloudfrontZoneId())
                    .evaluateTargetHealth(false)
                    .build())
                .build());

            var basePathMapping = new BasePathMapping("gateway-path-mapping", BasePathMappingArgs.builder()
                .restApi(api.api().apply(v -> v.id()))
                .stageName(api.stage().apply(n -> n.stageName()))
                .domainName(gatewayDomainName.domainName())
                .build());

            ctx.export("url", Output.format("https://%s", basePathMapping.domainName()));
        });
    }
}
