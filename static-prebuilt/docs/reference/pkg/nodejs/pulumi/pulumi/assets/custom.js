"use strict";
var pathname = location.pathname.replace(/\/$/, "");
var b = "/docs/reference/pkg/nodejs/pulumi";
var redirect = "";
// Pulumi
if (pathname == b + "/pulumi") {
  var redirects = {
    "#Alias": b + "/pulumi/interfaces/Alias.html",
    "#all": b + "/pulumi/functions/all.html",
    "#allAliases": b + "/pulumi/functions/allAliases.html",
    "#ComponentResource": b + "/pulumi/classes/ComponentResource.html",
    "#ComponentResourceOptions": b + "/pulumi/interfaces/ComponentResourceOptions.html",
    "#concat": b + "/pulumi/functions/concat.html",
    "#Config": b + "/pulumi/classes/Config.html",
    "#containsUnknowns": b + "/pulumi/functions/containsUnknowns.html",
    "#createUrn": b + "/pulumi/functions/createUrn.html",
    "#CustomResource": b + "/pulumi/classes/CustomResource.html",
    "#CustomResourceOptions": b + "/pulumi/interfaces/CustomResourceOptions.html",
    "#CustomTimeouts": b + "/pulumi/interfaces/CustomTimeouts.html",
    "#DependencyProviderResource": b + "/pulumi/classes/DependencyProviderResource.html",
    "#DependencyResource": b + "/pulumi/classes/DependencyResource.html",
    "#getOrganization": b + "/pulumi/functions/getOrganization.html",
    "#getProject": b + "/pulumi/functions/getProject.html",
    "#getStack": b + "/pulumi/functions/getStack.html",
    "#ID": b + "/pulumi/types/ID.html",
    "#Input": b + "/pulumi/types/Input.html",
    "#Inputs": b + "/pulumi/types/Inputs.html",
    "#interpolate": b + "/pulumi/functions/interpolate.html",
    "#InvokeOptions": b + "/pulumi/interfaces/InvokeOptions.html",
    "#isGrpcError": b + "/pulumi/functions/isGrpcError.html",
    "#isSecret": b + "/pulumi/functions/isSecret.html",
    "#isUnknown": b + "/pulumi/functions/isUnknown.html",
    "#jsonParse": b + "/pulumi/functions/jsonParse.html",
    "#jsonStringify": b + "/pulumi/functions/jsonStringify.html",
    "#Lifted": b + "/pulumi/types/Lifted.html",
    "#LiftedArray": b + "/pulumi/types/LiftedArray.html",
    "#LiftedObject": b + "/pulumi/types/LiftedObject.html",
    "#mergeOptions": b + "/pulumi/functions/mergeOptions.html",
    "#NumberConfigOptions": b + "/pulumi/interfaces/NumberConfigOptions.html",
    "#output": b + "/pulumi/functions/output-2.html",
    "#Output": b + "/pulumi/types/Output.html",
    "#OutputConstructor": b + "/pulumi/interfaces/OutputConstructor.html",
    "#OutputInstance": b + "/pulumi/interfaces/OutputInstance.html",
    "#ProviderResource": b + "/pulumi/classes/ProviderResource.html",
    "#Resource": b + "/pulumi/classes/Resource.html",
    "#ResourceError": b + "/pulumi/classes/ResourceError.html",
    "#ResourceOptions": b + "/pulumi/interfaces/ResourceOptions.html",
    "#ResourceTransform": b + "/pulumi/types/ResourceTransform.html",
    "#ResourceTransformArgs": b + "/pulumi/interfaces/ResourceTransformArgs.html",
    "#ResourceTransformation": b + "/pulumi/types/ResourceTransformation.html",
    "#ResourceTransformationArgs": b + "/pulumi/interfaces/ResourceTransformationArgs.html",
    "#ResourceTransformationResult": b + "/pulumi/interfaces/ResourceTransformationResult.html",
    "#ResourceTransformResult": b + "/pulumi/interfaces/ResourceTransformResult.html",
    "#rootStackResource": b + "/pulumi/variables/rootStackResource.html",
    "#RunError": b + "/pulumi/classes/RunError.html",
    "#secret": b + "/pulumi/functions/secret.html",
    "#StackReference": b + "/pulumi/classes/StackReference.html",
    "#StackReferenceArgs": b + "/pulumi/interfaces/StackReferenceArgs.html",
    "#StackReferenceOutputDetails": b + "/pulumi/interfaces/StackReferenceOutputDetails.html",
    "#StringConfigOptions": b + "/pulumi/interfaces/StringConfigOptions.html",
    "#unsecret": b + "/pulumi/functions/unsecret.html",
    "#Unwrap": b + "/pulumi/types/Unwrap.html",
    "#UnwrappedArray": b + "/pulumi/types/UnwrappedArray.html",
    "#UnwrappedObject": b + "/pulumi/types/UnwrappedObject.html",
    "#UnwrapSimple": b + "/pulumi/types/UnwrapSimple.html",
    "#URN": b + "/pulumi/types/URN.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/iterable.html") {
  var redirects = {
    "#toObject": b + "/pulumi/functions/iterable.toObject.html",
    "#groupBy": b + "/pulumi/functions/iterable.groupBy.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/dynamic.html") {
  var redirects = {
    "#Resource": b + "/pulumi/classes/dynamic.Resource.html",
    "#CheckFailure": b + "/pulumi/interfaces/dynamic.CheckFailure.html",
    "#CheckResult": b + "/pulumi/interfaces/dynamic.CheckResult.html",
    "#CreateResult": b + "/pulumi/interfaces/dynamic.CreateResult.html",
    "#DiffResult": b + "/pulumi/interfaces/dynamic.DiffResult.html",
    "#ReadResult": b + "/pulumi/interfaces/dynamic.ReadResult.html",
    "#ResourceProvider": b + "/pulumi/interfaces/dynamic.ResourceProvider.html",
    "#UpdateResult": b + "/pulumi/interfaces/dynamic.UpdateResult.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/runtime.html") {
  var redirects = {
    "#allConfig": b + "/pulumi/functions/runtime.allConfig.html",
    "#awaitStackRegistrations": b + "/pulumi/functions/runtime.awaitStackRegistrations.html",
    "#cacheDynamicProviders": b + "/pulumi/functions/runtime.cacheDynamicProviders.html",
    "#call": b + "/pulumi/functions/runtime.call.html",
    "#CodePathOptions": b + "/pulumi/interfaces/runtime.CodePathOptions.html",
    "#computeCodePaths": b + "/pulumi/functions/runtime.computeCodePaths.html",
    "#deserializeProperties": b + "/pulumi/functions/runtime.deserializeProperties.html",
    "#deserializeProperty": b + "/pulumi/functions/runtime.deserializeProperty.html",
    "#disconnect": b + "/pulumi/functions/runtime.disconnect.html",
    "#disconnectSync": b + "/pulumi/functions/runtime.disconnectSync.html",
    "#excessiveDebugOutput": b + "/pulumi/variables/runtime.excessiveDebugOutput.html",
    "#getCallbacks": b + "/pulumi/functions/runtime.getCallbacks.html",
    "#getConfig": b + "/pulumi/functions/runtime.getConfig.html",
    "#getEngine": b + "/pulumi/functions/runtime.getEngine.html",
    "#getMaximumListeners": b + "/pulumi/functions/runtime.getMaximumListeners.html",
    "#getMonitor": b + "/pulumi/functions/runtime.getMonitor.html",
    "#getOrganization": b + "/pulumi/functions/runtime.getOrganization.html",
    "#getProject": b + "/pulumi/functions/runtime.getProject.html",
    "#getResource": b + "/pulumi/functions/runtime.getResource.html",
    "#getResourceModule": b + "/pulumi/functions/runtime.getResourceModule.html",
    "#getResourcePackage": b + "/pulumi/functions/runtime.getResourcePackage.html",
    "#getStack": b + "/pulumi/functions/runtime.getStack.html",
    "#getStackResource": b + "/pulumi/functions/runtime.getStackResource.html",
    "#hasEngine": b + "/pulumi/functions/runtime.hasEngine.html",
    "#hasMonitor": b + "/pulumi/functions/runtime.hasMonitor.html",
    "#invoke": b + "/pulumi/functions/runtime.invoke.html",
    "#invokeSingle": b + "/pulumi/functions/runtime.invokeSingle.html",
    "#isDryRun": b + "/pulumi/functions/runtime.isDryRun.html",
    "#isLegacyApplyEnabled": b + "/pulumi/functions/runtime.isLegacyApplyEnabled.html",
    "#isQueryMode": b + "/pulumi/functions/runtime.isQueryMode.html",
    "#isRpcSecret": b + "/pulumi/functions/runtime.isRpcSecret.html",
    "#listResourceOutputs": b + "/pulumi/functions/runtime.listResourceOutputs.html",
    "#mapAliasesForRequest": b + "/pulumi/functions/runtime.mapAliasesForRequest.html",
    "#MockCallArgs": b + "/pulumi/interfaces/runtime.MockCallArgs.html",
    "#MockCallResult": b + "/pulumi/types/runtime.MockCallResult.html",
    "#MockResourceArgs": b + "/pulumi/interfaces/runtime.MockResourceArgs.html",
    "#MockResourceResult": b + "/pulumi/types/runtime.MockResourceResult.html",
    "#Mocks": b + "/pulumi/interfaces/runtime.Mocks.html",
    "#Options": b + "/pulumi/interfaces/runtime.Options.html",
    "#OutputResolvers": b + "/pulumi/types/runtime.OutputResolvers.html",
    "#readResource": b + "/pulumi/functions/runtime.readResource.html",
    "#registerResource": b + "/pulumi/functions/runtime.registerResource.html",
    "#registerResourceModule": b + "/pulumi/functions/runtime.registerResourceModule.html",
    "#registerResourceOutputs": b + "/pulumi/functions/runtime.registerResourceOutputs.html",
    "#registerResourcePackage": b + "/pulumi/functions/runtime.registerResourcePackage.html",
    "#registerStackTransformation": b + "/pulumi/functions/runtime.registerStackTransformation.html",
    "#resetOptions": b + "/pulumi/functions/runtime.resetOptions.html",
    "#resolveProperties": b + "/pulumi/functions/runtime.resolveProperties.html",
    "#ResourceModule": b + "/pulumi/interfaces/runtime.ResourceModule.html",
    "#ResourcePackage": b + "/pulumi/interfaces/runtime.ResourcePackage.html",
    "#rootPulumiStackTypeName": b + "/pulumi/variables/runtime.rootPulumiStackTypeName.html",
    "#rpcKeepAlive": b + "/pulumi/functions/runtime.rpcKeepAlive.html",
    "#runInPulumiStack": b + "/pulumi/functions/runtime.runInPulumiStack.html",
    "#SerializationOptions": b + "/pulumi/interfaces/runtime.SerializationOptions.html",
    "#serialize": b + "/pulumi/functions/runtime.serialize.html",
    "#SerializedFunction": b + "/pulumi/interfaces/runtime.SerializedFunction.html",
    "#serializeFunction": b + "/pulumi/functions/runtime.serializeFunction.html",
    "#SerializeFunctionArgs": b + "/pulumi/interfaces/runtime.SerializeFunctionArgs.html",
    "#serializeFunctionAsync": b + "/pulumi/functions/runtime.serializeFunctionAsync.html",
    "#serializeProperties": b + "/pulumi/functions/runtime.serializeProperties.html",
    "#serializeProperty": b + "/pulumi/functions/runtime.serializeProperty.html",
    "#serializeResourceProperties": b + "/pulumi/functions/runtime.serializeResourceProperties.html",
    "#setAllConfig": b + "/pulumi/functions/runtime.setAllConfig.html",
    "#setConfig": b + "/pulumi/functions/runtime.setConfig.html",
    "#setMockOptions": b + "/pulumi/functions/runtime.setMockOptions.html",
    "#setMocks": b + "/pulumi/functions/runtime.setMocks.html",
    "#setRootResource": b + "/pulumi/functions/runtime.setRootResource.html",
    "#SourcePosition": b + "/pulumi/interfaces/runtime.SourcePosition.html",
    "#specialArchiveSig": b + "/pulumi/variables/runtime.specialArchiveSig.html",
    "#specialAssetSig": b + "/pulumi/variables/runtime.specialAssetSig.html",
    "#specialOutputValueSig": b + "/pulumi/variables/runtime.specialOutputValueSig.html",
    "#specialResourceSig": b + "/pulumi/variables/runtime.specialResourceSig.html",
    "#specialSecretSig": b + "/pulumi/variables/runtime.specialSecretSig.html",
    "#specialSigKey": b + "/pulumi/variables/runtime.specialSigKey.html",
    "#Stack": b + "/pulumi/classes/runtime.Stack.html",
    "#streamInvoke": b + "/pulumi/functions/runtime.streamInvoke.html",
    "#StreamInvokeResponse": b + "/pulumi/classes/runtime.StreamInvokeResponse.html",
    "#suppressUnhandledGrpcRejections": b + "/pulumi/functions/runtime.suppressUnhandledGrpcRejections.html",
    "#terminateRpcs": b + "/pulumi/functions/runtime.terminateRpcs.html",
    "#transferProperties": b + "/pulumi/functions/runtime.transferProperties.html",
    "#unknownValue": b + "/pulumi/variables/runtime.unknownValue.html",
    "#unwrapRpcSecret": b + "/pulumi/functions/runtime.unwrapRpcSecret.html",
    "#xRegisterStackTransform": b + "/pulumi/functions/runtime.xRegisterStackTransform.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/provider.html") {
  var redirects = {
    "#CheckFailure": b + "/pulumi/interfaces/provider.CheckFailure.html",
    "#CheckResult": b + "/pulumi/interfaces/provider.CheckResult.html",
    "#ConstructResult": b + "/pulumi/interfaces/provider.ConstructResult.html",
    "#CreateResult": b + "/pulumi/interfaces/provider.CreateResult.html",
    "#DiffResult": b + "/pulumi/interfaces/provider.DiffResult.html",
    "#InvokeResult": b + "/pulumi/interfaces/provider.InvokeResult.html",
    "#main": b + "/pulumi/functions/provider.main.html",
    "#Provider": b + "/pulumi/interfaces/provider.Provider.html",
    "#ReadResult": b + "/pulumi/interfaces/provider.ReadResult.html",
    "#UpdateResult": b + "/pulumi/interfaces/provider.UpdateResult.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/asset.html") {
  var redirects = {
    "#Archive": b + "/pulumi/classes/asset.Archive.html",
    "#Asset": b + "/pulumi/classes/asset.Asset.html",
    "#AssetArchive": b + "/pulumi/classes/asset.AssetArchive.html",
    "#AssetMap": b + "/pulumi/types/asset.AssetMap.html",
    "#FileArchive": b + "/pulumi/classes/asset.FileArchive.html",
    "#FileAsset": b + "/pulumi/classes/asset.FileAsset.html",
    "#RemoteArchive": b + "/pulumi/classes/asset.RemoteArchive.html",
    "#RemoteAsset": b + "/pulumi/classes/asset.RemoteAsset.html",
    "#StringAsset": b + "/pulumi/classes/asset.StringAsset.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/log.html") {
  var redirects = {
    "#debug": b + "/pulumi/functions/log.debug.html",
    "#error": b + "/pulumi/functions/log.error.html",
    "#hasErrors": b + "/pulumi/functions/log.hasErrors.html",
    "#info": b + "/pulumi/functions/log.info.html",
    "#warn": b + "/pulumi/functions/log.warn.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/pulumi/modules/automation.html") {
  var redirects = {
    "#ConfigMap": b + "/pulumi/types/automation.ConfigMap.html",
    "#ConfigValue": b + "/pulumi/interfaces/automation.ConfigValue.html",
    "#Deployment": b + "/pulumi/interfaces/automation.Deployment.html",
    "#DestroyOptions": b + "/pulumi/interfaces/automation.DestroyOptions.html",
    "#DestroyResult": b + "/pulumi/interfaces/automation.DestroyResult.html",
    "#fullyQualifiedStackName": b + "/pulumi/functions/automation.fullyQualifiedStackName.html",
    "#GlobalOpts": b + "/pulumi/interfaces/automation.GlobalOpts.html",
    "#InlineProgramArgs": b + "/pulumi/interfaces/automation.InlineProgramArgs.html",
    "#LocalProgramArgs": b + "/pulumi/interfaces/automation.LocalProgramArgs.html",
    "#LocalWorkspace": b + "/pulumi/classes/automation.LocalWorkspace.html",
    "#LocalWorkspaceOptions": b + "/pulumi/interfaces/automation.LocalWorkspaceOptions.html",
    "#OpMap": b + "/pulumi/types/automation.OpMap.html",
    "#OpType": b + "/pulumi/types/automation.OpType.html",
    "#OutputMap": b + "/pulumi/types/automation.OutputMap.html",
    "#OutputValue": b + "/pulumi/interfaces/automation.OutputValue.html",
    "#PluginInfo": b + "/pulumi/interfaces/automation.PluginInfo.html",
    "#PluginKind": b + "/pulumi/types/automation.PluginKind.html",
    "#PreviewOptions": b + "/pulumi/interfaces/automation.PreviewOptions.html",
    "#PreviewResult": b + "/pulumi/interfaces/automation.PreviewResult.html",
    "#ProjectBackend": b + "/pulumi/interfaces/automation.ProjectBackend.html",
    "#ProjectRuntime": b + "/pulumi/types/automation.ProjectRuntime.html",
    "#ProjectRuntimeInfo": b + "/pulumi/interfaces/automation.ProjectRuntimeInfo.html",
    "#ProjectSettings": b + "/pulumi/interfaces/automation.ProjectSettings.html",
    "#ProjectTemplate": b + "/pulumi/interfaces/automation.ProjectTemplate.html",
    "#ProjectTemplateConfigValue": b + "/pulumi/interfaces/automation.ProjectTemplateConfigValue.html",
    "#PulumiCommand": b + "/pulumi/classes/automation.PulumiCommand.html",
    "#PulumiCommandOptions": b + "/pulumi/interfaces/automation.PulumiCommandOptions.html",
    "#PulumiFn": b + "/pulumi/types/automation.PulumiFn.html",
    "#RawJSON": b + "/pulumi/types/automation.RawJSON.html",
    "#RefreshOptions": b + "/pulumi/interfaces/automation.RefreshOptions.html",
    "#RefreshResult": b + "/pulumi/interfaces/automation.RefreshResult.html",
    "#RemoteDestroyOptions": b + "/pulumi/interfaces/automation.RemoteDestroyOptions.html",
    "#RemoteGitAuthArgs": b + "/pulumi/interfaces/automation.RemoteGitAuthArgs.html",
    "#RemoteGitProgramArgs": b + "/pulumi/interfaces/automation.RemoteGitProgramArgs.html",
    "#RemotePreviewOptions": b + "/pulumi/interfaces/automation.RemotePreviewOptions.html",
    "#RemoteRefreshOptions": b + "/pulumi/interfaces/automation.RemoteRefreshOptions.html",
    "#RemoteStack": b + "/pulumi/classes/automation.RemoteStack.html",
    "#RemoteUpOptions": b + "/pulumi/interfaces/automation.RemoteUpOptions.html",
    "#RemoteWorkspace": b + "/pulumi/classes/automation.RemoteWorkspace.html",
    "#RemoteWorkspaceOptions": b + "/pulumi/interfaces/automation.RemoteWorkspaceOptions.html",
    "#Stack": b + "/pulumi/classes/automation.Stack.html",
    "#StackSettings": b + "/pulumi/interfaces/automation.StackSettings.html",
    "#StackSettingsConfigValue": b + "/pulumi/types/automation.StackSettingsConfigValue.html",
    "#StackSettingsSecureConfigValue": b + "/pulumi/interfaces/automation.StackSettingsSecureConfigValue.html",
    "#StackSummary": b + "/pulumi/interfaces/automation.StackSummary.html",
    "#UpdateKind": b + "/pulumi/types/automation.UpdateKind.html",
    "#UpdateResult": b + "/pulumi/types/automation.UpdateResult.html",
    "#UpdateSummary": b + "/pulumi/interfaces/automation.UpdateSummary.html",
    "#UpOptions": b + "/pulumi/interfaces/automation.UpOptions.html",
    "#UpResult": b + "/pulumi/interfaces/automation.UpResult.html",
    "#WhoAmIResult": b + "/pulumi/interfaces/automation.WhoAmIResult.html",
    "#Workspace": b + "/pulumi/interfaces/automation.Workspace.html",
  };
  redirect = redirects[location.hash];
}
// Policy
if (pathname == b + "/policy") {
  var redirects = {
    "#EnforcementLevel": b + "/policy/types/EnforcementLevel.html",
    "#Policies": b + "/policy/types/Policies.html",
    "#Policy": b + "/policy/interfaces/Policy.html",
    // These types are not exported
    // "#PolicyConfigJSONSchema": base + "/policy/interfaces/PolicyConfigJSONSchema.html",
    // "#PolicyConfigJSONSchemaDefinition": base + "/policy/types/PolicyConfigJSONSchemaDefinition.html",
    // "#PolicyConfigJSONSchemaType": base + "/policy/types/PolicyConfigJSONSchemaType.html",
    // "#PolicyConfigJSONSchemaTypeName": base + "/policy/types/PolicyConfigJSONSchemaTypeName.html",
    "#PolicyConfigSchema": b + "/policy/interfaces/PolicyConfigSchema.html",
    "#PolicyCustomTimeouts": b + "/policy/interfaces/PolicyCustomTimeouts.html",
    "#PolicyPack": b + "/policy/classes/PolicyPack.html",
    "#PolicyPackArgs": b + "/policy/interfaces/PolicyPackArgs.html",
    "#PolicyPackConfig": b + "/policy/types/PolicyPackConfig.html",
    "#PolicyProviderResource": b + "/policy/interfaces/PolicyProviderResource.html",
    "#PolicyResource": b + "/policy/interfaces/PolicyResource.html",
    "#PolicyResourceOptions": b + "/policy/interfaces/PolicyResourceOptions.html",
    "#remediateResourceOfType": b + "/policy/functions/remediateResourceOfType.html",
    "#ReportViolation": b + "/policy/types/ReportViolation.html",
    "#ResourceRemediation": b + "/policy/types/ResourceRemediation.html",
    "#ResourceValidation": b + "/policy/types/ResourceValidation.html",
    "#ResourceValidationArgs": b + "/policy/interfaces/ResourceValidationArgs.html",
    "#ResourceValidationPolicy": b + "/policy/interfaces/ResourceValidationPolicy.html",
    "#Secret": b + "/policy/classes/Secret.html",
    "#StackValidation": b + "/policy/types/StackValidation.html",
    "#StackValidationArgs": b + "/policy/interfaces/StackValidationArgs.html",
    "#StackValidationPolicy": b + "/policy/interfaces/StackValidationPolicy.html",
    "#TypedResourceRemediation": b + "/policy/types/TypedResourceRemediation.html",
    "#TypedResourceValidation": b + "/policy/types/TypedResourceValidation.html",
    "#TypedResourceValidationRemediation": b + "/policy/types/TypedResourceValidationRemediation.html",
    "#validateRemediateResourceOfType": b + "/policy/functions/validateRemediateResourceOfType.html",
    "#validateResourceOfType": b + "/policy/functions/validateResourceOfType.html",
    "#validateStackResourcesOfType": b + "/policy/functions/validateStackResourcesOfType.html",
  };
  redirect = redirects[location.hash];
}
// Terraform
if (pathname == b + "/terraform/modules/state.html") {
  var redirects = {
    "#ArtifactoryRemoteStateReferenceArgs": b + "/terraform/interfaces/state.ArtifactoryRemoteStateReferenceArgs.html",
    "#AzureEnvironment": b + "/terraform/types/state.AzureEnvironment.html",
    "#AzureRMRemoteStateReferenceArgs": b + "/terraform/interfaces/state.AzureRMRemoteStateReferenceArgs.html",
    "#ConsulRemoteStateReferenceArgs": b + "/terraform/interfaces/state.ConsulRemoteStateReferenceArgs.html",
    "#EtcdV2RemoteStateReferenceArgs": b + "/terraform/interfaces/state.EtcdV2RemoteStateReferenceArgs.html",
    "#EtcdV3RemoteStateReferenceArgs": b + "/terraform/interfaces/state.EtcdV3RemoteStateReferenceArgs.html",
    "#GCSRemoteStateReferenceArgs": b + "/terraform/interfaces/state.GCSRemoteStateReferenceArgs.html",
    "#HttpRemoteStateReferenceArgs": b + "/terraform/interfaces/state.HttpRemoteStateReferenceArgs.html",
    "#LocalBackendRemoteStateReferenceArgs": b + "/terraform/interfaces/state.LocalBackendRemoteStateReferenceArgs.html",
    "#MantaRemoteStateReferenceArgs": b + "/terraform/interfaces/state.MantaRemoteStateReferenceArgs.html",
    "#OssRemoteStateReferenceArgs": b + "/terraform/interfaces/state.OssRemoteStateReferenceArgs.html",
    // "#PostgresRemoteStateReferenceArgs": base + "/terraform/interfaces/state.PostgresRemoteStateReferenceArgs.html",
    "#RemoteBackendRemoteStateReferenceArgs": b + "/terraform/interfaces/state.RemoteBackendRemoteStateReferenceArgs.html",
    "#RemoteBackendWorkspaceConfig": b + "/terraform/interfaces/state.RemoteBackendWorkspaceConfig.html",
    "#RemoteStateReference": b + "/terraform/classes/state.RemoteStateReference.html",
    "#RemoteStateReferenceArgs": b + "/terraform/types/state.RemoteStateReferenceArgs.html",
    "#S3RemoteStateReferenceArgs": b + "/terraform/interfaces/state.S3RemoteStateReferenceArgs.html",
    "#SwiftRemoteStateReferenceArgs": b + "/terraform/interfaces/state.SwiftRemoteStateReferenceArgs.html",
  };
  redirect = redirects[location.hash];
}
// AWSX
if (pathname == b + "/awsx") {
  var redirects = {
    "#Provider": b + "/awsx/types/Provider.html",
    "#ProviderArgs": b + "/awsx/interfaces/ProviderArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.html") {
  var redirects = {
    "#getAvailabilityZone": b + "/awsx/functions/classic.getAvailabilityZone.html",
    "#getAvailabilityZones": b + "/awsx/functions/classic.getAvailabilityZones.html",
    "#Overwrite": b + "/awsx/types/classic.Overwrite.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.dynamodb.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.dynamodb.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.billing.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.billing.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.sns.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.sns.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.lambda.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.lambda.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.autoscaling.html") {
  var redirects = {
    "#AdjustmentType": b + "/awsx/types/classic.autoscaling.AdjustmentType.html",
    "#ApplicationTargetGroupTrackingPolicyArgs": b + "/awsx/interfaces/classic.autoscaling.ApplicationTargetGroupTrackingPolicyArgs.html",
    "#AutoScalingGroup": b + "/awsx/classes/classic.autoscaling.AutoScalingGroup.html",
    "#AutoScalingGroupArgs": b + "/awsx/interfaces/classic.autoscaling.AutoScalingGroupArgs.html",
    "#AutoScalingLaunchConfiguration": b + "/awsx/classes/classic.autoscaling.AutoScalingLaunchConfiguration.html",
    "#AutoScalingLaunchConfigurationArgs": b + "/awsx/interfaces/classic.autoscaling.AutoScalingLaunchConfigurationArgs.html",
    "#AutoScalingUserData": b + "/awsx/interfaces/classic.autoscaling.AutoScalingUserData.html",
    "#cronExpression": b + "/awsx/functions/classic.autoscaling.cronExpression.html",
    "#CustomMetricTargetTrackingPolicyArgs": b + "/awsx/interfaces/classic.autoscaling.CustomMetricTargetTrackingPolicyArgs.html",
    "#DayOfWeek": b + "/awsx/types/classic.autoscaling.DayOfWeek.html",
    "#metrics": b + "/awsx/modules/classic.autoscaling.metrics.html",
    "#Month": b + "/awsx/types/classic.autoscaling.Month.html",
    "#ScalingStep": b + "/awsx/interfaces/classic.autoscaling.ScalingStep.html",
    "#ScalingSteps": b + "/awsx/interfaces/classic.autoscaling.ScalingSteps.html",
    "#ScheduleArgs": b + "/awsx/interfaces/classic.autoscaling.ScheduleArgs.html",
    "#ScheduleRecurrenceArgs": b + "/awsx/interfaces/classic.autoscaling.ScheduleRecurrenceArgs.html",
    "#StepScalingPolicy": b + "/awsx/classes/classic.autoscaling.StepScalingPolicy.html",
    "#StepScalingPolicyArgs": b + "/awsx/interfaces/classic.autoscaling.StepScalingPolicyArgs.html",
    "#TargetTrackingPolicyArgs": b + "/awsx/interfaces/classic.autoscaling.TargetTrackingPolicyArgs.html",
    "#TemplateParameters": b + "/awsx/interfaces/classic.autoscaling.TemplateParameters.html",
    "#UserDataLine": b + "/awsx/interfaces/classic.autoscaling.UserDataLine.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.ebs.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.ebs.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.acmpca.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.acmpca.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.efs.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.efs.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.ec2.html") {
  var redirects = {
    "#AllTcpPorts": b + "/awsx/classes/classic.ec2.AllTcpPorts.html",
    "#AllTraffic": b + "/awsx/classes/classic.ec2.AllTraffic.html",
    "#AllUdpPorts": b + "/awsx/classes/classic.ec2.AllUdpPorts.html",
    "#AnyIPv4Location": b + "/awsx/classes/classic.ec2.AnyIPv4Location.html",
    "#AnyIPv6Location": b + "/awsx/classes/classic.ec2.AnyIPv6Location.html",
    "#AvailabilityZoneDescription": b + "/awsx/interfaces/classic.ec2.AvailabilityZoneDescription.html",
    "#Cidr32Block": b + "/awsx/classes/classic.ec2.Cidr32Block.html",
    "#CidrBlock": b + "/awsx/types/classic.ec2.CidrBlock.html",
    "#create": b + "/awsx/functions/classic.ec2.create.html",
    "#EgressSecurityGroupRule": b + "/awsx/classes/classic.ec2.EgressSecurityGroupRule.html",
    "#EgressSecurityGroupRuleArgs": b + "/awsx/interfaces/classic.ec2.EgressSecurityGroupRuleArgs.html",
    "#ExistingInternetGatewayArgs": b + "/awsx/interfaces/classic.ec2.ExistingInternetGatewayArgs.html",
    "#ExistingNatGatewayArgs": b + "/awsx/interfaces/classic.ec2.ExistingNatGatewayArgs.html",
    "#ExistingSubnetArgs": b + "/awsx/interfaces/classic.ec2.ExistingSubnetArgs.html",
    "#ExistingVpcArgs": b + "/awsx/interfaces/classic.ec2.ExistingVpcArgs.html",
    "#ExistingVpcIdArgs": b + "/awsx/interfaces/classic.ec2.ExistingVpcIdArgs.html",
    "#getIPv4Address": b + "/awsx/functions/classic.ec2.getIPv4Address.html",
    "#IcmpPorts": b + "/awsx/classes/classic.ec2.IcmpPorts.html",
    "#IngressSecurityGroupRule": b + "/awsx/classes/classic.ec2.IngressSecurityGroupRule.html",
    "#IngressSecurityGroupRuleArgs": b + "/awsx/interfaces/classic.ec2.IngressSecurityGroupRuleArgs.html",
    "#InternetGateway": b + "/awsx/classes/classic.ec2.InternetGateway.html",
    "#metrics": b + "/awsx/modules/classic.ec2.metrics.html",
    "#NatGateway": b + "/awsx/classes/classic.ec2.NatGateway.html",
    "#NatGatewayArgs": b + "/awsx/interfaces/classic.ec2.NatGatewayArgs.html",
    "#NatGatewayDescription": b + "/awsx/interfaces/classic.ec2.NatGatewayDescription.html",
    "#NatRouteDescription": b + "/awsx/interfaces/classic.ec2.NatRouteDescription.html",
    "#RouteArgs": b + "/awsx/interfaces/classic.ec2.RouteArgs.html",
    "#SecurityGroup": b + "/awsx/classes/classic.ec2.SecurityGroup.html",
    "#SecurityGroupArgs": b + "/awsx/interfaces/classic.ec2.SecurityGroupArgs.html",
    "#SecurityGroupOrId": b + "/awsx/types/classic.ec2.SecurityGroupOrId.html",
    "#SecurityGroupRule": b + "/awsx/classes/classic.ec2.SecurityGroupRule.html",
    "#SecurityGroupRuleArgs": b + "/awsx/interfaces/classic.ec2.SecurityGroupRuleArgs.html",
    "#SecurityGroupRuleLocation": b + "/awsx/interfaces/classic.ec2.SecurityGroupRuleLocation.html",
    "#SecurityGroupRulePorts": b + "/awsx/interfaces/classic.ec2.SecurityGroupRulePorts.html",
    "#SecurityGroupRuleProtocol": b + "/awsx/types/classic.ec2.SecurityGroupRuleProtocol.html",
    "#SimpleSecurityGroupRuleArgs": b + "/awsx/interfaces/classic.ec2.SimpleSecurityGroupRuleArgs.html",
    "#Subnet": b + "/awsx/classes/classic.ec2.Subnet.html",
    "#SubnetArgs": b + "/awsx/interfaces/classic.ec2.SubnetArgs.html",
    "#SubnetDescription": b + "/awsx/interfaces/classic.ec2.SubnetDescription.html",
    "#SubnetOrId": b + "/awsx/types/classic.ec2.SubnetOrId.html",
    "#SubnetRouteProvider": b + "/awsx/interfaces/classic.ec2.SubnetRouteProvider.html",
    "#TcpPorts": b + "/awsx/classes/classic.ec2.TcpPorts.html",
    "#UdpPorts": b + "/awsx/classes/classic.ec2.UdpPorts.html",
    "#Vpc": b + "/awsx/classes/classic.ec2.Vpc.html",
    "#VpcArgs": b + "/awsx/interfaces/classic.ec2.VpcArgs.html",
    "#VpcSubnetArgs": b + "/awsx/interfaces/classic.ec2.VpcSubnetArgs.html",
    "#VpcSubnetLocation": b + "/awsx/interfaces/classic.ec2.VpcSubnetLocation.html",
    "#VpcSubnetType": b + "/awsx/types/classic.ec2.VpcSubnetType.html",
    "#VpcTopologyDescription": b + "/awsx/interfaces/classic.ec2.VpcTopologyDescription.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.cloudfront.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.cloudfront.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.cloudwatch.html") {
  var redirects = {
    "#AlarmAnnotation": b + "/awsx/classes/classic.cloudwatch.AlarmAnnotation.html",
    "#AlarmArgs": b + "/awsx/interfaces/classic.cloudwatch.AlarmArgs.html",
    "#AlarmComparisonOperator": b + "/awsx/types/classic.cloudwatch.AlarmComparisonOperator.html",
    "#AlarmWidget": b + "/awsx/classes/classic.cloudwatch.AlarmWidget.html",
    "#AlarmWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.AlarmWidgetArgs.html",
    "#AlarmWidgetJson": b + "/awsx/interfaces/classic.cloudwatch.AlarmWidgetJson.html",
    "#AlarmWidgetPropertiesJson": b + "/awsx/interfaces/classic.cloudwatch.AlarmWidgetPropertiesJson.html",
    "#BaseHorizontalAnnotationJson": b + "/awsx/interfaces/classic.cloudwatch.BaseHorizontalAnnotationJson.html",
    "#ColumnWidget": b + "/awsx/classes/classic.cloudwatch.ColumnWidget.html",
    "#Dashboard": b + "/awsx/classes/classic.cloudwatch.Dashboard.html",
    "#DashboardArgs": b + "/awsx/interfaces/classic.cloudwatch.DashboardArgs.html",
    "#ExpressionMetricJson": b + "/awsx/types/classic.cloudwatch.ExpressionMetricJson.html",
    "#ExpressionWidgetMetric": b + "/awsx/classes/classic.cloudwatch.ExpressionWidgetMetric.html",
    "#FlowWidget": b + "/awsx/classes/classic.cloudwatch.FlowWidget.html",
    "#GraphMetricWidget": b + "/awsx/classes/classic.cloudwatch.GraphMetricWidget.html",
    "#GraphMetricWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.GraphMetricWidgetArgs.html",
    "#HorizontalAlarmAnnotationArgs": b + "/awsx/interfaces/classic.cloudwatch.HorizontalAlarmAnnotationArgs.html",
    "#HorizontalAnnotation": b + "/awsx/classes/classic.cloudwatch.HorizontalAnnotation.html",
    "#HorizontalAnnotationArgs": b + "/awsx/interfaces/classic.cloudwatch.HorizontalAnnotationArgs.html",
    "#HorizontalAnnotationJson": b + "/awsx/interfaces/classic.cloudwatch.HorizontalAnnotationJson.html",
    "#HorizontalEdge": b + "/awsx/interfaces/classic.cloudwatch.HorizontalEdge.html",
    "#LineGraphMetricWidget": b + "/awsx/classes/classic.cloudwatch.LineGraphMetricWidget.html",
    "#LogWidget": b + "/awsx/classes/classic.cloudwatch.LogWidget.html",
    "#LogWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.LogWidgetArgs.html",
    "#LogWidgetJson": b + "/awsx/interfaces/classic.cloudwatch.LogWidgetJson.html",
    "#LogWidgetPropertiesJson": b + "/awsx/interfaces/classic.cloudwatch.LogWidgetPropertiesJson.html",
    "#Metric": b + "/awsx/classes/classic.cloudwatch.Metric.html",
    "#MetricArgs": b + "/awsx/interfaces/classic.cloudwatch.MetricArgs.html",
    "#MetricChange": b + "/awsx/interfaces/classic.cloudwatch.MetricChange.html",
    "#MetricJson": b + "/awsx/types/classic.cloudwatch.MetricJson.html",
    "#metrics": b + "/awsx/modules/classic.cloudwatch.metrics.html",
    "#MetricStatistic": b + "/awsx/types/classic.cloudwatch.MetricStatistic.html",
    "#MetricUnit": b + "/awsx/types/classic.cloudwatch.MetricUnit.html",
    "#MetricWidget": b + "/awsx/classes/classic.cloudwatch.MetricWidget.html",
    "#MetricWidgetAnnotationsJson": b + "/awsx/interfaces/classic.cloudwatch.MetricWidgetAnnotationsJson.html",
    "#MetricWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.MetricWidgetArgs.html",
    "#MetricWidgetJson": b + "/awsx/interfaces/classic.cloudwatch.MetricWidgetJson.html",
    "#MetricWidgetPropertiesJson": b + "/awsx/interfaces/classic.cloudwatch.MetricWidgetPropertiesJson.html",
    "#MinMax": b + "/awsx/interfaces/classic.cloudwatch.MinMax.html",
    "#RenderingPropertiesJson": b + "/awsx/interfaces/classic.cloudwatch.RenderingPropertiesJson.html",
    "#RowWidget": b + "/awsx/classes/classic.cloudwatch.RowWidget.html",
    "#SimpleWidget": b + "/awsx/classes/classic.cloudwatch.SimpleWidget.html",
    "#SimpleWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.SimpleWidgetArgs.html",
    "#SingleMetricJson": b + "/awsx/types/classic.cloudwatch.SingleMetricJson.html",
    "#SingleNumberMetricWidget": b + "/awsx/classes/classic.cloudwatch.SingleNumberMetricWidget.html",
    "#SpaceWidget": b + "/awsx/classes/classic.cloudwatch.SpaceWidget.html",
    "#StackedAreaGraphMetricWidget": b + "/awsx/classes/classic.cloudwatch.StackedAreaGraphMetricWidget.html",
    "#TextWidget": b + "/awsx/classes/classic.cloudwatch.TextWidget.html",
    "#TextWidgetArgs": b + "/awsx/interfaces/classic.cloudwatch.TextWidgetArgs.html",
    "#TextWidgetJson": b + "/awsx/interfaces/classic.cloudwatch.TextWidgetJson.html",
    "#VerticalAnnotation": b + "/awsx/classes/classic.cloudwatch.VerticalAnnotation.html",
    "#VerticalAnnotationArgs": b + "/awsx/interfaces/classic.cloudwatch.VerticalAnnotationArgs.html",
    "#VerticalAnnotationJson": b + "/awsx/interfaces/classic.cloudwatch.VerticalAnnotationJson.html",
    "#VerticalEdge": b + "/awsx/interfaces/classic.cloudwatch.VerticalEdge.html",
    "#Widget": b + "/awsx/interfaces/classic.cloudwatch.Widget.html",
    "#WidgetAlarm": b + "/awsx/interfaces/classic.cloudwatch.WidgetAlarm.html",
    "#WidgetAnnotation": b + "/awsx/interfaces/classic.cloudwatch.WidgetAnnotation.html",
    "#WidgetJson": b + "/awsx/interfaces/classic.cloudwatch.WidgetJson.html",
    "#WidgetMetric": b + "/awsx/interfaces/classic.cloudwatch.WidgetMetric.html",
    "#YAxis": b + "/awsx/interfaces/classic.cloudwatch.YAxis.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.apigateway.html") {
  var redirects = {
    "#AdditionalRoute": b + "/awsx/types/classic.apigateway.AdditionalRoute.html",
    "#API": b + "/awsx/classes/classic.apigateway.API.html",
    "#APIArgs": b + "/awsx/interfaces/classic.apigateway.APIArgs.html",
    "#ApigatewayAuth": b + "/awsx/interfaces/classic.apigateway.ApigatewayAuth.html",
    "#ApigatewayIntegration": b + "/awsx/interfaces/classic.apigateway.ApigatewayIntegration.html",
    "#APIKeyArgs": b + "/awsx/interfaces/classic.apigateway.APIKeyArgs.html",
    "#apiKeySecurityDefinition": b + "/awsx/variables/classic.apigateway.apiKeySecurityDefinition.html",
    "#APIKeySource": b + "/awsx/types/classic.apigateway.APIKeySource.html",
    "#AssociatedAPIKeys": b + "/awsx/interfaces/classic.apigateway.AssociatedAPIKeys.html",
    "#AuthorizerEvent": b + "/awsx/types/classic.apigateway.AuthorizerEvent.html",
    "#authorizerResponse": b + "/awsx/functions/classic.apigateway.authorizerResponse-1.html",
    "#AuthorizerResponse": b + "/awsx/types/classic.apigateway.AuthorizerResponse.html",
    "#AuthResponseContext": b + "/awsx/types/classic.apigateway.AuthResponseContext.html",
    "#BaseRoute": b + "/awsx/interfaces/classic.apigateway.BaseRoute.html",
    "#CognitoAuthorizer": b + "/awsx/interfaces/classic.apigateway.CognitoAuthorizer.html",
    "#CognitoAuthorizerArgs": b + "/awsx/interfaces/classic.apigateway.CognitoAuthorizerArgs.html",
    "#createAPI": b + "/awsx/functions/classic.apigateway.createAPI.html",
    "#createAssociatedAPIKeys": b + "/awsx/functions/classic.apigateway.createAssociatedAPIKeys.html",
    "#DeploymentArgs": b + "/awsx/interfaces/classic.apigateway.DeploymentArgs.html",
    "#Effect": b + "/awsx/types/classic.apigateway.Effect.html",
    "#Endpoint": b + "/awsx/interfaces/classic.apigateway.Endpoint.html",
    "#EventHandlerRoute": b + "/awsx/interfaces/classic.apigateway.EventHandlerRoute.html",
    "#getCognitoAuthorizer": b + "/awsx/functions/classic.apigateway.getCognitoAuthorizer.html",
    "#getRequestLambdaAuthorizer": b + "/awsx/functions/classic.apigateway.getRequestLambdaAuthorizer.html",
    "#getTokenLambdaAuthorizer": b + "/awsx/functions/classic.apigateway.getTokenLambdaAuthorizer.html",
    "#IntegrationConnectionType": b + "/awsx/types/classic.apigateway.IntegrationConnectionType.html",
    "#IntegrationPassthroughBehavior": b + "/awsx/types/classic.apigateway.IntegrationPassthroughBehavior.html",
    "#IntegrationRoute": b + "/awsx/interfaces/classic.apigateway.IntegrationRoute.html",
    "#IntegrationRouteTargetProvider": b + "/awsx/interfaces/classic.apigateway.IntegrationRouteTargetProvider.html",
    "#IntegrationTarget": b + "/awsx/interfaces/classic.apigateway.IntegrationTarget.html",
    "#IntegrationType": b + "/awsx/types/classic.apigateway.IntegrationType.html",
    "#Key": b + "/awsx/interfaces/classic.apigateway.Key.html",
    "#LambdaAuthorizer": b + "/awsx/interfaces/classic.apigateway.LambdaAuthorizer.html",
    "#LambdaAuthorizerInfo": b + "/awsx/interfaces/classic.apigateway.LambdaAuthorizerInfo.html",
    "#Method": b + "/awsx/types/classic.apigateway.Method.html",
    "#metrics": b + "/awsx/modules/classic.apigateway.metrics.html",
    "#Parameter": b + "/awsx/interfaces/classic.apigateway.Parameter.html",
    "#RawDataRoute": b + "/awsx/types/classic.apigateway.RawDataRoute.html",
    "#Request": b + "/awsx/types/classic.apigateway.Request.html",
    "#RequestAuthorizerArgs": b + "/awsx/interfaces/classic.apigateway.RequestAuthorizerArgs.html",
    "#RequestContext": b + "/awsx/types/classic.apigateway.RequestContext.html",
    "#RequestValidator": b + "/awsx/types/classic.apigateway.RequestValidator.html",
    "#Response": b + "/awsx/types/classic.apigateway.Response.html",
    "#RestApiArgs": b + "/awsx/types/classic.apigateway.RestApiArgs.html",
    "#Route": b + "/awsx/types/classic.apigateway.Route.html",
    "#SecurityDefinition": b + "/awsx/interfaces/classic.apigateway.SecurityDefinition.html",
    "#StageArgs": b + "/awsx/interfaces/classic.apigateway.StageArgs.html",
    "#StaticRoute": b + "/awsx/interfaces/classic.apigateway.StaticRoute.html",
    "#SwaggerAPIGatewayIntegrationResponse": b + "/awsx/interfaces/classic.apigateway.SwaggerAPIGatewayIntegrationResponse.html",
    "#SwaggerCognitoAuthorizer": b + "/awsx/interfaces/classic.apigateway.SwaggerCognitoAuthorizer.html",
    "#SwaggerGatewayResponse": b + "/awsx/interfaces/classic.apigateway.SwaggerGatewayResponse.html",
    "#SwaggerHeader": b + "/awsx/interfaces/classic.apigateway.SwaggerHeader.html",
    "#SwaggerInfo": b + "/awsx/interfaces/classic.apigateway.SwaggerInfo.html",
    "#SwaggerItems": b + "/awsx/interfaces/classic.apigateway.SwaggerItems.html",
    "#SwaggerLambdaAuthorizer": b + "/awsx/interfaces/classic.apigateway.SwaggerLambdaAuthorizer.html",
    "#SwaggerOperation": b + "/awsx/interfaces/classic.apigateway.SwaggerOperation.html",
    "#SwaggerParameter": b + "/awsx/interfaces/classic.apigateway.SwaggerParameter.html",
    "#SwaggerResponse": b + "/awsx/interfaces/classic.apigateway.SwaggerResponse.html",
    "#SwaggerSchema": b + "/awsx/interfaces/classic.apigateway.SwaggerSchema.html",
    "#SwaggerSpec": b + "/awsx/interfaces/classic.apigateway.SwaggerSpec.html",
    "#TokenAuthorizerArgs": b + "/awsx/interfaces/classic.apigateway.TokenAuthorizerArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.cognito.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.cognito.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.s3.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.s3.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.ecs.html") {
  var redirects = {
    "#CapacityProviderService": b + "/awsx/classes/classic.ecs.CapacityProviderService.html",
    "#CapacityProviderServiceArgs": b + "/awsx/interfaces/classic.ecs.CapacityProviderServiceArgs.html",
    "#Cluster": b + "/awsx/classes/classic.ecs.Cluster.html",
    "#ClusterArgs": b + "/awsx/interfaces/classic.ecs.ClusterArgs.html",
    "#Container": b + "/awsx/interfaces/classic.ecs.Container.html",
    "#ContainerDependency": b + "/awsx/interfaces/classic.ecs.ContainerDependency.html",
    "#ContainerImageProvider": b + "/awsx/interfaces/classic.ecs.ContainerImageProvider.html",
    "#ContainerLoadBalancer": b + "/awsx/interfaces/classic.ecs.ContainerLoadBalancer.html",
    "#ContainerLoadBalancerProvider": b + "/awsx/interfaces/classic.ecs.ContainerLoadBalancerProvider.html",
    "#ContainerPortMappingProvider": b + "/awsx/interfaces/classic.ecs.ContainerPortMappingProvider.html",
    "#EC2Service": b + "/awsx/classes/classic.ecs.EC2Service.html",
    "#EC2ServiceArgs": b + "/awsx/interfaces/classic.ecs.EC2ServiceArgs.html",
    "#EC2TaskDefinition": b + "/awsx/classes/classic.ecs.EC2TaskDefinition.html",
    "#EC2TaskDefinitionArgs": b + "/awsx/interfaces/classic.ecs.EC2TaskDefinitionArgs.html",
    "#EnvironmentFile": b + "/awsx/interfaces/classic.ecs.EnvironmentFile.html",
    "#FargateService": b + "/awsx/classes/classic.ecs.FargateService.html",
    "#FargateServiceArgs": b + "/awsx/interfaces/classic.ecs.FargateServiceArgs.html",
    "#FargateTaskDefinition": b + "/awsx/classes/classic.ecs.FargateTaskDefinition.html",
    "#FargateTaskDefinitionArgs": b + "/awsx/interfaces/classic.ecs.FargateTaskDefinitionArgs.html",
    "#FirelensConfiguration": b + "/awsx/interfaces/classic.ecs.FirelensConfiguration.html",
    "#Image": b + "/awsx/classes/classic.ecs.Image.html",
    "#KeyValuePair": b + "/awsx/interfaces/classic.ecs.KeyValuePair.html",
    "#metrics": b + "/awsx/modules/classic.ecs.metrics.html",
    "#NetworkConfiguration": b + "/awsx/interfaces/classic.ecs.NetworkConfiguration.html",
    "#RunTaskRequest": b + "/awsx/interfaces/classic.ecs.RunTaskRequest.html",
    "#Service": b + "/awsx/classes/classic.ecs.Service.html",
    "#ServiceArgs": b + "/awsx/interfaces/classic.ecs.ServiceArgs.html",
    "#ServiceLoadBalancer": b + "/awsx/interfaces/classic.ecs.ServiceLoadBalancer.html",
    "#ServiceLoadBalancerProvider": b + "/awsx/interfaces/classic.ecs.ServiceLoadBalancerProvider.html",
    "#TaskDefinition": b + "/awsx/classes/classic.ecs.TaskDefinition.html",
    "#TaskDefinitionArgs": b + "/awsx/interfaces/classic.ecs.TaskDefinitionArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.lb.html") {
  var redirects = {
    "#ApplicationListener": b + "/awsx/classes/classic.lb.ApplicationListener.html",
    "#ApplicationListenerArgs": b + "/awsx/interfaces/classic.lb.ApplicationListenerArgs.html",
    "#ApplicationLoadBalancer": b + "/awsx/classes/classic.lb.ApplicationLoadBalancer.html",
    "#ApplicationLoadBalancerArgs": b + "/awsx/interfaces/classic.lb.ApplicationLoadBalancerArgs.html",
    "#ApplicationProtocol": b + "/awsx/types/classic.lb.ApplicationProtocol.html",
    "#ApplicationTargetGroup": b + "/awsx/classes/classic.lb.ApplicationTargetGroup.html",
    "#ApplicationTargetGroupArgs": b + "/awsx/interfaces/classic.lb.ApplicationTargetGroupArgs.html",
    "#ApplicationTargetGroupHealthCheck": b + "/awsx/interfaces/classic.lb.ApplicationTargetGroupHealthCheck.html",
    "#isLoadBalancerTargetInfoProvider": b + "/awsx/functions/classic.lb.isLoadBalancerTargetInfoProvider.html",
    "#Listener": b + "/awsx/classes/classic.lb.Listener.html",
    "#ListenerActions": b + "/awsx/interfaces/classic.lb.ListenerActions.html",
    "#ListenerArgs": b + "/awsx/interfaces/classic.lb.ListenerArgs.html",
    "#ListenerDefaultAction": b + "/awsx/interfaces/classic.lb.ListenerDefaultAction.html",
    "#ListenerDefaultActionArgs": b + "/awsx/interfaces/classic.lb.ListenerDefaultActionArgs.html",
    "#ListenerEndpoint": b + "/awsx/interfaces/classic.lb.ListenerEndpoint.html",
    "#ListenerRule": b + "/awsx/classes/classic.lb.ListenerRule.html",
    "#ListenerRuleArgs": b + "/awsx/interfaces/classic.lb.ListenerRuleArgs.html",
    "#LoadBalancer": b + "/awsx/classes/classic.lb.LoadBalancer.html",
    "#LoadBalancerArgs": b + "/awsx/interfaces/classic.lb.LoadBalancerArgs.html",
    "#LoadBalancerSubnets": b + "/awsx/interfaces/classic.lb.LoadBalancerSubnets.html",
    "#LoadBalancerTarget": b + "/awsx/types/classic.lb.LoadBalancerTarget.html",
    "#LoadBalancerTargetInfo": b + "/awsx/interfaces/classic.lb.LoadBalancerTargetInfo.html",
    "#LoadBalancerTargetInfoProvider": b + "/awsx/interfaces/classic.lb.LoadBalancerTargetInfoProvider.html",
    "#metrics": b + "/awsx/modules/classic.lb.metrics.html",
    "#NetworkListener": b + "/awsx/classes/classic.lb.NetworkListener.html",
    "#NetworkListenerArgs": b + "/awsx/interfaces/classic.lb.NetworkListenerArgs.html",
    "#NetworkLoadBalancer": b + "/awsx/classes/classic.lb.NetworkLoadBalancer.html",
    "#NetworkLoadBalancerArgs": b + "/awsx/interfaces/classic.lb.NetworkLoadBalancerArgs.html",
    "#NetworkProtocol": b + "/awsx/types/classic.lb.NetworkProtocol.html",
    "#NetworkTargetGroup": b + "/awsx/classes/classic.lb.NetworkTargetGroup.html",
    "#NetworkTargetGroupArgs": b + "/awsx/interfaces/classic.lb.NetworkTargetGroupArgs.html",
    "#NetworkTargetGroupHealthCheck": b + "/awsx/interfaces/classic.lb.NetworkTargetGroupHealthCheck.html",
    "#TargetGroup": b + "/awsx/classes/classic.lb.TargetGroup.html",
    "#TargetGroupArgs": b + "/awsx/interfaces/classic.lb.TargetGroupArgs.html",
    "#TargetGroupAttachment": b + "/awsx/classes/classic.lb.TargetGroupAttachment.html",
    "#TargetGroupAttachmentArgs": b + "/awsx/interfaces/classic.lb.TargetGroupAttachmentArgs.html",
    "#TargetGroupHealthCheck": b + "/awsx/interfaces/classic.lb.TargetGroupHealthCheck.html",
    "#TargetType": b + "/awsx/types/classic.lb.TargetType.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.sqs.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.sqs.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.ecr.html") {
  var redirects = {
    "#buildAndPushImage": b + "/awsx/functions/classic.ecr.buildAndPushImage.html",
    "#LifecyclePolicy": b + "/awsx/classes/classic.ecr.LifecyclePolicy.html",
    "#LifecyclePolicyArgs": b + "/awsx/interfaces/classic.ecr.LifecyclePolicyArgs.html",
    "#LifecyclePolicyRule": b + "/awsx/interfaces/classic.ecr.LifecyclePolicyRule.html",
    "#Repository": b + "/awsx/classes/classic.ecr.Repository.html",
    "#RepositoryArgs": b + "/awsx/interfaces/classic.ecr.RepositoryArgs.html",
    "#RepositoryImage": b + "/awsx/classes/classic.ecr.RepositoryImage.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.codebuild.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.codebuild.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.rds.html") {
  var redirects = {
    "#metrics": b + "/awsx/modules/classic.rds.metrics.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/classic.cloudtrail.html") {
  var redirects = {
    "#Trail": b + "/awsx/classes/classic.cloudtrail.Trail.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/ec2.html") {
  var redirects = {
    "#DefaultVpc": b + "/awsx/types/ec2.DefaultVpc.html",
    "#DefaultVpcArgs": b + "/awsx/interfaces/ec2.DefaultVpcArgs.html",
    "#getDefaultVpc": b + "/awsx/functions/ec2.getDefaultVpc.html",
    "#GetDefaultVpcArgs": b + "/awsx/interfaces/ec2.GetDefaultVpcArgs.html",
    "#getDefaultVpcOutput": b + "/awsx/functions/ec2.getDefaultVpcOutput.html",
    "#GetDefaultVpcResult": b + "/awsx/interfaces/ec2.GetDefaultVpcResult.html",
    "#Vpc": b + "/awsx/types/ec2.Vpc.html",
    "#VpcArgs": b + "/awsx/interfaces/ec2.VpcArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/lb.html") {
  var redirects = {
    "#ApplicationLoadBalancer": b + "/awsx/types/lb.ApplicationLoadBalancer.html",
    "#ApplicationLoadBalancerArgs": b + "/awsx/interfaces/lb.ApplicationLoadBalancerArgs.html",
    "#NetworkLoadBalancer": b + "/awsx/types/lb.NetworkLoadBalancer.html",
    "#NetworkLoadBalancerArgs": b + "/awsx/interfaces/lb.NetworkLoadBalancerArgs.html",
    "#TargetGroupAttachment": b + "/awsx/types/lb.TargetGroupAttachment.html",
    "#TargetGroupAttachmentArgs": b + "/awsx/interfaces/lb.TargetGroupAttachmentArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/cloudtrail.html") {
  var redirects = {
    "#Trail": b + "/awsx/types/cloudtrail.Trail.html",
    "#TrailArgs": b + "/awsx/interfaces/cloudtrail.TrailArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/types.output.html") {
  var redirects = {
    "#awsx": b + "/awsx/modules/types.output.awsx.html",
    "#cloudtrail": b + "/awsx/modules/types.output.cloudtrail.html",
    "#ec2": b + "/awsx/modules/types.output.ec2.html",
    "#ecr": b + "/awsx/modules/types.output.ecr.html",
    "#ecs": b + "/awsx/modules/types.output.ecs.html",
    "#lb": b + "/awsx/modules/types.output.lb.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/types.input.html") {
  var redirects = {
    "#awsx": b + "/awsx/modules/types.input.awsx.html",
    "#cloudtrail": b + "/awsx/modules/types.input.cloudtrail.html",
    "#ec2": b + "/awsx/modules/types.input.ec2.html",
    "#ecr": b + "/awsx/modules/types.input.ecr.html",
    "#ecs": b + "/awsx/modules/types.input.ecs.html",
    "#lb": b + "/awsx/modules/types.input.lb.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/ecr.html") {
  var redirects = {
    "#Image": b + "/awsx/types/ecr.Image.html",
    "#ImageArgs": b + "/awsx/interfaces/ecr.ImageArgs.html",
    "#Repository": b + "/awsx/types/ecr.Repository.html",
    "#RepositoryArgs": b + "/awsx/interfaces/ecr.RepositoryArgs.html",
  };
  redirect = redirects[location.hash];
}
if (pathname == b + "/awsx/modules/ecs.html") {
  var redirects = {
    "#EC2Service": b + "/awsx/types/ecs.EC2Service.html",
    "#EC2ServiceArgs": b + "/awsx/interfaces/ecs.EC2ServiceArgs.html",
    "#EC2TaskDefinition": b + "/awsx/types/ecs.EC2TaskDefinition.html",
    "#EC2TaskDefinitionArgs": b + "/awsx/interfaces/ecs.EC2TaskDefinitionArgs.html",
    "#FargateService": b + "/awsx/types/ecs.FargateService.html",
    "#FargateServiceArgs": b + "/awsx/interfaces/ecs.FargateServiceArgs.html",
    "#FargateTaskDefinition": b + "/awsx/types/ecs.FargateTaskDefinition.html",
    "#FargateTaskDefinitionArgs": b + "/awsx/interfaces/ecs.FargateTaskDefinitionArgs.html",
  };
  redirect = redirects[location.hash];
}
// Kubernetesx
if (pathname == b + "/kubernetesx") {
  var redirects = {
    "#ConfigMap": b + "/kubernetesx/classes/ConfigMap.html",
    "#Deployment": b + "/kubernetesx/classes/Deployment.html",
    "#Job": b + "/kubernetesx/classes/Job.html",
    "#PersistentVolumeClaim": b + "/kubernetesx/classes/PersistentVolumeClaim.html",
    "#Pod": b + "/kubernetesx/classes/Pod.html",
    "#PodBuilder": b + "/kubernetesx/classes/PodBuilder.html",
    "#Secret": b + "/kubernetesx/classes/Secret.html",
    "#Service": b + "/kubernetesx/classes/Service.html",
    "#StatefulSet": b + "/kubernetesx/classes/StatefulSet.html",
    "#types": b + "/kubernetesx/modules/types.html",
  };
  redirect = redirects[location.hash];
}
// Cloud
if (pathname == b + "/cloud") {
  var redirects = {
    "#Action": b + "/cloud/types/timer.Action.html",
    "#API": b + "/cloud/interfaces/API.html",
    "#APIConstructor": b + "/cloud/interfaces/APIConstructor.html",
    "#Bucket": b + "/cloud/interfaces/Bucket.html",
    "#BucketConstructor": b + "/cloud/interfaces/BucketConstructor.html",
    "#BucketFilter": b + "/cloud/interfaces/BucketFilter.html",
    "#BucketHandler": b + "/cloud/types/BucketHandler.html",
    "#BucketHandlerArgs": b + "/cloud/interfaces/BucketHandlerArgs.html",
    "#CacheFrom": b + "/cloud/interfaces/CacheFrom.html",
    "#Container": b + "/cloud/interfaces/Container.html",
    "#ContainerBuild": b + "/cloud/interfaces/ContainerBuild.html",
    "#ContainerPort": b + "/cloud/interfaces/ContainerPort.html",
    "#ContainerProtocol": b + "/cloud/types/ContainerProtocol.html",
    "#Containers": b + "/cloud/interfaces/Containers.html",
    "#ContainerVolumeMount": b + "/cloud/interfaces/ContainerVolumeMount.html",
    "#cron": b + "/cloud/functions/timer.cron.html",
    "#daily": b + "/cloud/functions/timer.daily.html",
    "#DailySchedule": b + "/cloud/interfaces/timer.DailySchedule.html",
    "#Domain": b + "/cloud/interfaces/Domain.html",
    "#Endpoint": b + "/cloud/interfaces/Endpoint.html",
    "#Endpoints": b + "/cloud/interfaces/Endpoints.html",
    "#HostOperatingSystem": b + "/cloud/types/HostOperatingSystem.html",
    "#HostPathVolume": b + "/cloud/interfaces/HostPathVolume.html",
    "#HostPathVolumeConstructor": b + "/cloud/interfaces/HostPathVolumeConstructor.html",
    "#HostProperties": b + "/cloud/interfaces/HostProperties.html",
    "#hourly": b + "/cloud/functions/timer.hourly.html",
    "#HourlySchedule": b + "/cloud/interfaces/timer.HourlySchedule.html",
    "#HttpDeployment": b + "/cloud/interfaces/HttpDeployment.html",
    "#HttpEndpoint": b + "/cloud/types/HttpEndpoint.html",
    "#interval": b + "/cloud/functions/timer.interval.html",
    "#IntervalRate": b + "/cloud/interfaces/timer.IntervalRate.html",
    "#PrimaryKeyType": b + "/cloud/types/PrimaryKeyType.html",
    "#Request": b + "/cloud/interfaces/Request.html",
    "#Response": b + "/cloud/interfaces/Response.html",
    "#RouteHandler": b + "/cloud/types/RouteHandler.html",
    "#ServeStaticOptions": b + "/cloud/interfaces/ServeStaticOptions.html",
    "#Service": b + "/cloud/interfaces/Service.html",
    "#ServiceArguments": b + "/cloud/interfaces/ServiceArguments.html",
    "#ServiceConstructor": b + "/cloud/interfaces/ServiceConstructor.html",
    "#SharedVolume": b + "/cloud/interfaces/SharedVolume.html",
    "#SharedVolumeConstructor": b + "/cloud/interfaces/SharedVolumeConstructor.html",
    "#Stream": b + "/cloud/interfaces/Stream.html",
    "#Table": b + "/cloud/interfaces/Table.html",
    "#TableConstructor": b + "/cloud/interfaces/TableConstructor.html",
    "#Task": b + "/cloud/interfaces/Task.html",
    "#TaskConstructor": b + "/cloud/interfaces/TaskConstructor.html",
    "#TaskRunOptions": b + "/cloud/interfaces/TaskRunOptions.html",
    "#Topic": b + "/cloud/interfaces/Topic.html",
    "#TopicConstructor": b + "/cloud/interfaces/TopicConstructor.html",
    "#Volume": b + "/cloud/types/Volume.html",
    "#VolumeKind": b + "/cloud/types/VolumeKind.html",
  };
  redirect = redirects[location.hash];
}

if (redirect) {
  location.href = redirect;
}
