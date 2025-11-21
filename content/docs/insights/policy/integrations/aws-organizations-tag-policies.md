---
title_tag: "AWS Organizations Tag Policies | Pulumi Policy"
meta_desc: Enforce AWS Organizations Tag Policies on infrastructure as code, blocking deployments with missing required tags.
title: AWS Organizations Tag Policies
h1: AWS Organizations Tag Policies
weight: 2
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    insights:
        name: AWS Organizations Tag Policies
        parent: integrations
        weight: 2
---

## Overview

The [AWS Organizations Tag Policies policy pack](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/) is a pre-built policy pack that integrates Pulumi with AWS Organizations. This integration validates your infrastructure as code against Tag Policies configured in AWS Organizations, blocking deployments when required tags are missing. For more information about enforcing tag policies with AWS Organizations Tag Policies, see the [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html).

## How it works

1. **Configure tag policies in AWS Organizations**: Define your required tags using tag policies, specifying which tags are mandatory for which resource types. The pack reads all tag requirements specified by the `report_required_tag_for` field in your tag policy configuration.
1. **Enable the pack in Pulumi Cloud**: Add the AWS Organizations Tag Policies pack to your Pulumi organization, and configure a policy group. The pack supports two enforcement levels: advisory mode (warns about missing tags without blocking deployments) and mandatory mode (blocks non-compliant deployments).
1. **Validation during deployment**: When you run `pulumi up`, the policy pack retrieves your tag policy requirements from AWS and validates that resources have the specified tags.
1. **Enforcement levels**: Start in advisory mode to surface violations without blocking deployments. All policy violations are displayed in the Pulumi Cloud [Policy Findings](/docs/insights/policy/policy-findings/) page for monitoring and tracking, enabling a controlled migration to compliance. Once your Pulumi programs are compliant, switch to mandatory mode to block any future non-compliant deployments.

The pack uses AWS Organizations tag policies as the source of truth. Tag requirements are managed in AWS, not in Pulumi configuration.

## Prerequisites

Before using this policy pack, complete the following setup in AWS:

### Configure tag policies in AWS Organizations

Tag policies must be configured in your AWS Organization to define which tags are required for your resources. For detailed instructions, see the [AWS Organizations Tag Policies documentation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html).

### Grant required permissions

The AWS credentials used by your Pulumi stack must have permission to call the AWS Resource Groups Tagging API. Add the following IAM policy to the role or user running Pulumi deployments:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "resourcegroupstaggingapi:ListRequiredTags",
      "Resource": "*"
    }
  ]
}
```

The policy pack will use the same AWS credentials configured for your stack to fetch the required tags configuration.

## Enabling the pack

To enable this policy pack for your organization:

1. From within your organization, navigate to the **Policies** tab
1. Under Policy Packs, select the **Available** tab
1. Select **AWS Organizations Tag Policies** and select **Add to organization**
1. From the Organizations tab, apply the policy to a Policy Group to enforce tag validation

For more information about enabling policy packs, see [Pre-Built Packs](/docs/insights/policy/policy-packs/pre-built-packs/).

## Policy reference

This pack includes a single resource policy:

| Policy Name | Description | Default Enforcement Level | Severity |
| ----- | ----- | ----- | ----- |
| aws-tag-policies-compliance-validation | Validates that resources have required tags as defined in AWS Organizations Tag Policies | advisory | low |

## Supported resources

The pack works with both the AWS (`pulumi/aws`) and AWS Native (`pulumi/aws-native`) Pulumi providers.

### AWS Native Provider types

The AWS Native Provider (`pulumi/aws-native`) is based on AWS Cloud Control, and hence is natively supported by the AWS Organizations Tag Policies report_required_tag_for setting. For a complete list of supported resource types, see [Supported resources for tag policies enforcement](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_supported-resources-enforcement.html) in the AWS documentation.

### AWS Provider types

The AWS Provider (`pulumi/aws`) uses different resource type naming conventions than AWS Cloud Control. The pack automatically maps AWS tag policy resource types (specified in `report_required_tag_for`) to their corresponding Pulumi AWS resource types. The following table shows the supported mappings:

| AWS report_required_tag_for | Pulumi Types |
|------------------------------|--------------|
| access-analyzer:analyzer | aws:accessanalyzer/analyzer:Analyzer |
| acm-pca:certificate-authority | aws:acmpca/certificateAuthority:CertificateAuthority |
| acm:certificate | aws:acm/certificate:Certificate |
| airflow:environment | aws:mwaa/environment:Environment |
| amplify:apps | aws:amplify/app:App |
| aoss:collection | aws:opensearch/serverlessCollection:ServerlessCollection |
| app-integrations:data-integration | aws:appintegrations/dataIntegration:DataIntegration |
| app-integrations:event-integration | aws:appconfig/eventIntegration:EventIntegration |
| appconfig:application | aws:appconfig/application:Application |
| appconfig:application/configurationprofile | aws:appconfig/configurationProfile:ConfigurationProfile |
| appconfig:application/environment | aws:appconfig/environment:Environment |
| appconfig:deploymentstrategy | aws:appconfig/deploymentStrategy:DeploymentStrategy |
| appconfig:extension | aws:appconfig/extension:Extension |
| appflow:flow | aws:appflow/flow:Flow |
| applicationinsights:application | aws:applicationinsights/application:Application |
| appmesh:mesh | aws:appmesh/mesh:Mesh |
| appmesh:mesh/virtualGateway | aws:appmesh/virtualGateway:VirtualGateway |
| appmesh:mesh/virtualGateway/gatewayRoute | aws:appmesh/gatewayRoute:GatewayRoute |
| appmesh:mesh/virtualNode | aws:appmesh/virtualNode:VirtualNode |
| appmesh:mesh/virtualRouter | aws:appmesh/virtualRouter:VirtualRouter |
| appmesh:mesh/virtualRouter/route | aws:appmesh/route:Route |
| appmesh:mesh/virtualService | aws:appmesh/virtualService:VirtualService |
| apprunner:autoscalingconfiguration | aws:apprunner/autoScalingConfigurationVersion:AutoScalingConfigurationVersion |
| apprunner:observabilityconfiguration | aws:apprunner/observabilityConfiguration:ObservabilityConfiguration |
| apprunner:service | aws:apprunner/service:Service |
| apprunner:vpcconnector | aws:apprunner/vpcConnector:VpcConnector |
| apprunner:vpcingressconnection | aws:apprunner/vpcIngressConnection:VpcIngressConnection |
| appstream:fleet | aws:appstream/fleet:Fleet |
| appstream:image-builder | aws:appstream/imageBuilder:ImageBuilder |
| appstream:stack | aws:appstream/stack:Stack |
| aps:rulegroupsnamespace | aws:amp/ruleGroupNamespace:RuleGroupNamespace |
| aps:workspace | aws:amp/workspace:Workspace |
| athena:capacity-reservation | aws:athena/capacityReservation:CapacityReservation |
| athena:datacatalog | aws:athena/dataCatalog:DataCatalog |
| athena:workgroup | aws:athena/workgroup:Workgroup |
| auditmanager:assessment | aws:auditmanager/assessment:Assessment |
| backup:backup-plan | aws:backup/plan:Plan |
| backup:framework | aws:backup/framework:Framework |
| backup:report-plan | aws:backup/reportPlan:ReportPlan |
| backup:restore-testing-plan | aws:backup/restoreTestingPlan:RestoreTestingPlan |
| batch:compute-environment | aws:batch/computeEnvironment:ComputeEnvironment |
| batch:job-definition | aws:batch/jobDefinition:JobDefinition |
| batch:job-queue | aws:batch/jobQueue:JobQueue |
| batch:scheduling-policy | aws:batch/schedulingPolicy:SchedulingPolicy |
| bcm-data-exports:export | aws:bcmdata/export:Export |
| bedrock:agent | aws:bedrock/agentAgent:AgentAgent |
| bedrock:agent-alias | aws:bedrock/agentAgentAlias:AgentAgentAlias |
| bedrock:application-inference-profile | aws:bedrock/inferenceProfile:InferenceProfile |
| bedrock:flow | aws:bedrock/agentFlow:AgentFlow |
| bedrock:guardrail | aws:bedrock/guardrail:Guardrail |
| bedrock:knowledge-base | aws:bedrock/agentKnowledgeBase:AgentKnowledgeBase |
| bedrock:prompt | aws:bedrock/agentPrompt:AgentPrompt |
| budgets:budget | aws:budgets/budget:Budget |
| budgets:budget/action | aws:budgets/budgetAction:BudgetAction |
| cassandra:keyspace | aws:keyspaces/keyspace:Keyspace |
| catalog:portfolio | aws:servicecatalog/portfolio:Portfolio |
| ce:anomalymonitor | aws:costexplorer/anomalyMonitor:AnomalyMonitor |
| ce:anomalysubscription | aws:costexplorer/anomalySubscription:AnomalySubscription |
| ce:costcategory | aws:costexplorer/costCategory:CostCategory |
| cleanrooms:configuredtable | aws:cleanrooms/configuredTable:ConfiguredTable |
| cloudformation:stack | aws:cloudformation/stack:Stack |
| cloudformation:stackset | aws:cloudformation/stackSet:StackSet |
| cloudfront:distribution | aws:cloudfront/distribution:Distribution |
| cloudtrail:eventdatastore | aws:cloudtrail/eventDataStore:EventDataStore |
| cloudtrail:trail | aws:cloudtrail/trail:Trail |
| cloudwatch:alarm | aws:cloudwatch/metricAlarm:MetricAlarm |
| cloudwatch:insight-rule | aws:cloudwatch/contributorInsightRule:ContributorInsightRule |
| cloudwatch:metric-stream | aws:cloudwatch/metricStream:MetricStream |
| codeartifact:domain | aws:codeartifact/domain:Domain |
| codeartifact:repository | aws:codeartifact/repository:Repository |
| codebuild:project | aws:codebuild/project:Project |
| codebuild:report-group | aws:codebuild/reportGroup:ReportGroup |
| codecommit:repository | aws:codecommit/repository:Repository |
| codeconnections:connection | aws:codeconnections/connection:Connection |
| codedeploy:application | aws:codedeploy/application:Application |
| codeguru-profiler:profilingGroup | aws:codeguruprofiler/profilingGroup:ProfilingGroup |
| codeguru-reviewer:association | aws:codegurureviewer/repositoryAssociation:RepositoryAssociation |
| codepipeline:actiontype | aws:codepipeline/customActionType:CustomActionType |
| codepipeline:pipeline | aws:codepipeline/pipeline:Pipeline |
| codepipeline:webhook | aws:codepipeline/webhook:Webhook |
| codestar-connections:connection | aws:codestarconnections/connection:Connection |
| codestar-notifications:notificationrule | aws:codestarnotifications/notificationRule:NotificationRule |
| cognito-identity:identitypool | aws:cognito/identityPool:IdentityPool |
| cognito-idp:userpool | aws:cognito/userPool:UserPool |
| comprehend:document-classifier | aws:comprehend/documentClassifier:DocumentClassifier |
| config:aggregation-authorization | aws:cfg/aggregateAuthorization:AggregateAuthorization |
| config:config-aggregator | aws:cfg/configurationAggregator:ConfigurationAggregator |
| config:config-rule | aws:cfg/rule:Rule |
| connect:instance | aws:connect/instance:Instance |
| connect:instance/agent | aws:connect/user:User |
| connect:instance/contact-flow | aws:connect/contactFlow:ContactFlow |
| connect:instance/flow-module | aws:connect/contactFlowModule:ContactFlowModule |
| connect:instance/operating-hours | aws:connect/hoursOfOperation:HoursOfOperation |
| connect:instance/queue | aws:connect/queue:Queue |
| connect:instance/routing-profile | aws:connect/routingProfile:RoutingProfile |
| connect:instance/security-profile | aws:connect/securityProfile:SecurityProfile |
| connect:instance/transfer-destination | aws:connect/quickConnect:QuickConnect |
| connect:phone-number | aws:connect/phoneNumber:PhoneNumber |
| cur:definition | aws:cur/reportDefinition:ReportDefinition |
| datasync:task | aws:datasync/task:Task |
| datazone:domain | aws:datazone/domain:Domain |
| dax:cache | aws:dax/cluster:Cluster |
| detective:graph | aws:detective/graph:Graph |
| devicefarm:instanceprofile | aws:devicefarm/instanceProfile:InstanceProfile |
| devicefarm:project | aws:devicefarm/project:Project |
| devicefarm:testgrid-project | aws:devicefarm/testGridProject:TestGridProject |
| dlm:policy | aws:dlm/lifecyclePolicy:LifecyclePolicy |
| dms:cert | aws:dms/certificate:Certificate |
| dms:endpoint | aws:dms/endpoint:Endpoint |
| dms:es | aws:dms/eventSubscription:EventSubscription |
| dms:rep | aws:dms/replicationInstance:ReplicationInstance |
| dms:replication-config | aws:dms/replicationConfig:ReplicationConfig |
| dms:subgrp | aws:dms/replicationSubnetGroup:ReplicationSubnetGroup |
| dms:task | aws:dms/replicationTask:ReplicationTask |
| dsql:cluster | aws:dsql/cluster:Cluster |
| dynamodb:table | aws:dynamodb/table:Table |
| ec2:capacity-reservation | aws:ec2/capacityReservation:CapacityReservation |
| ec2:carrier-gateway | aws:ec2/carrierGateway:CarrierGateway |
| ec2:client-vpn-endpoint | aws:ec2clientvpn/endpoint:Endpoint |
| ec2:customer-gateway | aws:ec2/customerGateway:CustomerGateway |
| ec2:dedicated-host | aws:ec2/dedicatedHost:DedicatedHost |
| ec2:dhcp-options | aws:ec2/vpcDhcpOptions:VpcDhcpOptions |
| ec2:egress-only-internet-gateway | aws:ec2/egressOnlyInternetGateway:EgressOnlyInternetGateway |
| ec2:elastic-ip | aws:ec2/eip:Eip |
| ec2:fleet | aws:ec2/fleet:Fleet |
| ec2:instance | aws:ec2/instance:Instance |
| ec2:instance-connect-endpoint | aws:ec2transitgateway/instanceConnectEndpoint:InstanceConnectEndpoint |
| ec2:internet-gateway | aws:ec2/internetGateway:InternetGateway |
| ec2:ipam | aws:ec2/vpcIpam:VpcIpam |
| ec2:ipam-pool | aws:ec2/vpcIpamPool:VpcIpamPool |
| ec2:ipam-resource-discovery | aws:ec2/vpcIpamResourceDiscovery:VpcIpamResourceDiscovery |
| ec2:ipam-resource-discovery-association | aws:ec2/vpcIpamResourceDiscoveryAssociation:VpcIpamResourceDiscoveryAssociation |
| ec2:ipam-scope | aws:ec2/vpcIpamScope:VpcIpamScope |
| ec2:key-pair | aws:ec2/keyPair:KeyPair |
| ec2:launch-template | aws:ec2/launchTemplate:LaunchTemplate |
| ec2:local-gateway-route-table-vpc-association | aws:ec2/localGatewayRouteTableVpcAssociation:LocalGatewayRouteTableVpcAssociation |
| ec2:natgateway | aws:ec2/natGateway:NatGateway |
| ec2:network-acl | aws:ec2/networkAcl:NetworkAcl |
| ec2:network-insights-analysis | aws:ec2/networkInsightsAnalysis:NetworkInsightsAnalysis |
| ec2:network-insights-path | aws:ec2/networkInsightsPath:NetworkInsightsPath |
| ec2:network-interface | aws:ec2/networkInterface:NetworkInterface |
| ec2:placement-group | aws:ec2/placementGroup:PlacementGroup |
| ec2:prefix-list | aws:ec2/managedPrefixList:ManagedPrefixList |
| ec2:route-table | aws:ec2/routeTable:RouteTable |
| ec2:security-group | aws:ec2/securityGroup:SecurityGroup |
| ec2:spot-fleet-request | aws:ec2/spotFleetRequest:SpotFleetRequest |
| ec2:subnet | aws:ec2/subnet:Subnet |
| ec2:traffic-mirror-filter | aws:ec2/trafficMirrorFilter:TrafficMirrorFilter |
| ec2:traffic-mirror-session | aws:ec2/trafficMirrorSession:TrafficMirrorSession |
| ec2:traffic-mirror-target | aws:ec2/trafficMirrorTarget:TrafficMirrorTarget |
| ec2:transit-gateway | aws:ec2transitgateway/transitGateway:TransitGateway |
| ec2:transit-gateway-connect-peer | aws:ec2transitgateway/connectPeer:ConnectPeer |
| ec2:transit-gateway-multicast-domain | aws:ec2transitgateway/multicastDomain:MulticastDomain |
| ec2:transit-gateway-route-table | aws:ec2transitgateway/routeTable:RouteTable |
| ec2:verified-access-endpoint | aws:verifiedaccess/endpoint:Endpoint |
| ec2:verified-access-group | aws:verifiedaccess/group:Group |
| ec2:verified-access-instance | aws:verifiedaccess/instance:Instance |
| ec2:verified-access-trust-provider | aws:verifiedaccess/trustProvider:TrustProvider |
| ec2:volume | aws:ebs/volume:Volume |
| ec2:vpc | aws:ec2/vpc:Vpc |
| ec2:vpc-block-public-access-exclusion | aws:ec2/vpcBlockPublicAccessExclusion:VpcBlockPublicAccessExclusion |
| ec2:vpc-endpoint | aws:ec2/vpcEndpoint:VpcEndpoint |
| ec2:vpc-endpoint-service | aws:ec2/vpcEndpointService:VpcEndpointService |
| ec2:vpc-flow-log | aws:ec2/flowLog:FlowLog |
| ec2:vpc-peering-connection | aws:ec2/vpcPeeringConnection:VpcPeeringConnection |
| ec2:vpn-connection | aws:ec2/vpnConnection:VpnConnection |
| ec2:vpn-gateway | aws:ec2/vpnGateway:VpnGateway |
| ecr-public:repository | aws:ecrpublic/repository:Repository |
| ecr:repository | aws:ecr/repository:Repository |
| ecs:capacity-provider | aws:ecs/capacityProvider:CapacityProvider |
| ecs:cluster | aws:ecs/cluster:Cluster |
| ecs:service | aws:ecs/service:Service |
| ecs:task-definition | aws:ecs/taskDefinition:TaskDefinition |
| ecs:task-set | aws:ecs/taskSet:TaskSet |
| eks:access-entry | aws:eks/accessEntry:AccessEntry |
| eks:addon | aws:eks/addon:Addon |
| eks:cluster | aws:eks/cluster:Cluster |
| eks:fargateprofile | aws:eks/fargateProfile:FargateProfile |
| eks:identityproviderconfig | aws:eks/identityProviderConfig:IdentityProviderConfig |
| eks:nodegroup | aws:eks/nodeGroup:NodeGroup |
| eks:podidentityassociation | aws:eks/podIdentityAssociation:PodIdentityAssociation |
| elasticache:cluster | aws:elasticache/cluster:Cluster |
| elasticache:parametergroup | aws:elasticache/parameterGroup:ParameterGroup |
| elasticache:replicationgroup | aws:elasticache/replicationGroup:ReplicationGroup |
| elasticache:subnetgroup | aws:elasticache/subnetGroup:SubnetGroup |
| elasticache:user | aws:elasticache/user:User |
| elasticache:usergroup | aws:elasticache/userGroup:UserGroup |
| elasticbeanstalk:application | aws:elasticbeanstalk/application:Application |
| elasticbeanstalk:applicationversion | aws:elasticbeanstalk/applicationVersion:ApplicationVersion |
| elasticbeanstalk:environment | aws:elasticbeanstalk/environment:Environment |
| elasticfilesystem:access-point | aws:efs/accessPoint:AccessPoint |
| elasticfilesystem:file-system | aws:efs/fileSystem:FileSystem |
| elasticloadbalancing:listener | aws:alb/listener:Listener<br>aws:lb/listener:Listener |
| elasticloadbalancing:listener-rule | aws:alb/listenerRule:ListenerRule<br>aws:lb/listenerRule:ListenerRule |
| elasticloadbalancing:loadbalancer | aws:alb/loadBalancer:LoadBalancer<br>aws:lb/loadBalancer:LoadBalancer |
| elasticloadbalancing:targetgroup | aws:alb/targetGroup:TargetGroup<br>aws:lb/targetGroup:TargetGroup |
| elasticloadbalancing:truststore | aws:lb/trustStore:TrustStore |
| elasticmapreduce:cluster | aws:emr/cluster:Cluster |
| emr-containers:virtualclusters | aws:emrcontainers/virtualCluster:VirtualCluster |
| emr-serverless:applications | aws:emrserverless/application:Application |
| events:event-bus | aws:cloudwatch/eventBus:EventBus |
| events:rule | aws:cloudwatch/eventRule:EventRule |
| firehose:deliverystream | aws:kinesis/firehoseDeliveryStream:FirehoseDeliveryStream |
| fis:experiment-template | aws:fis/experimentTemplate:ExperimentTemplate |
| fsx:association | aws:fsx/dataRepositoryAssociation:DataRepositoryAssociation |
| fsx:file-system | aws:fsx/lustreFileSystem:LustreFileSystem<br>aws:fsx/ontapFileSystem:OntapFileSystem<br>aws:fsx/openZfsFileSystem:OpenZfsFileSystem<br>aws:fsx/windowsFileSystem:WindowsFileSystem |
| fsx:snapshot | aws:fsx/openZfsSnapshot:OpenZfsSnapshot |
| fsx:storage-virtual-machine | aws:fsx/ontapStorageVirtualMachine:OntapStorageVirtualMachine |
| fsx:volume | aws:fsx/ontapVolume:OntapVolume<br>aws:fsx/openZfsVolume:OpenZfsVolume |
| gamelift:alias | aws:gamelift/alias:Alias |
| gamelift:build | aws:gamelift/build:Build |
| gamelift:fleet | aws:gamelift/fleet:Fleet |
| gamelift:gameservergroup | aws:gamelift/gameServerGroup:GameServerGroup |
| gamelift:gamesessionqueue | aws:gamelift/gameSessionQueue:GameSessionQueue |
| gamelift:script | aws:gamelift/script:Script |
| geo:geofence-collection | aws:location/geofenceCollection:GeofenceCollection |
| geo:map | aws:location/map:Map |
| geo:place-index | aws:location/placeIndex:PlaceIndex |
| geo:route-calculator | aws:location/routeCalculation:RouteCalculation |
| geo:tracker | aws:location/tracker:Tracker |
| globalaccelerator:accelerator | aws:globalaccelerator/accelerator:Accelerator |
| globalaccelerator:attachment | aws:globalaccelerator/crossAccountAttachment:CrossAccountAttachment |
| glue:connection | aws:glue/connection:Connection |
| glue:crawler | aws:glue/crawler:Crawler |
| glue:dataQualityRuleset | aws:glue/dataQualityRuleset:DataQualityRuleset |
| glue:database | aws:glue/catalogDatabase:CatalogDatabase |
| glue:job | aws:glue/job:Job |
| glue:mlTransform | aws:glue/mLTransform:MLTransform |
| glue:registry | aws:glue/registry:Registry |
| glue:schema | aws:glue/schema:Schema |
| glue:trigger | aws:glue/trigger:Trigger |
| grafana:workspaces | aws:grafana/workspace:Workspace |
| guardduty:detector | aws:guardduty/detector:Detector |
| guardduty:detector/filter | aws:guardduty/filter:Filter |
| guardduty:detector/ipset | aws:guardduty/iPSet:IPSet |
| guardduty:detector/threatintelset | aws:guardduty/threatIntelSet:ThreatIntelSet |
| guardduty:malware-protection-plan | aws:guardduty/malwareProtectionPlan:MalwareProtectionPlan |
| iam:instance-profile | aws:iam/instanceProfile:InstanceProfile |
| iam:mfa | aws:iam/virtualMfaDevice:VirtualMfaDevice |
| iam:oidc-provider | aws:iam/openIdConnectProvider:OpenIdConnectProvider |
| iam:role | aws:iam/role:Role |
| iam:saml-provider | aws:iam/samlProvider:SamlProvider |
| iam:server-certificate | aws:iam/serverCertificate:ServerCertificate |
| iam:user | aws:iam/user:User |
| imagebuilder:component | aws:imagebuilder/component:Component |
| imagebuilder:container-recipe | aws:imagebuilder/containerRecipe:ContainerRecipe |
| imagebuilder:distribution-configuration | aws:imagebuilder/distributionConfiguration:DistributionConfiguration |
| imagebuilder:image | aws:imagebuilder/image:Image |
| imagebuilder:image-pipeline | aws:imagebuilder/imagePipeline:ImagePipeline |
| imagebuilder:image-recipe | aws:imagebuilder/imageRecipe:ImageRecipe |
| imagebuilder:infrastructure-configuration | aws:imagebuilder/infrastructureConfiguration:InfrastructureConfiguration |
| imagebuilder:lifecycle-policy | aws:imagebuilder/lifecyclePolicy:LifecyclePolicy |
| imagebuilder:workflow | aws:imagebuilder/workflow:Workflow |
| inspector2:filter | aws:inspector2/filter:Filter |
| internetmonitor:monitor | aws:cloudwatch/internetMonitor:InternetMonitor |
| iot:authorizer | aws:iot/authorizer:Authorizer |
| iot:billinggroup | aws:iot/billingGroup:BillingGroup |
| iot:cacert | aws:iot/caCertificate:CaCertificate |
| iot:policy | aws:iot/policy:Policy |
| iot:provisioningtemplate | aws:iot/provisioningTemplate:ProvisioningTemplate |
| iot:rolealias | aws:iot/roleAlias:RoleAlias |
| iot:rule | aws:iot/topicRule:TopicRule |
| iot:thinggroup | aws:iot/thingGroup:ThingGroup |
| iot:thingtype | aws:iot/thingType:ThingType |
| ivs:channel | aws:ivs/channel:Channel |
| ivs:playback-key | aws:ivs/playbackKeyPair:PlaybackKeyPair |
| ivs:recording-configuration | aws:ivs/recordingConfiguration:RecordingConfiguration |
| kafka:replicator | aws:msk/replicator:Replicator |
| kafkaconnect:custom-plugin | aws:mskconnect/customPlugin:CustomPlugin |
| kafkaconnect:worker-configuration | aws:mskconnect/workerConfiguration:WorkerConfiguration |
| kendra:index | aws:kendra/index:Index |
| kendra:index/data-source | aws:kendra/dataSource:DataSource |
| kinesis:stream | aws:kinesis/stream:Stream |
| kinesis:stream/consumer | aws:kinesis/streamConsumer:StreamConsumer |
| kinesisanalytics:application | aws:kinesisanalyticsv2/application:Application |
| kinesisvideo:stream | aws:kinesis/videoStream:VideoStream |
| kms:key | aws:kms/key:Key |
| lambda:code-signing-config | aws:lambda/codeSigningConfig:CodeSigningConfig |
| lambda:event-source-mapping | aws:lambda/eventSourceMapping:EventSourceMapping |
| lambda:function | aws:lambda/function:Function |
| lightsail:Bucket | aws:lightsail/bucket:Bucket |
| lightsail:Certificate | aws:lightsail/certificate:Certificate |
| lightsail:ContainerService | aws:lightsail/containerService:ContainerService |
| lightsail:Disk | aws:lightsail/disk:Disk |
| lightsail:Distribution | aws:lightsail/distribution:Distribution |
| lightsail:Instance | aws:lightsail/instance:Instance |
| lightsail:LoadBalancer | aws:lightsail/lb:Lb |
| logs:anomaly-detector | aws:cloudwatch/logAnomalyDetector:LogAnomalyDetector |
| logs:delivery | aws:cloudwatch/logDelivery:LogDelivery |
| logs:delivery-destination | aws:cloudwatch/logDeliveryDestination:LogDeliveryDestination |
| logs:delivery-source | aws:cloudwatch/logDeliverySource:LogDeliverySource |
| logs:destination | aws:cloudwatch/logDestination:LogDestination |
| logs:log-group | aws:cloudwatch/logGroup:LogGroup |
| m2:env | aws:m2/environment:Environment |
| mediaconvert:queues | aws:mediaconvert/queue:Queue |
| medialive:inputSecurityGroup | aws:medialive/inputSecurityGroup:InputSecurityGroup |
| medialive:multiplex | aws:medialive/multiplex:Multiplex |
| mediapackage:channels | aws:mediapackage/channel:Channel |
| mediapackagev2:channelGroup | aws:mediapackagev2/channelGroup:ChannelGroup |
| memorydb:acl | aws:memorydb/acl:Acl |
| memorydb:cluster | aws:memorydb/cluster:Cluster |
| memorydb:parametergroup | aws:memorydb/parameterGroup:ParameterGroup |
| memorydb:subnetgroup | aws:memorydb/subnetGroup:SubnetGroup |
| memorydb:user | aws:memorydb/user:User |
| mobiletargeting:apps | aws:pinpoint/app:App |
| mq:broker | aws:mq/broker:Broker |
| mq:configuration | aws:mq/configuration:Configuration |
| network-firewall:firewall | aws:networkfirewall/firewall:Firewall |
| network-firewall:firewall-policy | aws:networkfirewall/firewallPolicy:FirewallPolicy |
| network-firewall:stateless-rulegroup | aws:networkfirewall/ruleGroup:RuleGroup |
| networkmanager:connect-peer | aws:networkmanager/connectPeer:ConnectPeer |
| networkmanager:core-network | aws:networkmanager/coreNetwork:CoreNetwork |
| networkmanager:device | aws:networkmanager/device:Device |
| networkmanager:global-network | aws:networkmanager/globalNetwork:GlobalNetwork |
| networkmanager:link | aws:networkmanager/link:Link |
| networkmanager:site | aws:networkmanager/site:Site |
| notifications-contacts:emailcontact | aws:notifications/contactsEmailContact:ContactsEmailContact |
| oam:sink | aws:oam/sink:Sink |
| organizations:account | aws:organizations/account:Account |
| organizations:ou | aws:organizations/organizationalUnit:OrganizationalUnit |
| organizations:resourcepolicy | aws:organizations/resourcePolicy:ResourcePolicy |
| osis:pipeline | aws:opensearchingest/pipeline:Pipeline |
| payment-cryptography:key | aws:paymentcryptography/key:Key |
| pipes:pipe | aws:pipes/pipe:Pipe |
| profile:domains | aws:customerprofiles/domain:Domain |
| ram:resource-share | aws:ram/resourceShare:ResourceShare |
| rbin:rule | aws:rbin/rule:Rule |
| rds:cev | aws:rds/customDbEngineVersion:CustomDbEngineVersion |
| rds:cluster | aws:docdb/cluster:Cluster |
| rds:cluster-pg | aws:docdb/clusterParameterGroup:ClusterParameterGroup<br>aws:neptune/clusterParameterGroup:ClusterParameterGroup<br>aws:rds/clusterParameterGroup:ClusterParameterGroup |
| rds:db | aws:docdb/clusterInstance:ClusterInstance<br>aws:neptune/clusterInstance:ClusterInstance<br>aws:rds/clusterInstance:ClusterInstance<br>aws:rds/instance:Instance |
| rds:db-proxy | aws:rds/proxy:Proxy |
| rds:db-proxy-endpoint | aws:rds/proxyEndpoint:ProxyEndpoint |
| rds:es | aws:docdb/eventSubscription:EventSubscription<br>aws:rds/eventSubscription:EventSubscription |
| rds:global-cluster | aws:rds/globalCluster:GlobalCluster |
| rds:og | aws:rds/optionGroup:OptionGroup |
| rds:pg | aws:neptune/parameterGroup:ParameterGroup<br>aws:rds/parameterGroup:ParameterGroup |
| rds:subgrp | aws:docdb/subnetGroup:SubnetGroup<br>aws:neptune/subnetGroup:SubnetGroup<br>aws:rds/subnetGroup:SubnetGroup |
| redshift-serverless:namespace | aws:redshiftserverless/namespace:Namespace |
| redshift-serverless:workgroup | aws:redshiftserverless/workgroup:Workgroup |
| redshift:cluster | aws:redshift/cluster:Cluster |
| redshift:eventsubscription | aws:redshift/eventSubscription:EventSubscription |
| redshift:integration | aws:redshift/integration:Integration |
| redshift:parametergroup | aws:redshift/parameterGroup:ParameterGroup |
| redshift:subnetgroup | aws:redshift/subnetGroup:SubnetGroup |
| rekognition:collection | aws:rekognition/collection:Collection |
| resiliencehub:resiliency-policy | aws:resiliencehub/resiliencyPolicy:ResiliencyPolicy |
| resource-groups:group | aws:resourcegroups/group:Group |
| route53-recovery-control:cluster | aws:route53recoverycontrol/cluster:Cluster |
| route53-recovery-control:controlpanel | aws:route53recoverycontrol/controlPanel:ControlPanel |
| route53-recovery-control:controlpanel/safetyrule | aws:route53recoverycontrol/safetyRule:SafetyRule |
| route53-recovery-readiness:cell | aws:route53recoveryreadiness/cell:Cell |
| route53-recovery-readiness:readiness-check | aws:route53recoveryreadiness/readinessCheck:ReadinessCheck |
| route53-recovery-readiness:recovery-group | aws:route53recoveryreadiness/recoveryGroup:RecoveryGroup |
| route53-recovery-readiness:resource-set | aws:route53recoveryreadiness/resourceSet:ResourceSet |
| route53:healthcheck | aws:route53/healthCheck:HealthCheck |
| route53:hostedzone | aws:route53/zone:Zone |
| route53profiles:profile | aws:route53/profilesProfile:ProfilesProfile |
| route53profiles:profile-association | aws:route53/profilesAssociation:ProfilesAssociation |
| route53resolver:firewall-domain-list | aws:route53/resolverFirewallDomainList:ResolverFirewallDomainList |
| route53resolver:firewall-rule-group | aws:route53/resolverFirewallRuleGroup:ResolverFirewallRuleGroup |
| route53resolver:firewall-rule-group-association | aws:route53/resolverFirewallRuleGroupAssociation:ResolverFirewallRuleGroupAssociation |
| route53resolver:resolver-endpoint | aws:route53/resolverEndpoint:ResolverEndpoint |
| route53resolver:resolver-query-log-config | aws:route53/resolverQueryLogConfig:ResolverQueryLogConfig |
| route53resolver:resolver-rule | aws:route53/resolverRule:ResolverRule |
| rum:appmonitor | aws:rum/appMonitor:AppMonitor |
| s3:accesspoint | aws:s3/accessPoint:AccessPoint |
| s3:bucket | aws:s3/bucket:Bucket<br>aws:s3/bucketV2:BucketV2 |
| s3express:bucket | aws:s3/directoryBucket:DirectoryBucket |
| sagemaker:app | aws:sagemaker/app:App |
| sagemaker:app-image-config | aws:sagemaker/appImageConfig:AppImageConfig |
| sagemaker:code-repository | aws:sagemaker/codeRepository:CodeRepository |
| sagemaker:data-quality-job-definition | aws:sagemaker/dataQualityJobDefinition:DataQualityJobDefinition |
| sagemaker:domain | aws:sagemaker/domain:Domain |
| sagemaker:endpoint | aws:sagemaker/endpoint:Endpoint |
| sagemaker:endpoint-config | aws:sagemaker/endpointConfiguration:EndpointConfiguration |
| sagemaker:feature-group | aws:sagemaker/featureGroup:FeatureGroup |
| sagemaker:image | aws:sagemaker/image:Image |
| sagemaker:mlflow-tracking-server | aws:sagemaker/mlflowTrackingServer:MlflowTrackingServer |
| sagemaker:model | aws:sagemaker/model:Model |
| sagemaker:model-package-group | aws:sagemaker/modelPackageGroup:ModelPackageGroup |
| sagemaker:monitoring-schedule | aws:sagemaker/monitoringSchedule:MonitoringSchedule |
| sagemaker:notebook-instance | aws:sagemaker/notebookInstance:NotebookInstance |
| sagemaker:notebook-instance-lifecycle-config | aws:sagemaker/notebookInstanceLifecycleConfiguration:NotebookInstanceLifecycleConfiguration |
| sagemaker:pipeline | aws:sagemaker/pipeline:Pipeline |
| sagemaker:project | aws:sagemaker/project:Project |
| sagemaker:space | aws:sagemaker/space:Space |
| sagemaker:studio-lifecycle-config | aws:sagemaker/studioLifecycleConfig:StudioLifecycleConfig |
| sagemaker:user-profile | aws:sagemaker/userProfile:UserProfile |
| sagemaker:workteam | aws:sagemaker/workteam:Workteam |
| scheduler:schedule-group | aws:scheduler/scheduleGroup:ScheduleGroup |
| schemas:discoverer | aws:schemas/discoverer:Discoverer |
| schemas:registry | aws:schemas/registry:Registry |
| schemas:schema | aws:schemas/schema:Schema |
| secretsmanager:secret | aws:secretsmanager/secret:Secret |
| servicecatalog:applications | aws:servicecatalog/appregistryApplication:AppregistryApplication |
| servicecatalog:attribute-groups | aws:servicecatalog/appregistryAttributeGroup:AppregistryAttributeGroup |
| servicediscovery:service | aws:servicediscovery/service:Service |
| ses:configuration-set | aws:sesv2/configurationSet:ConfigurationSet |
| ses:contact-list | aws:sesv2/contactList:ContactList |
| ses:dedicated-ip-pool | aws:sesv2/dedicatedIpPool:DedicatedIpPool |
| ses:identity | aws:sesv2/emailIdentity:EmailIdentity |
| signer:signing-profiles | aws:signer/signingProfile:SigningProfile |
| sns:topic | aws:sns/topic:Topic |
| sqs:queue | aws:sqs/queue:Queue |
| ssm-incidents:replication-set | aws:ssmincidents/replicationSet:ReplicationSet |
| ssm-incidents:response-plan | aws:ssmincidents/responsePlan:ResponsePlan |
| ssm:association | aws:ssm/association:Association |
| ssm:document | aws:ssm/document:Document |
| ssm:maintenancewindow | aws:ssm/maintenanceWindow:MaintenanceWindow |
| ssm:parameter | aws:ssm/parameter:Parameter |
| ssm:patchbaseline | aws:ssm/patchBaseline:PatchBaseline |
| states:activity | aws:sfn/activity:Activity |
| states:stateMachine | aws:sfn/stateMachine:StateMachine |
| synthetics:canary | aws:synthetics/canary:Canary |
| synthetics:group | aws:synthetics/group:Group |
| timestream:database | aws:timestreamwrite/database:Database |
| timestream:database/table | aws:timestreamwrite/table:Table |
| timestream:scheduled-query | aws:timestreamquery/scheduledQuery:ScheduledQuery |
| transfer:agreement | aws:transfer/agreement:Agreement |
| transfer:certificate | aws:transfer/certificate:Certificate |
| transfer:connector | aws:transfer/connector:Connector |
| transfer:profile | aws:transfer/profile:Profile |
| transfer:server | aws:transfer/server:Server |
| transfer:user | aws:transfer/user:User |
| transfer:workflow | aws:transfer/workflow:Workflow |
| verifiedpermissions:policy-store | aws:verifiedpermissions/policyStore:PolicyStore |
| vpc-lattice:accesslogsubscription | aws:vpclattice/accessLogSubscription:AccessLogSubscription |
| vpc-lattice:service | aws:vpclattice/service:Service |
| vpc-lattice:service/listener | aws:vpclattice/listener:Listener |
| vpc-lattice:service/listener/rule | aws:vpclattice/listenerRule:ListenerRule |
| vpc-lattice:servicenetwork | aws:vpclattice/serviceNetwork:ServiceNetwork |
| vpc-lattice:servicenetworkserviceassociation | aws:vpclattice/serviceNetworkServiceAssociation:ServiceNetworkServiceAssociation |
| vpc-lattice:servicenetworkvpcassociation | aws:vpclattice/serviceNetworkVpcAssociation:ServiceNetworkVpcAssociation |
| vpc-lattice:targetgroup | aws:vpclattice/targetGroup:TargetGroup |
| workspaces-web:browserSettings | aws:workspacesweb/browserSettings:BrowserSettings |
| workspaces-web:ipAccessSettings | aws:workspacesweb/ipAccessSettings:IpAccessSettings |
| workspaces-web:networkSettings | aws:workspacesweb/networkSettings:NetworkSettings |
| workspaces-web:portal | aws:workspacesweb/portal:Portal |
| workspaces-web:trustStore | aws:workspacesweb/trustStore:TrustStore |
| workspaces-web:userAccessLoggingSettings | aws:workspacesweb/userAccessLoggingSettings:UserAccessLoggingSettings |
| workspaces-web:userSettings | aws:workspacesweb/userSettings:UserSettings |
| workspaces:connectionalias | aws:workspaces/connectionAlias:ConnectionAlias |
| xray:group | aws:xray/group:Group |
| xray:sampling-rule | aws:xray/samplingRule:SamplingRule |

## Related documentation

- [Policy as Code get started guide](/docs/insights/policy/get-started/)
- [Pre-Built Policy Packs](/docs/insights/policy/policy-packs/pre-built-packs/)
