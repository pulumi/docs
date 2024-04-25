import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

hosted_zone_name = "example.com"
domain_name = f"myapp.{hosted_zone_name}"

# Look up your existing Route 53 hosted zone.
zone = aws.route53.get_zone(name=hosted_zone_name)

us_east_1 = aws.Provider(
    "us-east-1",
    aws.ProviderArgs(
        region="us-east-1",
    ),
)

# Provision a new ACM certificate.
certificate = aws.acm.Certificate(
    "certificate",
    aws.acm.CertificateArgs(
        domain_name=domain_name,
        validation_method="DNS",
    ),
    opts=pulumi.ResourceOptions(provider=us_east_1),
)

validation_option = certificate.domain_validation_options[0]
validation_record = aws.route53.Record(
    "certificate-validation-record",
    aws.route53.RecordArgs(
        name=validation_option["resource_record_name"],
        type=validation_option["resource_record_type"],
        records=[validation_option["resource_record_value"]],
        zone_id=zone.zone_id,
        ttl=60,
    ),
)

validation = aws.acm.CertificateValidation(
    "certificate-validation",
    aws.acm.CertificateValidationArgs(
        certificate_arn=certificate.arn,
        validation_record_fqdns=[validation_record.fqdn],
    ),
    opts=pulumi.ResourceOptions(provider=us_east_1),
)

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            local_path="www",
        )
    ],
)

gatewayDomainName = aws.apigateway.DomainName(
    "gateway-domain-name",
    aws.apigateway.DomainNameArgs(
        certificate_arn=certificate.arn,
        domain_name=domain_name,
    ),
    opts=pulumi.ResourceOptions(depends_on=validation),
)

gateway_dns_record = aws.route53.Record(
    "gateway-dns-record",
    aws.route53.RecordArgs(
        zone_id=zone.zone_id,
        type="A",
        name=domain_name,
        aliases=[
            aws.route53.RecordAliasArgs(
                name=gatewayDomainName.cloudfront_domain_name,
                zone_id=gatewayDomainName.cloudfront_zone_id,
                evaluate_target_health=False,
            )
        ],
    ),
)

base_path_mapping = aws.apigateway.BasePathMapping(
    "gateway-path-mapping",
    aws.apigateway.BasePathMappingArgs(
        rest_api=api.api.id,
        stage_name=api.stage.stage_name,
        domain_name=gatewayDomainName.domain_name,
    ),
)

pulumi.export("url", pulumi.Output.concat("https://", base_path_mapping.domain_name))
