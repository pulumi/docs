import pulumi_aws as aws

zone = aws.route53.Zone("zone",
    name="example.com",
)

certificate = aws.acm.Certificate("cert",
    domain_name="example.com",
    validation_method="DNS",
)

# Using apply to access nested output values
cert_validation_apply = aws.route53.Record("certValidationApply",
    name=certificate.domain_validation_options.apply(
        lambda domain_validation_options: domain_validation_options[0].resource_record_name
    ),
    type=certificate.domain_validation_options.apply(
        lambda domain_validation_options: domain_validation_options[0].resource_record_type
    ),
    zone_id=zone.zone_id,
    ttl=60,
    records=[
        certificate.domain_validation_options.apply(
            lambda domain_validation_options: domain_validation_options[0].resource_record_value
        )
    ],
)

# Using lifting to access nested output values
cert_validation_lifting = aws.route53.Record("certValidationLifting",
    name=certificate.domain_validation_options[0].resource_record_name,
    type=certificate.domain_validation_options[0].resource_record_type,
    zone_id=zone.zone_id,
    ttl=60,
    records=[
        certificate.domain_validation_options[0].resource_record_value
    ],
)
