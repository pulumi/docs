import pulumi
import pulumi_aws as aws

certificate = aws.acm.Certificate('cert',
    domain_name='example.com',
    validation_method='DNS'
)