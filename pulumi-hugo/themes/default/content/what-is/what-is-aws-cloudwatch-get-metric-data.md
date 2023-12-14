---
title: Dynamic Credentials with "aws cloudwatch get-metric-data"
meta_desc: |
     Use Pulumi ESC Dynamic Credentials to run aws cloudwatch get-metric-data.

type: what-is
page_title: Dynamic Credentials with "aws cloudwatch get-metric-data"
---


{{% notes type="warn" %}}
TODO - copy contents once finalized.
{{% /notes %}}

The `aws cloudwatch get-metric-data` command is part of the AWS Command Line Interface (CLI), and it retrieves metric data from Amazon CloudWatch. This command allows you to query and retrieve time-series data for a specified metric or set of metrics.

### Step 5: Create sample metric data

You will need to add metric data if you do not already have it. With your environment set up, validate your configuration by adding sample metric data. First, make sure that your local environment does not have any AWS credentials configured. You can do this by running the `aws configure list` command as shown below:

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key                <not set>             None    None
secret_key                <not set>             None    None
    region                <not set>             None    None
```

To add the metrics, run the command using `esc run` as shown below, making sure to replace `<your-pulumi-org-name>`, `<your-environment-name>`, and `<aws-region>` with the names of your own Pulumi organization, ESC environment, and AWS Region, respectively.

```bash
$  esc run <your-pulumi-org-name>/<your-environment-name> -- aws cloudwatch put-metric-data --namespace pulumiDemo --metric-name Invocations --dimensions FunctionName=helloWorld --value 10 --unit Count --timestamp 2023-12-12T04:00:00Z --region <aws-region>
$  esc run <your-pulumi-org-name>/<your-environment-name> -- aws cloudwatch put-metric-data --namespace pulumiDemo --metric-name Invocations --dimensions FunctionName=helloWorld --value 10 --unit Count --timestamp 2023-12-12T04:05:00Z --region <aws-region>
$  esc run <your-pulumi-org-name>/<your-environment-name> -- aws cloudwatch put-metric-data --namespace pulumiDemo --metric-name Errors --dimensions FunctionName=helloWorld --value 9 --unit Count --timestamp 2023-12-12T04:15:00Z --region <aws-region>
$  esc run <your-pulumi-org-name>/<your-environment-name> -- aws cloudwatch put-metric-data --namespace pulumiDemo --metric-name Errors --dimensions FunctionName=helloWorld --value 1 --unit Count --timestamp 2023-12-12T04:20:00Z --region <aws-region>
```

### Step 6: Create a sample metric data query file

Create a file named `sampleQuery.json` to contain three sample queries.

```bash
$ cat <<EOF> sampleQuery.json
[
    {
        "Id": "e1",
        "Expression": "m1 / m2",
        "Label": "ErrorRate"
    },
    {
        "Id": "m1",
        "MetricStat": {
            "Metric": {
                "Namespace": "pulumiDemo",
                "MetricName": "Errors",
                "Dimensions": [
                    {
                        "Name": "FunctionName",
                        "Value": "helloWorld"
                    }
                ]
            },
            "Period": 300,
            "Stat": "Sum",
            "Unit": "Count"
        },
        "ReturnData": false
    },
    {
        "Id": "m2",
        "MetricStat": {
            "Metric": {
                "Namespace": "pulumiDemo",
                "MetricName": "Invocations",
                "Dimensions": [
                    {
                        "Name": "FunctionName",
                        "Value": "helloWorld"
                    }
                ]
            },
            "Period": 300,
            "Stat": "Sum",
            "Unit": "Count"
        },
        "ReturnData": false
    }
]
EOF
```

### Step 7: Run aws cloudwatch get-metric-data

At this point, you have validated your environment, added sample data, and added queries.

To get the metrics, run the command using `esc run` as shown below, making sure to replace `<your-pulumi-org-name>`, `<your-environment-name>`, and `<aws-region>` with the names of your own Pulumi organization, ESC environment, and AWS Region, respectively.

```bash
$ esc run <your-pulumi-org-name>/<your-environment-name> -- aws cloudwatch get-metric-data --metric-data-queries file://./sampleQuery.json --start-time 2023-12-12T04:00:00Z --end-time 2023-12-12T04:30:00Z  --region <aws-region>
```

Then validate that your output is similar to the following:

```bash
TODO
```

## Conclusion

{{% notes type="warn" %}}
TODO - copy contents once finalized.
{{% /notes %}}
