---
title: Pulumi for Terraform Users
layout: terraform
url: /terraform

benefits:
  title: The benefits of using Pulumi
  items:
    - title: Tame cloud complexity
      icon: code-window
      icon_color: salmon
      description: |
        Deliver infrastructure from 50+ cloud and SaaS providers. Pulumi’s SDKs provide a complete and consistent interface that offers full access to
        clouds and abstracts complexity.

    - title: Bring the cloud closer to application development
      icon: download-from-cloud
      icon_color: violet
      description: |
        Build reusable cloud infrastructure and infrastructure platforms that empower
        developers to build modern cloud applications faster and with less overhead.

    - title: Use engineering practices with infrastructure
      icon: exchange
      icon_color: blue
      description: |
        Use engineering practices with infrastructure” to: “Replace inefficient, manual infrastructure processes with automation.
        Test and deliver infrastructure through CI/CD workflows or automate deployments with code at runtime.
    - title: Foster collaboration and innovate faster
      icon: lightning
      icon_color: yellow
      description: |
        Unite infrastructure teams, developers, and security teams around shared languages and tools so that everyone can ship products quickly and reliably.

meta_desc: How to migrate to Pulumi from Terraform for huge productivity gains, and a unified programming model for Devs and DevOps.
hero_form:
    hubspot_form_id: 123cfbdb-9ce4-4d33-a9b7-c30302463d7a
    headline: Need help converting?
contact_us_form:
    section_id: contact-us
    hubspot_form_id: 123cfbdb-9ce4-4d33-a9b7-c30302463d7a
    headline: Need assistance?
    quote:
        title: See how top engineering teams enable developers and operators to work better together with Pulumi.
        name: Kim Hamilton
        name_title: CTO, Learning Machine
        content: |
            Pulumi has given our team the tools and framework to achieve a unified development and DevOps model,
            boosting productivity and taking our business to any cloud environment that our customers need. We
            retired 25,000 lines of complex code that few team members understood and replaced it with 100s of
            lines in a familiar programming language.
examples:
    one:
        ts: |
            import * as aws from "@pulumi/aws";
            import { readdirSync } from "fs";
            import { join as pathjoin } from "path";

            const bucket = new aws.s3.Bucket("mybucket");
            const folder = "./files";
            let files = readdirSync(folder);

            for (let file of files) {
                const object = new aws.s3.BucketObject(file, {
                    bucket: bucket,
                    source: new pulumi.FileAsset(pathjoin(folder, file))
                });
            }

            export const bucketname = bucket.id;
        tf: |
            resource "aws_s3_bucket" "mybucket" {
                bucket_prefix = "mybucket"
            }

            resource "aws_s3_bucket_object" "data_txt" {
                key        = "data.txt"
                bucket     = "${aws_s3_bucket.mybucket.id}"
                source     = "./files/data.txt"
            }

            resource "aws_s3_bucket_object" "index_html" {
                key        = "index.html"
                bucket     = "${aws_s3_bucket.mybucket.id}"
                source     = "./files/index.html"
            }

            resource "aws_s3_bucket_object" "index_js" {
                key        = "index.js"
                bucket     = "${aws_s3_bucket.mybucket.id}"
                source     = "./files/index.js"
            }

            resource "aws_s3_bucket_object" "main.css" {
                key        = "main.css"
                bucket     = "${aws_s3_bucket.mybucket.id}"
                source     = "./files/main.css"
            }

            resource "aws_s3_bucket_object" "favicon.ico" {
                key        = "favicon.ico"
                bucket     = "${aws_s3_bucket.mybucket.id}"
                source     = "./files/favicon.ico"
            }
    two:
        ts: |
            import * as aws from "@pulumi/aws";

            // Create an S3 Bucket.
            const bucket = new aws.s3.Bucket("mybucket");

            // Register a Lambda to handle the Bucket notification.
            bucket.onObjectCreated("newObj", async (ev, ctx) => {
                // Write code inline, or use a Zip
                console.log(JSON.stringify(ev));
            });

            // Export the bucket name for easy scripting.
            export const bucketName = bucket.id;
        tf: |
            resource "aws_s3_bucket" "mybucket" {
                bucket_prefix = "mybucket"
            }

            data "archive_file" "lambda_zip" {
                type        = "zip"
                output_path = "lambda.zip"

                source {
                    filename = "index.js"
                    content = < {
                        console.log(JSON.stringify(ev))
                    }
                    EOF
                }
            }

            data "aws_iam_policy_document" "lambda-assume-role-policy" {
                statement {
                    actions = ["sts:AssumeRole"]

                    principals {
                        type        = "Service"
                        identifiers = ["lambda.amazonaws.com"]
                    }
                }
            }

            resource "aws_iam_role" "lambda" {
                assume_role_policy = "${data.aws_iam_policy_document.lambda-assume-role-policy.json}"
            }

            resource "aws_lambda_function" "my_lambda" {
                filename = "${data.archive_file.lambda_zip.output_path}"
                source_code_hash = "${data.archive_file.lambda_zip.output_base64sha256}"
                function_name = "my_lambda"
                role = "${aws_iam_role.lambda.arn}"
                handler = "index.handler"
                runtime = "nodejs8.10"
            }

            resource "aws_lambda_permission" "allow_bucket" {
                statement_id  = "AllowExecutionFromS3Bucket"
                action        = "lambda:InvokeFunction"
                function_name = "${aws_lambda_function.my_lambda.arn}"
                principal     = "s3.amazonaws.com"
                source_arn    = "${aws_s3_bucket.mybucket.arn}"
            }

            resource "aws_s3_bucket_notification" "bucket_notification" {
                bucket = "${aws_s3_bucket.mybucket.id}"

                lambda_function {
                    lambda_function_arn = "${aws_lambda_function.my_lambda.arn}"
                    events              = ["s3:ObjectCreated:*"]
                }
            }

            output "bucket_name" {
                value = "${aws_s3_bucket.mybucket.id}"
            }
---
