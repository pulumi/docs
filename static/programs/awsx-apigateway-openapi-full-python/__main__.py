import json
import pulumi
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI("api", apigateway.RestAPIArgs(
    swagger_string=json.dumps(
        {
            "swagger": "2.0",
            "info": {
                "title": "example",
                "version": "1.0",
            },
            "paths": {
                "/": {
                    "get": {
                        "x-amazon-apigateway-integration": {
                            "httpMethod": "GET",
                            "passthroughBehavior": "when_no_match",
                            "type": "http_proxy",
                            "uri": "https://httpbin.org/uuid",
                        },
                    },
                },
            },
            "x-amazon-apigateway-binary-media-types": ["*/*"],
        }
    )),
)

pulumi.export("url", api.url)
