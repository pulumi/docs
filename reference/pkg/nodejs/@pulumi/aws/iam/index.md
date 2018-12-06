---
title: Module iam
---

<a href="../index.html">@pulumi/aws</a> &gt; iam

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AccessKey">class AccessKey</a>
* <a href="#AccountAlias">class AccountAlias</a>
* <a href="#AccountPasswordPolicy">class AccountPasswordPolicy</a>
* <a href="#Group">class Group</a>
* <a href="#GroupMembership">class GroupMembership</a>
* <a href="#GroupPolicy">class GroupPolicy</a>
* <a href="#GroupPolicyAttachment">class GroupPolicyAttachment</a>
* <a href="#InstanceProfile">class InstanceProfile</a>
* <a href="#OpenIdConnectProvider">class OpenIdConnectProvider</a>
* <a href="#Policy">class Policy</a>
* <a href="#PolicyAttachment">class PolicyAttachment</a>
* <a href="#Role">class Role</a>
* <a href="#RolePolicy">class RolePolicy</a>
* <a href="#RolePolicyAttachment">class RolePolicyAttachment</a>
* <a href="#SamlProvider">class SamlProvider</a>
* <a href="#ServerCertificate">class ServerCertificate</a>
* <a href="#ServiceLinkedRole">class ServiceLinkedRole</a>
* <a href="#SshKey">class SshKey</a>
* <a href="#User">class User</a>
* <a href="#UserGroupMembership">class UserGroupMembership</a>
* <a href="#UserLoginProfile">class UserLoginProfile</a>
* <a href="#UserPolicy">class UserPolicy</a>
* <a href="#UserPolicyAttachment">class UserPolicyAttachment</a>
* <a href="#AWSAccountActivityAccess">const AWSAccountActivityAccess</a>
* <a href="#AWSAccountUsageReportAccess">const AWSAccountUsageReportAccess</a>
* <a href="#AWSAgentlessDiscoveryService">const AWSAgentlessDiscoveryService</a>
* <a href="#AWSApplicationDiscoveryAgentAccess">const AWSApplicationDiscoveryAgentAccess</a>
* <a href="#AWSApplicationDiscoveryServiceFullAccess">const AWSApplicationDiscoveryServiceFullAccess</a>
* <a href="#AWSBatchFullAccess">const AWSBatchFullAccess</a>
* <a href="#AWSBatchServiceRole">const AWSBatchServiceRole</a>
* <a href="#AWSCertificateManagerFullAccess">const AWSCertificateManagerFullAccess</a>
* <a href="#AWSCertificateManagerReadOnly">const AWSCertificateManagerReadOnly</a>
* <a href="#AWSCloudFormationReadOnlyAccess">const AWSCloudFormationReadOnlyAccess</a>
* <a href="#AWSCloudHSMFullAccess">const AWSCloudHSMFullAccess</a>
* <a href="#AWSCloudHSMReadOnlyAccess">const AWSCloudHSMReadOnlyAccess</a>
* <a href="#AWSCloudHSMRole">const AWSCloudHSMRole</a>
* <a href="#AWSCloudTrailFullAccess">const AWSCloudTrailFullAccess</a>
* <a href="#AWSCloudTrailReadOnlyAccess">const AWSCloudTrailReadOnlyAccess</a>
* <a href="#AWSCodeBuildAdminAccess">const AWSCodeBuildAdminAccess</a>
* <a href="#AWSCodeBuildDeveloperAccess">const AWSCodeBuildDeveloperAccess</a>
* <a href="#AWSCodeBuildReadOnlyAccess">const AWSCodeBuildReadOnlyAccess</a>
* <a href="#AWSCodeCommitFullAccess">const AWSCodeCommitFullAccess</a>
* <a href="#AWSCodeCommitPowerUser">const AWSCodeCommitPowerUser</a>
* <a href="#AWSCodeCommitReadOnly">const AWSCodeCommitReadOnly</a>
* <a href="#AWSCodeDeployDeployerAccess">const AWSCodeDeployDeployerAccess</a>
* <a href="#AWSCodeDeployFullAccess">const AWSCodeDeployFullAccess</a>
* <a href="#AWSCodeDeployReadOnlyAccess">const AWSCodeDeployReadOnlyAccess</a>
* <a href="#AWSCodeDeployRole">const AWSCodeDeployRole</a>
* <a href="#AWSCodePipelineApproverAccess">const AWSCodePipelineApproverAccess</a>
* <a href="#AWSCodePipelineCustomActionAccess">const AWSCodePipelineCustomActionAccess</a>
* <a href="#AWSCodePipelineFullAccess">const AWSCodePipelineFullAccess</a>
* <a href="#AWSCodePipelineReadOnlyAccess">const AWSCodePipelineReadOnlyAccess</a>
* <a href="#AWSCodeStarFullAccess">const AWSCodeStarFullAccess</a>
* <a href="#AWSCodeStarServiceRole">const AWSCodeStarServiceRole</a>
* <a href="#AWSConfigRole">const AWSConfigRole</a>
* <a href="#AWSConfigRulesExecutionRole">const AWSConfigRulesExecutionRole</a>
* <a href="#AWSConfigUserAccess">const AWSConfigUserAccess</a>
* <a href="#AWSConnector">const AWSConnector</a>
* <a href="#AWSDataPipelineRole">const AWSDataPipelineRole</a>
* <a href="#AWSDataPipeline_FullAccess">const AWSDataPipeline_FullAccess</a>
* <a href="#AWSDataPipeline_PowerUser">const AWSDataPipeline_PowerUser</a>
* <a href="#AWSDeviceFarmFullAccess">const AWSDeviceFarmFullAccess</a>
* <a href="#AWSDirectConnectFullAccess">const AWSDirectConnectFullAccess</a>
* <a href="#AWSDirectConnectReadOnlyAccess">const AWSDirectConnectReadOnlyAccess</a>
* <a href="#AWSDirectoryServiceFullAccess">const AWSDirectoryServiceFullAccess</a>
* <a href="#AWSDirectoryServiceReadOnlyAccess">const AWSDirectoryServiceReadOnlyAccess</a>
* <a href="#AWSElasticBeanstalkCustomPlatformforEC2Role">const AWSElasticBeanstalkCustomPlatformforEC2Role</a>
* <a href="#AWSElasticBeanstalkEnhancedHealth">const AWSElasticBeanstalkEnhancedHealth</a>
* <a href="#AWSElasticBeanstalkFullAccess">const AWSElasticBeanstalkFullAccess</a>
* <a href="#AWSElasticBeanstalkMulticontainerDocker">const AWSElasticBeanstalkMulticontainerDocker</a>
* <a href="#AWSElasticBeanstalkReadOnlyAccess">const AWSElasticBeanstalkReadOnlyAccess</a>
* <a href="#AWSElasticBeanstalkService">const AWSElasticBeanstalkService</a>
* <a href="#AWSElasticBeanstalkWebTier">const AWSElasticBeanstalkWebTier</a>
* <a href="#AWSElasticBeanstalkWorkerTier">const AWSElasticBeanstalkWorkerTier</a>
* <a href="#AWSGreengrassFullAccess">const AWSGreengrassFullAccess</a>
* <a href="#AWSGreengrassResourceAccessRolePolicy">const AWSGreengrassResourceAccessRolePolicy</a>
* <a href="#AWSHealthFullAccess">const AWSHealthFullAccess</a>
* <a href="#AWSImportExportFullAccess">const AWSImportExportFullAccess</a>
* <a href="#AWSImportExportReadOnlyAccess">const AWSImportExportReadOnlyAccess</a>
* <a href="#AWSIoTConfigAccess">const AWSIoTConfigAccess</a>
* <a href="#AWSIoTConfigReadOnlyAccess">const AWSIoTConfigReadOnlyAccess</a>
* <a href="#AWSIoTDataAccess">const AWSIoTDataAccess</a>
* <a href="#AWSIoTFullAccess">const AWSIoTFullAccess</a>
* <a href="#AWSIoTLogging">const AWSIoTLogging</a>
* <a href="#AWSIoTRuleActions">const AWSIoTRuleActions</a>
* <a href="#AWSKeyManagementServicePowerUser">const AWSKeyManagementServicePowerUser</a>
* <a href="#AWSLambdaBasicExecutionRole">const AWSLambdaBasicExecutionRole</a>
* <a href="#AWSLambdaDynamoDBExecutionRole">const AWSLambdaDynamoDBExecutionRole</a>
* <a href="#AWSLambdaENIManagementAccess">const AWSLambdaENIManagementAccess</a>
* <a href="#AWSLambdaExecute">const AWSLambdaExecute</a>
* <a href="#AWSLambdaFullAccess">const AWSLambdaFullAccess</a>
* <a href="#AWSLambdaInvocationDynamoDB">const AWSLambdaInvocationDynamoDB</a>
* <a href="#AWSLambdaKinesisExecutionRole">const AWSLambdaKinesisExecutionRole</a>
* <a href="#AWSLambdaReadOnlyAccess">const AWSLambdaReadOnlyAccess</a>
* <a href="#AWSLambdaRole">const AWSLambdaRole</a>
* <a href="#AWSLambdaVPCAccessExecutionRole">const AWSLambdaVPCAccessExecutionRole</a>
* <a href="#AWSMarketplaceFullAccess">const AWSMarketplaceFullAccess</a>
* <a href="#AWSMarketplaceGetEntitlements">const AWSMarketplaceGetEntitlements</a>
* <a href="#AWSMarketplaceManageSubscriptions">const AWSMarketplaceManageSubscriptions</a>
* <a href="#AWSMarketplaceMeteringFullAccess">const AWSMarketplaceMeteringFullAccess</a>
* <a href="#AWSMarketplaceReadonly">const AWSMarketplaceReadonly</a>
* <a href="#AWSMobileHub_FullAccess">const AWSMobileHub_FullAccess</a>
* <a href="#AWSMobileHub_ReadOnly">const AWSMobileHub_ReadOnly</a>
* <a href="#AWSMobileHub_ServiceUseOnly">const AWSMobileHub_ServiceUseOnly</a>
* <a href="#AWSOpsWorksCMInstanceProfileRole">const AWSOpsWorksCMInstanceProfileRole</a>
* <a href="#AWSOpsWorksCMServiceRole">const AWSOpsWorksCMServiceRole</a>
* <a href="#AWSOpsWorksCloudWatchLogs">const AWSOpsWorksCloudWatchLogs</a>
* <a href="#AWSOpsWorksFullAccess">const AWSOpsWorksFullAccess</a>
* <a href="#AWSOpsWorksInstanceRegistration">const AWSOpsWorksInstanceRegistration</a>
* <a href="#AWSOpsWorksRegisterCLI">const AWSOpsWorksRegisterCLI</a>
* <a href="#AWSOpsWorksRole">const AWSOpsWorksRole</a>
* <a href="#AWSQuickSightDescribeRDS">const AWSQuickSightDescribeRDS</a>
* <a href="#AWSQuickSightDescribeRedshift">const AWSQuickSightDescribeRedshift</a>
* <a href="#AWSQuickSightListIAM">const AWSQuickSightListIAM</a>
* <a href="#AWSQuicksightAthenaAccess">const AWSQuicksightAthenaAccess</a>
* <a href="#AWSStepFunctionsConsoleFullAccess">const AWSStepFunctionsConsoleFullAccess</a>
* <a href="#AWSStepFunctionsFullAccess">const AWSStepFunctionsFullAccess</a>
* <a href="#AWSStepFunctionsReadOnlyAccess">const AWSStepFunctionsReadOnlyAccess</a>
* <a href="#AWSStorageGatewayFullAccess">const AWSStorageGatewayFullAccess</a>
* <a href="#AWSStorageGatewayReadOnlyAccess">const AWSStorageGatewayReadOnlyAccess</a>
* <a href="#AWSSupportAccess">const AWSSupportAccess</a>
* <a href="#AWSWAFFullAccess">const AWSWAFFullAccess</a>
* <a href="#AWSWAFReadOnlyAccess">const AWSWAFReadOnlyAccess</a>
* <a href="#AWSXrayFullAccess">const AWSXrayFullAccess</a>
* <a href="#AWSXrayReadOnlyAccess">const AWSXrayReadOnlyAccess</a>
* <a href="#AWSXrayWriteOnlyAccess">const AWSXrayWriteOnlyAccess</a>
* <a href="#AcmServicePrincipal">const AcmServicePrincipal</a>
* <a href="#AdministratorAccess">const AdministratorAccess</a>
* <a href="#AmazonAPIGatewayAdministrator">const AmazonAPIGatewayAdministrator</a>
* <a href="#AmazonAPIGatewayInvokeFullAccess">const AmazonAPIGatewayInvokeFullAccess</a>
* <a href="#AmazonAPIGatewayPushToCloudWatchLogs">const AmazonAPIGatewayPushToCloudWatchLogs</a>
* <a href="#AmazonAppStreamFullAccess">const AmazonAppStreamFullAccess</a>
* <a href="#AmazonAppStreamReadOnlyAccess">const AmazonAppStreamReadOnlyAccess</a>
* <a href="#AmazonAppStreamServiceAccess">const AmazonAppStreamServiceAccess</a>
* <a href="#AmazonAthenaFullAccess">const AmazonAthenaFullAccess</a>
* <a href="#AmazonCloudDirectoryFullAccess">const AmazonCloudDirectoryFullAccess</a>
* <a href="#AmazonCloudDirectoryReadOnlyAccess">const AmazonCloudDirectoryReadOnlyAccess</a>
* <a href="#AmazonCognitoDeveloperAuthenticatedIdentities">const AmazonCognitoDeveloperAuthenticatedIdentities</a>
* <a href="#AmazonCognitoPowerUser">const AmazonCognitoPowerUser</a>
* <a href="#AmazonCognitoReadOnly">const AmazonCognitoReadOnly</a>
* <a href="#AmazonDMSCloudWatchLogsRole">const AmazonDMSCloudWatchLogsRole</a>
* <a href="#AmazonDMSRedshiftS3Role">const AmazonDMSRedshiftS3Role</a>
* <a href="#AmazonDMSVPCManagementRole">const AmazonDMSVPCManagementRole</a>
* <a href="#AmazonDRSVPCManagement">const AmazonDRSVPCManagement</a>
* <a href="#AmazonDynamoDBFullAccess">const AmazonDynamoDBFullAccess</a>
* <a href="#AmazonDynamoDBFullAccesswithDataPipeline">const AmazonDynamoDBFullAccesswithDataPipeline</a>
* <a href="#AmazonDynamoDBReadOnlyAccess">const AmazonDynamoDBReadOnlyAccess</a>
* <a href="#AmazonEC2ContainerRegistryFullAccess">const AmazonEC2ContainerRegistryFullAccess</a>
* <a href="#AmazonEC2ContainerRegistryPowerUser">const AmazonEC2ContainerRegistryPowerUser</a>
* <a href="#AmazonEC2ContainerRegistryReadOnly">const AmazonEC2ContainerRegistryReadOnly</a>
* <a href="#AmazonEC2ContainerServiceAutoscaleRole">const AmazonEC2ContainerServiceAutoscaleRole</a>
* <a href="#AmazonEC2ContainerServiceFullAccess">const AmazonEC2ContainerServiceFullAccess</a>
* <a href="#AmazonEC2ContainerServiceRole">const AmazonEC2ContainerServiceRole</a>
* <a href="#AmazonEC2ContainerServiceforEC2Role">const AmazonEC2ContainerServiceforEC2Role</a>
* <a href="#AmazonEC2FullAccess">const AmazonEC2FullAccess</a>
* <a href="#AmazonEC2ReadOnlyAccess">const AmazonEC2ReadOnlyAccess</a>
* <a href="#AmazonEC2ReportsAccess">const AmazonEC2ReportsAccess</a>
* <a href="#AmazonEC2RoleforAWSCodeDeploy">const AmazonEC2RoleforAWSCodeDeploy</a>
* <a href="#AmazonEC2RoleforDataPipelineRole">const AmazonEC2RoleforDataPipelineRole</a>
* <a href="#AmazonEC2RoleforSSM">const AmazonEC2RoleforSSM</a>
* <a href="#AmazonEC2SpotFleetAutoscaleRole">const AmazonEC2SpotFleetAutoscaleRole</a>
* <a href="#AmazonEC2SpotFleetRole">const AmazonEC2SpotFleetRole</a>
* <a href="#AmazonESFullAccess">const AmazonESFullAccess</a>
* <a href="#AmazonESReadOnlyAccess">const AmazonESReadOnlyAccess</a>
* <a href="#AmazonElastiCacheFullAccess">const AmazonElastiCacheFullAccess</a>
* <a href="#AmazonElastiCacheReadOnlyAccess">const AmazonElastiCacheReadOnlyAccess</a>
* <a href="#AmazonElasticFileSystemFullAccess">const AmazonElasticFileSystemFullAccess</a>
* <a href="#AmazonElasticFileSystemReadOnlyAccess">const AmazonElasticFileSystemReadOnlyAccess</a>
* <a href="#AmazonElasticMapReduceFullAccess">const AmazonElasticMapReduceFullAccess</a>
* <a href="#AmazonElasticMapReduceReadOnlyAccess">const AmazonElasticMapReduceReadOnlyAccess</a>
* <a href="#AmazonElasticMapReduceRole">const AmazonElasticMapReduceRole</a>
* <a href="#AmazonElasticMapReduceforAutoScalingRole">const AmazonElasticMapReduceforAutoScalingRole</a>
* <a href="#AmazonElasticMapReduceforEC2Role">const AmazonElasticMapReduceforEC2Role</a>
* <a href="#AmazonElasticTranscoderFullAccess">const AmazonElasticTranscoderFullAccess</a>
* <a href="#AmazonElasticTranscoderJobsSubmitter">const AmazonElasticTranscoderJobsSubmitter</a>
* <a href="#AmazonElasticTranscoderReadOnlyAccess">const AmazonElasticTranscoderReadOnlyAccess</a>
* <a href="#AmazonElasticTranscoderRole">const AmazonElasticTranscoderRole</a>
* <a href="#AmazonGlacierFullAccess">const AmazonGlacierFullAccess</a>
* <a href="#AmazonGlacierReadOnlyAccess">const AmazonGlacierReadOnlyAccess</a>
* <a href="#AmazonInspectorFullAccess">const AmazonInspectorFullAccess</a>
* <a href="#AmazonInspectorReadOnlyAccess">const AmazonInspectorReadOnlyAccess</a>
* <a href="#AmazonKinesisAnalyticsFullAccess">const AmazonKinesisAnalyticsFullAccess</a>
* <a href="#AmazonKinesisAnalyticsReadOnly">const AmazonKinesisAnalyticsReadOnly</a>
* <a href="#AmazonKinesisFirehoseFullAccess">const AmazonKinesisFirehoseFullAccess</a>
* <a href="#AmazonKinesisFirehoseReadOnlyAccess">const AmazonKinesisFirehoseReadOnlyAccess</a>
* <a href="#AmazonKinesisFullAccess">const AmazonKinesisFullAccess</a>
* <a href="#AmazonKinesisReadOnlyAccess">const AmazonKinesisReadOnlyAccess</a>
* <a href="#AmazonLexFullAccess">const AmazonLexFullAccess</a>
* <a href="#AmazonLexReadOnly">const AmazonLexReadOnly</a>
* <a href="#AmazonLexRunBotsOnly">const AmazonLexRunBotsOnly</a>
* <a href="#AmazonMachineLearningBatchPredictionsAccess">const AmazonMachineLearningBatchPredictionsAccess</a>
* <a href="#AmazonMachineLearningCreateOnlyAccess">const AmazonMachineLearningCreateOnlyAccess</a>
* <a href="#AmazonMachineLearningFullAccess">const AmazonMachineLearningFullAccess</a>
* <a href="#AmazonMachineLearningManageRealTimeEndpointOnlyAccess">const AmazonMachineLearningManageRealTimeEndpointOnlyAccess</a>
* <a href="#AmazonMachineLearningReadOnlyAccess">const AmazonMachineLearningReadOnlyAccess</a>
* <a href="#AmazonMachineLearningRealTimePredictionOnlyAccess">const AmazonMachineLearningRealTimePredictionOnlyAccess</a>
* <a href="#AmazonMachineLearningRoleforRedshiftDataSource">const AmazonMachineLearningRoleforRedshiftDataSource</a>
* <a href="#AmazonMechanicalTurkFullAccess">const AmazonMechanicalTurkFullAccess</a>
* <a href="#AmazonMechanicalTurkReadOnly">const AmazonMechanicalTurkReadOnly</a>
* <a href="#AmazonMobileAnalyticsFinancialReportAccess">const AmazonMobileAnalyticsFinancialReportAccess</a>
* <a href="#AmazonMobileAnalyticsFullAccess">const AmazonMobileAnalyticsFullAccess</a>
* <a href="#AmazonMobileAnalyticsNonfinancialReportAccess">const AmazonMobileAnalyticsNonfinancialReportAccess</a>
* <a href="#AmazonMobileAnalyticsWriteOnlyAccess">const AmazonMobileAnalyticsWriteOnlyAccess</a>
* <a href="#AmazonPollyFullAccess">const AmazonPollyFullAccess</a>
* <a href="#AmazonPollyReadOnlyAccess">const AmazonPollyReadOnlyAccess</a>
* <a href="#AmazonRDSDirectoryServiceAccess">const AmazonRDSDirectoryServiceAccess</a>
* <a href="#AmazonRDSEnhancedMonitoringRole">const AmazonRDSEnhancedMonitoringRole</a>
* <a href="#AmazonRDSFullAccess">const AmazonRDSFullAccess</a>
* <a href="#AmazonRDSReadOnlyAccess">const AmazonRDSReadOnlyAccess</a>
* <a href="#AmazonRedshiftFullAccess">const AmazonRedshiftFullAccess</a>
* <a href="#AmazonRedshiftReadOnlyAccess">const AmazonRedshiftReadOnlyAccess</a>
* <a href="#AmazonRekognitionFullAccess">const AmazonRekognitionFullAccess</a>
* <a href="#AmazonRekognitionReadOnlyAccess">const AmazonRekognitionReadOnlyAccess</a>
* <a href="#AmazonRoute53DomainsFullAccess">const AmazonRoute53DomainsFullAccess</a>
* <a href="#AmazonRoute53DomainsReadOnlyAccess">const AmazonRoute53DomainsReadOnlyAccess</a>
* <a href="#AmazonRoute53FullAccess">const AmazonRoute53FullAccess</a>
* <a href="#AmazonRoute53ReadOnlyAccess">const AmazonRoute53ReadOnlyAccess</a>
* <a href="#AmazonS3FullAccess">const AmazonS3FullAccess</a>
* <a href="#AmazonS3ReadOnlyAccess">const AmazonS3ReadOnlyAccess</a>
* <a href="#AmazonSESFullAccess">const AmazonSESFullAccess</a>
* <a href="#AmazonSESReadOnlyAccess">const AmazonSESReadOnlyAccess</a>
* <a href="#AmazonSNSFullAccess">const AmazonSNSFullAccess</a>
* <a href="#AmazonSNSReadOnlyAccess">const AmazonSNSReadOnlyAccess</a>
* <a href="#AmazonSNSRole">const AmazonSNSRole</a>
* <a href="#AmazonSQSFullAccess">const AmazonSQSFullAccess</a>
* <a href="#AmazonSQSReadOnlyAccess">const AmazonSQSReadOnlyAccess</a>
* <a href="#AmazonSSMAutomationRole">const AmazonSSMAutomationRole</a>
* <a href="#AmazonSSMFullAccess">const AmazonSSMFullAccess</a>
* <a href="#AmazonSSMMaintenanceWindowRole">const AmazonSSMMaintenanceWindowRole</a>
* <a href="#AmazonSSMReadOnlyAccess">const AmazonSSMReadOnlyAccess</a>
* <a href="#AmazonVPCFullAccess">const AmazonVPCFullAccess</a>
* <a href="#AmazonVPCReadOnlyAccess">const AmazonVPCReadOnlyAccess</a>
* <a href="#AmazonWorkMailFullAccess">const AmazonWorkMailFullAccess</a>
* <a href="#AmazonWorkMailReadOnlyAccess">const AmazonWorkMailReadOnlyAccess</a>
* <a href="#AmazonWorkSpacesAdmin">const AmazonWorkSpacesAdmin</a>
* <a href="#AmazonWorkSpacesApplicationManagerAdminAccess">const AmazonWorkSpacesApplicationManagerAdminAccess</a>
* <a href="#AmazonZocaloFullAccess">const AmazonZocaloFullAccess</a>
* <a href="#AmazonZocaloReadOnlyAccess">const AmazonZocaloReadOnlyAccess</a>
* <a href="#ApiGatewayPrincipal">const ApiGatewayPrincipal</a>
* <a href="#ApplicationAutoScalingForAmazonAppStreamAccess">const ApplicationAutoScalingForAmazonAppStreamAccess</a>
* <a href="#AthenaPrincipal">const AthenaPrincipal</a>
* <a href="#AutoScalingConsoleFullAccess">const AutoScalingConsoleFullAccess</a>
* <a href="#AutoScalingConsoleReadOnlyAccess">const AutoScalingConsoleReadOnlyAccess</a>
* <a href="#AutoScalingFullAccess">const AutoScalingFullAccess</a>
* <a href="#AutoScalingNotificationAccessRole">const AutoScalingNotificationAccessRole</a>
* <a href="#AutoScalingReadOnlyAccess">const AutoScalingReadOnlyAccess</a>
* <a href="#AutoscalingPrincipal">const AutoscalingPrincipal</a>
* <a href="#Billing">const Billing</a>
* <a href="#CloudDirectoryPrincipal">const CloudDirectoryPrincipal</a>
* <a href="#CloudFrontFullAccess">const CloudFrontFullAccess</a>
* <a href="#CloudFrontReadOnlyAccess">const CloudFrontReadOnlyAccess</a>
* <a href="#CloudSearchFullAccess">const CloudSearchFullAccess</a>
* <a href="#CloudSearchPrincipal">const CloudSearchPrincipal</a>
* <a href="#CloudSearchReadOnlyAccess">const CloudSearchReadOnlyAccess</a>
* <a href="#CloudWatchActionsEC2Access">const CloudWatchActionsEC2Access</a>
* <a href="#CloudWatchEventsBuiltInTargetExecutionAccess">const CloudWatchEventsBuiltInTargetExecutionAccess</a>
* <a href="#CloudWatchEventsFullAccess">const CloudWatchEventsFullAccess</a>
* <a href="#CloudWatchEventsInvocationAccess">const CloudWatchEventsInvocationAccess</a>
* <a href="#CloudWatchEventsReadOnlyAccess">const CloudWatchEventsReadOnlyAccess</a>
* <a href="#CloudWatchFullAccess">const CloudWatchFullAccess</a>
* <a href="#CloudWatchLogsFullAccess">const CloudWatchLogsFullAccess</a>
* <a href="#CloudWatchLogsReadOnlyAccess">const CloudWatchLogsReadOnlyAccess</a>
* <a href="#CloudWatchReadOnlyAccess">const CloudWatchReadOnlyAccess</a>
* <a href="#CloudformationPrincipal">const CloudformationPrincipal</a>
* <a href="#CloudfrontPrincipal">const CloudfrontPrincipal</a>
* <a href="#CloudtrailPrincipal">const CloudtrailPrincipal</a>
* <a href="#CodeCommitPrincipal">const CodeCommitPrincipal</a>
* <a href="#CodeDeployPrincipal">const CodeDeployPrincipal</a>
* <a href="#CodePipelinePrincipal">const CodePipelinePrincipal</a>
* <a href="#ConfigPrincipal">const ConfigPrincipal</a>
* <a href="#DataPipelinePrincipal">const DataPipelinePrincipal</a>
* <a href="#DataScientist">const DataScientist</a>
* <a href="#DatabaseAdministrator">const DatabaseAdministrator</a>
* <a href="#DirectConnectPrincipal">const DirectConnectPrincipal</a>
* <a href="#DirectoryServicesPrincipal">const DirectoryServicesPrincipal</a>
* <a href="#DynamoDbPrincipal">const DynamoDbPrincipal</a>
* <a href="#Ec2Principal">const Ec2Principal</a>
* <a href="#EcrPrincipal">const EcrPrincipal</a>
* <a href="#EcsPrincipal">const EcsPrincipal</a>
* <a href="#EdgeLambdaPrincipal">const EdgeLambdaPrincipal</a>
* <a href="#ElasticBeanstalkPrincipal">const ElasticBeanstalkPrincipal</a>
* <a href="#ElasticFileSystemPrincipal">const ElasticFileSystemPrincipal</a>
* <a href="#ElasticLoadBalancingPrincipal">const ElasticLoadBalancingPrincipal</a>
* <a href="#ElasticMapReducePrincipal">const ElasticMapReducePrincipal</a>
* <a href="#ElasticachePrincipal">const ElasticachePrincipal</a>
* <a href="#EventsPrincipal">const EventsPrincipal</a>
* <a href="#HealthPrincipal">const HealthPrincipal</a>
* <a href="#IAMFullAccess">const IAMFullAccess</a>
* <a href="#IAMReadOnlyAccess">const IAMReadOnlyAccess</a>
* <a href="#IAMSelfManageServiceSpecificCredentials">const IAMSelfManageServiceSpecificCredentials</a>
* <a href="#IAMUserChangePassword">const IAMUserChangePassword</a>
* <a href="#IAMUserSSHKeys">const IAMUserSSHKeys</a>
* <a href="#IamPrincipal">const IamPrincipal</a>
* <a href="#InspectorPrincipal">const InspectorPrincipal</a>
* <a href="#KinesisPrincipal">const KinesisPrincipal</a>
* <a href="#KmsPrincipal">const KmsPrincipal</a>
* <a href="#LambdaPrincipal">const LambdaPrincipal</a>
* <a href="#LightsailPrincipal">const LightsailPrincipal</a>
* <a href="#LogsPrincipal">const LogsPrincipal</a>
* <a href="#MonitoringPrincipal">const MonitoringPrincipal</a>
* <a href="#NetworkAdministrator">const NetworkAdministrator</a>
* <a href="#OpsworksPrincipal">const OpsworksPrincipal</a>
* <a href="#OrganizationsPrincipal">const OrganizationsPrincipal</a>
* <a href="#PowerUserAccess">const PowerUserAccess</a>
* <a href="#RDSCloudHsmAuthorizationRole">const RDSCloudHsmAuthorizationRole</a>
* <a href="#RdsPrincipal">const RdsPrincipal</a>
* <a href="#ReadOnlyAccess">const ReadOnlyAccess</a>
* <a href="#RedshiftPrincipal">const RedshiftPrincipal</a>
* <a href="#ResourceGroupsandTagEditorFullAccess">const ResourceGroupsandTagEditorFullAccess</a>
* <a href="#ResourceGroupsandTagEditorReadOnlyAccess">const ResourceGroupsandTagEditorReadOnlyAccess</a>
* <a href="#Route53Principal">const Route53Principal</a>
* <a href="#S3Principal">const S3Principal</a>
* <a href="#SecurityAudit">const SecurityAudit</a>
* <a href="#ServerMigrationConnector">const ServerMigrationConnector</a>
* <a href="#ServerMigrationServiceRole">const ServerMigrationServiceRole</a>
* <a href="#ServiceCatalogAdminFullAccess">const ServiceCatalogAdminFullAccess</a>
* <a href="#ServiceCatalogAdminReadOnlyAccess">const ServiceCatalogAdminReadOnlyAccess</a>
* <a href="#ServiceCatalogEndUserAccess">const ServiceCatalogEndUserAccess</a>
* <a href="#ServiceCatalogEndUserFullAccess">const ServiceCatalogEndUserFullAccess</a>
* <a href="#ServiceCatalogPrincipal">const ServiceCatalogPrincipal</a>
* <a href="#SesPrincipal">const SesPrincipal</a>
* <a href="#SigninPrincipal">const SigninPrincipal</a>
* <a href="#SimpleWorkflowFullAccess">const SimpleWorkflowFullAccess</a>
* <a href="#SnsPrincipal">const SnsPrincipal</a>
* <a href="#SqsPrincipal">const SqsPrincipal</a>
* <a href="#SsmPrincipal">const SsmPrincipal</a>
* <a href="#StorageGatewayPrincipal">const StorageGatewayPrincipal</a>
* <a href="#StsPrincipal">const StsPrincipal</a>
* <a href="#SupportPrincipal">const SupportPrincipal</a>
* <a href="#SupportUser">const SupportUser</a>
* <a href="#SystemAdministrator">const SystemAdministrator</a>
* <a href="#VMImportExportRoleForAWSConnector">const VMImportExportRoleForAWSConnector</a>
* <a href="#ViewOnlyAccess">const ViewOnlyAccess</a>
* <a href="#VmiePrincipal">const VmiePrincipal</a>
* <a href="#VpcFlowLogsPrincipal">const VpcFlowLogsPrincipal</a>
* <a href="#WafPrincipal">const WafPrincipal</a>
* <a href="#WorkDocsPrincipal">const WorkDocsPrincipal</a>
* <a href="#WorkspacesPrincipal">const WorkspacesPrincipal</a>
* <a href="#assumeRolePolicyForPrincipal">function assumeRolePolicyForPrincipal</a>
* <a href="#getAccountAlias">function getAccountAlias</a>
* <a href="#getGroup">function getGroup</a>
* <a href="#getInstanceProfile">function getInstanceProfile</a>
* <a href="#getPolicy">function getPolicy</a>
* <a href="#getPolicyDocument">function getPolicyDocument</a>
* <a href="#getRole">function getRole</a>
* <a href="#getServerCertificate">function getServerCertificate</a>
* <a href="#getUser">function getUser</a>
* <a href="#AWSPrincipal">interface AWSPrincipal</a>
* <a href="#AccessKeyArgs">interface AccessKeyArgs</a>
* <a href="#AccessKeyState">interface AccessKeyState</a>
* <a href="#AccountAliasArgs">interface AccountAliasArgs</a>
* <a href="#AccountAliasState">interface AccountAliasState</a>
* <a href="#AccountPasswordPolicyArgs">interface AccountPasswordPolicyArgs</a>
* <a href="#AccountPasswordPolicyState">interface AccountPasswordPolicyState</a>
* <a href="#ConditionArguments">interface ConditionArguments</a>
* <a href="#Conditions">interface Conditions</a>
* <a href="#FederatedPrincipal">interface FederatedPrincipal</a>
* <a href="#GetAccountAliasResult">interface GetAccountAliasResult</a>
* <a href="#GetGroupArgs">interface GetGroupArgs</a>
* <a href="#GetGroupResult">interface GetGroupResult</a>
* <a href="#GetInstanceProfileArgs">interface GetInstanceProfileArgs</a>
* <a href="#GetInstanceProfileResult">interface GetInstanceProfileResult</a>
* <a href="#GetPolicyArgs">interface GetPolicyArgs</a>
* <a href="#GetPolicyDocumentArgs">interface GetPolicyDocumentArgs</a>
* <a href="#GetPolicyDocumentResult">interface GetPolicyDocumentResult</a>
* <a href="#GetPolicyResult">interface GetPolicyResult</a>
* <a href="#GetRoleArgs">interface GetRoleArgs</a>
* <a href="#GetRoleResult">interface GetRoleResult</a>
* <a href="#GetServerCertificateArgs">interface GetServerCertificateArgs</a>
* <a href="#GetServerCertificateResult">interface GetServerCertificateResult</a>
* <a href="#GetUserArgs">interface GetUserArgs</a>
* <a href="#GetUserResult">interface GetUserResult</a>
* <a href="#GroupArgs">interface GroupArgs</a>
* <a href="#GroupMembershipArgs">interface GroupMembershipArgs</a>
* <a href="#GroupMembershipState">interface GroupMembershipState</a>
* <a href="#GroupPolicyArgs">interface GroupPolicyArgs</a>
* <a href="#GroupPolicyAttachmentArgs">interface GroupPolicyAttachmentArgs</a>
* <a href="#GroupPolicyAttachmentState">interface GroupPolicyAttachmentState</a>
* <a href="#GroupPolicyState">interface GroupPolicyState</a>
* <a href="#GroupState">interface GroupState</a>
* <a href="#InstanceProfileArgs">interface InstanceProfileArgs</a>
* <a href="#InstanceProfileState">interface InstanceProfileState</a>
* <a href="#OpenIdConnectProviderArgs">interface OpenIdConnectProviderArgs</a>
* <a href="#OpenIdConnectProviderState">interface OpenIdConnectProviderState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyAttachmentArgs">interface PolicyAttachmentArgs</a>
* <a href="#PolicyAttachmentState">interface PolicyAttachmentState</a>
* <a href="#PolicyDocument">interface PolicyDocument</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#PolicyStatement">interface PolicyStatement</a>
* <a href="#RoleArgs">interface RoleArgs</a>
* <a href="#RolePolicyArgs">interface RolePolicyArgs</a>
* <a href="#RolePolicyAttachmentArgs">interface RolePolicyAttachmentArgs</a>
* <a href="#RolePolicyAttachmentState">interface RolePolicyAttachmentState</a>
* <a href="#RolePolicyState">interface RolePolicyState</a>
* <a href="#RoleState">interface RoleState</a>
* <a href="#SamlProviderArgs">interface SamlProviderArgs</a>
* <a href="#SamlProviderState">interface SamlProviderState</a>
* <a href="#ServerCertificateArgs">interface ServerCertificateArgs</a>
* <a href="#ServerCertificateState">interface ServerCertificateState</a>
* <a href="#ServiceLinkedRoleArgs">interface ServiceLinkedRoleArgs</a>
* <a href="#ServiceLinkedRoleState">interface ServiceLinkedRoleState</a>
* <a href="#ServicePrincipal">interface ServicePrincipal</a>
* <a href="#SshKeyArgs">interface SshKeyArgs</a>
* <a href="#SshKeyState">interface SshKeyState</a>
* <a href="#UserArgs">interface UserArgs</a>
* <a href="#UserGroupMembershipArgs">interface UserGroupMembershipArgs</a>
* <a href="#UserGroupMembershipState">interface UserGroupMembershipState</a>
* <a href="#UserLoginProfileArgs">interface UserLoginProfileArgs</a>
* <a href="#UserLoginProfileState">interface UserLoginProfileState</a>
* <a href="#UserPolicyArgs">interface UserPolicyArgs</a>
* <a href="#UserPolicyAttachmentArgs">interface UserPolicyAttachmentArgs</a>
* <a href="#UserPolicyAttachmentState">interface UserPolicyAttachmentState</a>
* <a href="#UserPolicyState">interface UserPolicyState</a>
* <a href="#UserState">interface UserState</a>
* <a href="#Principal">type Principal</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts">iam/accessKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts">iam/accountAlias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts">iam/accountPasswordPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts">iam/documents.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getAccountAlias.ts">iam/getAccountAlias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts">iam/getGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts">iam/getInstanceProfile.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts">iam/getPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts">iam/getPolicyDocument.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts">iam/getRole.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts">iam/getServerCertificate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts">iam/getUser.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts">iam/group.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts">iam/groupMembership.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts">iam/groupPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts">iam/groupPolicyAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts">iam/instanceProfile.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts">iam/managedPolicies.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts">iam/openIdConnectProvider.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts">iam/policy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts">iam/policyAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts">iam/principals.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts">iam/role.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts">iam/rolePolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts">iam/rolePolicyAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts">iam/samlProvider.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts">iam/serverCertificate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts">iam/serviceLinkedRole.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts">iam/sshKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts">iam/user.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts">iam/userGroupMembership.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts">iam/userLoginProfile.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts">iam/userPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts">iam/userPolicyAttachment.ts</a> 


<h2 class="pdoc-module-header" id="AccessKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L10">class AccessKey</a>
</h2>

Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L59">constructor</a>
</h3>

```typescript
new AccessKey(name: string, args: AccessKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AccessKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccessKeyState): AccessKey
```


Get an existing AccessKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L28">property encryptedSecret</a>
</h3>

```typescript
public encryptedSecret: pulumi.Output<string>;
```


The encrypted secret, base64 encoded.
~> **NOTE:** The encrypted secret may be decrypted using the command line,
for example: `terraform output encrypted_secret | base64 --decode | keybase pgp decrypt`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L33">property keyFingerprint</a>
</h3>

```typescript
public keyFingerprint: pulumi.Output<string>;
```


The fingerprint of the PGP key used to encrypt
the secret

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L38">property pgpKey</a>
</h3>

```typescript
public pgpKey: pulumi.Output<string | undefined>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:some_person_that_exists`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L44">property secret</a>
</h3>

```typescript
public secret: pulumi.Output<string>;
```


The secret access key. Note that this will be written
to the state file. Please supply a `pgp_key` instead, which will prevent the
secret from being stored in plain text

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L50">property sesSmtpPassword</a>
</h3>

```typescript
public sesSmtpPassword: pulumi.Output<string>;
```


The secret access key converted into an SES SMTP
password by applying [AWS's documented conversion
algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L55">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


"Active" or "Inactive". Keys are initially active, but can be made
inactive by other means.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L59">property user</a>
</h3>

```typescript
public user: pulumi.Output<string>;
```


The IAM user to associate with this access key.

<h2 class="pdoc-module-header" id="AccountAlias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L12">class AccountAlias</a>
</h2>

-> **Note:** There is only a single account alias per AWS account.

Manages the account alias for the AWS Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L28">constructor</a>
</h3>

```typescript
new AccountAlias(name: string, args: AccountAliasArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AccountAlias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountAliasState): AccountAlias
```


Get an existing AccountAlias resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L28">property accountAlias</a>
</h3>

```typescript
public accountAlias: pulumi.Output<string>;
```


The account alias

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AccountPasswordPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L14">class AccountPasswordPolicy</a>
</h2>

-> **Note:** There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.

Manages Password Policy for the AWS Account.
See more about [Account Password Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
in the official AWS docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L69">constructor</a>
</h3>

```typescript
new AccountPasswordPolicy(name: string, args?: AccountPasswordPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AccountPasswordPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountPasswordPolicyState): AccountPasswordPolicy
```


Get an existing AccountPasswordPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L30">property allowUsersToChangePassword</a>
</h3>

```typescript
public allowUsersToChangePassword: pulumi.Output<boolean | undefined>;
```


Whether to allow users to change their own password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L36">property expirePasswords</a>
</h3>

```typescript
public expirePasswords: pulumi.Output<boolean>;
```


Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L41">property hardExpiry</a>
</h3>

```typescript
public hardExpiry: pulumi.Output<boolean>;
```


Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L45">property maxPasswordAge</a>
</h3>

```typescript
public maxPasswordAge: pulumi.Output<number>;
```


The number of days that an user password is valid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L49">property minimumPasswordLength</a>
</h3>

```typescript
public minimumPasswordLength: pulumi.Output<number | undefined>;
```


Minimum length to require for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L53">property passwordReusePrevention</a>
</h3>

```typescript
public passwordReusePrevention: pulumi.Output<number>;
```


The number of previous passwords that users are prevented from reusing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L57">property requireLowercaseCharacters</a>
</h3>

```typescript
public requireLowercaseCharacters: pulumi.Output<boolean>;
```


Whether to require lowercase characters for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L61">property requireNumbers</a>
</h3>

```typescript
public requireNumbers: pulumi.Output<boolean>;
```


Whether to require numbers for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L65">property requireSymbols</a>
</h3>

```typescript
public requireSymbols: pulumi.Output<boolean>;
```


Whether to require symbols for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L69">property requireUppercaseCharacters</a>
</h3>

```typescript
public requireUppercaseCharacters: pulumi.Output<boolean>;
```


Whether to require uppercase characters for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Group">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L10">class Group</a>
</h2>

Provides an IAM group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L38">constructor</a>
</h3>

```typescript
new Group(name: string, args?: GroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState): Group
```


Get an existing Group resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS for this group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L34">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


Path in which to create the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L38">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The [unique ID][1] assigned by AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GroupMembership">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L17">class GroupMembership</a>
</h2>

~> **WARNING:** Multiple aws_iam_group_membership resources with the same group name will produce inconsistent behavior!

Provides a top level resource to manage IAM Group membership for IAM Users. For
more information on managing IAM Groups or IAM Users, see [IAM Groups][1] or
[IAM Users][2]

~> **Note:** `aws_iam_group_membership` will conflict with itself if used more than once with the same group. To non-exclusively manage the users in a group, see the
[`aws_iam_user_group_membership` resource][3].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L41">constructor</a>
</h3>

```typescript
new GroupMembership(name: string, args: GroupMembershipArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GroupMembership resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupMembershipState): GroupMembership
```


Get an existing GroupMembership resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L33">property group</a>
</h3>

```typescript
public group: pulumi.Output<string>;
```


The IAM Group name to attach the list of `users` to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to identify the Group Membership

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L41">property users</a>
</h3>

```typescript
public users: pulumi.Output<string[]>;
```


A list of IAM User names to associate with the Group

<h2 class="pdoc-module-header" id="GroupPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L12">class GroupPolicy</a>
</h2>

Provides an IAM policy attached to a group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L42">constructor</a>
</h3>

```typescript
new GroupPolicy(name: string, args: GroupPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GroupPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupPolicyState): GroupPolicy
```


Get an existing GroupPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L28">property group</a>
</h3>

```typescript
public group: pulumi.Output<string>;
```


The IAM group to attach to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L38">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L42">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GroupPolicyAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L15">class GroupPolicyAttachment</a>
</h2>

Attaches a Managed IAM Policy to an IAM group

~> **NOTE:** The usage of this resource conflicts with the `aws_iam_policy_attachment` resource and will permanently show a difference if both are defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L35">constructor</a>
</h3>

```typescript
new GroupPolicyAttachment(name: string, args: GroupPolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GroupPolicyAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupPolicyAttachmentState): GroupPolicyAttachment
```


Get an existing GroupPolicyAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L31">property group</a>
</h3>

```typescript
public group: pulumi.Output<Group>;
```


The group the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L35">property policyArn</a>
</h3>

```typescript
public policyArn: pulumi.Output<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="InstanceProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L14">class InstanceProfile</a>
</h2>

Provides an IAM instance profile.

~> **NOTE:** Either `role` or `roles` (**deprecated**) must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L60">constructor</a>
</h3>

```typescript
new InstanceProfile(name: string, args?: InstanceProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a InstanceProfile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceProfileState): InstanceProfile
```


Get an existing InstanceProfile resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L34">property createDate</a>
</h3>

```typescript
public createDate: pulumi.Output<string>;
```


The creation timestamp of the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The profile's name. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L46">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


Path in which to create the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L50">property role</a>
</h3>

```typescript
public role: pulumi.Output<Role>;
```


The role name to include in the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L56">property roles</a>
</h3>

```typescript
public roles: pulumi.Output<Role[]>;
```


A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
WARNING: This is deprecated since [version 0.9.3 (April 12, 2017)](https://github.com/hashicorp/terraform/blob/master/CHANGELOG.md#093-april-12-2017), as >= 2 roles are not possible. See [issue #11575](https://github.com/hashicorp/terraform/issues/11575).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L60">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The [unique ID][1] assigned by AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="OpenIdConnectProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L10">class OpenIdConnectProvider</a>
</h2>

Provides an IAM OpenID Connect provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L38">constructor</a>
</h3>

```typescript
new OpenIdConnectProvider(name: string, args: OpenIdConnectProviderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OpenIdConnectProvider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OpenIdConnectProviderState): OpenIdConnectProvider
```


Get an existing OpenIdConnectProvider resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS for this provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L30">property clientIdLists</a>
</h3>

```typescript
public clientIdLists: pulumi.Output<string[]>;
```


A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L34">property thumbprintLists</a>
</h3>

```typescript
public thumbprintLists: pulumi.Output<string[]>;
```


A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L38">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL of the identity provider. Corresponds to the _iss_ claim.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L10">class Policy</a>
</h2>

Provides an IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L47">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L38">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L43">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


Path in which to create the policy.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L47">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PolicyAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L19">class PolicyAttachment</a>
</h2>

Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)

!> **WARNING:** The aws_iam_policy_attachment resource creates **exclusive** attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single aws_iam_policy_attachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other Terraform resources) will have that attached policy revoked by this resource. Consider `aws_iam_role_policy_attachment`, `aws_iam_user_policy_attachment`, or `aws_iam_group_policy_attachment` instead. These resources do not enforce exclusive attachment of an IAM policy.

~> **NOTE:** The usage of this resource conflicts with the `aws_iam_group_policy_attachment`, `aws_iam_role_policy_attachment`, and `aws_iam_user_policy_attachment` resources and will permanently show a difference if both are defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L51">constructor</a>
</h3>

```typescript
new PolicyAttachment(name: string, args: PolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PolicyAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyAttachmentState): PolicyAttachment
```


Get an existing PolicyAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L35">property groups</a>
</h3>

```typescript
public groups: pulumi.Output<Group[] | undefined>;
```


The group(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the attachment. This cannot be an empty string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L43">property policyArn</a>
</h3>

```typescript
public policyArn: pulumi.Output<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L47">property roles</a>
</h3>

```typescript
public roles: pulumi.Output<Role[] | undefined>;
```


The role(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L51">property users</a>
</h3>

```typescript
public users: pulumi.Output<User[] | undefined>;
```


The user(s) the policy should be applied to

<h2 class="pdoc-module-header" id="Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L12">class Role</a>
</h2>

Provides an IAM role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L73">constructor</a>
</h3>

```typescript
new Role(name: string, args: RoleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Role resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RoleState): Role
```


Get an existing Role resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L32">property assumeRolePolicy</a>
</h3>

```typescript
public assumeRolePolicy: pulumi.Output<string>;
```


The policy that grants an entity permission to assume the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L36">property createDate</a>
</h3>

```typescript
public createDate: pulumi.Output<string>;
```


The creation date of the IAM role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L40">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L44">property forceDetachPolicies</a>
</h3>

```typescript
public forceDetachPolicies: pulumi.Output<boolean | undefined>;
```


Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L48">property maxSessionDuration</a>
</h3>

```typescript
public maxSessionDuration: pulumi.Output<number | undefined>;
```


The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the role. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L56">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L61">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


The path to the role.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L65">property permissionsBoundary</a>
</h3>

```typescript
public permissionsBoundary: pulumi.Output<string | undefined>;
```


The ARN of the policy that is used to set the permissions boundary for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L69">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


Key-value mapping of tags for the IAM role

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L73">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The stable and unique string identifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RolePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L13">class RolePolicy</a>
</h2>

Provides an IAM role policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L43">constructor</a>
</h3>

```typescript
new RolePolicy(name: string, args: RolePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RolePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RolePolicyState): RolePolicy
```


Get an existing RolePolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the role policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L35">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L39">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L43">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The IAM role to attach to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RolePolicyAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L15">class RolePolicyAttachment</a>
</h2>

Attaches a Managed IAM Policy to an IAM role

~> **NOTE:** The usage of this resource conflicts with the `aws_iam_policy_attachment` resource and will permanently show a difference if both are defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L35">constructor</a>
</h3>

```typescript
new RolePolicyAttachment(name: string, args: RolePolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RolePolicyAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RolePolicyAttachmentState): RolePolicyAttachment
```


Get an existing RolePolicyAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L31">property policyArn</a>
</h3>

```typescript
public policyArn: pulumi.Output<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L35">property role</a>
</h3>

```typescript
public role: pulumi.Output<Role>;
```


The role the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SamlProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L10">class SamlProvider</a>
</h2>

Provides an IAM SAML provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L38">constructor</a>
</h3>

```typescript
new SamlProvider(name: string, args: SamlProviderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SamlProvider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SamlProviderState): SamlProvider
```


Get an existing SamlProvider resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS for this provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the provider to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L34">property samlMetadataDocument</a>
</h3>

```typescript
public samlMetadataDocument: pulumi.Output<string>;
```


An XML document generated by an identity provider that supports SAML 2.0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L38">property validUntil</a>
</h3>

```typescript
public validUntil: pulumi.Output<string>;
```


The expiration date and time for the SAML provider in RFC1123 format, e.g. `Mon, 02 Jan 2006 15:04:05 MST`.

<h2 class="pdoc-module-header" id="ServerCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L22">class ServerCertificate</a>
</h2>

Provides an IAM Server Certificate resource to upload Server Certificates.
Certs uploaded to IAM can easily work with other AWS services such as:

- AWS Elastic Beanstalk
- Elastic Load Balancing
- CloudFront
- AWS OpsWorks

For information about server certificates in IAM, see [Managing Server
Certificates][2] in AWS Documentation.

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L70">constructor</a>
</h3>

```typescript
new ServerCertificate(name: string, args: ServerCertificateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServerCertificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerCertificateState): ServerCertificate
```


Get an existing ServerCertificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L38">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the server certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L43">property certificateBody</a>
</h3>

```typescript
public certificateBody: pulumi.Output<string>;
```


The contents of the public key certificate in
PEM-encoded format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L49">property certificateChain</a>
</h3>

```typescript
public certificateChain: pulumi.Output<string | undefined>;
```


The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Server Certificate. Do not include the
path in this value. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L59">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L66">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
See [IAM Identifiers][1] for more details on IAM Paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L70">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string>;
```


The contents of the private key in PEM-encoded format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServiceLinkedRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L10">class ServiceLinkedRole</a>
</h2>

Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L54">constructor</a>
</h3>

```typescript
new ServiceLinkedRole(name: string, args: ServiceLinkedRoleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServiceLinkedRole resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceLinkedRoleState): ServiceLinkedRole
```


Get an existing ServiceLinkedRole resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L30">property awsServiceName</a>
</h3>

```typescript
public awsServiceName: pulumi.Output<string>;
```


The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L34">property createDate</a>
</h3>

```typescript
public createDate: pulumi.Output<string>;
```


The creation date of the IAM role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L38">property customSuffix</a>
</h3>

```typescript
public customSuffix: pulumi.Output<string | undefined>;
```


Additional string appended to the role name. Not all AWS services support custom suffixes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L50">property path</a>
</h3>

```typescript
public path: pulumi.Output<string>;
```


The path of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L54">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The stable and unique string identifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SshKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L10">class SshKey</a>
</h2>

Uploads an SSH public key and associates it with the specified IAM user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L46">constructor</a>
</h3>

```typescript
new SshKey(name: string, args: SshKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SshKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SshKeyState): SshKey
```


Get an existing SshKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L26">property encoding</a>
</h3>

```typescript
public encoding: pulumi.Output<string>;
```


Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L30">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The MD5 message digest of the SSH public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L34">property publicKey</a>
</h3>

```typescript
public publicKey: pulumi.Output<string>;
```


The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L38">property sshPublicKeyId</a>
</h3>

```typescript
public sshPublicKeyId: pulumi.Output<string>;
```


The unique identifier for the SSH public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L42">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L46">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


The name of the IAM user to associate the SSH public key with.

<h2 class="pdoc-module-header" id="User">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L10">class User</a>
</h2>

Provides an IAM user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L52">constructor</a>
</h3>

```typescript
new User(name: string, args?: UserArgs, opts?: pulumi.CustomResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState): User
```


Get an existing User resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS for this user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L32">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


When destroying this user, destroy even if it
has non-Terraform-managed IAM access keys, login profile or MFA devices. Without `force_destroy`
a user with non-Terraform-managed access keys and login profile will fail to be destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L40">property path</a>
</h3>

```typescript
public path: pulumi.Output<string | undefined>;
```


Path in which to create the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L44">property permissionsBoundary</a>
</h3>

```typescript
public permissionsBoundary: pulumi.Output<string | undefined>;
```


The ARN of the policy that is used to set the permissions boundary for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L48">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


Key-value mapping of tags for the IAM user

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L52">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The [unique ID][1] assigned by AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="UserGroupMembership">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L15">class UserGroupMembership</a>
</h2>

Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.

To exclusively manage the users in a group, see the
[`aws_iam_group_membership` resource][3].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L35">constructor</a>
</h3>

```typescript
new UserGroupMembership(name: string, args: UserGroupMembershipArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserGroupMembership resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserGroupMembershipState): UserGroupMembership
```


Get an existing UserGroupMembership resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L31">property groups</a>
</h3>

```typescript
public groups: pulumi.Output<string[]>;
```


A list of [IAM Groups][1] to add the user to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L35">property user</a>
</h3>

```typescript
public user: pulumi.Output<string>;
```


The name of the [IAM User][2] to add to groups

<h2 class="pdoc-module-header" id="UserLoginProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L12">class UserLoginProfile</a>
</h2>

Provides one-time creation of a IAM user login profile, and uses PGP to
encrypt the password for safe transport to the user. PGP keys can be
obtained from Keybase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L52">constructor</a>
</h3>

```typescript
new UserLoginProfile(name: string, args: UserLoginProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserLoginProfile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserLoginProfileState): UserLoginProfile
```


Get an existing UserLoginProfile resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L28">property encryptedPassword</a>
</h3>

```typescript
public encryptedPassword: pulumi.Output<string>;
```


The encrypted password, base64 encoded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L33">property keyFingerprint</a>
</h3>

```typescript
public keyFingerprint: pulumi.Output<string>;
```


The fingerprint of the PGP key used to encrypt
the password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L38">property passwordLength</a>
</h3>

```typescript
public passwordLength: pulumi.Output<number | undefined>;
```


The length of the generated
password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L43">property passwordResetRequired</a>
</h3>

```typescript
public passwordResetRequired: pulumi.Output<boolean | undefined>;
```


Whether the
user should be forced to reset the generated password on first login.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L48">property pgpKey</a>
</h3>

```typescript
public pgpKey: pulumi.Output<string>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:username`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L52">property user</a>
</h3>

```typescript
public user: pulumi.Output<string>;
```


The IAM user's name.

<h2 class="pdoc-module-header" id="UserPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L12">class UserPolicy</a>
</h2>

Provides an IAM policy attached to a user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L40">constructor</a>
</h3>

```typescript
new UserPolicy(name: string, args: UserPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPolicyState): UserPolicy
```


Get an existing UserPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L28">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L32">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L36">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L40">property user</a>
</h3>

```typescript
public user: pulumi.Output<string>;
```


IAM user to which to attach this policy.

<h2 class="pdoc-module-header" id="UserPolicyAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L15">class UserPolicyAttachment</a>
</h2>

Attaches a Managed IAM Policy to an IAM user

~> **NOTE:** The usage of this resource conflicts with the `aws_iam_policy_attachment` resource and will permanently show a difference if both are defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L35">constructor</a>
</h3>

```typescript
new UserPolicyAttachment(name: string, args: UserPolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserPolicyAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPolicyAttachmentState): UserPolicyAttachment
```


Get an existing UserPolicyAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L31">property policyArn</a>
</h3>

```typescript
public policyArn: pulumi.Output<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L35">property user</a>
</h3>

```typescript
public user: pulumi.Output<User>;
```


The user the policy should be applied to

<h2 class="pdoc-module-header" id="AWSAccountActivityAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L18">const AWSAccountActivityAccess</a>
</h2>

```typescript
const AWSAccountActivityAccess: ARN = "arn:aws:iam::aws:policy/AWSAccountActivityAccess";
```

<h2 class="pdoc-module-header" id="AWSAccountUsageReportAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L19">const AWSAccountUsageReportAccess</a>
</h2>

```typescript
const AWSAccountUsageReportAccess: ARN = "arn:aws:iam::aws:policy/AWSAccountUsageReportAccess";
```

<h2 class="pdoc-module-header" id="AWSAgentlessDiscoveryService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L20">const AWSAgentlessDiscoveryService</a>
</h2>

```typescript
const AWSAgentlessDiscoveryService: ARN = "arn:aws:iam::aws:policy/AWSAgentlessDiscoveryService";
```

<h2 class="pdoc-module-header" id="AWSApplicationDiscoveryAgentAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L21">const AWSApplicationDiscoveryAgentAccess</a>
</h2>

```typescript
const AWSApplicationDiscoveryAgentAccess: ARN = "arn:aws:iam::aws:policy/AWSApplicationDiscoveryAgentAccess";
```

<h2 class="pdoc-module-header" id="AWSApplicationDiscoveryServiceFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L22">const AWSApplicationDiscoveryServiceFullAccess</a>
</h2>

```typescript
const AWSApplicationDiscoveryServiceFullAccess: ARN = "arn:aws:iam::aws:policy/AWSApplicationDiscoveryServiceFullAccess";
```

<h2 class="pdoc-module-header" id="AWSBatchFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L23">const AWSBatchFullAccess</a>
</h2>

```typescript
const AWSBatchFullAccess: ARN = "arn:aws:iam::aws:policy/AWSBatchFullAccess";
```

<h2 class="pdoc-module-header" id="AWSBatchServiceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L24">const AWSBatchServiceRole</a>
</h2>

```typescript
const AWSBatchServiceRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole";
```

<h2 class="pdoc-module-header" id="AWSCertificateManagerFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L25">const AWSCertificateManagerFullAccess</a>
</h2>

```typescript
const AWSCertificateManagerFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCertificateManagerReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L26">const AWSCertificateManagerReadOnly</a>
</h2>

```typescript
const AWSCertificateManagerReadOnly: ARN = "arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly";
```

<h2 class="pdoc-module-header" id="AWSCloudFormationReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L27">const AWSCloudFormationReadOnlyAccess</a>
</h2>

```typescript
const AWSCloudFormationReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCloudHSMFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L28">const AWSCloudHSMFullAccess</a>
</h2>

```typescript
const AWSCloudHSMFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCloudHSMFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCloudHSMReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L29">const AWSCloudHSMReadOnlyAccess</a>
</h2>

```typescript
const AWSCloudHSMReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCloudHSMReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCloudHSMRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L30">const AWSCloudHSMRole</a>
</h2>

```typescript
const AWSCloudHSMRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSCloudHSMRole";
```

<h2 class="pdoc-module-header" id="AWSCloudTrailFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L31">const AWSCloudTrailFullAccess</a>
</h2>

```typescript
const AWSCloudTrailFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCloudTrailFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCloudTrailReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L32">const AWSCloudTrailReadOnlyAccess</a>
</h2>

```typescript
const AWSCloudTrailReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCloudTrailReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeBuildAdminAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L33">const AWSCodeBuildAdminAccess</a>
</h2>

```typescript
const AWSCodeBuildAdminAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeBuildAdminAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeBuildDeveloperAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L34">const AWSCodeBuildDeveloperAccess</a>
</h2>

```typescript
const AWSCodeBuildDeveloperAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeBuildDeveloperAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeBuildReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L35">const AWSCodeBuildReadOnlyAccess</a>
</h2>

```typescript
const AWSCodeBuildReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeBuildReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeCommitFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L36">const AWSCodeCommitFullAccess</a>
</h2>

```typescript
const AWSCodeCommitFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeCommitFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeCommitPowerUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L37">const AWSCodeCommitPowerUser</a>
</h2>

```typescript
const AWSCodeCommitPowerUser: ARN = "arn:aws:iam::aws:policy/AWSCodeCommitPowerUser";
```

<h2 class="pdoc-module-header" id="AWSCodeCommitReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L38">const AWSCodeCommitReadOnly</a>
</h2>

```typescript
const AWSCodeCommitReadOnly: ARN = "arn:aws:iam::aws:policy/AWSCodeCommitReadOnly";
```

<h2 class="pdoc-module-header" id="AWSCodeDeployDeployerAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L39">const AWSCodeDeployDeployerAccess</a>
</h2>

```typescript
const AWSCodeDeployDeployerAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeDeployDeployerAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeDeployFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L40">const AWSCodeDeployFullAccess</a>
</h2>

```typescript
const AWSCodeDeployFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeDeployFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeDeployReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L41">const AWSCodeDeployReadOnlyAccess</a>
</h2>

```typescript
const AWSCodeDeployReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeDeployReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeDeployRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L42">const AWSCodeDeployRole</a>
</h2>

```typescript
const AWSCodeDeployRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole";
```

<h2 class="pdoc-module-header" id="AWSCodePipelineApproverAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L43">const AWSCodePipelineApproverAccess</a>
</h2>

```typescript
const AWSCodePipelineApproverAccess: ARN = "arn:aws:iam::aws:policy/AWSCodePipelineApproverAccess";
```

<h2 class="pdoc-module-header" id="AWSCodePipelineCustomActionAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L44">const AWSCodePipelineCustomActionAccess</a>
</h2>

```typescript
const AWSCodePipelineCustomActionAccess: ARN = "arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess";
```

<h2 class="pdoc-module-header" id="AWSCodePipelineFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L45">const AWSCodePipelineFullAccess</a>
</h2>

```typescript
const AWSCodePipelineFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCodePipelineFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCodePipelineReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L46">const AWSCodePipelineReadOnlyAccess</a>
</h2>

```typescript
const AWSCodePipelineReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSCodePipelineReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeStarFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L47">const AWSCodeStarFullAccess</a>
</h2>

```typescript
const AWSCodeStarFullAccess: ARN = "arn:aws:iam::aws:policy/AWSCodeStarFullAccess";
```

<h2 class="pdoc-module-header" id="AWSCodeStarServiceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L48">const AWSCodeStarServiceRole</a>
</h2>

```typescript
const AWSCodeStarServiceRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSCodeStarServiceRole";
```

<h2 class="pdoc-module-header" id="AWSConfigRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L49">const AWSConfigRole</a>
</h2>

```typescript
const AWSConfigRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSConfigRole";
```

<h2 class="pdoc-module-header" id="AWSConfigRulesExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L50">const AWSConfigRulesExecutionRole</a>
</h2>

```typescript
const AWSConfigRulesExecutionRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSConfigRulesExecutionRole";
```

<h2 class="pdoc-module-header" id="AWSConfigUserAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L51">const AWSConfigUserAccess</a>
</h2>

```typescript
const AWSConfigUserAccess: ARN = "arn:aws:iam::aws:policy/AWSConfigUserAccess";
```

<h2 class="pdoc-module-header" id="AWSConnector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L52">const AWSConnector</a>
</h2>

```typescript
const AWSConnector: ARN = "arn:aws:iam::aws:policy/AWSConnector";
```

<h2 class="pdoc-module-header" id="AWSDataPipelineRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L53">const AWSDataPipelineRole</a>
</h2>

```typescript
const AWSDataPipelineRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSDataPipelineRole";
```

<h2 class="pdoc-module-header" id="AWSDataPipeline_FullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L54">const AWSDataPipeline_FullAccess</a>
</h2>

```typescript
const AWSDataPipeline_FullAccess: ARN = "arn:aws:iam::aws:policy/AWSDataPipeline_FullAccess";
```

<h2 class="pdoc-module-header" id="AWSDataPipeline_PowerUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L55">const AWSDataPipeline_PowerUser</a>
</h2>

```typescript
const AWSDataPipeline_PowerUser: ARN = "arn:aws:iam::aws:policy/AWSDataPipeline_PowerUser";
```

<h2 class="pdoc-module-header" id="AWSDeviceFarmFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L56">const AWSDeviceFarmFullAccess</a>
</h2>

```typescript
const AWSDeviceFarmFullAccess: ARN = "arn:aws:iam::aws:policy/AWSDeviceFarmFullAccess";
```

<h2 class="pdoc-module-header" id="AWSDirectConnectFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L57">const AWSDirectConnectFullAccess</a>
</h2>

```typescript
const AWSDirectConnectFullAccess: ARN = "arn:aws:iam::aws:policy/AWSDirectConnectFullAccess";
```

<h2 class="pdoc-module-header" id="AWSDirectConnectReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L58">const AWSDirectConnectReadOnlyAccess</a>
</h2>

```typescript
const AWSDirectConnectReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSDirectoryServiceFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L59">const AWSDirectoryServiceFullAccess</a>
</h2>

```typescript
const AWSDirectoryServiceFullAccess: ARN = "arn:aws:iam::aws:policy/AWSDirectoryServiceFullAccess";
```

<h2 class="pdoc-module-header" id="AWSDirectoryServiceReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L60">const AWSDirectoryServiceReadOnlyAccess</a>
</h2>

```typescript
const AWSDirectoryServiceReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSDirectoryServiceReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkCustomPlatformforEC2Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L61">const AWSElasticBeanstalkCustomPlatformforEC2Role</a>
</h2>

```typescript
const AWSElasticBeanstalkCustomPlatformforEC2Role: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkCustomPlatformforEC2Role";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkEnhancedHealth">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L62">const AWSElasticBeanstalkEnhancedHealth</a>
</h2>

```typescript
const AWSElasticBeanstalkEnhancedHealth: ARN = "arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkEnhancedHealth";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L63">const AWSElasticBeanstalkFullAccess</a>
</h2>

```typescript
const AWSElasticBeanstalkFullAccess: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkFullAccess";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkMulticontainerDocker">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L64">const AWSElasticBeanstalkMulticontainerDocker</a>
</h2>

```typescript
const AWSElasticBeanstalkMulticontainerDocker: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkMulticontainerDocker";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L65">const AWSElasticBeanstalkReadOnlyAccess</a>
</h2>

```typescript
const AWSElasticBeanstalkReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L66">const AWSElasticBeanstalkService</a>
</h2>

```typescript
const AWSElasticBeanstalkService: ARN = "arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkService";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkWebTier">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L67">const AWSElasticBeanstalkWebTier</a>
</h2>

```typescript
const AWSElasticBeanstalkWebTier: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier";
```

<h2 class="pdoc-module-header" id="AWSElasticBeanstalkWorkerTier">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L68">const AWSElasticBeanstalkWorkerTier</a>
</h2>

```typescript
const AWSElasticBeanstalkWorkerTier: ARN = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWorkerTier";
```

<h2 class="pdoc-module-header" id="AWSGreengrassFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L69">const AWSGreengrassFullAccess</a>
</h2>

```typescript
const AWSGreengrassFullAccess: ARN = "arn:aws:iam::aws:policy/AWSGreengrassFullAccess";
```

<h2 class="pdoc-module-header" id="AWSGreengrassResourceAccessRolePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L70">const AWSGreengrassResourceAccessRolePolicy</a>
</h2>

```typescript
const AWSGreengrassResourceAccessRolePolicy: ARN = "arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy";
```

<h2 class="pdoc-module-header" id="AWSHealthFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L71">const AWSHealthFullAccess</a>
</h2>

```typescript
const AWSHealthFullAccess: ARN = "arn:aws:iam::aws:policy/AWSHealthFullAccess";
```

<h2 class="pdoc-module-header" id="AWSImportExportFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L72">const AWSImportExportFullAccess</a>
</h2>

```typescript
const AWSImportExportFullAccess: ARN = "arn:aws:iam::aws:policy/AWSImportExportFullAccess";
```

<h2 class="pdoc-module-header" id="AWSImportExportReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L73">const AWSImportExportReadOnlyAccess</a>
</h2>

```typescript
const AWSImportExportReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSImportExportReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSIoTConfigAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L74">const AWSIoTConfigAccess</a>
</h2>

```typescript
const AWSIoTConfigAccess: ARN = "arn:aws:iam::aws:policy/AWSIoTConfigAccess";
```

<h2 class="pdoc-module-header" id="AWSIoTConfigReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L75">const AWSIoTConfigReadOnlyAccess</a>
</h2>

```typescript
const AWSIoTConfigReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSIoTConfigReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSIoTDataAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L76">const AWSIoTDataAccess</a>
</h2>

```typescript
const AWSIoTDataAccess: ARN = "arn:aws:iam::aws:policy/AWSIoTDataAccess";
```

<h2 class="pdoc-module-header" id="AWSIoTFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L77">const AWSIoTFullAccess</a>
</h2>

```typescript
const AWSIoTFullAccess: ARN = "arn:aws:iam::aws:policy/AWSIoTFullAccess";
```

<h2 class="pdoc-module-header" id="AWSIoTLogging">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L78">const AWSIoTLogging</a>
</h2>

```typescript
const AWSIoTLogging: ARN = "arn:aws:iam::aws:policy/service-role/AWSIoTLogging";
```

<h2 class="pdoc-module-header" id="AWSIoTRuleActions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L79">const AWSIoTRuleActions</a>
</h2>

```typescript
const AWSIoTRuleActions: ARN = "arn:aws:iam::aws:policy/service-role/AWSIoTRuleActions";
```

<h2 class="pdoc-module-header" id="AWSKeyManagementServicePowerUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L80">const AWSKeyManagementServicePowerUser</a>
</h2>

```typescript
const AWSKeyManagementServicePowerUser: ARN = "arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser";
```

<h2 class="pdoc-module-header" id="AWSLambdaBasicExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L81">const AWSLambdaBasicExecutionRole</a>
</h2>

```typescript
const AWSLambdaBasicExecutionRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole";
```

<h2 class="pdoc-module-header" id="AWSLambdaDynamoDBExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L82">const AWSLambdaDynamoDBExecutionRole</a>
</h2>

```typescript
const AWSLambdaDynamoDBExecutionRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole";
```

<h2 class="pdoc-module-header" id="AWSLambdaENIManagementAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L83">const AWSLambdaENIManagementAccess</a>
</h2>

```typescript
const AWSLambdaENIManagementAccess: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaENIManagementAccess";
```

<h2 class="pdoc-module-header" id="AWSLambdaExecute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L84">const AWSLambdaExecute</a>
</h2>

```typescript
const AWSLambdaExecute: ARN = "arn:aws:iam::aws:policy/AWSLambdaExecute";
```

<h2 class="pdoc-module-header" id="AWSLambdaFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L85">const AWSLambdaFullAccess</a>
</h2>

```typescript
const AWSLambdaFullAccess: ARN = "arn:aws:iam::aws:policy/AWSLambdaFullAccess";
```

<h2 class="pdoc-module-header" id="AWSLambdaInvocationDynamoDB">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L86">const AWSLambdaInvocationDynamoDB</a>
</h2>

```typescript
const AWSLambdaInvocationDynamoDB: ARN = "arn:aws:iam::aws:policy/AWSLambdaInvocation-DynamoDB";
```

<h2 class="pdoc-module-header" id="AWSLambdaKinesisExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L87">const AWSLambdaKinesisExecutionRole</a>
</h2>

```typescript
const AWSLambdaKinesisExecutionRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole";
```

<h2 class="pdoc-module-header" id="AWSLambdaReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L88">const AWSLambdaReadOnlyAccess</a>
</h2>

```typescript
const AWSLambdaReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSLambdaReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSLambdaRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L89">const AWSLambdaRole</a>
</h2>

```typescript
const AWSLambdaRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaRole";
```

<h2 class="pdoc-module-header" id="AWSLambdaVPCAccessExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L90">const AWSLambdaVPCAccessExecutionRole</a>
</h2>

```typescript
const AWSLambdaVPCAccessExecutionRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole";
```

<h2 class="pdoc-module-header" id="AWSMarketplaceFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L91">const AWSMarketplaceFullAccess</a>
</h2>

```typescript
const AWSMarketplaceFullAccess: ARN = "arn:aws:iam::aws:policy/AWSMarketplaceFullAccess";
```

<h2 class="pdoc-module-header" id="AWSMarketplaceGetEntitlements">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L92">const AWSMarketplaceGetEntitlements</a>
</h2>

```typescript
const AWSMarketplaceGetEntitlements: ARN = "arn:aws:iam::aws:policy/AWSMarketplaceGetEntitlements";
```

<h2 class="pdoc-module-header" id="AWSMarketplaceManageSubscriptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L93">const AWSMarketplaceManageSubscriptions</a>
</h2>

```typescript
const AWSMarketplaceManageSubscriptions: ARN = "arn:aws:iam::aws:policy/AWSMarketplaceManageSubscriptions";
```

<h2 class="pdoc-module-header" id="AWSMarketplaceMeteringFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L94">const AWSMarketplaceMeteringFullAccess</a>
</h2>

```typescript
const AWSMarketplaceMeteringFullAccess: ARN = "arn:aws:iam::aws:policy/AWSMarketplaceMeteringFullAccess";
```

<h2 class="pdoc-module-header" id="AWSMarketplaceReadonly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L95">const AWSMarketplaceReadonly</a>
</h2>

```typescript
const AWSMarketplaceReadonly: ARN = "arn:aws:iam::aws:policy/AWSMarketplaceRead-only";
```

<h2 class="pdoc-module-header" id="AWSMobileHub_FullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L96">const AWSMobileHub_FullAccess</a>
</h2>

```typescript
const AWSMobileHub_FullAccess: ARN = "arn:aws:iam::aws:policy/AWSMobileHub_FullAccess";
```

<h2 class="pdoc-module-header" id="AWSMobileHub_ReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L97">const AWSMobileHub_ReadOnly</a>
</h2>

```typescript
const AWSMobileHub_ReadOnly: ARN = "arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly";
```

<h2 class="pdoc-module-header" id="AWSMobileHub_ServiceUseOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L98">const AWSMobileHub_ServiceUseOnly</a>
</h2>

```typescript
const AWSMobileHub_ServiceUseOnly: ARN = "arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksCMInstanceProfileRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L99">const AWSOpsWorksCMInstanceProfileRole</a>
</h2>

```typescript
const AWSOpsWorksCMInstanceProfileRole: ARN = "arn:aws:iam::aws:policy/AWSOpsWorksCMInstanceProfileRole";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksCMServiceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L100">const AWSOpsWorksCMServiceRole</a>
</h2>

```typescript
const AWSOpsWorksCMServiceRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSOpsWorksCMServiceRole";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksCloudWatchLogs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L101">const AWSOpsWorksCloudWatchLogs</a>
</h2>

```typescript
const AWSOpsWorksCloudWatchLogs: ARN = "arn:aws:iam::aws:policy/AWSOpsWorksCloudWatchLogs";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L102">const AWSOpsWorksFullAccess</a>
</h2>

```typescript
const AWSOpsWorksFullAccess: ARN = "arn:aws:iam::aws:policy/AWSOpsWorksFullAccess";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksInstanceRegistration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L103">const AWSOpsWorksInstanceRegistration</a>
</h2>

```typescript
const AWSOpsWorksInstanceRegistration: ARN = "arn:aws:iam::aws:policy/AWSOpsWorksInstanceRegistration";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksRegisterCLI">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L104">const AWSOpsWorksRegisterCLI</a>
</h2>

```typescript
const AWSOpsWorksRegisterCLI: ARN = "arn:aws:iam::aws:policy/AWSOpsWorksRegisterCLI";
```

<h2 class="pdoc-module-header" id="AWSOpsWorksRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L105">const AWSOpsWorksRole</a>
</h2>

```typescript
const AWSOpsWorksRole: ARN = "arn:aws:iam::aws:policy/service-role/AWSOpsWorksRole";
```

<h2 class="pdoc-module-header" id="AWSQuickSightDescribeRDS">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L106">const AWSQuickSightDescribeRDS</a>
</h2>

```typescript
const AWSQuickSightDescribeRDS: ARN = "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRDS";
```

<h2 class="pdoc-module-header" id="AWSQuickSightDescribeRedshift">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L107">const AWSQuickSightDescribeRedshift</a>
</h2>

```typescript
const AWSQuickSightDescribeRedshift: ARN = "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRedshift";
```

<h2 class="pdoc-module-header" id="AWSQuickSightListIAM">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L108">const AWSQuickSightListIAM</a>
</h2>

```typescript
const AWSQuickSightListIAM: ARN = "arn:aws:iam::aws:policy/service-role/AWSQuickSightListIAM";
```

<h2 class="pdoc-module-header" id="AWSQuicksightAthenaAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L109">const AWSQuicksightAthenaAccess</a>
</h2>

```typescript
const AWSQuicksightAthenaAccess: ARN = "arn:aws:iam::aws:policy/service-role/AWSQuicksightAthenaAccess";
```

<h2 class="pdoc-module-header" id="AWSStepFunctionsConsoleFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L110">const AWSStepFunctionsConsoleFullAccess</a>
</h2>

```typescript
const AWSStepFunctionsConsoleFullAccess: ARN = "arn:aws:iam::aws:policy/AWSStepFunctionsConsoleFullAccess";
```

<h2 class="pdoc-module-header" id="AWSStepFunctionsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L111">const AWSStepFunctionsFullAccess</a>
</h2>

```typescript
const AWSStepFunctionsFullAccess: ARN = "arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess";
```

<h2 class="pdoc-module-header" id="AWSStepFunctionsReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L112">const AWSStepFunctionsReadOnlyAccess</a>
</h2>

```typescript
const AWSStepFunctionsReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSStepFunctionsReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSStorageGatewayFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L113">const AWSStorageGatewayFullAccess</a>
</h2>

```typescript
const AWSStorageGatewayFullAccess: ARN = "arn:aws:iam::aws:policy/AWSStorageGatewayFullAccess";
```

<h2 class="pdoc-module-header" id="AWSStorageGatewayReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L114">const AWSStorageGatewayReadOnlyAccess</a>
</h2>

```typescript
const AWSStorageGatewayReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSStorageGatewayReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSSupportAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L115">const AWSSupportAccess</a>
</h2>

```typescript
const AWSSupportAccess: ARN = "arn:aws:iam::aws:policy/AWSSupportAccess";
```

<h2 class="pdoc-module-header" id="AWSWAFFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L116">const AWSWAFFullAccess</a>
</h2>

```typescript
const AWSWAFFullAccess: ARN = "arn:aws:iam::aws:policy/AWSWAFFullAccess";
```

<h2 class="pdoc-module-header" id="AWSWAFReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L117">const AWSWAFReadOnlyAccess</a>
</h2>

```typescript
const AWSWAFReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSWAFReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSXrayFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L118">const AWSXrayFullAccess</a>
</h2>

```typescript
const AWSXrayFullAccess: ARN = "arn:aws:iam::aws:policy/AWSXrayFullAccess";
```

<h2 class="pdoc-module-header" id="AWSXrayReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L119">const AWSXrayReadOnlyAccess</a>
</h2>

```typescript
const AWSXrayReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSXrayReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AWSXrayWriteOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L120">const AWSXrayWriteOnlyAccess</a>
</h2>

```typescript
const AWSXrayWriteOnlyAccess: ARN = "arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess";
```

<h2 class="pdoc-module-header" id="AcmServicePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L20">const AcmServicePrincipal</a>
</h2>

Service Principal for Amazon Certificate Manager

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L20">let Service</a>
</h3>

```typescript
let Service: string = "acm.amazonaws.com";
```

<h2 class="pdoc-module-header" id="AdministratorAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L121">const AdministratorAccess</a>
</h2>

```typescript
const AdministratorAccess: ARN = "arn:aws:iam::aws:policy/AdministratorAccess";
```

<h2 class="pdoc-module-header" id="AmazonAPIGatewayAdministrator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L122">const AmazonAPIGatewayAdministrator</a>
</h2>

```typescript
const AmazonAPIGatewayAdministrator: ARN = "arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator";
```

<h2 class="pdoc-module-header" id="AmazonAPIGatewayInvokeFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L123">const AmazonAPIGatewayInvokeFullAccess</a>
</h2>

```typescript
const AmazonAPIGatewayInvokeFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonAPIGatewayPushToCloudWatchLogs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L124">const AmazonAPIGatewayPushToCloudWatchLogs</a>
</h2>

```typescript
const AmazonAPIGatewayPushToCloudWatchLogs: ARN = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs";
```

<h2 class="pdoc-module-header" id="AmazonAppStreamFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L125">const AmazonAppStreamFullAccess</a>
</h2>

```typescript
const AmazonAppStreamFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonAppStreamFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonAppStreamReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L126">const AmazonAppStreamReadOnlyAccess</a>
</h2>

```typescript
const AmazonAppStreamReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonAppStreamReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonAppStreamServiceAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L127">const AmazonAppStreamServiceAccess</a>
</h2>

```typescript
const AmazonAppStreamServiceAccess: ARN = "arn:aws:iam::aws:policy/service-role/AmazonAppStreamServiceAccess";
```

<h2 class="pdoc-module-header" id="AmazonAthenaFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L128">const AmazonAthenaFullAccess</a>
</h2>

```typescript
const AmazonAthenaFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonAthenaFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonCloudDirectoryFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L129">const AmazonCloudDirectoryFullAccess</a>
</h2>

```typescript
const AmazonCloudDirectoryFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonCloudDirectoryFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonCloudDirectoryReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L130">const AmazonCloudDirectoryReadOnlyAccess</a>
</h2>

```typescript
const AmazonCloudDirectoryReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonCloudDirectoryReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonCognitoDeveloperAuthenticatedIdentities">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L131">const AmazonCognitoDeveloperAuthenticatedIdentities</a>
</h2>

```typescript
const AmazonCognitoDeveloperAuthenticatedIdentities: ARN = "arn:aws:iam::aws:policy/AmazonCognitoDeveloperAuthenticatedIdentities";
```

<h2 class="pdoc-module-header" id="AmazonCognitoPowerUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L132">const AmazonCognitoPowerUser</a>
</h2>

```typescript
const AmazonCognitoPowerUser: ARN = "arn:aws:iam::aws:policy/AmazonCognitoPowerUser";
```

<h2 class="pdoc-module-header" id="AmazonCognitoReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L133">const AmazonCognitoReadOnly</a>
</h2>

```typescript
const AmazonCognitoReadOnly: ARN = "arn:aws:iam::aws:policy/AmazonCognitoReadOnly";
```

<h2 class="pdoc-module-header" id="AmazonDMSCloudWatchLogsRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L134">const AmazonDMSCloudWatchLogsRole</a>
</h2>

```typescript
const AmazonDMSCloudWatchLogsRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole";
```

<h2 class="pdoc-module-header" id="AmazonDMSRedshiftS3Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L135">const AmazonDMSRedshiftS3Role</a>
</h2>

```typescript
const AmazonDMSRedshiftS3Role: ARN = "arn:aws:iam::aws:policy/service-role/AmazonDMSRedshiftS3Role";
```

<h2 class="pdoc-module-header" id="AmazonDMSVPCManagementRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L136">const AmazonDMSVPCManagementRole</a>
</h2>

```typescript
const AmazonDMSVPCManagementRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole";
```

<h2 class="pdoc-module-header" id="AmazonDRSVPCManagement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L137">const AmazonDRSVPCManagement</a>
</h2>

```typescript
const AmazonDRSVPCManagement: ARN = "arn:aws:iam::aws:policy/AmazonDRSVPCManagement";
```

<h2 class="pdoc-module-header" id="AmazonDynamoDBFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L138">const AmazonDynamoDBFullAccess</a>
</h2>

```typescript
const AmazonDynamoDBFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonDynamoDBFullAccesswithDataPipeline">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L139">const AmazonDynamoDBFullAccesswithDataPipeline</a>
</h2>

```typescript
const AmazonDynamoDBFullAccesswithDataPipeline: ARN = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccesswithDataPipeline";
```

<h2 class="pdoc-module-header" id="AmazonDynamoDBReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L140">const AmazonDynamoDBReadOnlyAccess</a>
</h2>

```typescript
const AmazonDynamoDBReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerRegistryFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L141">const AmazonEC2ContainerRegistryFullAccess</a>
</h2>

```typescript
const AmazonEC2ContainerRegistryFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerRegistryPowerUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L142">const AmazonEC2ContainerRegistryPowerUser</a>
</h2>

```typescript
const AmazonEC2ContainerRegistryPowerUser: ARN = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerRegistryReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L143">const AmazonEC2ContainerRegistryReadOnly</a>
</h2>

```typescript
const AmazonEC2ContainerRegistryReadOnly: ARN = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerServiceAutoscaleRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L144">const AmazonEC2ContainerServiceAutoscaleRole</a>
</h2>

```typescript
const AmazonEC2ContainerServiceAutoscaleRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceAutoscaleRole";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerServiceFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L145">const AmazonEC2ContainerServiceFullAccess</a>
</h2>

```typescript
const AmazonEC2ContainerServiceFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerServiceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L146">const AmazonEC2ContainerServiceRole</a>
</h2>

```typescript
const AmazonEC2ContainerServiceRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceRole";
```

<h2 class="pdoc-module-header" id="AmazonEC2ContainerServiceforEC2Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L147">const AmazonEC2ContainerServiceforEC2Role</a>
</h2>

```typescript
const AmazonEC2ContainerServiceforEC2Role: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role";
```

<h2 class="pdoc-module-header" id="AmazonEC2FullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L148">const AmazonEC2FullAccess</a>
</h2>

```typescript
const AmazonEC2FullAccess: ARN = "arn:aws:iam::aws:policy/AmazonEC2FullAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2ReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L149">const AmazonEC2ReadOnlyAccess</a>
</h2>

```typescript
const AmazonEC2ReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2ReportsAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L150">const AmazonEC2ReportsAccess</a>
</h2>

```typescript
const AmazonEC2ReportsAccess: ARN = "arn:aws:iam::aws:policy/AmazonEC2ReportsAccess";
```

<h2 class="pdoc-module-header" id="AmazonEC2RoleforAWSCodeDeploy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L151">const AmazonEC2RoleforAWSCodeDeploy</a>
</h2>

```typescript
const AmazonEC2RoleforAWSCodeDeploy: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforAWSCodeDeploy";
```

<h2 class="pdoc-module-header" id="AmazonEC2RoleforDataPipelineRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L152">const AmazonEC2RoleforDataPipelineRole</a>
</h2>

```typescript
const AmazonEC2RoleforDataPipelineRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole";
```

<h2 class="pdoc-module-header" id="AmazonEC2RoleforSSM">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L153">const AmazonEC2RoleforSSM</a>
</h2>

```typescript
const AmazonEC2RoleforSSM: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM";
```

<h2 class="pdoc-module-header" id="AmazonEC2SpotFleetAutoscaleRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L154">const AmazonEC2SpotFleetAutoscaleRole</a>
</h2>

```typescript
const AmazonEC2SpotFleetAutoscaleRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetAutoscaleRole";
```

<h2 class="pdoc-module-header" id="AmazonEC2SpotFleetRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L155">const AmazonEC2SpotFleetRole</a>
</h2>

```typescript
const AmazonEC2SpotFleetRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole";
```

<h2 class="pdoc-module-header" id="AmazonESFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L156">const AmazonESFullAccess</a>
</h2>

```typescript
const AmazonESFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonESFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonESReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L157">const AmazonESReadOnlyAccess</a>
</h2>

```typescript
const AmazonESReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonESReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonElastiCacheFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L158">const AmazonElastiCacheFullAccess</a>
</h2>

```typescript
const AmazonElastiCacheFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonElastiCacheFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonElastiCacheReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L159">const AmazonElastiCacheReadOnlyAccess</a>
</h2>

```typescript
const AmazonElastiCacheReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonElastiCacheReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticFileSystemFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L160">const AmazonElasticFileSystemFullAccess</a>
</h2>

```typescript
const AmazonElasticFileSystemFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticFileSystemFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticFileSystemReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L161">const AmazonElasticFileSystemReadOnlyAccess</a>
</h2>

```typescript
const AmazonElasticFileSystemReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticFileSystemReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticMapReduceFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L162">const AmazonElasticMapReduceFullAccess</a>
</h2>

```typescript
const AmazonElasticMapReduceFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticMapReduceReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L163">const AmazonElasticMapReduceReadOnlyAccess</a>
</h2>

```typescript
const AmazonElasticMapReduceReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticMapReduceReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticMapReduceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L164">const AmazonElasticMapReduceRole</a>
</h2>

```typescript
const AmazonElasticMapReduceRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole";
```

<h2 class="pdoc-module-header" id="AmazonElasticMapReduceforAutoScalingRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L165">const AmazonElasticMapReduceforAutoScalingRole</a>
</h2>

```typescript
const AmazonElasticMapReduceforAutoScalingRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforAutoScalingRole";
```

<h2 class="pdoc-module-header" id="AmazonElasticMapReduceforEC2Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L166">const AmazonElasticMapReduceforEC2Role</a>
</h2>

```typescript
const AmazonElasticMapReduceforEC2Role: ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role";
```

<h2 class="pdoc-module-header" id="AmazonElasticTranscoderFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L167">const AmazonElasticTranscoderFullAccess</a>
</h2>

```typescript
const AmazonElasticTranscoderFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticTranscoderFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticTranscoderJobsSubmitter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L168">const AmazonElasticTranscoderJobsSubmitter</a>
</h2>

```typescript
const AmazonElasticTranscoderJobsSubmitter: ARN = "arn:aws:iam::aws:policy/AmazonElasticTranscoderJobsSubmitter";
```

<h2 class="pdoc-module-header" id="AmazonElasticTranscoderReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L169">const AmazonElasticTranscoderReadOnlyAccess</a>
</h2>

```typescript
const AmazonElasticTranscoderReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonElasticTranscoderReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonElasticTranscoderRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L170">const AmazonElasticTranscoderRole</a>
</h2>

```typescript
const AmazonElasticTranscoderRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticTranscoderRole";
```

<h2 class="pdoc-module-header" id="AmazonGlacierFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L171">const AmazonGlacierFullAccess</a>
</h2>

```typescript
const AmazonGlacierFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonGlacierFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonGlacierReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L172">const AmazonGlacierReadOnlyAccess</a>
</h2>

```typescript
const AmazonGlacierReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonGlacierReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonInspectorFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L173">const AmazonInspectorFullAccess</a>
</h2>

```typescript
const AmazonInspectorFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonInspectorFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonInspectorReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L174">const AmazonInspectorReadOnlyAccess</a>
</h2>

```typescript
const AmazonInspectorReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonInspectorReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonKinesisAnalyticsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L175">const AmazonKinesisAnalyticsFullAccess</a>
</h2>

```typescript
const AmazonKinesisAnalyticsFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonKinesisAnalyticsFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonKinesisAnalyticsReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L176">const AmazonKinesisAnalyticsReadOnly</a>
</h2>

```typescript
const AmazonKinesisAnalyticsReadOnly: ARN = "arn:aws:iam::aws:policy/AmazonKinesisAnalyticsReadOnly";
```

<h2 class="pdoc-module-header" id="AmazonKinesisFirehoseFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L177">const AmazonKinesisFirehoseFullAccess</a>
</h2>

```typescript
const AmazonKinesisFirehoseFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonKinesisFirehoseFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonKinesisFirehoseReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L178">const AmazonKinesisFirehoseReadOnlyAccess</a>
</h2>

```typescript
const AmazonKinesisFirehoseReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonKinesisFirehoseReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonKinesisFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L179">const AmazonKinesisFullAccess</a>
</h2>

```typescript
const AmazonKinesisFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonKinesisFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonKinesisReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L180">const AmazonKinesisReadOnlyAccess</a>
</h2>

```typescript
const AmazonKinesisReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonKinesisReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonLexFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L181">const AmazonLexFullAccess</a>
</h2>

```typescript
const AmazonLexFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonLexFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonLexReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L182">const AmazonLexReadOnly</a>
</h2>

```typescript
const AmazonLexReadOnly: ARN = "arn:aws:iam::aws:policy/AmazonLexReadOnly";
```

<h2 class="pdoc-module-header" id="AmazonLexRunBotsOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L183">const AmazonLexRunBotsOnly</a>
</h2>

```typescript
const AmazonLexRunBotsOnly: ARN = "arn:aws:iam::aws:policy/AmazonLexRunBotsOnly";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningBatchPredictionsAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L184">const AmazonMachineLearningBatchPredictionsAccess</a>
</h2>

```typescript
const AmazonMachineLearningBatchPredictionsAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningBatchPredictionsAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningCreateOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L185">const AmazonMachineLearningCreateOnlyAccess</a>
</h2>

```typescript
const AmazonMachineLearningCreateOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningCreateOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L186">const AmazonMachineLearningFullAccess</a>
</h2>

```typescript
const AmazonMachineLearningFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningManageRealTimeEndpointOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L187">const AmazonMachineLearningManageRealTimeEndpointOnlyAccess</a>
</h2>

```typescript
const AmazonMachineLearningManageRealTimeEndpointOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningManageRealTimeEndpointOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L188">const AmazonMachineLearningReadOnlyAccess</a>
</h2>

```typescript
const AmazonMachineLearningReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningRealTimePredictionOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L189">const AmazonMachineLearningRealTimePredictionOnlyAccess</a>
</h2>

```typescript
const AmazonMachineLearningRealTimePredictionOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonMachineLearningRealTimePredictionOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonMachineLearningRoleforRedshiftDataSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L190">const AmazonMachineLearningRoleforRedshiftDataSource</a>
</h2>

```typescript
const AmazonMachineLearningRoleforRedshiftDataSource: ARN = "arn:aws:iam::aws:policy/service-role/AmazonMachineLearningRoleforRedshiftDataSource";
```

<h2 class="pdoc-module-header" id="AmazonMechanicalTurkFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L191">const AmazonMechanicalTurkFullAccess</a>
</h2>

```typescript
const AmazonMechanicalTurkFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonMechanicalTurkFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonMechanicalTurkReadOnly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L192">const AmazonMechanicalTurkReadOnly</a>
</h2>

```typescript
const AmazonMechanicalTurkReadOnly: ARN = "arn:aws:iam::aws:policy/AmazonMechanicalTurkReadOnly";
```

<h2 class="pdoc-module-header" id="AmazonMobileAnalyticsFinancialReportAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L193">const AmazonMobileAnalyticsFinancialReportAccess</a>
</h2>

```typescript
const AmazonMobileAnalyticsFinancialReportAccess: ARN = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFinancialReportAccess";
```

<h2 class="pdoc-module-header" id="AmazonMobileAnalyticsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L194">const AmazonMobileAnalyticsFullAccess</a>
</h2>

```typescript
const AmazonMobileAnalyticsFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonMobileAnalyticsNonfinancialReportAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L195">const AmazonMobileAnalyticsNonfinancialReportAccess</a>
</h2>

```typescript
const AmazonMobileAnalyticsNonfinancialReportAccess: ARN = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsNon-financialReportAccess";
```

<h2 class="pdoc-module-header" id="AmazonMobileAnalyticsWriteOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L196">const AmazonMobileAnalyticsWriteOnlyAccess</a>
</h2>

```typescript
const AmazonMobileAnalyticsWriteOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsWriteOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonPollyFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L197">const AmazonPollyFullAccess</a>
</h2>

```typescript
const AmazonPollyFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonPollyFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonPollyReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L198">const AmazonPollyReadOnlyAccess</a>
</h2>

```typescript
const AmazonPollyReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonPollyReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonRDSDirectoryServiceAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L199">const AmazonRDSDirectoryServiceAccess</a>
</h2>

```typescript
const AmazonRDSDirectoryServiceAccess: ARN = "arn:aws:iam::aws:policy/service-role/AmazonRDSDirectoryServiceAccess";
```

<h2 class="pdoc-module-header" id="AmazonRDSEnhancedMonitoringRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L200">const AmazonRDSEnhancedMonitoringRole</a>
</h2>

```typescript
const AmazonRDSEnhancedMonitoringRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole";
```

<h2 class="pdoc-module-header" id="AmazonRDSFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L201">const AmazonRDSFullAccess</a>
</h2>

```typescript
const AmazonRDSFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonRDSFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonRDSReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L202">const AmazonRDSReadOnlyAccess</a>
</h2>

```typescript
const AmazonRDSReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonRDSReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonRedshiftFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L203">const AmazonRedshiftFullAccess</a>
</h2>

```typescript
const AmazonRedshiftFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonRedshiftFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonRedshiftReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L204">const AmazonRedshiftReadOnlyAccess</a>
</h2>

```typescript
const AmazonRedshiftReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonRedshiftReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonRekognitionFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L205">const AmazonRekognitionFullAccess</a>
</h2>

```typescript
const AmazonRekognitionFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonRekognitionFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonRekognitionReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L206">const AmazonRekognitionReadOnlyAccess</a>
</h2>

```typescript
const AmazonRekognitionReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonRekognitionReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonRoute53DomainsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L207">const AmazonRoute53DomainsFullAccess</a>
</h2>

```typescript
const AmazonRoute53DomainsFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonRoute53DomainsFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonRoute53DomainsReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L208">const AmazonRoute53DomainsReadOnlyAccess</a>
</h2>

```typescript
const AmazonRoute53DomainsReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonRoute53DomainsReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonRoute53FullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L209">const AmazonRoute53FullAccess</a>
</h2>

```typescript
const AmazonRoute53FullAccess: ARN = "arn:aws:iam::aws:policy/AmazonRoute53FullAccess";
```

<h2 class="pdoc-module-header" id="AmazonRoute53ReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L210">const AmazonRoute53ReadOnlyAccess</a>
</h2>

```typescript
const AmazonRoute53ReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonS3FullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L211">const AmazonS3FullAccess</a>
</h2>

```typescript
const AmazonS3FullAccess: ARN = "arn:aws:iam::aws:policy/AmazonS3FullAccess";
```

<h2 class="pdoc-module-header" id="AmazonS3ReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L212">const AmazonS3ReadOnlyAccess</a>
</h2>

```typescript
const AmazonS3ReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonSESFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L213">const AmazonSESFullAccess</a>
</h2>

```typescript
const AmazonSESFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonSESFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonSESReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L214">const AmazonSESReadOnlyAccess</a>
</h2>

```typescript
const AmazonSESReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonSESReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonSNSFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L215">const AmazonSNSFullAccess</a>
</h2>

```typescript
const AmazonSNSFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonSNSFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonSNSReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L216">const AmazonSNSReadOnlyAccess</a>
</h2>

```typescript
const AmazonSNSReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonSNSReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonSNSRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L217">const AmazonSNSRole</a>
</h2>

```typescript
const AmazonSNSRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonSNSRole";
```

<h2 class="pdoc-module-header" id="AmazonSQSFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L218">const AmazonSQSFullAccess</a>
</h2>

```typescript
const AmazonSQSFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonSQSFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonSQSReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L219">const AmazonSQSReadOnlyAccess</a>
</h2>

```typescript
const AmazonSQSReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonSSMAutomationRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L220">const AmazonSSMAutomationRole</a>
</h2>

```typescript
const AmazonSSMAutomationRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonSSMAutomationRole";
```

<h2 class="pdoc-module-header" id="AmazonSSMFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L221">const AmazonSSMFullAccess</a>
</h2>

```typescript
const AmazonSSMFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonSSMFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonSSMMaintenanceWindowRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L222">const AmazonSSMMaintenanceWindowRole</a>
</h2>

```typescript
const AmazonSSMMaintenanceWindowRole: ARN = "arn:aws:iam::aws:policy/service-role/AmazonSSMMaintenanceWindowRole";
```

<h2 class="pdoc-module-header" id="AmazonSSMReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L223">const AmazonSSMReadOnlyAccess</a>
</h2>

```typescript
const AmazonSSMReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonVPCFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L224">const AmazonVPCFullAccess</a>
</h2>

```typescript
const AmazonVPCFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonVPCFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonVPCReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L225">const AmazonVPCReadOnlyAccess</a>
</h2>

```typescript
const AmazonVPCReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonVPCReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonWorkMailFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L226">const AmazonWorkMailFullAccess</a>
</h2>

```typescript
const AmazonWorkMailFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonWorkMailFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonWorkMailReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L227">const AmazonWorkMailReadOnlyAccess</a>
</h2>

```typescript
const AmazonWorkMailReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AmazonWorkSpacesAdmin">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L228">const AmazonWorkSpacesAdmin</a>
</h2>

```typescript
const AmazonWorkSpacesAdmin: ARN = "arn:aws:iam::aws:policy/AmazonWorkSpacesAdmin";
```

<h2 class="pdoc-module-header" id="AmazonWorkSpacesApplicationManagerAdminAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L229">const AmazonWorkSpacesApplicationManagerAdminAccess</a>
</h2>

```typescript
const AmazonWorkSpacesApplicationManagerAdminAccess: ARN = "arn:aws:iam::aws:policy/AmazonWorkSpacesApplicationManagerAdminAccess";
```

<h2 class="pdoc-module-header" id="AmazonZocaloFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L230">const AmazonZocaloFullAccess</a>
</h2>

```typescript
const AmazonZocaloFullAccess: ARN = "arn:aws:iam::aws:policy/AmazonZocaloFullAccess";
```

<h2 class="pdoc-module-header" id="AmazonZocaloReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L231">const AmazonZocaloReadOnlyAccess</a>
</h2>

```typescript
const AmazonZocaloReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AmazonZocaloReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="ApiGatewayPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L25">const ApiGatewayPrincipal</a>
</h2>

Service Principal for API Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L25">let Service</a>
</h3>

```typescript
let Service: string = "apigateway.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ApplicationAutoScalingForAmazonAppStreamAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L232">const ApplicationAutoScalingForAmazonAppStreamAccess</a>
</h2>

```typescript
const ApplicationAutoScalingForAmazonAppStreamAccess: ARN = "arn:aws:iam::aws:policy/service-role/ApplicationAutoScalingForAmazonAppStreamAccess";
```

<h2 class="pdoc-module-header" id="AthenaPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L30">const AthenaPrincipal</a>
</h2>

Service Principal for Athena

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L30">let Service</a>
</h3>

```typescript
let Service: string = "athena.amazonaws.com";
```

<h2 class="pdoc-module-header" id="AutoScalingConsoleFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L233">const AutoScalingConsoleFullAccess</a>
</h2>

```typescript
const AutoScalingConsoleFullAccess: ARN = "arn:aws:iam::aws:policy/AutoScalingConsoleFullAccess";
```

<h2 class="pdoc-module-header" id="AutoScalingConsoleReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L234">const AutoScalingConsoleReadOnlyAccess</a>
</h2>

```typescript
const AutoScalingConsoleReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AutoScalingConsoleReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AutoScalingFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L235">const AutoScalingFullAccess</a>
</h2>

```typescript
const AutoScalingFullAccess: ARN = "arn:aws:iam::aws:policy/AutoScalingFullAccess";
```

<h2 class="pdoc-module-header" id="AutoScalingNotificationAccessRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L236">const AutoScalingNotificationAccessRole</a>
</h2>

```typescript
const AutoScalingNotificationAccessRole: ARN = "arn:aws:iam::aws:policy/service-role/AutoScalingNotificationAccessRole";
```

<h2 class="pdoc-module-header" id="AutoScalingReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L237">const AutoScalingReadOnlyAccess</a>
</h2>

```typescript
const AutoScalingReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/AutoScalingReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="AutoscalingPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L35">const AutoscalingPrincipal</a>
</h2>

Service Principal for Autoscaling

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L35">let Service</a>
</h3>

```typescript
let Service: string = "autoscaling.amazonaws.com";
```

<h2 class="pdoc-module-header" id="Billing">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L238">const Billing</a>
</h2>

```typescript
const Billing: ARN = "arn:aws:iam::aws:policy/job-function/Billing";
```

<h2 class="pdoc-module-header" id="CloudDirectoryPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L40">const CloudDirectoryPrincipal</a>
</h2>

Service Principal for Cloud Directory

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L40">let Service</a>
</h3>

```typescript
let Service: string = "clouddirectory.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CloudFrontFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L239">const CloudFrontFullAccess</a>
</h2>

```typescript
const CloudFrontFullAccess: ARN = "arn:aws:iam::aws:policy/CloudFrontFullAccess";
```

<h2 class="pdoc-module-header" id="CloudFrontReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L240">const CloudFrontReadOnlyAccess</a>
</h2>

```typescript
const CloudFrontReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/CloudFrontReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="CloudSearchFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L241">const CloudSearchFullAccess</a>
</h2>

```typescript
const CloudSearchFullAccess: ARN = "arn:aws:iam::aws:policy/CloudSearchFullAccess";
```

<h2 class="pdoc-module-header" id="CloudSearchPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L55">const CloudSearchPrincipal</a>
</h2>

Service Principal for Cloud Search

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L55">let Service</a>
</h3>

```typescript
let Service: string = "cloudsearch.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CloudSearchReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L242">const CloudSearchReadOnlyAccess</a>
</h2>

```typescript
const CloudSearchReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/CloudSearchReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchActionsEC2Access">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L243">const CloudWatchActionsEC2Access</a>
</h2>

```typescript
const CloudWatchActionsEC2Access: ARN = "arn:aws:iam::aws:policy/CloudWatchActionsEC2Access";
```

<h2 class="pdoc-module-header" id="CloudWatchEventsBuiltInTargetExecutionAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L244">const CloudWatchEventsBuiltInTargetExecutionAccess</a>
</h2>

```typescript
const CloudWatchEventsBuiltInTargetExecutionAccess: ARN = "arn:aws:iam::aws:policy/service-role/CloudWatchEventsBuiltInTargetExecutionAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchEventsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L245">const CloudWatchEventsFullAccess</a>
</h2>

```typescript
const CloudWatchEventsFullAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchEventsFullAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchEventsInvocationAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L246">const CloudWatchEventsInvocationAccess</a>
</h2>

```typescript
const CloudWatchEventsInvocationAccess: ARN = "arn:aws:iam::aws:policy/service-role/CloudWatchEventsInvocationAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchEventsReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L247">const CloudWatchEventsReadOnlyAccess</a>
</h2>

```typescript
const CloudWatchEventsReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchEventsReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L248">const CloudWatchFullAccess</a>
</h2>

```typescript
const CloudWatchFullAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchFullAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchLogsFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L249">const CloudWatchLogsFullAccess</a>
</h2>

```typescript
const CloudWatchLogsFullAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchLogsReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L250">const CloudWatchLogsReadOnlyAccess</a>
</h2>

```typescript
const CloudWatchLogsReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchLogsReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="CloudWatchReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L251">const CloudWatchReadOnlyAccess</a>
</h2>

```typescript
const CloudWatchReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="CloudformationPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L45">const CloudformationPrincipal</a>
</h2>

Service Principal for Cloudformation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L45">let Service</a>
</h3>

```typescript
let Service: string = "cloudformation.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CloudfrontPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L50">const CloudfrontPrincipal</a>
</h2>

Service Principal for Cloudfront

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L50">let Service</a>
</h3>

```typescript
let Service: string = "cloudfront.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CloudtrailPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L60">const CloudtrailPrincipal</a>
</h2>

Service Principal for Cloudtrail

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L60">let Service</a>
</h3>

```typescript
let Service: string = "cloudtrail.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CodeCommitPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L65">const CodeCommitPrincipal</a>
</h2>

Service Principal for CodeCommit

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L65">let Service</a>
</h3>

```typescript
let Service: string = "codecommit.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CodeDeployPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L70">const CodeDeployPrincipal</a>
</h2>

Service Principal for CodeDeploy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L70">let Service</a>
</h3>

```typescript
let Service: string = "codedeploy.amazonaws.com";
```

<h2 class="pdoc-module-header" id="CodePipelinePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L75">const CodePipelinePrincipal</a>
</h2>

Service Principal for CodePipeline

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L75">let Service</a>
</h3>

```typescript
let Service: string = "codepipeline.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ConfigPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L80">const ConfigPrincipal</a>
</h2>

Service Principal for EC2 Config Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L80">let Service</a>
</h3>

```typescript
let Service: string = "config.amazonaws.com";
```

<h2 class="pdoc-module-header" id="DataPipelinePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L85">const DataPipelinePrincipal</a>
</h2>

Service Principal for Data Pipeline

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L85">let Service</a>
</h3>

```typescript
let Service: string = "datapipeline.amazonaws.com";
```

<h2 class="pdoc-module-header" id="DataScientist">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L252">const DataScientist</a>
</h2>

```typescript
const DataScientist: ARN = "arn:aws:iam::aws:policy/job-function/DataScientist";
```

<h2 class="pdoc-module-header" id="DatabaseAdministrator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L253">const DatabaseAdministrator</a>
</h2>

```typescript
const DatabaseAdministrator: ARN = "arn:aws:iam::aws:policy/job-function/DatabaseAdministrator";
```

<h2 class="pdoc-module-header" id="DirectConnectPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L90">const DirectConnectPrincipal</a>
</h2>

Service Principal for DirectConnect

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L90">let Service</a>
</h3>

```typescript
let Service: string = "directconnect.amazonaws.com";
```

<h2 class="pdoc-module-header" id="DirectoryServicesPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L95">const DirectoryServicesPrincipal</a>
</h2>

Service Principal for Directory Services

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L95">let Service</a>
</h3>

```typescript
let Service: string = "ds.amazonaws.com";
```

<h2 class="pdoc-module-header" id="DynamoDbPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L100">const DynamoDbPrincipal</a>
</h2>

Service Principal for DynamoDB

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L100">let Service</a>
</h3>

```typescript
let Service: string = "dynamodb.amazonaws.com";
```

<h2 class="pdoc-module-header" id="Ec2Principal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L105">const Ec2Principal</a>
</h2>

Service Principal for EC2

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L105">let Service</a>
</h3>

```typescript
let Service: string = "ec2.amazonaws.com";
```

<h2 class="pdoc-module-header" id="EcrPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L110">const EcrPrincipal</a>
</h2>

Service Principal for Elastic Container Registry

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L110">let Service</a>
</h3>

```typescript
let Service: string = "ecr.amazonaws.com";
```

<h2 class="pdoc-module-header" id="EcsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L115">const EcsPrincipal</a>
</h2>

Service Principal for Elastic Container Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L115">let Service</a>
</h3>

```typescript
let Service: string = "ecs.amazonaws.com";
```

<h2 class="pdoc-module-header" id="EdgeLambdaPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L120">const EdgeLambdaPrincipal</a>
</h2>

Service Principal for Edge Lambda

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L120">let Service</a>
</h3>

```typescript
let Service: string = "edgelambda.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ElasticBeanstalkPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L130">const ElasticBeanstalkPrincipal</a>
</h2>

Service Principal for Elastic Beanstalk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L130">let Service</a>
</h3>

```typescript
let Service: string = "elasticbeanstalk.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ElasticFileSystemPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L135">const ElasticFileSystemPrincipal</a>
</h2>

Service Principal for Elastic File System

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L135">let Service</a>
</h3>

```typescript
let Service: string = "elasticfilesystem.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ElasticLoadBalancingPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L140">const ElasticLoadBalancingPrincipal</a>
</h2>

Service Principal for Elastic Load Balancing

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L140">let Service</a>
</h3>

```typescript
let Service: string = "elasticloadbalancing.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ElasticMapReducePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L145">const ElasticMapReducePrincipal</a>
</h2>

Service Principal for Elastic MapReduce

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L145">let Service</a>
</h3>

```typescript
let Service: string = "elasticmapreduce.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ElasticachePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L125">const ElasticachePrincipal</a>
</h2>

Service Principal for Elasticache

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L125">let Service</a>
</h3>

```typescript
let Service: string = "elasticache.amazonaws.com";
```

<h2 class="pdoc-module-header" id="EventsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L150">const EventsPrincipal</a>
</h2>

Service Principal for Events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L150">let Service</a>
</h3>

```typescript
let Service: string = "events.amazonaws.com";
```

<h2 class="pdoc-module-header" id="HealthPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L155">const HealthPrincipal</a>
</h2>

Service Principal for Health

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L155">let Service</a>
</h3>

```typescript
let Service: string = "health.amazonaws.com";
```

<h2 class="pdoc-module-header" id="IAMFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L254">const IAMFullAccess</a>
</h2>

```typescript
const IAMFullAccess: ARN = "arn:aws:iam::aws:policy/IAMFullAccess";
```

<h2 class="pdoc-module-header" id="IAMReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L255">const IAMReadOnlyAccess</a>
</h2>

```typescript
const IAMReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/IAMReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="IAMSelfManageServiceSpecificCredentials">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L256">const IAMSelfManageServiceSpecificCredentials</a>
</h2>

```typescript
const IAMSelfManageServiceSpecificCredentials: ARN = "arn:aws:iam::aws:policy/IAMSelfManageServiceSpecificCredentials";
```

<h2 class="pdoc-module-header" id="IAMUserChangePassword">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L257">const IAMUserChangePassword</a>
</h2>

```typescript
const IAMUserChangePassword: ARN = "arn:aws:iam::aws:policy/IAMUserChangePassword";
```

<h2 class="pdoc-module-header" id="IAMUserSSHKeys">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L258">const IAMUserSSHKeys</a>
</h2>

```typescript
const IAMUserSSHKeys: ARN = "arn:aws:iam::aws:policy/IAMUserSSHKeys";
```

<h2 class="pdoc-module-header" id="IamPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L160">const IamPrincipal</a>
</h2>

Service Principal for IAM

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L160">let Service</a>
</h3>

```typescript
let Service: string = "iam.amazonaws.com";
```

<h2 class="pdoc-module-header" id="InspectorPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L165">const InspectorPrincipal</a>
</h2>

Service Principal for AWS Inspector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L165">let Service</a>
</h3>

```typescript
let Service: string = "inspector.amazonaws.com";
```

<h2 class="pdoc-module-header" id="KinesisPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L170">const KinesisPrincipal</a>
</h2>

Service Principal for Kinesis

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L170">let Service</a>
</h3>

```typescript
let Service: string = "kinesis.amazonaws.com";
```

<h2 class="pdoc-module-header" id="KmsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L175">const KmsPrincipal</a>
</h2>

Service Principal for Key Mangaement Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L175">let Service</a>
</h3>

```typescript
let Service: string = "kms.amazonaws.com";
```

<h2 class="pdoc-module-header" id="LambdaPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L180">const LambdaPrincipal</a>
</h2>

Service Principal for Lambda

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L180">let Service</a>
</h3>

```typescript
let Service: string = "lambda.amazonaws.com";
```

<h2 class="pdoc-module-header" id="LightsailPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L185">const LightsailPrincipal</a>
</h2>

Service Principal for Lightsail

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L185">let Service</a>
</h3>

```typescript
let Service: string = "lightsail.amazonaws.com";
```

<h2 class="pdoc-module-header" id="LogsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L190">const LogsPrincipal</a>
</h2>

Service Principal for Cloudwatch Logs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L190">let Service</a>
</h3>

```typescript
let Service: string = "logs.amazonaws.com";
```

<h2 class="pdoc-module-header" id="MonitoringPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L195">const MonitoringPrincipal</a>
</h2>

Service Principal for Cloudwatch Monitoring

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L195">let Service</a>
</h3>

```typescript
let Service: string = "monitoring.amazonaws.com";
```

<h2 class="pdoc-module-header" id="NetworkAdministrator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L259">const NetworkAdministrator</a>
</h2>

```typescript
const NetworkAdministrator: ARN = "arn:aws:iam::aws:policy/job-function/NetworkAdministrator";
```

<h2 class="pdoc-module-header" id="OpsworksPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L200">const OpsworksPrincipal</a>
</h2>

Service Principal for Opsworks

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L200">let Service</a>
</h3>

```typescript
let Service: string = "opsworks.amazonaws.com";
```

<h2 class="pdoc-module-header" id="OrganizationsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L205">const OrganizationsPrincipal</a>
</h2>

Service Principal for Organizations

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L205">let Service</a>
</h3>

```typescript
let Service: string = "organizations.amazonaws.com";
```

<h2 class="pdoc-module-header" id="PowerUserAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L260">const PowerUserAccess</a>
</h2>

```typescript
const PowerUserAccess: ARN = "arn:aws:iam::aws:policy/PowerUserAccess";
```

<h2 class="pdoc-module-header" id="RDSCloudHsmAuthorizationRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L261">const RDSCloudHsmAuthorizationRole</a>
</h2>

```typescript
const RDSCloudHsmAuthorizationRole: ARN = "arn:aws:iam::aws:policy/service-role/RDSCloudHsmAuthorizationRole";
```

<h2 class="pdoc-module-header" id="RdsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L210">const RdsPrincipal</a>
</h2>

Service Principal for Relational Database Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L210">let Service</a>
</h3>

```typescript
let Service: string = "rds.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L262">const ReadOnlyAccess</a>
</h2>

```typescript
const ReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/ReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="RedshiftPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L215">const RedshiftPrincipal</a>
</h2>

Service Principal for Redshift

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L215">let Service</a>
</h3>

```typescript
let Service: string = "redshift.amazonaws.com";
```

<h2 class="pdoc-module-header" id="ResourceGroupsandTagEditorFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L263">const ResourceGroupsandTagEditorFullAccess</a>
</h2>

```typescript
const ResourceGroupsandTagEditorFullAccess: ARN = "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess";
```

<h2 class="pdoc-module-header" id="ResourceGroupsandTagEditorReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L264">const ResourceGroupsandTagEditorReadOnlyAccess</a>
</h2>

```typescript
const ResourceGroupsandTagEditorReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="Route53Principal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L220">const Route53Principal</a>
</h2>

Service Principal for Route 53

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L220">let Service</a>
</h3>

```typescript
let Service: string = "route53.amazonaws.com";
```

<h2 class="pdoc-module-header" id="S3Principal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L225">const S3Principal</a>
</h2>

Service Principal for S3

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L225">let Service</a>
</h3>

```typescript
let Service: string = "s3.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SecurityAudit">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L265">const SecurityAudit</a>
</h2>

```typescript
const SecurityAudit: ARN = "arn:aws:iam::aws:policy/SecurityAudit";
```

<h2 class="pdoc-module-header" id="ServerMigrationConnector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L266">const ServerMigrationConnector</a>
</h2>

```typescript
const ServerMigrationConnector: ARN = "arn:aws:iam::aws:policy/ServerMigrationConnector";
```

<h2 class="pdoc-module-header" id="ServerMigrationServiceRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L267">const ServerMigrationServiceRole</a>
</h2>

```typescript
const ServerMigrationServiceRole: ARN = "arn:aws:iam::aws:policy/service-role/ServerMigrationServiceRole";
```

<h2 class="pdoc-module-header" id="ServiceCatalogAdminFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L268">const ServiceCatalogAdminFullAccess</a>
</h2>

```typescript
const ServiceCatalogAdminFullAccess: ARN = "arn:aws:iam::aws:policy/ServiceCatalogAdminFullAccess";
```

<h2 class="pdoc-module-header" id="ServiceCatalogAdminReadOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L269">const ServiceCatalogAdminReadOnlyAccess</a>
</h2>

```typescript
const ServiceCatalogAdminReadOnlyAccess: ARN = "arn:aws:iam::aws:policy/ServiceCatalogAdminReadOnlyAccess";
```

<h2 class="pdoc-module-header" id="ServiceCatalogEndUserAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L270">const ServiceCatalogEndUserAccess</a>
</h2>

```typescript
const ServiceCatalogEndUserAccess: ARN = "arn:aws:iam::aws:policy/ServiceCatalogEndUserAccess";
```

<h2 class="pdoc-module-header" id="ServiceCatalogEndUserFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L271">const ServiceCatalogEndUserFullAccess</a>
</h2>

```typescript
const ServiceCatalogEndUserFullAccess: ARN = "arn:aws:iam::aws:policy/ServiceCatalogEndUserFullAccess";
```

<h2 class="pdoc-module-header" id="ServiceCatalogPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L230">const ServiceCatalogPrincipal</a>
</h2>

Service Principal for Service Catalog

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L230">let Service</a>
</h3>

```typescript
let Service: string = "servicecatalog.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SesPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L235">const SesPrincipal</a>
</h2>

Service Principal for Simple Email Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L235">let Service</a>
</h3>

```typescript
let Service: string = "ses.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SigninPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L240">const SigninPrincipal</a>
</h2>

Service Principal for Signin Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L240">let Service</a>
</h3>

```typescript
let Service: string = "signin.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SimpleWorkflowFullAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L272">const SimpleWorkflowFullAccess</a>
</h2>

```typescript
const SimpleWorkflowFullAccess: ARN = "arn:aws:iam::aws:policy/SimpleWorkflowFullAccess";
```

<h2 class="pdoc-module-header" id="SnsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L245">const SnsPrincipal</a>
</h2>

Service Principal for Simple Notification Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L245">let Service</a>
</h3>

```typescript
let Service: string = "sns.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SqsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L250">const SqsPrincipal</a>
</h2>

Service Principal for Simple Queue Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L250">let Service</a>
</h3>

```typescript
let Service: string = "sqs.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SsmPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L255">const SsmPrincipal</a>
</h2>

Service Principal for Systems Manager

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L255">let Service</a>
</h3>

```typescript
let Service: string = "ssm.amazonaws.com";
```

<h2 class="pdoc-module-header" id="StorageGatewayPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L260">const StorageGatewayPrincipal</a>
</h2>

Service Principal for Storage Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L260">let Service</a>
</h3>

```typescript
let Service: string = "storagegateway.amazonaws.com";
```

<h2 class="pdoc-module-header" id="StsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L265">const StsPrincipal</a>
</h2>

Service Principal for Security Token Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L265">let Service</a>
</h3>

```typescript
let Service: string = "sts.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SupportPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L270">const SupportPrincipal</a>
</h2>

Service Principal for AWS Support

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L270">let Service</a>
</h3>

```typescript
let Service: string = "support.amazonaws.com";
```

<h2 class="pdoc-module-header" id="SupportUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L273">const SupportUser</a>
</h2>

```typescript
const SupportUser: ARN = "arn:aws:iam::aws:policy/job-function/SupportUser";
```

<h2 class="pdoc-module-header" id="SystemAdministrator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L274">const SystemAdministrator</a>
</h2>

```typescript
const SystemAdministrator: ARN = "arn:aws:iam::aws:policy/job-function/SystemAdministrator";
```

<h2 class="pdoc-module-header" id="VMImportExportRoleForAWSConnector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L275">const VMImportExportRoleForAWSConnector</a>
</h2>

```typescript
const VMImportExportRoleForAWSConnector: ARN = "arn:aws:iam::aws:policy/service-role/VMImportExportRoleForAWSConnector";
```

<h2 class="pdoc-module-header" id="ViewOnlyAccess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/managedPolicies.ts#L276">const ViewOnlyAccess</a>
</h2>

```typescript
const ViewOnlyAccess: ARN = "arn:aws:iam::aws:policy/job-function/ViewOnlyAccess";
```

<h2 class="pdoc-module-header" id="VmiePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L275">const VmiePrincipal</a>
</h2>

Service Principal for VM Import/Export

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L275">let Service</a>
</h3>

```typescript
let Service: string = "vmie.amazonaws.com";
```

<h2 class="pdoc-module-header" id="VpcFlowLogsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L280">const VpcFlowLogsPrincipal</a>
</h2>

Service Principal for VPC Flow Logs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L280">let Service</a>
</h3>

```typescript
let Service: string = "vpc-flow-logs.amazonaws.com";
```

<h2 class="pdoc-module-header" id="WafPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L285">const WafPrincipal</a>
</h2>

Service Principal for Web Application Firewall

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L285">let Service</a>
</h3>

```typescript
let Service: string = "waf.amazonaws.com";
```

<h2 class="pdoc-module-header" id="WorkDocsPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L290">const WorkDocsPrincipal</a>
</h2>

Service Principal for WorkDocs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L290">let Service</a>
</h3>

```typescript
let Service: string = "workdocs.amazonaws.com";
```

<h2 class="pdoc-module-header" id="WorkspacesPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L295">const WorkspacesPrincipal</a>
</h2>

Service Principal for Workspaces

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/principals.ts#L295">let Service</a>
</h3>

```typescript
let Service: string = "workspaces.amazonaws.com";
```

<h2 class="pdoc-module-header" id="assumeRolePolicyForPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L178">function assumeRolePolicyForPrincipal</a>
</h2>

```typescript
assumeRolePolicyForPrincipal(principal: Principal): PolicyDocument
```


assumeRolePolicyForPrincipal returns a well-formed policy document which can be
used to control which principals may assume an IAM Role, by granting the `sts:AssumeRole`
action to those principals.

<h2 class="pdoc-module-header" id="getAccountAlias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getAccountAlias.ts#L11">function getAccountAlias</a>
</h2>

```typescript
getAccountAlias(opts?: pulumi.InvokeOptions): Promise<GetAccountAliasResult>
```


The IAM Account Alias data source allows access to the account alias
for the effective account in which Terraform is working.

<h2 class="pdoc-module-header" id="getGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L12">function getGroup</a>
</h2>

```typescript
getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult>
```


This data source can be used to fetch information about a specific
IAM group. By using this data source, you can reference IAM group
properties without having to hard code ARNs as input.

<h2 class="pdoc-module-header" id="getInstanceProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L12">function getInstanceProfile</a>
</h2>

```typescript
getInstanceProfile(args: GetInstanceProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceProfileResult>
```


This data source can be used to fetch information about a specific
IAM instance profile. By using this data source, you can reference IAM
instance profile properties without having to hard code ARNs as input.

<h2 class="pdoc-module-header" id="getPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L11">function getPolicy</a>
</h2>

```typescript
getPolicy(args: GetPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetPolicyResult>
```


This data source can be used to fetch information about a specific
IAM policy.

<h2 class="pdoc-module-header" id="getPolicyDocument">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L75">function getPolicyDocument</a>
</h2>

```typescript
getPolicyDocument(args?: GetPolicyDocumentArgs, opts?: pulumi.InvokeOptions): Promise<GetPolicyDocumentResult>
```


Generates an IAM policy document in JSON format.

This is a data source which can be used to construct a JSON representation of
an IAM policy document, for use with resources which expect policy documents,
such as the `aws_iam_policy` resource.

-> For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

```hcl
data "aws_iam_policy_document" "example" {
  statement {
    sid = "1"

    actions = [
      "s3:ListAllMyBuckets",
      "s3:GetBucketLocation",
    ]

    resources = [
      "arn:aws:s3:::*",
    ]
  }

  statement {
    actions = [
      "s3:ListBucket",
    ]

    resources = [
      "arn:aws:s3:::${var.s3_bucket_name}",
    ]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"

      values = [
        "",
        "home/",
        "home/&{aws:username}/",
      ]
    }
  }

  statement {
    actions = [
      "s3:*",
    ]

    resources = [
      "arn:aws:s3:::${var.s3_bucket_name}/home/&{aws:username}",
      "arn:aws:s3:::${var.s3_bucket_name}/home/&{aws:username}/*",
    ]
  }
}

resource "aws_iam_policy" "example" {
  name   = "example_policy"
  path   = "/"
  policy = "${data.aws_iam_policy_document.example.json}"
}
```

Using this data source to generate policy documents is *optional*. It is also
valid to use literal JSON strings within your configuration, or to use the
`file` interpolation function to read a raw JSON policy document from a file.

<h2 class="pdoc-module-header" id="getRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L12">function getRole</a>
</h2>

```typescript
getRole(args?: GetRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleResult>
```


This data source can be used to fetch information about a specific
IAM role. By using this data source, you can reference IAM role
properties without having to hard code ARNs as input.

<h2 class="pdoc-module-header" id="getServerCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L10">function getServerCertificate</a>
</h2>

```typescript
getServerCertificate(args?: GetServerCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetServerCertificateResult>
```


Use this data source to lookup information about IAM Server Certificates.

<h2 class="pdoc-module-header" id="getUser">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L12">function getUser</a>
</h2>

```typescript
getUser(args: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult>
```


This data source can be used to fetch information about a specific
IAM user. By using this data source, you can reference IAM user
properties without having to hard code ARNs or unique IDs as input.

<h2 class="pdoc-module-header" id="AWSPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L149">interface AWSPrincipal</a>
</h2>

When you use an AWS account identifier as the principal in a policy, the permissions in the policy statement can be
granted to all identities contained in that account. This includes IAM users and roles in that account. When you
specify an AWS account, you can use the account ARN (arn:aws:iam::AWS-account-ID:root), or a shortened form that
consists of the AWS: prefix followed by the account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L150">property AWS</a>
</h3>

```typescript
AWS: string | string[];
```

<h2 class="pdoc-module-header" id="AccessKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L143">interface AccessKeyArgs</a>
</h2>

The set of arguments for constructing a AccessKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L148">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:some_person_that_exists`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L152">property user</a>
</h3>

```typescript
user: pulumi.Input<string>;
```


The IAM user to associate with this access key.

<h2 class="pdoc-module-header" id="AccessKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L100">interface AccessKeyState</a>
</h2>

Input properties used for looking up and filtering AccessKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L106">property encryptedSecret</a>
</h3>

```typescript
encryptedSecret?: pulumi.Input<string>;
```


The encrypted secret, base64 encoded.
~> **NOTE:** The encrypted secret may be decrypted using the command line,
for example: `terraform output encrypted_secret | base64 --decode | keybase pgp decrypt`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L111">property keyFingerprint</a>
</h3>

```typescript
keyFingerprint?: pulumi.Input<string>;
```


The fingerprint of the PGP key used to encrypt
the secret

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L116">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:some_person_that_exists`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L122">property secret</a>
</h3>

```typescript
secret?: pulumi.Input<string>;
```


The secret access key. Note that this will be written
to the state file. Please supply a `pgp_key` instead, which will prevent the
secret from being stored in plain text

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L128">property sesSmtpPassword</a>
</h3>

```typescript
sesSmtpPassword?: pulumi.Input<string>;
```


The secret access key converted into an SES SMTP
password by applying [AWS's documented conversion
algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L133">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


"Active" or "Inactive". Keys are initially active, but can be made
inactive by other means.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accessKey.ts#L137">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


The IAM user to associate with this access key.

<h2 class="pdoc-module-header" id="AccountAliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L67">interface AccountAliasArgs</a>
</h2>

The set of arguments for constructing a AccountAlias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L71">property accountAlias</a>
</h3>

```typescript
accountAlias: pulumi.Input<string>;
```


The account alias

<h2 class="pdoc-module-header" id="AccountAliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L57">interface AccountAliasState</a>
</h2>

Input properties used for looking up and filtering AccountAlias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountAlias.ts#L61">property accountAlias</a>
</h3>

```typescript
accountAlias?: pulumi.Input<string>;
```


The account alias

<h2 class="pdoc-module-header" id="AccountPasswordPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L162">interface AccountPasswordPolicyArgs</a>
</h2>

The set of arguments for constructing a AccountPasswordPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L166">property allowUsersToChangePassword</a>
</h3>

```typescript
allowUsersToChangePassword?: pulumi.Input<boolean>;
```


Whether to allow users to change their own password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L171">property hardExpiry</a>
</h3>

```typescript
hardExpiry?: pulumi.Input<boolean>;
```


Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L175">property maxPasswordAge</a>
</h3>

```typescript
maxPasswordAge?: pulumi.Input<number>;
```


The number of days that an user password is valid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L179">property minimumPasswordLength</a>
</h3>

```typescript
minimumPasswordLength?: pulumi.Input<number>;
```


Minimum length to require for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L183">property passwordReusePrevention</a>
</h3>

```typescript
passwordReusePrevention?: pulumi.Input<number>;
```


The number of previous passwords that users are prevented from reusing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L187">property requireLowercaseCharacters</a>
</h3>

```typescript
requireLowercaseCharacters?: pulumi.Input<boolean>;
```


Whether to require lowercase characters for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L191">property requireNumbers</a>
</h3>

```typescript
requireNumbers?: pulumi.Input<boolean>;
```


Whether to require numbers for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L195">property requireSymbols</a>
</h3>

```typescript
requireSymbols?: pulumi.Input<boolean>;
```


Whether to require symbols for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L199">property requireUppercaseCharacters</a>
</h3>

```typescript
requireUppercaseCharacters?: pulumi.Input<boolean>;
```


Whether to require uppercase characters for user passwords.

<h2 class="pdoc-module-header" id="AccountPasswordPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L113">interface AccountPasswordPolicyState</a>
</h2>

Input properties used for looking up and filtering AccountPasswordPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L117">property allowUsersToChangePassword</a>
</h3>

```typescript
allowUsersToChangePassword?: pulumi.Input<boolean>;
```


Whether to allow users to change their own password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L123">property expirePasswords</a>
</h3>

```typescript
expirePasswords?: pulumi.Input<boolean>;
```


Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L128">property hardExpiry</a>
</h3>

```typescript
hardExpiry?: pulumi.Input<boolean>;
```


Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L132">property maxPasswordAge</a>
</h3>

```typescript
maxPasswordAge?: pulumi.Input<number>;
```


The number of days that an user password is valid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L136">property minimumPasswordLength</a>
</h3>

```typescript
minimumPasswordLength?: pulumi.Input<number>;
```


Minimum length to require for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L140">property passwordReusePrevention</a>
</h3>

```typescript
passwordReusePrevention?: pulumi.Input<number>;
```


The number of previous passwords that users are prevented from reusing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L144">property requireLowercaseCharacters</a>
</h3>

```typescript
requireLowercaseCharacters?: pulumi.Input<boolean>;
```


Whether to require lowercase characters for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L148">property requireNumbers</a>
</h3>

```typescript
requireNumbers?: pulumi.Input<boolean>;
```


Whether to require numbers for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L152">property requireSymbols</a>
</h3>

```typescript
requireSymbols?: pulumi.Input<boolean>;
```


Whether to require symbols for user passwords.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/accountPasswordPolicy.ts#L156">property requireUppercaseCharacters</a>
</h3>

```typescript
requireUppercaseCharacters?: pulumi.Input<boolean>;
```


Whether to require uppercase characters for user passwords.

<h2 class="pdoc-module-header" id="ConditionArguments">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L111">interface ConditionArguments</a>
</h2>
<h2 class="pdoc-module-header" id="Conditions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L92">interface Conditions</a>
</h2>

The Condition element (or Condition block) lets you specify conditions for when a policy is in effect. The Condition
element is optional. In the Condition element, you build expressions in which you use condition operators (equal,
less than, etc.) to match the condition in the policy against values in the request. Condition values can include
date, time, the IP address of the requester, the ARN of the request source, the user name, user ID, and the user
agent of the requester. Some services let you specify additional values in conditions; for example, Amazon S3
lets you write a condition using the s3:VersionId key, which is unique to that service.

<h2 class="pdoc-module-header" id="FederatedPrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L166">interface FederatedPrincipal</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L167">property Federated</a>
</h3>

```typescript
Federated: string | string[];
```

<h2 class="pdoc-module-header" id="GetAccountAliasResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getAccountAlias.ts#L19">interface GetAccountAliasResult</a>
</h2>

A collection of values returned by getAccountAlias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getAccountAlias.ts#L23">property accountAlias</a>
</h3>

```typescript
accountAlias: string;
```


The alias associated with the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getAccountAlias.ts#L27">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L21">interface GetGroupArgs</a>
</h2>

A collection of arguments for invoking getGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L25">property groupName</a>
</h3>

```typescript
groupName: string;
```


The friendly IAM group name to match.

<h2 class="pdoc-module-header" id="GetGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L31">interface GetGroupResult</a>
</h2>

A collection of values returned by getGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) specifying the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L39">property groupId</a>
</h3>

```typescript
groupId: string;
```


The stable and unique string identifying the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getGroup.ts#L43">property path</a>
</h3>

```typescript
path: string;
```


The path to the group.

<h2 class="pdoc-module-header" id="GetInstanceProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L21">interface GetInstanceProfileArgs</a>
</h2>

A collection of arguments for invoking getInstanceProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The friendly IAM instance profile name to match.

<h2 class="pdoc-module-header" id="GetInstanceProfileResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L31">interface GetInstanceProfileResult</a>
</h2>

A collection of values returned by getInstanceProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) specifying the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L40">property createDate</a>
</h3>

```typescript
createDate: string;
```


The string representation of the date the instance profile
was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L60">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L44">property path</a>
</h3>

```typescript
path: string;
```


The path to the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L48">property roleArn</a>
</h3>

```typescript
roleArn: string;
```


The role arn associated with this instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L52">property roleId</a>
</h3>

```typescript
roleId: string;
```


The role id associated with this instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getInstanceProfile.ts#L56">property roleName</a>
</h3>

```typescript
roleName: string;
```


The role name associated with this instance profile.

<h2 class="pdoc-module-header" id="GetPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L20">interface GetPolicyArgs</a>
</h2>

A collection of arguments for invoking getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L24">property arn</a>
</h3>

```typescript
arn: string;
```


ARN of the IAM policy.

<h2 class="pdoc-module-header" id="GetPolicyDocumentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L88">interface GetPolicyDocumentArgs</a>
</h2>

A collection of arguments for invoking getPolicyDocument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L95">property overrideJson</a>
</h3>

```typescript
overrideJson?: string;
```


An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L99">property policyId</a>
</h3>

```typescript
policyId?: string;
```


An ID for the policy document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L106">property sourceJson</a>
</h3>

```typescript
sourceJson?: string;
```


An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L111">property statements</a>
</h3>

```typescript
statements?: { ... }[];
```


A nested configuration block (described below)
configuring one *statement* to be included in the policy document.

<h2 class="pdoc-module-header" id="GetPolicyDocumentResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L117">interface GetPolicyDocumentResult</a>
</h2>

A collection of values returned by getPolicyDocument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L125">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicyDocument.ts#L121">property json</a>
</h3>

```typescript
json: string;
```


The above arguments serialized as a standard JSON policy document.

<h2 class="pdoc-module-header" id="GetPolicyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L30">interface GetPolicyResult</a>
</h2>

A collection of values returned by getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L34">property description</a>
</h3>

```typescript
description: string;
```


The description of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L38">property name</a>
</h3>

```typescript
name: string;
```


The name of the IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L42">property path</a>
</h3>

```typescript
path: string;
```


The path to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getPolicy.ts#L46">property policy</a>
</h3>

```typescript
policy: string;
```


The policy document of the policy.

<h2 class="pdoc-module-header" id="GetRoleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L23">interface GetRoleArgs</a>
</h2>

A collection of arguments for invoking getRole.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L27">property name</a>
</h3>

```typescript
name?: string;
```


The friendly IAM role name to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L28">property roleName</a>
</h3>

```typescript
roleName?: string;
```

<h2 class="pdoc-module-header" id="GetRoleResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L34">interface GetRoleResult</a>
</h2>

A collection of values returned by getRole.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L38">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) specifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L42">property assumeRolePolicy</a>
</h3>

```typescript
assumeRolePolicy: string;
```


The policy document associated with the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L43">property assumeRolePolicyDocument</a>
</h3>

```typescript
assumeRolePolicyDocument: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L44">property createDate</a>
</h3>

```typescript
createDate: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L45">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L63">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L46">property maxSessionDuration</a>
</h3>

```typescript
maxSessionDuration: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L50">property path</a>
</h3>

```typescript
path: string;
```


The path to the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L54">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary: string;
```


The ARN of the policy that is used to set the permissions boundary for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L55">property roleId</a>
</h3>

```typescript
roleId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getRole.ts#L59">property uniqueId</a>
</h3>

```typescript
uniqueId: string;
```


The stable and unique string identifying the role.

<h2 class="pdoc-module-header" id="GetServerCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L23">interface GetServerCertificateArgs</a>
</h2>

A collection of arguments for invoking getServerCertificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L27">property latest</a>
</h3>

```typescript
latest?: boolean;
```


sort results by expiration date. returns the certificate with expiration date in furthest in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L31">property name</a>
</h3>

```typescript
name?: string;
```


exact name of the cert to lookup

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L35">property namePrefix</a>
</h3>

```typescript
namePrefix?: string;
```


prefix of cert to filter by

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L39">property pathPrefix</a>
</h3>

```typescript
pathPrefix?: string;
```


prefix of path to filter by

<h2 class="pdoc-module-header" id="GetServerCertificateResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L45">interface GetServerCertificateResult</a>
</h2>

A collection of values returned by getServerCertificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L46">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L47">property certificateBody</a>
</h3>

```typescript
certificateBody: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L48">property certificateChain</a>
</h3>

```typescript
certificateChain: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L49">property expirationDate</a>
</h3>

```typescript
expirationDate: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L56">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L50">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L51">property path</a>
</h3>

```typescript
path: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getServerCertificate.ts#L52">property uploadDate</a>
</h3>

```typescript
uploadDate: string;
```

<h2 class="pdoc-module-header" id="GetUserArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L21">interface GetUserArgs</a>
</h2>

A collection of arguments for invoking getUser.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L25">property userName</a>
</h3>

```typescript
userName: string;
```


The friendly IAM user name to match.

<h2 class="pdoc-module-header" id="GetUserResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L31">interface GetUserResult</a>
</h2>

A collection of values returned by getUser.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) assigned by AWS for this user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L39">property path</a>
</h3>

```typescript
path: string;
```


Path in which this user was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L43">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary: string;
```


The ARN of the policy that is used to set the permissions boundary for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/getUser.ts#L47">property userId</a>
</h3>

```typescript
userId: string;
```


The unique ID assigned by AWS for this user.

<h2 class="pdoc-module-header" id="GroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L92">interface GroupArgs</a>
</h2>

The set of arguments for constructing a Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L100">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the group.

<h2 class="pdoc-module-header" id="GroupMembershipArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L95">interface GroupMembershipArgs</a>
</h2>

The set of arguments for constructing a GroupMembership resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L99">property group</a>
</h3>

```typescript
group: pulumi.Input<string>;
```


The IAM Group name to attach the list of `users` to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to identify the Group Membership

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L107">property users</a>
</h3>

```typescript
users: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IAM User names to associate with the Group

<h2 class="pdoc-module-header" id="GroupMembershipState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L77">interface GroupMembershipState</a>
</h2>

Input properties used for looking up and filtering GroupMembership resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L81">property group</a>
</h3>

```typescript
group?: pulumi.Input<string>;
```


The IAM Group name to attach the list of `users` to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to identify the Group Membership

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupMembership.ts#L89">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IAM User names to associate with the Group

<h2 class="pdoc-module-header" id="GroupPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L104">interface GroupPolicyArgs</a>
</h2>

The set of arguments for constructing a GroupPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L108">property group</a>
</h3>

```typescript
group: pulumi.Input<string>;
```


The IAM group to attach to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L118">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L122">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h2 class="pdoc-module-header" id="GroupPolicyAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L83">interface GroupPolicyAttachmentArgs</a>
</h2>

The set of arguments for constructing a GroupPolicyAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L87">property group</a>
</h3>

```typescript
group: pulumi.Input<Group>;
```


The group the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L91">property policyArn</a>
</h3>

```typescript
policyArn: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h2 class="pdoc-module-header" id="GroupPolicyAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L69">interface GroupPolicyAttachmentState</a>
</h2>

Input properties used for looking up and filtering GroupPolicyAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L73">property group</a>
</h3>

```typescript
group?: pulumi.Input<Group>;
```


The group the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicyAttachment.ts#L77">property policyArn</a>
</h3>

```typescript
policyArn?: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h2 class="pdoc-module-header" id="GroupPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L80">interface GroupPolicyState</a>
</h2>

Input properties used for looking up and filtering GroupPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L84">property group</a>
</h3>

```typescript
group?: pulumi.Input<string>;
```


The IAM group to attach to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L94">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/groupPolicy.ts#L98">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h2 class="pdoc-module-header" id="GroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L70">interface GroupState</a>
</h2>

Input properties used for looking up and filtering Group resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L74">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS for this group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L78">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L82">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/group.ts#L86">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The [unique ID][1] assigned by AWS.

<h2 class="pdoc-module-header" id="InstanceProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L140">interface InstanceProfileArgs</a>
</h2>

The set of arguments for constructing a InstanceProfile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The profile's name. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L148">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L152">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L156">property role</a>
</h3>

```typescript
role?: pulumi.Input<Role>;
```


The role name to include in the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L162">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<pulumi.Input<Role>[]>;
```


A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
WARNING: This is deprecated since [version 0.9.3 (April 12, 2017)](https://github.com/hashicorp/terraform/blob/master/CHANGELOG.md#093-april-12-2017), as >= 2 roles are not possible. See [issue #11575](https://github.com/hashicorp/terraform/issues/11575).

<h2 class="pdoc-module-header" id="InstanceProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L100">interface InstanceProfileState</a>
</h2>

Input properties used for looking up and filtering InstanceProfile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L104">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L108">property createDate</a>
</h3>

```typescript
createDate?: pulumi.Input<string>;
```


The creation timestamp of the instance profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The profile's name. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L116">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L120">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L124">property role</a>
</h3>

```typescript
role?: pulumi.Input<Role>;
```


The role name to include in the profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L130">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<pulumi.Input<Role>[]>;
```


A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
WARNING: This is deprecated since [version 0.9.3 (April 12, 2017)](https://github.com/hashicorp/terraform/blob/master/CHANGELOG.md#093-april-12-2017), as >= 2 roles are not possible. See [issue #11575](https://github.com/hashicorp/terraform/issues/11575).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/instanceProfile.ts#L134">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The [unique ID][1] assigned by AWS.

<h2 class="pdoc-module-header" id="OpenIdConnectProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L101">interface OpenIdConnectProviderArgs</a>
</h2>

The set of arguments for constructing a OpenIdConnectProvider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L105">property clientIdLists</a>
</h3>

```typescript
clientIdLists: pulumi.Input<pulumi.Input<string>[]>;
```


A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L109">property thumbprintLists</a>
</h3>

```typescript
thumbprintLists: pulumi.Input<pulumi.Input<string>[]>;
```


A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L113">property url</a>
</h3>

```typescript
url: pulumi.Input<string>;
```


The URL of the identity provider. Corresponds to the _iss_ claim.

<h2 class="pdoc-module-header" id="OpenIdConnectProviderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L79">interface OpenIdConnectProviderState</a>
</h2>

Input properties used for looking up and filtering OpenIdConnectProvider resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L83">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS for this provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L87">property clientIdLists</a>
</h3>

```typescript
clientIdLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L91">property thumbprintLists</a>
</h3>

```typescript
thumbprintLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/openIdConnectProvider.ts#L95">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL of the identity provider. Corresponds to the _iss_ claim.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L117">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L129">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L134">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the policy.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L138">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h2 class="pdoc-module-header" id="PolicyAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L114">interface PolicyAttachmentArgs</a>
</h2>

The set of arguments for constructing a PolicyAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L118">property groups</a>
</h3>

```typescript
groups?: pulumi.Input<pulumi.Input<Group>[]>;
```


The group(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attachment. This cannot be an empty string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L126">property policyArn</a>
</h3>

```typescript
policyArn: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L130">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<pulumi.Input<Role>[]>;
```


The role(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L134">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<User>[]>;
```


The user(s) the policy should be applied to

<h2 class="pdoc-module-header" id="PolicyAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L88">interface PolicyAttachmentState</a>
</h2>

Input properties used for looking up and filtering PolicyAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L92">property groups</a>
</h3>

```typescript
groups?: pulumi.Input<pulumi.Input<Group>[]>;
```


The group(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attachment. This cannot be an empty string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L100">property policyArn</a>
</h3>

```typescript
policyArn?: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L104">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<pulumi.Input<Role>[]>;
```


The role(s) the policy should be applied to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policyAttachment.ts#L108">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<User>[]>;
```


The user(s) the policy should be applied to

<h2 class="pdoc-module-header" id="PolicyDocument">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L45">interface PolicyDocument</a>
</h2>

You manage access in AWS by creating policies and attaching them to IAM identities or AWS resources. A policy is an
object in AWS that, when associated with an entity or resource, defines their permissions. AWS evaluates these
policies when a principal, such as a user, makes a request. Permissions in the policies determine whether the
request is allowed or denied.

IAM policies define permissions for an action regardless of the method that you use to perform the operation. For
example, if a policy allows the `GetUser` action, then a user with that policy can get user information from the
AWS Management Console, the AWS CLI, or the AWS API. When you create an IAM user, you can set up the user to
allow console or programmatic access. The IAM user can sign in to the console using a user name and password.
Or they can use access keys to work with the CLI or API.

Most policies are stored in AWS as JSON documents. Identity-based policies, policies used to set boundaries, or AWS
STS boundary policies are JSON policy documents that you attach to a user or role. Resource-based policies are JSON
policy documents that you attach to a resource. SCPs are JSON policy documents with restricted syntax that you
attach to an AWS Organizations organizational unit (OU). ACLs are also attached to a resource, but you must use a
different syntax.

A JSON policy document includes these elements:

    - Optional policywide information at the top of the document
    - One or more individual statements

Each statement includes information about a single permission. If a policy includes multiple statements, AWS applies
a logical OR across the statements when evaluating them. If multiple policies apply to a request, AWS applies a
logical OR across all of those policies when evaluating them.

For more details about IAM policies, please refer to the AWS documentation online:
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L49">property Id</a>
</h3>

```typescript
Id?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L51">property Statement</a>
</h3>

```typescript
Statement: PolicyStatement[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L47">property Version</a>
</h3>

```typescript
Version: 2008-10-17 | 2012-10-17;
```

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L86">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L90">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L102">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L107">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the policy.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/policy.ts#L111">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h2 class="pdoc-module-header" id="PolicyStatement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L58">interface PolicyStatement</a>
</h2>

The Statement element is the main element for a policy. This element is required. It can include multiple elements
(see the subsequent sections in this page). The Statement element contains an array of individual statements.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L71">property Action</a>
</h3>

```typescript
Action?: string | string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L81">property Condition</a>
</h3>

```typescript
Condition?: Conditions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L62">property Effect</a>
</h3>

```typescript
Effect: Allow | Deny;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L73">property NotAction</a>
</h3>

```typescript
NotAction?: string | string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L68">property NotPrincipal</a>
</h3>

```typescript
NotPrincipal?: Principal;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L78">property NotResource</a>
</h3>

```typescript
NotResource?: string | string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L66">property Principal</a>
</h3>

```typescript
Principal?: Principal;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L76">property Resource</a>
</h3>

```typescript
Resource?: string | string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L60">property Sid</a>
</h3>

```typescript
Sid?: string;
```

<h2 class="pdoc-module-header" id="RoleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L179">interface RoleArgs</a>
</h2>

The set of arguments for constructing a Role resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L183">property assumeRolePolicy</a>
</h3>

```typescript
assumeRolePolicy: pulumi.Input<string | PolicyDocument>;
```


The policy that grants an entity permission to assume the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L187">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L191">property forceDetachPolicies</a>
</h3>

```typescript
forceDetachPolicies?: pulumi.Input<boolean>;
```


Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L195">property maxSessionDuration</a>
</h3>

```typescript
maxSessionDuration?: pulumi.Input<number>;
```


The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L203">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L208">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The path to the role.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L212">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary?: pulumi.Input<string>;
```


The ARN of the policy that is used to set the permissions boundary for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Key-value mapping of tags for the IAM role

<h2 class="pdoc-module-header" id="RolePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L105">interface RolePolicyArgs</a>
</h2>

The set of arguments for constructing a RolePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L115">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L119">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L123">property role</a>
</h3>

```typescript
role: pulumi.Input<string | Role>;
```


The IAM role to attach to the policy.

<h2 class="pdoc-module-header" id="RolePolicyAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L83">interface RolePolicyAttachmentArgs</a>
</h2>

The set of arguments for constructing a RolePolicyAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L87">property policyArn</a>
</h3>

```typescript
policyArn: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L91">property role</a>
</h3>

```typescript
role: pulumi.Input<Role>;
```


The role the policy should be applied to

<h2 class="pdoc-module-header" id="RolePolicyAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L69">interface RolePolicyAttachmentState</a>
</h2>

Input properties used for looking up and filtering RolePolicyAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L73">property policyArn</a>
</h3>

```typescript
policyArn?: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicyAttachment.ts#L77">property role</a>
</h3>

```typescript
role?: pulumi.Input<Role>;
```


The role the policy should be applied to

<h2 class="pdoc-module-header" id="RolePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L81">interface RolePolicyState</a>
</h2>

Input properties used for looking up and filtering RolePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role policy. If omitted, Terraform will
assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L91">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L95">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/rolePolicy.ts#L99">property role</a>
</h3>

```typescript
role?: pulumi.Input<string | Role>;
```


The IAM role to attach to the policy.

<h2 class="pdoc-module-header" id="RoleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L124">interface RoleState</a>
</h2>

Input properties used for looking up and filtering Role resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L128">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L132">property assumeRolePolicy</a>
</h3>

```typescript
assumeRolePolicy?: pulumi.Input<string | PolicyDocument>;
```


The policy that grants an entity permission to assume the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L136">property createDate</a>
</h3>

```typescript
createDate?: pulumi.Input<string>;
```


The creation date of the IAM role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L140">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L144">property forceDetachPolicies</a>
</h3>

```typescript
forceDetachPolicies?: pulumi.Input<boolean>;
```


Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L148">property maxSessionDuration</a>
</h3>

```typescript
maxSessionDuration?: pulumi.Input<number>;
```


The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L156">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L161">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The path to the role.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L165">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary?: pulumi.Input<string>;
```


The ARN of the policy that is used to set the permissions boundary for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L169">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Key-value mapping of tags for the IAM role

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/role.ts#L173">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The stable and unique string identifying the role.

<h2 class="pdoc-module-header" id="SamlProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L95">interface SamlProviderArgs</a>
</h2>

The set of arguments for constructing a SamlProvider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the provider to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L103">property samlMetadataDocument</a>
</h3>

```typescript
samlMetadataDocument: pulumi.Input<string>;
```


An XML document generated by an identity provider that supports SAML 2.0.

<h2 class="pdoc-module-header" id="SamlProviderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L73">interface SamlProviderState</a>
</h2>

Input properties used for looking up and filtering SamlProvider resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS for this provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the provider to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L85">property samlMetadataDocument</a>
</h3>

```typescript
samlMetadataDocument?: pulumi.Input<string>;
```


An XML document generated by an identity provider that supports SAML 2.0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/samlProvider.ts#L89">property validUntil</a>
</h3>

```typescript
validUntil?: pulumi.Input<string>;
```


The expiration date and time for the SAML provider in RFC1123 format, e.g. `Mon, 02 Jan 2006 15:04:05 MST`.

<h2 class="pdoc-module-header" id="ServerCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L156">interface ServerCertificateArgs</a>
</h2>

The set of arguments for constructing a ServerCertificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L160">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the server certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L165">property certificateBody</a>
</h3>

```typescript
certificateBody: pulumi.Input<string>;
```


The contents of the public key certificate in
PEM-encoded format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L171">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Server Certificate. Do not include the
path in this value. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L181">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L188">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
See [IAM Identifiers][1] for more details on IAM Paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L192">property privateKey</a>
</h3>

```typescript
privateKey: pulumi.Input<string>;
```


The contents of the private key in PEM-encoded format.

<h2 class="pdoc-module-header" id="ServerCertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L114">interface ServerCertificateState</a>
</h2>

Input properties used for looking up and filtering ServerCertificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L118">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the server certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L123">property certificateBody</a>
</h3>

```typescript
certificateBody?: pulumi.Input<string>;
```


The contents of the public key certificate in
PEM-encoded format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L129">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Server Certificate. Do not include the
path in this value. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L139">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L146">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
See [IAM Identifiers][1] for more details on IAM Paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serverCertificate.ts#L150">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```


The contents of the private key in PEM-encoded format.

<h2 class="pdoc-module-header" id="ServiceLinkedRoleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L135">interface ServiceLinkedRoleArgs</a>
</h2>

The set of arguments for constructing a ServiceLinkedRole resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L139">property awsServiceName</a>
</h3>

```typescript
awsServiceName: pulumi.Input<string>;
```


The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L143">property customSuffix</a>
</h3>

```typescript
customSuffix?: pulumi.Input<string>;
```


Additional string appended to the role name. Not all AWS services support custom suffixes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L147">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the role.

<h2 class="pdoc-module-header" id="ServiceLinkedRoleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L97">interface ServiceLinkedRoleState</a>
</h2>

Input properties used for looking up and filtering ServiceLinkedRole resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L101">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L105">property awsServiceName</a>
</h3>

```typescript
awsServiceName?: pulumi.Input<string>;
```


The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L109">property createDate</a>
</h3>

```typescript
createDate?: pulumi.Input<string>;
```


The creation date of the IAM role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L113">property customSuffix</a>
</h3>

```typescript
customSuffix?: pulumi.Input<string>;
```


Additional string appended to the role name. Not all AWS services support custom suffixes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L125">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The path of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/serviceLinkedRole.ts#L129">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The stable and unique string identifying the role.

<h2 class="pdoc-module-header" id="ServicePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L162">interface ServicePrincipal</a>
</h2>

IAM roles that can be assumed by an AWS service are called service roles. Service roles must include a trust policy.
Trust policies are resource-based policies that are attached to a role that define which principals can assume the
role. Some service role have predefined trust policies. However, in some cases, you must specify the service
principal in the trust policy. A service principal is an identifier that is used to grant permissions to a service.
The identifier includes the long version of a service name, e.g. `long_service_name.amazonaws.com`. The service
principal is defined by the service. To learn the service principal for a service, see the documentation for that
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L163">property Service</a>
</h3>

```typescript
Service: string | string[];
```

<h2 class="pdoc-module-header" id="SshKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L121">interface SshKeyArgs</a>
</h2>

The set of arguments for constructing a SshKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L125">property encoding</a>
</h3>

```typescript
encoding: pulumi.Input<string>;
```


Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L129">property publicKey</a>
</h3>

```typescript
publicKey: pulumi.Input<string>;
```


The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L133">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L137">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


The name of the IAM user to associate the SSH public key with.

<h2 class="pdoc-module-header" id="SshKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L91">interface SshKeyState</a>
</h2>

Input properties used for looking up and filtering SshKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L95">property encoding</a>
</h3>

```typescript
encoding?: pulumi.Input<string>;
```


Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L99">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The MD5 message digest of the SSH public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L103">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L107">property sshPublicKeyId</a>
</h3>

```typescript
sshPublicKeyId?: pulumi.Input<string>;
```


The unique identifier for the SSH public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L111">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/sshKey.ts#L115">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The name of the IAM user to associate the SSH public key with.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L126">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L132">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


When destroying this user, destroy even if it
has non-Terraform-managed IAM access keys, login profile or MFA devices. Without `force_destroy`
a user with non-Terraform-managed access keys and login profile will fail to be destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L140">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L144">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary?: pulumi.Input<string>;
```


The ARN of the policy that is used to set the permissions boundary for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L148">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Key-value mapping of tags for the IAM user

<h2 class="pdoc-module-header" id="UserGroupMembershipArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L83">interface UserGroupMembershipArgs</a>
</h2>

The set of arguments for constructing a UserGroupMembership resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L87">property groups</a>
</h3>

```typescript
groups: pulumi.Input<pulumi.Input<string>[]>;
```


A list of [IAM Groups][1] to add the user to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L91">property user</a>
</h3>

```typescript
user: pulumi.Input<string>;
```


The name of the [IAM User][2] to add to groups

<h2 class="pdoc-module-header" id="UserGroupMembershipState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L69">interface UserGroupMembershipState</a>
</h2>

Input properties used for looking up and filtering UserGroupMembership resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L73">property groups</a>
</h3>

```typescript
groups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of [IAM Groups][1] to add the user to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userGroupMembership.ts#L77">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


The name of the [IAM User][2] to add to groups

<h2 class="pdoc-module-header" id="UserLoginProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L128">interface UserLoginProfileArgs</a>
</h2>

The set of arguments for constructing a UserLoginProfile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L133">property passwordLength</a>
</h3>

```typescript
passwordLength?: pulumi.Input<number>;
```


The length of the generated
password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L138">property passwordResetRequired</a>
</h3>

```typescript
passwordResetRequired?: pulumi.Input<boolean>;
```


Whether the
user should be forced to reset the generated password on first login.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L143">property pgpKey</a>
</h3>

```typescript
pgpKey: pulumi.Input<string>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:username`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L147">property user</a>
</h3>

```typescript
user: pulumi.Input<string>;
```


The IAM user's name.

<h2 class="pdoc-module-header" id="UserLoginProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L94">interface UserLoginProfileState</a>
</h2>

Input properties used for looking up and filtering UserLoginProfile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L98">property encryptedPassword</a>
</h3>

```typescript
encryptedPassword?: pulumi.Input<string>;
```


The encrypted password, base64 encoded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L103">property keyFingerprint</a>
</h3>

```typescript
keyFingerprint?: pulumi.Input<string>;
```


The fingerprint of the PGP key used to encrypt
the password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L108">property passwordLength</a>
</h3>

```typescript
passwordLength?: pulumi.Input<number>;
```


The length of the generated
password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L113">property passwordResetRequired</a>
</h3>

```typescript
passwordResetRequired?: pulumi.Input<boolean>;
```


Whether the
user should be forced to reset the generated password on first login.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L118">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:username`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userLoginProfile.ts#L122">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


The IAM user's name.

<h2 class="pdoc-module-header" id="UserPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L100">interface UserPolicyArgs</a>
</h2>

The set of arguments for constructing a UserPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L108">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L112">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L116">property user</a>
</h3>

```typescript
user: pulumi.Input<string>;
```


IAM user to which to attach this policy.

<h2 class="pdoc-module-header" id="UserPolicyAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L83">interface UserPolicyAttachmentArgs</a>
</h2>

The set of arguments for constructing a UserPolicyAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L87">property policyArn</a>
</h3>

```typescript
policyArn: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L91">property user</a>
</h3>

```typescript
user: pulumi.Input<User>;
```


The user the policy should be applied to

<h2 class="pdoc-module-header" id="UserPolicyAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L69">interface UserPolicyAttachmentState</a>
</h2>

Input properties used for looking up and filtering UserPolicyAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L73">property policyArn</a>
</h3>

```typescript
policyArn?: pulumi.Input<ARN>;
```


The ARN of the policy you want to apply

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicyAttachment.ts#L77">property user</a>
</h3>

```typescript
user?: pulumi.Input<User>;
```


The user the policy should be applied to

<h2 class="pdoc-module-header" id="UserPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L78">interface UserPolicyState</a>
</h2>

Input properties used for looking up and filtering UserPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L86">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L90">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string | PolicyDocument>;
```


The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/userPolicy.ts#L94">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


IAM user to which to attach this policy.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L90">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L94">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS for this user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L100">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


When destroying this user, destroy even if it
has non-Terraform-managed IAM access keys, login profile or MFA devices. Without `force_destroy`
a user with non-Terraform-managed access keys and login profile will fail to be destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L108">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path in which to create the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L112">property permissionsBoundary</a>
</h3>

```typescript
permissionsBoundary?: pulumi.Input<string>;
```


The ARN of the policy that is used to set the permissions boundary for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L116">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Key-value mapping of tags for the IAM user

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/user.ts#L120">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The [unique ID][1] assigned by AWS.

<h2 class="pdoc-module-header" id="Principal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iam/documents.ts#L141">type Principal</a>
</h2>

```typescript
type Principal = * | AWSPrincipal | ServicePrincipal | FederatedPrincipal;
```


Use the Principal element to specify the user (IAM user, federated user, or assumed-role user), AWS account, AWS
service, or other principal entity that is allowed or denied access to a resource. You use the Principal element in
the trust policies for IAM roles and in resource-based policies—that is, in policies that you embed directly in a
resource. For example, you can embed such policies in an Amazon S3 bucket, an Amazon Glacier vault, an Amazon SNS
topic, an Amazon SQS queue, or an AWS KMS customer master key (CMK).

Use the Principal element in these ways:

    - In IAM roles, use the Principal element in the role's trust policy to specify who can assume the role. For
      cross-account access, you must specify the 12-digit identifier of the trusted account.

      Note: After you create the role, you can change the account to "*" to allow everyone to assume the role. If
      you do this, we strongly recommend that you limit who can access the role through other means, such as a
      Condition element that limits access to only certain IP addresses. Do not leave your role accessible to
      everyone!

    - In resource-based policies, use the Principal element to specify the accounts or users who are allowed to
      access the resource.

Do not use the Principal element in policies that you attach to IAM users and groups. Similarly, you do not specify
a principal in the permission policy for an IAM role. In those cases, the principal is implicitly the user that the
policy is attached to (for IAM users) or the user who assumes the role (for role access policies). When the policy
is attached to an IAM group, the principal is the IAM user in that group who is making the request.

