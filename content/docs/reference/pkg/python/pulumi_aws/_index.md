---
---

<div class="section" id="pulumi-aws">
<h1>Pulumi AWS<a class="headerlink" href="#pulumi-aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="acm/">acm</a></li>
<li class="toctree-l1"><a class="reference internal" href="acmpca/">acmpca</a></li>
<li class="toctree-l1"><a class="reference internal" href="apigateway/">apigateway</a></li>
<li class="toctree-l1"><a class="reference internal" href="appautoscaling/">appautoscaling</a></li>
<li class="toctree-l1"><a class="reference internal" href="applicationloadbalancing/">applicationloadbalancing</a></li>
<li class="toctree-l1"><a class="reference internal" href="appmesh/">appmesh</a></li>
<li class="toctree-l1"><a class="reference internal" href="appsync/">appsync</a></li>
<li class="toctree-l1"><a class="reference internal" href="athena/">athena</a></li>
<li class="toctree-l1"><a class="reference internal" href="autoscaling/">autoscaling</a></li>
<li class="toctree-l1"><a class="reference internal" href="backup/">backup</a></li>
<li class="toctree-l1"><a class="reference internal" href="batch/">batch</a></li>
<li class="toctree-l1"><a class="reference internal" href="budgets/">budgets</a></li>
<li class="toctree-l1"><a class="reference internal" href="cfg/">cfg</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloud9/">cloud9</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloudformation/">cloudformation</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloudfront/">cloudfront</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloudhsmv2/">cloudhsmv2</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloudtrail/">cloudtrail</a></li>
<li class="toctree-l1"><a class="reference internal" href="cloudwatch/">cloudwatch</a></li>
<li class="toctree-l1"><a class="reference internal" href="codebuild/">codebuild</a></li>
<li class="toctree-l1"><a class="reference internal" href="codecommit/">codecommit</a></li>
<li class="toctree-l1"><a class="reference internal" href="codedeploy/">codedeploy</a></li>
<li class="toctree-l1"><a class="reference internal" href="codepipeline/">codepipeline</a></li>
<li class="toctree-l1"><a class="reference internal" href="cognito/">cognito</a></li>
<li class="toctree-l1"><a class="reference internal" href="cur/">cur</a></li>
<li class="toctree-l1"><a class="reference internal" href="datapipeline/">datapipeline</a></li>
<li class="toctree-l1"><a class="reference internal" href="datasync/">datasync</a></li>
<li class="toctree-l1"><a class="reference internal" href="dax/">dax</a></li>
<li class="toctree-l1"><a class="reference internal" href="devicefarm/">devicefarm</a></li>
<li class="toctree-l1"><a class="reference internal" href="directconnect/">directconnect</a></li>
<li class="toctree-l1"><a class="reference internal" href="directoryservice/">directoryservice</a></li>
<li class="toctree-l1"><a class="reference internal" href="dlm/">dlm</a></li>
<li class="toctree-l1"><a class="reference internal" href="dms/">dms</a></li>
<li class="toctree-l1"><a class="reference internal" href="docdb/">docdb</a></li>
<li class="toctree-l1"><a class="reference internal" href="dynamodb/">dynamodb</a></li>
<li class="toctree-l1"><a class="reference internal" href="ebs/">ebs</a></li>
<li class="toctree-l1"><a class="reference internal" href="ec2/">ec2</a></li>
<li class="toctree-l1"><a class="reference internal" href="ec2clientvpn/">ec2clientvpn</a></li>
<li class="toctree-l1"><a class="reference internal" href="ec2transitgateway/">ec2transitgateway</a></li>
<li class="toctree-l1"><a class="reference internal" href="ecr/">ecr</a></li>
<li class="toctree-l1"><a class="reference internal" href="ecs/">ecs</a></li>
<li class="toctree-l1"><a class="reference internal" href="efs/">efs</a></li>
<li class="toctree-l1"><a class="reference internal" href="eks/">eks</a></li>
<li class="toctree-l1"><a class="reference internal" href="elasticache/">elasticache</a></li>
<li class="toctree-l1"><a class="reference internal" href="elasticbeanstalk/">elasticbeanstalk</a></li>
<li class="toctree-l1"><a class="reference internal" href="elasticloadbalancing/">elasticloadbalancing</a></li>
<li class="toctree-l1"><a class="reference internal" href="elasticloadbalancingv2/">elasticloadbalancingv2</a></li>
<li class="toctree-l1"><a class="reference internal" href="elasticsearch/">elasticsearch</a></li>
<li class="toctree-l1"><a class="reference internal" href="elastictranscoder/">elastictranscoder</a></li>
<li class="toctree-l1"><a class="reference internal" href="emr/">emr</a></li>
<li class="toctree-l1"><a class="reference internal" href="gamelift/">gamelift</a></li>
<li class="toctree-l1"><a class="reference internal" href="glacier/">glacier</a></li>
<li class="toctree-l1"><a class="reference internal" href="globalaccelerator/">globalaccelerator</a></li>
<li class="toctree-l1"><a class="reference internal" href="glue/">glue</a></li>
<li class="toctree-l1"><a class="reference internal" href="guardduty/">guardduty</a></li>
<li class="toctree-l1"><a class="reference internal" href="iam/">iam</a></li>
<li class="toctree-l1"><a class="reference internal" href="inspector/">inspector</a></li>
<li class="toctree-l1"><a class="reference internal" href="iot/">iot</a></li>
<li class="toctree-l1"><a class="reference internal" href="kinesis/">kinesis</a></li>
<li class="toctree-l1"><a class="reference internal" href="kms/">kms</a></li>
<li class="toctree-l1"><a class="reference internal" href="lambda_/">lambda</a></li>
<li class="toctree-l1"><a class="reference internal" href="licensemanager/">licensemanager</a></li>
<li class="toctree-l1"><a class="reference internal" href="lightsail/">lightsail</a></li>
<li class="toctree-l1"><a class="reference internal" href="macie/">macie</a></li>
<li class="toctree-l1"><a class="reference internal" href="mediapackage/">mediapackage</a></li>
<li class="toctree-l1"><a class="reference internal" href="mediastore/">mediastore</a></li>
<li class="toctree-l1"><a class="reference internal" href="mq/">mq</a></li>
<li class="toctree-l1"><a class="reference internal" href="msk/">msk</a></li>
<li class="toctree-l1"><a class="reference internal" href="neptune/">neptune</a></li>
<li class="toctree-l1"><a class="reference internal" href="opsworks/">opsworks</a></li>
<li class="toctree-l1"><a class="reference internal" href="organizations/">organizations</a></li>
<li class="toctree-l1"><a class="reference internal" href="pinpoint/">pinpoint</a></li>
<li class="toctree-l1"><a class="reference internal" href="pricing/">pricing</a></li>
<li class="toctree-l1"><a class="reference internal" href="ram/">ram</a></li>
<li class="toctree-l1"><a class="reference internal" href="rds/">rds</a></li>
<li class="toctree-l1"><a class="reference internal" href="redshift/">redshift</a></li>
<li class="toctree-l1"><a class="reference internal" href="resourcegroups/">resourcegroups</a></li>
<li class="toctree-l1"><a class="reference internal" href="route53/">route53</a></li>
<li class="toctree-l1"><a class="reference internal" href="s3/">s3</a></li>
<li class="toctree-l1"><a class="reference internal" href="sagemaker/">sagemaker</a></li>
<li class="toctree-l1"><a class="reference internal" href="secretsmanager/">secretsmanager</a></li>
<li class="toctree-l1"><a class="reference internal" href="securityhub/">securityhub</a></li>
<li class="toctree-l1"><a class="reference internal" href="servicecatalog/">servicecatalog</a></li>
<li class="toctree-l1"><a class="reference internal" href="servicediscovery/">servicediscovery</a></li>
<li class="toctree-l1"><a class="reference internal" href="servicequotas/">servicequotas</a></li>
<li class="toctree-l1"><a class="reference internal" href="ses/">ses</a></li>
<li class="toctree-l1"><a class="reference internal" href="sfn/">sfn</a></li>
<li class="toctree-l1"><a class="reference internal" href="shield/">shield</a></li>
<li class="toctree-l1"><a class="reference internal" href="simpledb/">simpledb</a></li>
<li class="toctree-l1"><a class="reference internal" href="sns/">sns</a></li>
<li class="toctree-l1"><a class="reference internal" href="sqs/">sqs</a></li>
<li class="toctree-l1"><a class="reference internal" href="ssm/">ssm</a></li>
<li class="toctree-l1"><a class="reference internal" href="storagegateway/">storagegateway</a></li>
<li class="toctree-l1"><a class="reference internal" href="swf/">swf</a></li>
<li class="toctree-l1"><a class="reference internal" href="transfer/">transfer</a></li>
<li class="toctree-l1"><a class="reference internal" href="waf/">waf</a></li>
<li class="toctree-l1"><a class="reference internal" href="wafregional/">wafregional</a></li>
<li class="toctree-l1"><a class="reference internal" href="worklink/">worklink</a></li>
<li class="toctree-l1"><a class="reference internal" href="workspaces/">workspaces</a></li>
<li class="toctree-l1"><a class="reference internal" href="xray/">xray</a></li>
</ul>
</div>
</div>
