---
title: Module ec2
---

<a href="../index.html">@pulumi/aws</a> &gt; ec2

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Ami">class Ami</a>
* <a href="#AmiCopy">class AmiCopy</a>
* <a href="#AmiFromInstance">class AmiFromInstance</a>
* <a href="#AmiLaunchPermission">class AmiLaunchPermission</a>
* <a href="#CustomerGateway">class CustomerGateway</a>
* <a href="#DefaultNetworkAcl">class DefaultNetworkAcl</a>
* <a href="#DefaultRouteTable">class DefaultRouteTable</a>
* <a href="#DefaultSecurityGroup">class DefaultSecurityGroup</a>
* <a href="#DefaultSubnet">class DefaultSubnet</a>
* <a href="#DefaultVpc">class DefaultVpc</a>
* <a href="#DefaultVpcDhcpOptions">class DefaultVpcDhcpOptions</a>
* <a href="#EgressOnlyInternetGateway">class EgressOnlyInternetGateway</a>
* <a href="#Eip">class Eip</a>
* <a href="#EipAssociation">class EipAssociation</a>
* <a href="#FlowLog">class FlowLog</a>
* <a href="#Instance">class Instance</a>
* <a href="#InternetGateway">class InternetGateway</a>
* <a href="#KeyPair">class KeyPair</a>
* <a href="#LaunchConfiguration">class LaunchConfiguration</a>
* <a href="#LaunchTemplate">class LaunchTemplate</a>
* <a href="#MainRouteTableAssociation">class MainRouteTableAssociation</a>
* <a href="#NatGateway">class NatGateway</a>
* <a href="#NetworkAcl">class NetworkAcl</a>
* <a href="#NetworkAclRule">class NetworkAclRule</a>
* <a href="#NetworkInterface">class NetworkInterface</a>
* <a href="#NetworkInterfaceAttachment">class NetworkInterfaceAttachment</a>
* <a href="#NetworkInterfaceSecurityGroupAttachment">class NetworkInterfaceSecurityGroupAttachment</a>
* <a href="#PeeringConnectionOptions">class PeeringConnectionOptions</a>
* <a href="#PlacementGroup">class PlacementGroup</a>
* <a href="#ProxyProtocolPolicy">class ProxyProtocolPolicy</a>
* <a href="#Route">class Route</a>
* <a href="#RouteTable">class RouteTable</a>
* <a href="#RouteTableAssociation">class RouteTableAssociation</a>
* <a href="#SecurityGroup">class SecurityGroup</a>
* <a href="#SecurityGroupRule">class SecurityGroupRule</a>
* <a href="#SnapshotCreateVolumePermission">class SnapshotCreateVolumePermission</a>
* <a href="#SpotDatafeedSubscription">class SpotDatafeedSubscription</a>
* <a href="#SpotFleetRequest">class SpotFleetRequest</a>
* <a href="#SpotInstanceRequest">class SpotInstanceRequest</a>
* <a href="#Subnet">class Subnet</a>
* <a href="#VolumeAttachment">class VolumeAttachment</a>
* <a href="#Vpc">class Vpc</a>
* <a href="#VpcDhcpOptions">class VpcDhcpOptions</a>
* <a href="#VpcDhcpOptionsAssociation">class VpcDhcpOptionsAssociation</a>
* <a href="#VpcEndpoint">class VpcEndpoint</a>
* <a href="#VpcEndpointConnectionNotification">class VpcEndpointConnectionNotification</a>
* <a href="#VpcEndpointRouteTableAssociation">class VpcEndpointRouteTableAssociation</a>
* <a href="#VpcEndpointService">class VpcEndpointService</a>
* <a href="#VpcEndpointServiceAllowedPrinciple">class VpcEndpointServiceAllowedPrinciple</a>
* <a href="#VpcEndpointSubnetAssociation">class VpcEndpointSubnetAssociation</a>
* <a href="#VpcIpv4CidrBlockAssociation">class VpcIpv4CidrBlockAssociation</a>
* <a href="#VpcPeeringConnection">class VpcPeeringConnection</a>
* <a href="#VpcPeeringConnectionAccepter">class VpcPeeringConnectionAccepter</a>
* <a href="#VpnConnection">class VpnConnection</a>
* <a href="#VpnConnectionRoute">class VpnConnectionRoute</a>
* <a href="#VpnGateway">class VpnGateway</a>
* <a href="#VpnGatewayAttachment">class VpnGatewayAttachment</a>
* <a href="#VpnGatewayRoutePropagation">class VpnGatewayRoutePropagation</a>
* <a href="#getInstance">function getInstance</a>
* <a href="#getInstances">function getInstances</a>
* <a href="#getInternetGateway">function getInternetGateway</a>
* <a href="#getLaunchConfiguration">function getLaunchConfiguration</a>
* <a href="#getNatGateway">function getNatGateway</a>
* <a href="#getNetworkAcls">function getNetworkAcls</a>
* <a href="#getNetworkInterface">function getNetworkInterface</a>
* <a href="#getNetworkInterfaces">function getNetworkInterfaces</a>
* <a href="#getRoute">function getRoute</a>
* <a href="#getRouteTable">function getRouteTable</a>
* <a href="#getRouteTables">function getRouteTables</a>
* <a href="#getSecurityGroup">function getSecurityGroup</a>
* <a href="#getSecurityGroups">function getSecurityGroups</a>
* <a href="#getSubnet">function getSubnet</a>
* <a href="#getSubnetIds">function getSubnetIds</a>
* <a href="#getVpc">function getVpc</a>
* <a href="#getVpcDhcpOptions">function getVpcDhcpOptions</a>
* <a href="#getVpcEndpoint">function getVpcEndpoint</a>
* <a href="#getVpcEndpointService">function getVpcEndpointService</a>
* <a href="#getVpcPeeringConnection">function getVpcPeeringConnection</a>
* <a href="#getVpcs">function getVpcs</a>
* <a href="#getVpnGateway">function getVpnGateway</a>
* <a href="#AmiArgs">interface AmiArgs</a>
* <a href="#AmiCopyArgs">interface AmiCopyArgs</a>
* <a href="#AmiCopyState">interface AmiCopyState</a>
* <a href="#AmiFromInstanceArgs">interface AmiFromInstanceArgs</a>
* <a href="#AmiFromInstanceState">interface AmiFromInstanceState</a>
* <a href="#AmiLaunchPermissionArgs">interface AmiLaunchPermissionArgs</a>
* <a href="#AmiLaunchPermissionState">interface AmiLaunchPermissionState</a>
* <a href="#AmiState">interface AmiState</a>
* <a href="#CustomerGatewayArgs">interface CustomerGatewayArgs</a>
* <a href="#CustomerGatewayState">interface CustomerGatewayState</a>
* <a href="#DefaultNetworkAclArgs">interface DefaultNetworkAclArgs</a>
* <a href="#DefaultNetworkAclState">interface DefaultNetworkAclState</a>
* <a href="#DefaultRouteTableArgs">interface DefaultRouteTableArgs</a>
* <a href="#DefaultRouteTableState">interface DefaultRouteTableState</a>
* <a href="#DefaultSecurityGroupArgs">interface DefaultSecurityGroupArgs</a>
* <a href="#DefaultSecurityGroupState">interface DefaultSecurityGroupState</a>
* <a href="#DefaultSubnetArgs">interface DefaultSubnetArgs</a>
* <a href="#DefaultSubnetState">interface DefaultSubnetState</a>
* <a href="#DefaultVpcArgs">interface DefaultVpcArgs</a>
* <a href="#DefaultVpcDhcpOptionsArgs">interface DefaultVpcDhcpOptionsArgs</a>
* <a href="#DefaultVpcDhcpOptionsState">interface DefaultVpcDhcpOptionsState</a>
* <a href="#DefaultVpcState">interface DefaultVpcState</a>
* <a href="#EgressOnlyInternetGatewayArgs">interface EgressOnlyInternetGatewayArgs</a>
* <a href="#EgressOnlyInternetGatewayState">interface EgressOnlyInternetGatewayState</a>
* <a href="#EipArgs">interface EipArgs</a>
* <a href="#EipAssociationArgs">interface EipAssociationArgs</a>
* <a href="#EipAssociationState">interface EipAssociationState</a>
* <a href="#EipState">interface EipState</a>
* <a href="#FlowLogArgs">interface FlowLogArgs</a>
* <a href="#FlowLogState">interface FlowLogState</a>
* <a href="#GetInstanceArgs">interface GetInstanceArgs</a>
* <a href="#GetInstanceResult">interface GetInstanceResult</a>
* <a href="#GetInstancesArgs">interface GetInstancesArgs</a>
* <a href="#GetInstancesResult">interface GetInstancesResult</a>
* <a href="#GetInternetGatewayArgs">interface GetInternetGatewayArgs</a>
* <a href="#GetInternetGatewayResult">interface GetInternetGatewayResult</a>
* <a href="#GetLaunchConfigurationArgs">interface GetLaunchConfigurationArgs</a>
* <a href="#GetLaunchConfigurationResult">interface GetLaunchConfigurationResult</a>
* <a href="#GetNatGatewayArgs">interface GetNatGatewayArgs</a>
* <a href="#GetNatGatewayResult">interface GetNatGatewayResult</a>
* <a href="#GetNetworkAclsArgs">interface GetNetworkAclsArgs</a>
* <a href="#GetNetworkAclsResult">interface GetNetworkAclsResult</a>
* <a href="#GetNetworkInterfaceArgs">interface GetNetworkInterfaceArgs</a>
* <a href="#GetNetworkInterfaceResult">interface GetNetworkInterfaceResult</a>
* <a href="#GetNetworkInterfacesArgs">interface GetNetworkInterfacesArgs</a>
* <a href="#GetNetworkInterfacesResult">interface GetNetworkInterfacesResult</a>
* <a href="#GetRouteArgs">interface GetRouteArgs</a>
* <a href="#GetRouteResult">interface GetRouteResult</a>
* <a href="#GetRouteTableArgs">interface GetRouteTableArgs</a>
* <a href="#GetRouteTableResult">interface GetRouteTableResult</a>
* <a href="#GetRouteTablesArgs">interface GetRouteTablesArgs</a>
* <a href="#GetRouteTablesResult">interface GetRouteTablesResult</a>
* <a href="#GetSecurityGroupArgs">interface GetSecurityGroupArgs</a>
* <a href="#GetSecurityGroupResult">interface GetSecurityGroupResult</a>
* <a href="#GetSecurityGroupsArgs">interface GetSecurityGroupsArgs</a>
* <a href="#GetSecurityGroupsResult">interface GetSecurityGroupsResult</a>
* <a href="#GetSubnetArgs">interface GetSubnetArgs</a>
* <a href="#GetSubnetIdsArgs">interface GetSubnetIdsArgs</a>
* <a href="#GetSubnetIdsResult">interface GetSubnetIdsResult</a>
* <a href="#GetSubnetResult">interface GetSubnetResult</a>
* <a href="#GetVpcArgs">interface GetVpcArgs</a>
* <a href="#GetVpcDhcpOptionsArgs">interface GetVpcDhcpOptionsArgs</a>
* <a href="#GetVpcDhcpOptionsResult">interface GetVpcDhcpOptionsResult</a>
* <a href="#GetVpcEndpointArgs">interface GetVpcEndpointArgs</a>
* <a href="#GetVpcEndpointResult">interface GetVpcEndpointResult</a>
* <a href="#GetVpcEndpointServiceArgs">interface GetVpcEndpointServiceArgs</a>
* <a href="#GetVpcEndpointServiceResult">interface GetVpcEndpointServiceResult</a>
* <a href="#GetVpcPeeringConnectionArgs">interface GetVpcPeeringConnectionArgs</a>
* <a href="#GetVpcPeeringConnectionResult">interface GetVpcPeeringConnectionResult</a>
* <a href="#GetVpcResult">interface GetVpcResult</a>
* <a href="#GetVpcsArgs">interface GetVpcsArgs</a>
* <a href="#GetVpcsResult">interface GetVpcsResult</a>
* <a href="#GetVpnGatewayArgs">interface GetVpnGatewayArgs</a>
* <a href="#GetVpnGatewayResult">interface GetVpnGatewayResult</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#InternetGatewayArgs">interface InternetGatewayArgs</a>
* <a href="#InternetGatewayState">interface InternetGatewayState</a>
* <a href="#KeyPairArgs">interface KeyPairArgs</a>
* <a href="#KeyPairState">interface KeyPairState</a>
* <a href="#LaunchConfigurationArgs">interface LaunchConfigurationArgs</a>
* <a href="#LaunchConfigurationState">interface LaunchConfigurationState</a>
* <a href="#LaunchTemplateArgs">interface LaunchTemplateArgs</a>
* <a href="#LaunchTemplateState">interface LaunchTemplateState</a>
* <a href="#MainRouteTableAssociationArgs">interface MainRouteTableAssociationArgs</a>
* <a href="#MainRouteTableAssociationState">interface MainRouteTableAssociationState</a>
* <a href="#NatGatewayArgs">interface NatGatewayArgs</a>
* <a href="#NatGatewayState">interface NatGatewayState</a>
* <a href="#NetworkAclArgs">interface NetworkAclArgs</a>
* <a href="#NetworkAclRuleArgs">interface NetworkAclRuleArgs</a>
* <a href="#NetworkAclRuleState">interface NetworkAclRuleState</a>
* <a href="#NetworkAclState">interface NetworkAclState</a>
* <a href="#NetworkInterfaceArgs">interface NetworkInterfaceArgs</a>
* <a href="#NetworkInterfaceAttachmentArgs">interface NetworkInterfaceAttachmentArgs</a>
* <a href="#NetworkInterfaceAttachmentState">interface NetworkInterfaceAttachmentState</a>
* <a href="#NetworkInterfaceSecurityGroupAttachmentArgs">interface NetworkInterfaceSecurityGroupAttachmentArgs</a>
* <a href="#NetworkInterfaceSecurityGroupAttachmentState">interface NetworkInterfaceSecurityGroupAttachmentState</a>
* <a href="#NetworkInterfaceState">interface NetworkInterfaceState</a>
* <a href="#PeeringConnectionOptionsArgs">interface PeeringConnectionOptionsArgs</a>
* <a href="#PeeringConnectionOptionsState">interface PeeringConnectionOptionsState</a>
* <a href="#PlacementGroupArgs">interface PlacementGroupArgs</a>
* <a href="#PlacementGroupState">interface PlacementGroupState</a>
* <a href="#ProxyProtocolPolicyArgs">interface ProxyProtocolPolicyArgs</a>
* <a href="#ProxyProtocolPolicyState">interface ProxyProtocolPolicyState</a>
* <a href="#RouteArgs">interface RouteArgs</a>
* <a href="#RouteState">interface RouteState</a>
* <a href="#RouteTableArgs">interface RouteTableArgs</a>
* <a href="#RouteTableAssociationArgs">interface RouteTableAssociationArgs</a>
* <a href="#RouteTableAssociationState">interface RouteTableAssociationState</a>
* <a href="#RouteTableState">interface RouteTableState</a>
* <a href="#SecurityGroupArgs">interface SecurityGroupArgs</a>
* <a href="#SecurityGroupRuleArgs">interface SecurityGroupRuleArgs</a>
* <a href="#SecurityGroupRuleState">interface SecurityGroupRuleState</a>
* <a href="#SecurityGroupState">interface SecurityGroupState</a>
* <a href="#SnapshotCreateVolumePermissionArgs">interface SnapshotCreateVolumePermissionArgs</a>
* <a href="#SnapshotCreateVolumePermissionState">interface SnapshotCreateVolumePermissionState</a>
* <a href="#SpotDatafeedSubscriptionArgs">interface SpotDatafeedSubscriptionArgs</a>
* <a href="#SpotDatafeedSubscriptionState">interface SpotDatafeedSubscriptionState</a>
* <a href="#SpotFleetRequestArgs">interface SpotFleetRequestArgs</a>
* <a href="#SpotFleetRequestState">interface SpotFleetRequestState</a>
* <a href="#SpotInstanceRequestArgs">interface SpotInstanceRequestArgs</a>
* <a href="#SpotInstanceRequestState">interface SpotInstanceRequestState</a>
* <a href="#SubnetArgs">interface SubnetArgs</a>
* <a href="#SubnetState">interface SubnetState</a>
* <a href="#VolumeAttachmentArgs">interface VolumeAttachmentArgs</a>
* <a href="#VolumeAttachmentState">interface VolumeAttachmentState</a>
* <a href="#VpcArgs">interface VpcArgs</a>
* <a href="#VpcDhcpOptionsArgs">interface VpcDhcpOptionsArgs</a>
* <a href="#VpcDhcpOptionsAssociationArgs">interface VpcDhcpOptionsAssociationArgs</a>
* <a href="#VpcDhcpOptionsAssociationState">interface VpcDhcpOptionsAssociationState</a>
* <a href="#VpcDhcpOptionsState">interface VpcDhcpOptionsState</a>
* <a href="#VpcEndpointArgs">interface VpcEndpointArgs</a>
* <a href="#VpcEndpointConnectionNotificationArgs">interface VpcEndpointConnectionNotificationArgs</a>
* <a href="#VpcEndpointConnectionNotificationState">interface VpcEndpointConnectionNotificationState</a>
* <a href="#VpcEndpointRouteTableAssociationArgs">interface VpcEndpointRouteTableAssociationArgs</a>
* <a href="#VpcEndpointRouteTableAssociationState">interface VpcEndpointRouteTableAssociationState</a>
* <a href="#VpcEndpointServiceAllowedPrincipleArgs">interface VpcEndpointServiceAllowedPrincipleArgs</a>
* <a href="#VpcEndpointServiceAllowedPrincipleState">interface VpcEndpointServiceAllowedPrincipleState</a>
* <a href="#VpcEndpointServiceArgs">interface VpcEndpointServiceArgs</a>
* <a href="#VpcEndpointServiceState">interface VpcEndpointServiceState</a>
* <a href="#VpcEndpointState">interface VpcEndpointState</a>
* <a href="#VpcEndpointSubnetAssociationArgs">interface VpcEndpointSubnetAssociationArgs</a>
* <a href="#VpcEndpointSubnetAssociationState">interface VpcEndpointSubnetAssociationState</a>
* <a href="#VpcIpv4CidrBlockAssociationArgs">interface VpcIpv4CidrBlockAssociationArgs</a>
* <a href="#VpcIpv4CidrBlockAssociationState">interface VpcIpv4CidrBlockAssociationState</a>
* <a href="#VpcPeeringConnectionAccepterArgs">interface VpcPeeringConnectionAccepterArgs</a>
* <a href="#VpcPeeringConnectionAccepterState">interface VpcPeeringConnectionAccepterState</a>
* <a href="#VpcPeeringConnectionArgs">interface VpcPeeringConnectionArgs</a>
* <a href="#VpcPeeringConnectionState">interface VpcPeeringConnectionState</a>
* <a href="#VpcState">interface VpcState</a>
* <a href="#VpnConnectionArgs">interface VpnConnectionArgs</a>
* <a href="#VpnConnectionRouteArgs">interface VpnConnectionRouteArgs</a>
* <a href="#VpnConnectionRouteState">interface VpnConnectionRouteState</a>
* <a href="#VpnConnectionState">interface VpnConnectionState</a>
* <a href="#VpnGatewayArgs">interface VpnGatewayArgs</a>
* <a href="#VpnGatewayAttachmentArgs">interface VpnGatewayAttachmentArgs</a>
* <a href="#VpnGatewayAttachmentState">interface VpnGatewayAttachmentState</a>
* <a href="#VpnGatewayRoutePropagationArgs">interface VpnGatewayRoutePropagationArgs</a>
* <a href="#VpnGatewayRoutePropagationState">interface VpnGatewayRoutePropagationState</a>
* <a href="#VpnGatewayState">interface VpnGatewayState</a>
* <a href="#C3Instance2XLarge">let C3Instance2XLarge</a>
* <a href="#C3Instance4XLarge">let C3Instance4XLarge</a>
* <a href="#C3Instance8XLarge">let C3Instance8XLarge</a>
* <a href="#C3InstanceLarge">let C3InstanceLarge</a>
* <a href="#C3InstanceXLarge">let C3InstanceXLarge</a>
* <a href="#C4Instance2XLarge">let C4Instance2XLarge</a>
* <a href="#C4Instance4XLarge">let C4Instance4XLarge</a>
* <a href="#C4Instance8XLarge">let C4Instance8XLarge</a>
* <a href="#C4InstanceLarge">let C4InstanceLarge</a>
* <a href="#C4InstanceXLarge">let C4InstanceXLarge</a>
* <a href="#D2Instance2XLarge">let D2Instance2XLarge</a>
* <a href="#D2Instance4XLarge">let D2Instance4XLarge</a>
* <a href="#D2Instance8XLarge">let D2Instance8XLarge</a>
* <a href="#D2InstanceXLarge">let D2InstanceXLarge</a>
* <a href="#F1Instance16XLarge">let F1Instance16XLarge</a>
* <a href="#F1Instance2XLarge">let F1Instance2XLarge</a>
* <a href="#G2Instance2XLarge">let G2Instance2XLarge</a>
* <a href="#G2Instance8XLarge">let G2Instance8XLarge</a>
* <a href="#I3Instance16XLarge">let I3Instance16XLarge</a>
* <a href="#I3Instance2XLarge">let I3Instance2XLarge</a>
* <a href="#I3Instance4XLarge">let I3Instance4XLarge</a>
* <a href="#I3Instance8XLarge">let I3Instance8XLarge</a>
* <a href="#I3InstanceLarge">let I3InstanceLarge</a>
* <a href="#I3InstanceXLarge">let I3InstanceXLarge</a>
* <a href="#M3Instance2XLarge">let M3Instance2XLarge</a>
* <a href="#M3InstanceLarge">let M3InstanceLarge</a>
* <a href="#M3InstanceMedium">let M3InstanceMedium</a>
* <a href="#M3InstanceXLarge">let M3InstanceXLarge</a>
* <a href="#M4Instance10XLarge">let M4Instance10XLarge</a>
* <a href="#M4Instance16XLarge">let M4Instance16XLarge</a>
* <a href="#M4Instance2XLarge">let M4Instance2XLarge</a>
* <a href="#M4Instance4XLarge">let M4Instance4XLarge</a>
* <a href="#M4InstanceLarge">let M4InstanceLarge</a>
* <a href="#M4InstanceXLarge">let M4InstanceXLarge</a>
* <a href="#P2Instance16XLarge">let P2Instance16XLarge</a>
* <a href="#P2Instance8XLarge">let P2Instance8XLarge</a>
* <a href="#P2InstanceXLarge">let P2InstanceXLarge</a>
* <a href="#R3Instance2XLarge">let R3Instance2XLarge</a>
* <a href="#R3Instance4XLarge">let R3Instance4XLarge</a>
* <a href="#R3Instance8XLarge">let R3Instance8XLarge</a>
* <a href="#R3InstanceLarge">let R3InstanceLarge</a>
* <a href="#R3InstanceXLarge">let R3InstanceXLarge</a>
* <a href="#R4Instance16XLarge">let R4Instance16XLarge</a>
* <a href="#R4Instance2XLarge">let R4Instance2XLarge</a>
* <a href="#R4Instance4XLarge">let R4Instance4XLarge</a>
* <a href="#R4Instance8XLarge">let R4Instance8XLarge</a>
* <a href="#R4InstanceLarge">let R4InstanceLarge</a>
* <a href="#R4InstanceXLarge">let R4InstanceXLarge</a>
* <a href="#T2Instance2XLarge">let T2Instance2XLarge</a>
* <a href="#T2InstanceLarge">let T2InstanceLarge</a>
* <a href="#T2InstanceMedium">let T2InstanceMedium</a>
* <a href="#T2InstanceMicro">let T2InstanceMicro</a>
* <a href="#T2InstanceNano">let T2InstanceNano</a>
* <a href="#T2InstanceSmall">let T2InstanceSmall</a>
* <a href="#T2InstanceXLarge">let T2InstanceXLarge</a>
* <a href="#X1Instance16XLarge">let X1Instance16XLarge</a>
* <a href="#X1Instance32XLarge">let X1Instance32XLarge</a>
* <a href="#InstanceType">type InstanceType</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts">ec2/ami.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts">ec2/amiCopy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts">ec2/amiFromInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts">ec2/amiLaunchPermission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts">ec2/customerGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts">ec2/defaultNetworkAcl.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts">ec2/defaultRouteTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts">ec2/defaultSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts">ec2/defaultSubnet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts">ec2/defaultVpc.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts">ec2/defaultVpcDhcpOptions.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts">ec2/egressOnlyInternetGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts">ec2/eip.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts">ec2/eipAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts">ec2/flowLog.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts">ec2/getInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts">ec2/getInstances.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts">ec2/getInternetGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts">ec2/getLaunchConfiguration.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts">ec2/getNatGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts">ec2/getNetworkAcls.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts">ec2/getNetworkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts">ec2/getNetworkInterfaces.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts">ec2/getRoute.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts">ec2/getRouteTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts">ec2/getRouteTables.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts">ec2/getSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts">ec2/getSecurityGroups.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts">ec2/getSubnet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts">ec2/getSubnetIds.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts">ec2/getVpc.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts">ec2/getVpcDhcpOptions.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts">ec2/getVpcEndpoint.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts">ec2/getVpcEndpointService.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts">ec2/getVpcPeeringConnection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts">ec2/getVpcs.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts">ec2/getVpnGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts">ec2/instance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts">ec2/instanceType.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts">ec2/internetGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts">ec2/keyPair.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts">ec2/launchConfiguration.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts">ec2/launchTemplate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts">ec2/mainRouteTableAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts">ec2/natGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts">ec2/networkAcl.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts">ec2/networkAclRule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts">ec2/networkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts">ec2/networkInterfaceAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts">ec2/networkInterfaceSecurityGroupAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts">ec2/peeringConnectionOptions.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts">ec2/placementGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts">ec2/proxyProtocolPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts">ec2/route.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts">ec2/routeTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts">ec2/routeTableAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts">ec2/securityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts">ec2/securityGroupRule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts">ec2/snapshotCreateVolumePermission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts">ec2/spotDatafeedSubscription.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts">ec2/spotFleetRequest.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts">ec2/spotInstanceRequest.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts">ec2/subnet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts">ec2/volumeAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts">ec2/vpc.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts">ec2/vpcDhcpOptions.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts">ec2/vpcDhcpOptionsAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts">ec2/vpcEndpoint.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts">ec2/vpcEndpointConnectionNotification.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts">ec2/vpcEndpointRouteTableAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts">ec2/vpcEndpointService.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts">ec2/vpcEndpointServiceAllowedPrinciple.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts">ec2/vpcEndpointSubnetAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts">ec2/vpcIpv4CidrBlockAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts">ec2/vpcPeeringConnection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts">ec2/vpcPeeringConnectionAccepter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts">ec2/vpnConnection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts">ec2/vpnConnectionRoute.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts">ec2/vpnGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts">ec2/vpnGatewayAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts">ec2/vpnGatewayRoutePropagation.ts</a> 


<h2 class="pdoc-module-header" id="Ami">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L17">class Ami</a>
</h2>

The AMI resource allows the creation and management of a completely-custom
*Amazon Machine Image* (AMI).

If you just want to duplicate an existing AMI, possibly copying it to another
region, it's better to use `aws_ami_copy` instead.

If you just want to share an existing AMI with another AWS account,
it's better to use `aws_ami_launch_permission` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L91">constructor</a>
</h3>

```typescript
new Ami(name: string, args?: AmiArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Ami resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AmiState): Ami
```


Get an existing Ami resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L33">property architecture</a>
</h3>

```typescript
public architecture: pulumi.Output<string | undefined>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L42">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L46">property enaSupport</a>
</h3>

```typescript
public enaSupport: pulumi.Output<boolean | undefined>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L51">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L56">property imageLocation</a>
</h3>

```typescript
public imageLocation: pulumi.Output<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L61">property kernelId</a>
</h3>

```typescript
public kernelId: pulumi.Output<string | undefined>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L62">property manageEbsSnapshots</a>
</h3>

```typescript
public manageEbsSnapshots: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L66">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L71">property ramdiskId</a>
</h3>

```typescript
public ramdiskId: pulumi.Output<string | undefined>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L75">property rootDeviceName</a>
</h3>

```typescript
public rootDeviceName: pulumi.Output<string | undefined>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L79">property rootSnapshotId</a>
</h3>

```typescript
public rootSnapshotId: pulumi.Output<string>;
```


The Snapshot ID for the root volume (for EBS-backed AMIs)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L84">property sriovNetSupport</a>
</h3>

```typescript
public sriovNetSupport: pulumi.Output<string | undefined>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L85">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L91">property virtualizationType</a>
</h3>

```typescript
public virtualizationType: pulumi.Output<string | undefined>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiCopy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L22">class AmiCopy</a>
</h2>

The "AMI copy" resource allows duplication of an Amazon Machine Image (AMI),
including cross-region copies.

If the source AMI has associated EBS snapshots, those will also be duplicated
along with the AMI.

This is useful for taking a single AMI provisioned in one region and making
it available in another for a multi-region deployment.

Copying an AMI can take several minutes. The creation of this resource will
block until the new AMI is available for use on new instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L111">constructor</a>
</h3>

```typescript
new AmiCopy(name: string, args: AmiCopyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AmiCopy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AmiCopyState): AmiCopy
```


Get an existing AmiCopy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L38">property architecture</a>
</h3>

```typescript
public architecture: pulumi.Output<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L47">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L51">property enaSupport</a>
</h3>

```typescript
public enaSupport: pulumi.Output<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L55">property encrypted</a>
</h3>

```typescript
public encrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L60">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L65">property imageLocation</a>
</h3>

```typescript
public imageLocation: pulumi.Output<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L70">property kernelId</a>
</h3>

```typescript
public kernelId: pulumi.Output<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L74">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L75">property manageEbsSnapshots</a>
</h3>

```typescript
public manageEbsSnapshots: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L79">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L84">property ramdiskId</a>
</h3>

```typescript
public ramdiskId: pulumi.Output<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L88">property rootDeviceName</a>
</h3>

```typescript
public rootDeviceName: pulumi.Output<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L89">property rootSnapshotId</a>
</h3>

```typescript
public rootSnapshotId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L94">property sourceAmiId</a>
</h3>

```typescript
public sourceAmiId: pulumi.Output<string>;
```


The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L99">property sourceAmiRegion</a>
</h3>

```typescript
public sourceAmiRegion: pulumi.Output<string>;
```


The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L104">property sriovNetSupport</a>
</h3>

```typescript
public sriovNetSupport: pulumi.Output<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L105">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L111">property virtualizationType</a>
</h3>

```typescript
public virtualizationType: pulumi.Output<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiFromInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L26">class AmiFromInstance</a>
</h2>

The "AMI from instance" resource allows the creation of an Amazon Machine
Image (AMI) modelled after an existing EBS-backed EC2 instance.

The created AMI will refer to implicitly-created snapshots of the instance's
EBS volumes and mimick its assigned block device configuration at the time
the resource is created.

This resource is best applied to an instance that is stopped when this instance
is created, so that the contents of the created image are predictable. When
applied to an instance that is running, *the instance will be stopped before taking
the snapshots and then started back up again*, resulting in a period of
downtime.

Note that the source instance is inspected only at the initial creation of this
resource. Ongoing updates to the referenced instance will not be propagated into
the generated AMI. Users may taint or otherwise recreate the resource in order
to produce a fresh snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L108">constructor</a>
</h3>

```typescript
new AmiFromInstance(name: string, args: AmiFromInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AmiFromInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L35">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AmiFromInstanceState): AmiFromInstance
```


Get an existing AmiFromInstance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L42">property architecture</a>
</h3>

```typescript
public architecture: pulumi.Output<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L46">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L51">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L55">property enaSupport</a>
</h3>

```typescript
public enaSupport: pulumi.Output<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L60">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L65">property imageLocation</a>
</h3>

```typescript
public imageLocation: pulumi.Output<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L70">property kernelId</a>
</h3>

```typescript
public kernelId: pulumi.Output<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L71">property manageEbsSnapshots</a>
</h3>

```typescript
public manageEbsSnapshots: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L80">property ramdiskId</a>
</h3>

```typescript
public ramdiskId: pulumi.Output<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L84">property rootDeviceName</a>
</h3>

```typescript
public rootDeviceName: pulumi.Output<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L85">property rootSnapshotId</a>
</h3>

```typescript
public rootSnapshotId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L92">property snapshotWithoutReboot</a>
</h3>

```typescript
public snapshotWithoutReboot: pulumi.Output<boolean | undefined>;
```


Boolean that overrides the behavior of stopping
the instance before snapshotting. This is risky since it may cause a snapshot of an
inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
guarantees that no filesystem writes will be underway at the time of snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L96">property sourceInstanceId</a>
</h3>

```typescript
public sourceInstanceId: pulumi.Output<string>;
```


The id of the instance to use as the basis of the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L101">property sriovNetSupport</a>
</h3>

```typescript
public sriovNetSupport: pulumi.Output<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L102">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L108">property virtualizationType</a>
</h3>

```typescript
public virtualizationType: pulumi.Output<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiLaunchPermission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L10">class AmiLaunchPermission</a>
</h2>

Adds launch permission to Amazon Machine Image (AMI) from another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L30">constructor</a>
</h3>

```typescript
new AmiLaunchPermission(name: string, args: AmiLaunchPermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AmiLaunchPermission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AmiLaunchPermissionState): AmiLaunchPermission
```


Get an existing AmiLaunchPermission resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L26">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


An AWS Account ID to add launch permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L30">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CustomerGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L12">class CustomerGateway</a>
</h2>

Provides a customer gateway inside a VPC. These objects can be connected to VPN gateways via VPN connections, and allow you to establish tunnels between your network and the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L41">constructor</a>
</h3>

```typescript
new CustomerGateway(name: string, args: CustomerGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomerGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomerGatewayState): CustomerGateway
```


Get an existing CustomerGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L28">property bgpAsn</a>
</h3>

```typescript
public bgpAsn: pulumi.Output<number>;
```


The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L32">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The IP address of the gateway's Internet-routable external interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L36">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Tags to apply to the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L41">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of customer gateway. The only type AWS
supports at this time is "ipsec.1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DefaultNetworkAcl">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L35">class DefaultNetworkAcl</a>
</h2>

Provides a resource to manage the default AWS Network ACL. VPC Only.

Each VPC created in AWS comes with a Default Network ACL that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `aws_default_network_acl` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Network
ACL that cannot be destroyed, and is created with a known set of default rules.

When Terraform first adopts the Default Network ACL, it **immediately removes all
rules in the ACL**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diffs being shown. For these reasons, this resource is incompatible with the
`aws_network_acl_rule` resource.

For more information about Network ACLs, see the AWS Documentation on
[Network ACLs][aws-network-acls].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L73">constructor</a>
</h3>

```typescript
new DefaultNetworkAcl(name: string, args: DefaultNetworkAclArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultNetworkAcl resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L44">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultNetworkAclState): DefaultNetworkAcl
```


Get an existing DefaultNetworkAcl resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L52">property defaultNetworkAclId</a>
</h3>

```typescript
public defaultNetworkAclId: pulumi.Output<string>;
```


The Network ACL ID to manage. This
attribute is exported from `aws_vpc`, or manually found via the AWS Console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L56">property egress</a>
</h3>

```typescript
public egress: pulumi.Output<{ ... }[] | undefined>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L60">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[] | undefined>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L65">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[] | undefined>;
```


A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L69">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L73">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the associated VPC

<h2 class="pdoc-module-header" id="DefaultRouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L42">class DefaultRouteTable</a>
</h2>

Provides a resource to manage a Default VPC Routing Table.

Each VPC created in AWS comes with a Default Route Table that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource. It is recommended you **do not** use both `aws_default_route_table` to
manage the default route table **and** use the `aws_main_route_table_association`,
due to possible conflict in routes.

The `aws_default_route_table` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Route
Table that cannot be destroyed, and is created with a single route.

When Terraform first adopts the Default Route Table, it **immediately removes all
defined routes**. It then proceeds to create any routes specified in the
configuration. This step is required so that only the routes specified in the
configuration present in the Default Route Table.

For more information about Route Tables, see the AWS Documentation on
[Route Tables][aws-route-tables].

For more information about managing normal Route Tables in Terraform, see our
documentation on [aws_route_table][tf-route-tables].

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite routes.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L71">constructor</a>
</h3>

```typescript
new DefaultRouteTable(name: string, args: DefaultRouteTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultRouteTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L51">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultRouteTableState): DefaultRouteTable
```


Get an existing DefaultRouteTable resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L58">property defaultRouteTableId</a>
</h3>

```typescript
public defaultRouteTableId: pulumi.Output<string>;
```


The ID of the Default Routing Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L62">property propagatingVgws</a>
</h3>

```typescript
public propagatingVgws: pulumi.Output<string[] | undefined>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L66">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L70">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L71">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="DefaultSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L36">class DefaultSecurityGroup</a>
</h2>

Provides a resource to manage the default AWS Security Group.

For EC2 Classic accounts, each region comes with a Default Security Group.
Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `aws_default_security_group` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management. We can do this because these default security groups cannot be
destroyed, and are created with a known set of default ingress/egress rules.

When Terraform first adopts the Default Security Group, it **immediately removes all
ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diff shown. For these reasons, this resource is incompatible with the
`aws_security_group_rule` resource.

For more information about Default Security Groups, see the AWS Documentation on
[Default Security Groups][aws-default-security-groups].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L78">constructor</a>
</h3>

```typescript
new DefaultSecurityGroup(name: string, args?: DefaultSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultSecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L45">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultSecurityGroupState): DefaultSecurityGroup
```


Get an existing DefaultSecurityGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L49">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L54">property egress</a>
</h3>

```typescript
public egress: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L59">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L63">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the security group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L67">property ownerId</a>
</h3>

```typescript
public ownerId: pulumi.Output<string>;
```


The owner ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L68">property revokeRulesOnDelete</a>
</h3>

```typescript
public revokeRulesOnDelete: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L72">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L78">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID. **Note that changing
the `vpc_id` will _not_ restore any default security group rules that were
modified, added, or removed.** It will be left in its current state

<h2 class="pdoc-module-header" id="DefaultSubnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L17">class DefaultSubnet</a>
</h2>

Provides a resource to manage a [default AWS VPC subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html#default-vpc-basics)
in the current region.

The `aws_default_subnet` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L55">constructor</a>
</h3>

```typescript
new DefaultSubnet(name: string, args: DefaultSubnetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultSubnet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultSubnetState): DefaultSubnet
```


Get an existing DefaultSubnet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L31">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
public assignIpv6AddressOnCreation: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L32">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L36">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string>;
```


The CIDR block for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L40">property ipv6CidrBlock</a>
</h3>

```typescript
public ipv6CidrBlock: pulumi.Output<string>;
```


The IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L41">property ipv6CidrBlockAssociationId</a>
</h3>

```typescript
public ipv6CidrBlockAssociationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L47">property mapPublicIpOnLaunch</a>
</h3>

```typescript
public mapPublicIpOnLaunch: pulumi.Output<boolean>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L51">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L55">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="DefaultVpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L21">class DefaultVpc</a>
</h2>

Provides a resource to manage the [default AWS VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html)
in the current region.

For AWS accounts created after 2013-12-04, each region comes with a Default VPC.
**This is an advanced resource**, and has special caveats to be aware of when
using it. Please read this document in its entirety before using this resource.

The `aws_default_vpc` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L96">constructor</a>
</h3>

```typescript
new DefaultVpc(name: string, args?: DefaultVpcArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultVpc resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L30">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultVpcState): DefaultVpc
```


Get an existing DefaultVpc resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L37">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L42">property assignGeneratedIpv6CidrBlock</a>
</h3>

```typescript
public assignGeneratedIpv6CidrBlock: pulumi.Output<boolean>;
```


Whether or not an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC was assigned

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L46">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string>;
```


The CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L50">property defaultNetworkAclId</a>
</h3>

```typescript
public defaultNetworkAclId: pulumi.Output<string>;
```


The ID of the network ACL created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L54">property defaultRouteTableId</a>
</h3>

```typescript
public defaultRouteTableId: pulumi.Output<string>;
```


The ID of the route table created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L58">property defaultSecurityGroupId</a>
</h3>

```typescript
public defaultSecurityGroupId: pulumi.Output<string>;
```


The ID of the security group created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L59">property dhcpOptionsId</a>
</h3>

```typescript
public dhcpOptionsId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L65">property enableClassiclink</a>
</h3>

```typescript
public enableClassiclink: pulumi.Output<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L66">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
public enableClassiclinkDnsSupport: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L70">property enableDnsHostnames</a>
</h3>

```typescript
public enableDnsHostnames: pulumi.Output<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L74">property enableDnsSupport</a>
</h3>

```typescript
public enableDnsSupport: pulumi.Output<boolean | undefined>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L78">property instanceTenancy</a>
</h3>

```typescript
public instanceTenancy: pulumi.Output<string>;
```


Tenancy of instances spin up within VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L82">property ipv6AssociationId</a>
</h3>

```typescript
public ipv6AssociationId: pulumi.Output<string>;
```


The association ID for the IPv6 CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L86">property ipv6CidrBlock</a>
</h3>

```typescript
public ipv6CidrBlock: pulumi.Output<string>;
```


The IPv6 CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L92">property mainRouteTableId</a>
</h3>

```typescript
public mainRouteTableId: pulumi.Output<string>;
```


The ID of the main route table associated with
this VPC. Note that you can change a VPC's main route table by using an
[`aws_main_route_table_association`](https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L96">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DefaultVpcDhcpOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L21">class DefaultVpcDhcpOptions</a>
</h2>

Provides a resource to manage the [default AWS DHCP Options Set](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#AmazonDNS)
in the current region.

Each AWS region comes with a default set of DHCP options.
**This is an advanced resource**, and has special caveats to be aware of when
using it. Please read this document in its entirety before using this resource.

The `aws_default_vpc_dhcp_options` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L48">constructor</a>
</h3>

```typescript
new DefaultVpcDhcpOptions(name: string, args?: DefaultVpcDhcpOptionsArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DefaultVpcDhcpOptions resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L30">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultVpcDhcpOptionsState): DefaultVpcDhcpOptions
```


Get an existing DefaultVpcDhcpOptions resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L34">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L35">property domainNameServers</a>
</h3>

```typescript
public domainNameServers: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L39">property netbiosNameServers</a>
</h3>

```typescript
public netbiosNameServers: pulumi.Output<string[] | undefined>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L43">property netbiosNodeType</a>
</h3>

```typescript
public netbiosNodeType: pulumi.Output<string | undefined>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L44">property ntpServers</a>
</h3>

```typescript
public ntpServers: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L48">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EgressOnlyInternetGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L13">class EgressOnlyInternetGateway</a>
</h2>

[IPv6 only] Creates an egress-only Internet gateway for your VPC.
An egress-only Internet gateway is used to enable outbound communication
over IPv6 from instances in your VPC to the Internet, and prevents hosts
outside of your VPC from initiating an IPv6 connection with your instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L29">constructor</a>
</h3>

```typescript
new EgressOnlyInternetGateway(name: string, args: EgressOnlyInternetGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EgressOnlyInternetGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EgressOnlyInternetGatewayState): EgressOnlyInternetGateway
```


Get an existing EgressOnlyInternetGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L29">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="Eip">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L16">class Eip</a>
</h2>

Provides an Elastic IP resource.

~> **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.

~> **Note:** Do not use `network_interface` to associate the EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L61">constructor</a>
</h3>

```typescript
new Eip(name: string, args?: EipArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Eip resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EipState): Eip
```


Get an existing Eip resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L29">property allocationId</a>
</h3>

```typescript
public allocationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L35">property associateWithPrivateIp</a>
</h3>

```typescript
public associateWithPrivateIp: pulumi.Output<string | undefined>;
```


A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L36">property associationId</a>
</h3>

```typescript
public associationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L37">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L41">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


EC2 instance ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L45">property networkInterface</a>
</h3>

```typescript
public networkInterface: pulumi.Output<string>;
```


Network interface ID to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L49">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


Contains the private IP address (if in VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L53">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


Contains the public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L57">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L61">property vpc</a>
</h3>

```typescript
public vpc: pulumi.Output<boolean>;
```


Boolean if the EIP is in a VPC or not.

<h2 class="pdoc-module-header" id="EipAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L16">class EipAssociation</a>
</h2>

Provides an AWS EIP Association as a top level resource, to associate and
disassociate Elastic IPs from AWS Instances and Network Interfaces.

~> **NOTE:** Do not use this resource to associate an EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

~> **NOTE:** `aws_eip_association` is useful in scenarios where EIPs are either
pre-existing or distributed to customers or users and therefore cannot be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L61">constructor</a>
</h3>

```typescript
new EipAssociation(name: string, args?: EipAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EipAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EipAssociationState): EipAssociation
```


Get an existing EipAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L32">property allocationId</a>
</h3>

```typescript
public allocationId: pulumi.Output<string>;
```


The allocation ID. This is required for EC2-VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L37">property allowReassociation</a>
</h3>

```typescript
public allowReassociation: pulumi.Output<boolean | undefined>;
```


Whether to allow an Elastic IP to
be re-associated. Defaults to `true` in VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L44">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L50">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L57">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```


The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L61">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The Elastic IP address. This is required for EC2-Classic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FlowLog">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L11">class FlowLog</a>
</h2>

Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L49">constructor</a>
</h3>

```typescript
new FlowLog(name: string, args: FlowLogArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FlowLog resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FlowLogState): FlowLog
```


Get an existing FlowLog resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L27">property eniId</a>
</h3>

```typescript
public eniId: pulumi.Output<string | undefined>;
```


Elastic Network Interface ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L32">property iamRoleArn</a>
</h3>

```typescript
public iamRoleArn: pulumi.Output<string>;
```


The ARN for the IAM role that's used to post flow
logs to a CloudWatch Logs log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L36">property logGroupName</a>
</h3>

```typescript
public logGroupName: pulumi.Output<string>;
```


The name of the CloudWatch log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L40">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L45">property trafficType</a>
</h3>

```typescript
public trafficType: pulumi.Output<string>;
```


The type of traffic to capture. Valid values:
`ACCEPT`,`REJECT`, `ALL`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L49">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string | undefined>;
```


VPC ID to attach to

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L14">class Instance</a>
</h2>

Provides an EC2 instance resource. This allows instances to be created, updated,
and deleted. Instances also support [provisioning](https://www.terraform.io/docs/provisioners/index.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L200">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L30">property ami</a>
</h3>

```typescript
public ami: pulumi.Output<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L34">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L38">property associatePublicIpAddress</a>
</h3>

```typescript
public associatePublicIpAddress: pulumi.Output<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L42">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L48">property cpuCoreCount</a>
</h3>

```typescript
public cpuCoreCount: pulumi.Output<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L52">property cpuThreadsPerCore</a>
</h3>

```typescript
public cpuThreadsPerCore: pulumi.Output<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L56">property creditSpecification</a>
</h3>

```typescript
public creditSpecification: pulumi.Output<{ ... } | undefined>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L61">property disableApiTermination</a>
</h3>

```typescript
public disableApiTermination: pulumi.Output<boolean | undefined>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L66">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L74">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L79">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L83">property getPasswordData</a>
</h3>

```typescript
public getPasswordData: pulumi.Output<boolean | undefined>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L89">property iamInstanceProfile</a>
</h3>

```typescript
public iamInstanceProfile: pulumi.Output<string | undefined>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L96">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
public instanceInitiatedShutdownBehavior: pulumi.Output<string | undefined>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L97">property instanceState</a>
</h3>

```typescript
public instanceState: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L101">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<InstanceType>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L102">property ipv6AddressCount</a>
</h3>

```typescript
public ipv6AddressCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L106">property ipv6Addresses</a>
</h3>

```typescript
public ipv6Addresses: pulumi.Output<string[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L110">property keyName</a>
</h3>

```typescript
public keyName: pulumi.Output<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L114">property monitoring</a>
</h3>

```typescript
public monitoring: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L122">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the network interface that was created with the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L118">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L130">property passwordData</a>
</h3>

```typescript
public passwordData: pulumi.Output<string>;
```


Base-64 encoded encrypted password data for the instance.
Useful for getting the administrator password for instances running Microsoft Windows.
This attribute is only exported if `get_password_data` is true.
Note that this encrypted value will be stored in the state file, as with all exported attributes.
See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L134">property placementGroup</a>
</h3>

```typescript
public placementGroup: pulumi.Output<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L138">property primaryNetworkInterfaceId</a>
</h3>

```typescript
public primaryNetworkInterfaceId: pulumi.Output<string>;
```


The ID of the instance's primary network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L144">property privateDns</a>
</h3>

```typescript
public privateDns: pulumi.Output<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L149">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L154">property publicDns</a>
</h3>

```typescript
public publicDns: pulumi.Output<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L158">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The public IP address assigned to the instance, if applicable. **NOTE**: If you are using an [`aws_eip`](https://www.terraform.io/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address directly and not use `public_ip`, as this field will change after the EIP is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L163">property rootBlockDevice</a>
</h3>

```typescript
public rootBlockDevice: pulumi.Output<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L167">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L172">property sourceDestCheck</a>
</h3>

```typescript
public sourceDestCheck: pulumi.Output<boolean | undefined>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L176">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L180">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L184">property tenancy</a>
</h3>

```typescript
public tenancy: pulumi.Output<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L188">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L192">property userDataBase64</a>
</h3>

```typescript
public userDataBase64: pulumi.Output<string | undefined>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L196">property volumeTags</a>
</h3>

```typescript
public volumeTags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L200">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="InternetGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L12">class InternetGateway</a>
</h2>

Provides a resource to create a VPC Internet Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L32">constructor</a>
</h3>

```typescript
new InternetGateway(name: string, args?: InternetGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a InternetGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InternetGatewayState): InternetGateway
```


Get an existing InternetGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L28">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L32">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string | undefined>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="KeyPair">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L18">class KeyPair</a>
</h2>

Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.

Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:

* OpenSSH public key format (the format in ~/.ssh/authorized_keys)
* Base64 encoded DER format
* SSH public key file format as specified in RFC4716

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L46">constructor</a>
</h3>

```typescript
new KeyPair(name: string, args: KeyPairArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyPair resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyPairState): KeyPair
```


Get an existing KeyPair resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L34">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The MD5 public key fingerprint as specified in section 4 of RFC 4716.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L38">property keyName</a>
</h3>

```typescript
public keyName: pulumi.Output<string>;
```


The name for the key pair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L42">property keyNamePrefix</a>
</h3>

```typescript
public keyNamePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L46">property publicKey</a>
</h3>

```typescript
public publicKey: pulumi.Output<string>;
```


The public key material.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LaunchConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L10">class LaunchConfiguration</a>
</h2>

Provides a resource to create a new launch configuration, used for autoscaling groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L106">constructor</a>
</h3>

```typescript
new LaunchConfiguration(name: string, args: LaunchConfigurationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LaunchConfiguration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LaunchConfigurationState): LaunchConfiguration
```


Get an existing LaunchConfiguration resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L26">property associatePublicIpAddress</a>
</h3>

```typescript
public associatePublicIpAddress: pulumi.Output<boolean | undefined>;
```


Associate a public ip address with an instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L31">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L35">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L39">property enableMonitoring</a>
</h3>

```typescript
public enableMonitoring: pulumi.Output<boolean | undefined>;
```


Enables/disables detailed monitoring. This is enabled by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L44">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[] | undefined>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L49">property iamInstanceProfile</a>
</h3>

```typescript
public iamInstanceProfile: pulumi.Output<string | undefined>;
```


The IAM instance profile to associate
with launched instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L53">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string>;
```


The EC2 image ID to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L57">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string>;
```


The size of instance to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L61">property keyName</a>
</h3>

```typescript
public keyName: pulumi.Output<string>;
```


The key name that should be used for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L66">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the launch configuration. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L71">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L77">property placementTenancy</a>
</h3>

```typescript
public placementTenancy: pulumi.Output<string | undefined>;
```


The tenancy of the instance. Valid values are
`"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L82">property rootBlockDevice</a>
</h3>

```typescript
public rootBlockDevice: pulumi.Output<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L86">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[] | undefined>;
```


A list of associated security group IDS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L90">property spotPrice</a>
</h3>

```typescript
public spotPrice: pulumi.Output<string | undefined>;
```


The maximum price to use for reserving spot instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L94">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L98">property userDataBase64</a>
</h3>

```typescript
public userDataBase64: pulumi.Output<string | undefined>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L102">property vpcClassicLinkId</a>
</h3>

```typescript
public vpcClassicLinkId: pulumi.Output<string | undefined>;
```


The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L106">property vpcClassicLinkSecurityGroups</a>
</h3>

```typescript
public vpcClassicLinkSecurityGroups: pulumi.Output<string[] | undefined>;
```


The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).

<h2 class="pdoc-module-header" id="LaunchTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L12">class LaunchTemplate</a>
</h2>

Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L141">constructor</a>
</h3>

```typescript
new LaunchTemplate(name: string, args?: LaunchTemplateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LaunchTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LaunchTemplateState): LaunchTemplate
```


Get an existing LaunchTemplate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L33">property blockDeviceMappings</a>
</h3>

```typescript
public blockDeviceMappings: pulumi.Output<{ ... }[] | undefined>;
```


Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L38">property creditSpecification</a>
</h3>

```typescript
public creditSpecification: pulumi.Output<{ ... } | undefined>;
```


Customize the credit specification of the instance. See Credit
Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L42">property defaultVersion</a>
</h3>

```typescript
public defaultVersion: pulumi.Output<number>;
```


The default version of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L46">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L51">property disableApiTermination</a>
</h3>

```typescript
public disableApiTermination: pulumi.Output<boolean | undefined>;
```


If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L55">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


If `true`, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L60">property elasticGpuSpecifications</a>
</h3>

```typescript
public elasticGpuSpecifications: pulumi.Output<{ ... }[] | undefined>;
```


The elastic GPU to attach to the instance. See Elastic GPU
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L65">property iamInstanceProfile</a>
</h3>

```typescript
public iamInstanceProfile: pulumi.Output<{ ... } | undefined>;
```


The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L69">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The AMI from which to launch the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L74">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
public instanceInitiatedShutdownBehavior: pulumi.Output<string | undefined>;
```


Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L79">property instanceMarketOptions</a>
</h3>

```typescript
public instanceMarketOptions: pulumi.Output<{ ... } | undefined>;
```


The market (purchasing) option for the instance. See Market Options
below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L83">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string | undefined>;
```


The type of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L87">property kernelId</a>
</h3>

```typescript
public kernelId: pulumi.Output<string | undefined>;
```


The kernel ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L91">property keyName</a>
</h3>

```typescript
public keyName: pulumi.Output<string | undefined>;
```


The key name to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L95">property latestVersion</a>
</h3>

```typescript
public latestVersion: pulumi.Output<number>;
```


The latest version of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L99">property monitoring</a>
</h3>

```typescript
public monitoring: pulumi.Output<{ ... } | undefined>;
```


The monitoring option for the instance. See Monitoring below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L103">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the launch template. If you leave this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L107">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L112">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[] | undefined>;
```


Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L116">property placement</a>
</h3>

```typescript
public placement: pulumi.Output<{ ... } | undefined>;
```


The placement of the instance. See Placement below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L120">property ramDiskId</a>
</h3>

```typescript
public ramDiskId: pulumi.Output<string | undefined>;
```


The ID of the RAM disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L125">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[] | undefined>;
```


A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L129">property tagSpecifications</a>
</h3>

```typescript
public tagSpecifications: pulumi.Output<{ ... }[] | undefined>;
```


The tags to apply to the resources during launch. See Tags below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L133">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L137">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


The Base64-encoded user data to provide when launching the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L141">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="MainRouteTableAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L10">class MainRouteTableAssociation</a>
</h2>

Provides a resource for managing the main routing table of a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L35">constructor</a>
</h3>

```typescript
new MainRouteTableAssociation(name: string, args: MainRouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MainRouteTableAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MainRouteTableAssociationState): MainRouteTableAssociation
```


Get an existing MainRouteTableAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L26">property originalRouteTableId</a>
</h3>

```typescript
public originalRouteTableId: pulumi.Output<string>;
```


Used internally, see __Notes__ below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L31">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The ID of the Route Table to set as the new
main route table for the target VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L35">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the VPC whose main route table should be set

<h2 class="pdoc-module-header" id="NatGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L12">class NatGateway</a>
</h2>

Provides a resource to create a VPC NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L48">constructor</a>
</h3>

```typescript
new NatGateway(name: string, args: NatGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NatGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatGatewayState): NatGateway
```


Get an existing NatGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L28">property allocationId</a>
</h3>

```typescript
public allocationId: pulumi.Output<string>;
```


The Allocation ID of the Elastic IP address for the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L32">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ENI ID of the network interface created by the NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L36">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


The private IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L40">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The public IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L44">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The Subnet ID of the subnet in which to place the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L48">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkAcl">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L19">class NetworkAcl</a>
</h2>

Provides an network ACL resource. You might set up network ACLs with rules similar
to your security groups in order to add an additional layer of security to your VPC.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L56">constructor</a>
</h3>

```typescript
new NetworkAcl(name: string, args: NetworkAclArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkAcl resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkAclState): NetworkAcl
```


Get an existing NetworkAcl resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L35">property egress</a>
</h3>

```typescript
public egress: pulumi.Output<{ ... }[]>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L39">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[]>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L44">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


The ID of the associated Subnet. This
attribute is deprecated, please use the `subnet_ids` attribute instead

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L48">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


A list of Subnet IDs to apply the ACL to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L56">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the associated VPC.

<h2 class="pdoc-module-header" id="NetworkAclRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L16">class NetworkAclRule</a>
</h2>

Creates an entry (a rule) in a network ACL with the specified rule number.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L72">constructor</a>
</h3>

```typescript
new NetworkAclRule(name: string, args: NetworkAclRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkAclRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkAclRuleState): NetworkAclRule
```


Get an existing NetworkAclRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L32">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string | undefined>;
```


The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L36">property egress</a>
</h3>

```typescript
public egress: pulumi.Output<boolean | undefined>;
```


Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L40">property fromPort</a>
</h3>

```typescript
public fromPort: pulumi.Output<number | undefined>;
```


The from port to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L44">property icmpCode</a>
</h3>

```typescript
public icmpCode: pulumi.Output<string | undefined>;
```


ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L48">property icmpType</a>
</h3>

```typescript
public icmpType: pulumi.Output<string | undefined>;
```


ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L52">property ipv6CidrBlock</a>
</h3>

```typescript
public ipv6CidrBlock: pulumi.Output<string | undefined>;
```


The IPv6 CIDR block to allow or deny.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L56">property networkAclId</a>
</h3>

```typescript
public networkAclId: pulumi.Output<string>;
```


The ID of the network ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L60">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol. A value of -1 means all protocols.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L64">property ruleAction</a>
</h3>

```typescript
public ruleAction: pulumi.Output<string>;
```


Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L68">property ruleNumber</a>
</h3>

```typescript
public ruleNumber: pulumi.Output<number>;
```


The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L72">property toPort</a>
</h3>

```typescript
public toPort: pulumi.Output<number | undefined>;
```


The to port to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L12">class NetworkInterface</a>
</h2>

Provides an Elastic network interface (ENI) resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L58">constructor</a>
</h3>

```typescript
new NetworkInterface(name: string, args: NetworkInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceState): NetworkInterface
```


Get an existing NetworkInterface resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L28">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


Block to define the attachment of the ENI. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L33">property privateDnsName</a>
</h3>

```typescript
public privateDnsName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L34">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L38">property privateIps</a>
</h3>

```typescript
public privateIps: pulumi.Output<string[]>;
```


List of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L42">property privateIpsCount</a>
</h3>

```typescript
public privateIpsCount: pulumi.Output<number>;
```


Number of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L46">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[]>;
```


List of security group IDs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L50">property sourceDestCheck</a>
</h3>

```typescript
public sourceDestCheck: pulumi.Output<boolean | undefined>;
```


Whether to enable source destination checking for the ENI. Default true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L54">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


Subnet ID to create the ENI in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L58">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkInterfaceAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L10">class NetworkInterfaceAttachment</a>
</h2>

Attach an Elastic network interface (ENI) resource with EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L42">constructor</a>
</h3>

```typescript
new NetworkInterfaceAttachment(name: string, args: NetworkInterfaceAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterfaceAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceAttachmentState): NetworkInterfaceAttachment
```


Get an existing NetworkInterfaceAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L26">property attachmentId</a>
</h3>

```typescript
public attachmentId: pulumi.Output<string>;
```


The ENI Attachment ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L30">property deviceIndex</a>
</h3>

```typescript
public deviceIndex: pulumi.Output<number>;
```


Network interface index (int).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L34">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


Instance ID to attach.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L38">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


ENI ID to attach.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L42">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The status of the Network Interface Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkInterfaceSecurityGroupAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L22">class NetworkInterfaceSecurityGroupAttachment</a>
</h2>

This resource attaches a security group to an Elastic Network Interface (ENI).
It can be used to attach a security group to any existing ENI, be it a
secondary ENI or one attached as the primary interface on an instance.

~> **NOTE on instances, interfaces, and security groups:** Terraform currently
provides the capability to assign security groups via the [`aws_instance`][1]
and the [`aws_network_interface`][2] resources. Using this resource in
conjunction with security groups provided in-line in those resources will cause
conflicts, and will lead to spurious diffs and undefined behavior - please use
one or the other.

[1]: /docs/providers/aws/d/instance.html
[2]: /docs/providers/aws/r/network_interface.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L42">constructor</a>
</h3>

```typescript
new NetworkInterfaceSecurityGroupAttachment(name: string, args: NetworkInterfaceSecurityGroupAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterfaceSecurityGroupAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceSecurityGroupAttachmentState): NetworkInterfaceSecurityGroupAttachment
```


Get an existing NetworkInterfaceSecurityGroupAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L38">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the network interface to attach to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L42">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The ID of the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PeeringConnectionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L86">class PeeringConnectionOptions</a>
</h2>

Provides a resource to manage VPC peering connection options.

~> **NOTE on VPC Peering Connections and VPC Peering Connection Options:** Terraform provides
both a standalone VPC Peering Connection Options and a VPC Peering Connection
resource with `accepter` and `requester` attributes. Do not manage options for the same VPC peering
connection in both a VPC Peering Connection resource and a VPC Peering Connection Options resource.
Doing so will cause a conflict of options and will overwrite the options.
Using a VPC Peering Connection Options resource decouples management of the connection options from
management of the VPC Peering Connection and allows options to be set correctly in cross-account scenarios.

Basic usage:

```hcl
resource "aws_vpc" "foo" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_vpc" "bar" {
  cidr_block = "10.1.0.0/16"
}

resource "aws_vpc_peering_connection" "foo" {
  vpc_id        = "${aws_vpc.foo.id}"
  peer_vpc_id   = "${aws_vpc.bar.id}"
  auto_accept   = true
}

resource "aws_vpc_peering_connection_options" "foo" {
  vpc_peering_connection_id = "${aws_vpc_peering_connection.foo.id}"

  accepter {
    allow_remote_vpc_dns_resolution = true
  }

  requester {
    allow_vpc_to_remote_classic_link = true
    allow_classic_link_to_remote_vpc = true
  }
}
```

Basic cross-account usage:

```hcl
provider "aws" {
  alias = "requester"

  # Requester's credentials.
}

provider "aws" {
  alias = "accepter"

  # Accepter's credentials.
}

resource "aws_vpc" "main" {
  provider = "aws.requester"

  cidr_block = "10.0.0.0/16"

  enable_dns_support   = true
  enable_dns_hostnames = true
}

resource "aws_vpc" "peer" {
  provider = "aws.accepter"

  cidr_block = "10.1.0.0/16"

  enable_dns_support   = true
  enable_dns_hostnames = true
}

data "aws_caller_identity" "peer" {
  provider = "aws.accepter"
}

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L114">constructor</a>
</h3>

```typescript
new PeeringConnectionOptions(name: string, args: PeeringConnectionOptionsArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PeeringConnectionOptions resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L95">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PeeringConnectionOptionsState): PeeringConnectionOptions
```


Get an existing PeeringConnectionOptions resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L104">property accepter</a>
</h3>

```typescript
public accepter: pulumi.Output<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L110">property requester</a>
</h3>

```typescript
public requester: pulumi.Output<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L114">property vpcPeeringConnectionId</a>
</h3>

```typescript
public vpcPeeringConnectionId: pulumi.Output<string>;
```


The ID of the requester VPC peering connection.

<h2 class="pdoc-module-header" id="PlacementGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L11">class PlacementGroup</a>
</h2>

Provides an EC2 placement group. Read more about placement groups
in [AWS Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L31">constructor</a>
</h3>

```typescript
new PlacementGroup(name: string, args: PlacementGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PlacementGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlacementGroupState): PlacementGroup
```


Get an existing PlacementGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the placement group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L31">property strategy</a>
</h3>

```typescript
public strategy: pulumi.Output<string>;
```


The placement strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProxyProtocolPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L10">class ProxyProtocolPolicy</a>
</h2>

Provides a proxy protocol policy, which allows an ELB to carry a client connection information to a backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L32">constructor</a>
</h3>

```typescript
new ProxyProtocolPolicy(name: string, args: ProxyProtocolPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ProxyProtocolPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProxyProtocolPolicyState): ProxyProtocolPolicy
```


Get an existing ProxyProtocolPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L27">property instancePorts</a>
</h3>

```typescript
public instancePorts: pulumi.Output<string[]>;
```


List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L32">property loadBalancer</a>
</h3>

```typescript
public loadBalancer: pulumi.Output<string>;
```


The load balancer to which the policy
should be attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L16">class Route</a>
</h2>

Provides a resource to create a routing table entry (a route) in a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L68">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState): Route
```


Get an existing Route resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L32">property destinationCidrBlock</a>
</h3>

```typescript
public destinationCidrBlock: pulumi.Output<string | undefined>;
```


The destination CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L36">property destinationIpv6CidrBlock</a>
</h3>

```typescript
public destinationIpv6CidrBlock: pulumi.Output<string | undefined>;
```


The destination IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L37">property destinationPrefixListId</a>
</h3>

```typescript
public destinationPrefixListId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L41">property egressOnlyGatewayId</a>
</h3>

```typescript
public egressOnlyGatewayId: pulumi.Output<string>;
```


An ID of a VPC Egress Only Internet Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L45">property gatewayId</a>
</h3>

```typescript
public gatewayId: pulumi.Output<string>;
```


An ID of a VPC internet gateway or a virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L49">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


An ID of an EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L50">property instanceOwnerId</a>
</h3>

```typescript
public instanceOwnerId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L54">property natGatewayId</a>
</h3>

```typescript
public natGatewayId: pulumi.Output<string>;
```


An ID of a VPC NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L58">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


An ID of a network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L59">property origin</a>
</h3>

```typescript
public origin: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L63">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The ID of the routing table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L64">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L68">property vpcPeeringConnectionId</a>
</h3>

```typescript
public vpcPeeringConnectionId: pulumi.Output<string | undefined>;
```


An ID of a VPC peering connection.

<h2 class="pdoc-module-header" id="RouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L31">class RouteTable</a>
</h2>

Provides a resource to create a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE on `gateway_id` and `nat_gateway_id`:** The AWS API is very forgiving with these two
attributes and the `aws_route_table` resource can be created with a NAT ID specified as a Gateway ID attribute.
This _will_ lead to a permanent diff between your configuration and statefile, as the API returns the correct
parameters in the returned route table. If you're experiencing constant diffs in your `aws_route_table` resources,
the first thing to check is whether or not you're specifying a NAT ID instead of a Gateway ID, or vice-versa.

~> **NOTE on `propagating_vgws` and the `aws_vpn_gateway_route_propagation` resource:**
If the `propagating_vgws` argument is present, it's not supported to _also_
define route propagations using `aws_vpn_gateway_route_propagation`, since
this resource will delete any propagating gateways not explicitly listed in
`propagating_vgws`. Omit this argument when defining route propagation using
the separate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L59">constructor</a>
</h3>

```typescript
new RouteTable(name: string, args: RouteTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L40">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableState): RouteTable
```


Get an existing RouteTable resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L47">property propagatingVgws</a>
</h3>

```typescript
public propagatingVgws: pulumi.Output<string[]>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L51">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L55">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L59">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="RouteTableAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L10">class RouteTableAssociation</a>
</h2>

Provides a resource to create an association between a subnet and routing table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L30">constructor</a>
</h3>

```typescript
new RouteTableAssociation(name: string, args: RouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTableAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableAssociationState): RouteTableAssociation
```


Get an existing RouteTableAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L26">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The ID of the routing table to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L30">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The subnet ID to create an association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L19">class SecurityGroup</a>
</h2>

Provides a security group resource.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone Security Group Rule resource (a single `ingress` or
`egress` rule), and a Security Group resource with `ingress` and `egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L84">constructor</a>
</h3>

```typescript
new SecurityGroup(name: string, args?: SecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityGroupState): SecurityGroup
```


Get an existing SecurityGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the security group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The security group description. Defaults to
"Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you'd like
to classify your security groups in a way that can be updated, use `tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L47">property egress</a>
</h3>

```typescript
public egress: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L52">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the security group. If omitted, Terraform will
assign a random, unique name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L62">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L66">property ownerId</a>
</h3>

```typescript
public ownerId: pulumi.Output<string>;
```


The owner ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L76">property revokeRulesOnDelete</a>
</h3>

```typescript
public revokeRulesOnDelete: pulumi.Output<boolean | undefined>;
```


Instruct Terraform to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L80">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L84">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="SecurityGroupRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L18">class SecurityGroupRule</a>
</h2>

Provides a security group rule resource. Represents a single `ingress` or
`egress` group rule, which can be added to external Security Groups.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone Security Group Rule resource (a single `ingress` or
`egress` rule), and a Security Group resource with `ingress` and `egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L78">constructor</a>
</h3>

```typescript
new SecurityGroupRule(name: string, args: SecurityGroupRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroupRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityGroupRuleState): SecurityGroupRule
```


Get an existing SecurityGroupRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L34">property cidrBlocks</a>
</h3>

```typescript
public cidrBlocks: pulumi.Output<string[] | undefined>;
```


List of CIDR blocks. Cannot be specified with `source_security_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L38">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L42">property fromPort</a>
</h3>

```typescript
public fromPort: pulumi.Output<number>;
```


The start port (or ICMP type number if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L46">property ipv6CidrBlocks</a>
</h3>

```typescript
public ipv6CidrBlocks: pulumi.Output<string[] | undefined>;
```


List of IPv6 CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L51">property prefixListIds</a>
</h3>

```typescript
public prefixListIds: pulumi.Output<string[] | undefined>;
```


List of prefix list IDs (for allowing access to VPC endpoints).
Only valid with `egress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L55">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L59">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The security group to apply this rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L64">property self</a>
</h3>

```typescript
public self: pulumi.Output<boolean | undefined>;
```


If true, the security group itself will be added as
a source to this ingress rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L69">property sourceSecurityGroupId</a>
</h3>

```typescript
public sourceSecurityGroupId: pulumi.Output<string>;
```


The security group id to allow access to/from,
depending on the `type`. Cannot be specified with `cidr_blocks`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L73">property toPort</a>
</h3>

```typescript
public toPort: pulumi.Output<number>;
```


The end port (or ICMP code if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L78">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of rule being created. Valid options are `ingress` (inbound)
or `egress` (outbound).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SnapshotCreateVolumePermission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L10">class SnapshotCreateVolumePermission</a>
</h2>

Adds permission to create volumes off of a given EBS Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L30">constructor</a>
</h3>

```typescript
new SnapshotCreateVolumePermission(name: string, args: SnapshotCreateVolumePermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SnapshotCreateVolumePermission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotCreateVolumePermissionState): SnapshotCreateVolumePermission
```


Get an existing SnapshotCreateVolumePermission resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L26">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


An AWS Account ID to add create volume permissions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L30">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string>;
```


A snapshot ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SpotDatafeedSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L13">class SpotDatafeedSubscription</a>
</h2>

-> **Note:** There is only a single subscription allowed per account.

To help you understand the charges for your Spot instances, Amazon EC2 provides a data feed that describes your Spot instance usage and pricing.
This data feed is sent to an Amazon S3 bucket that you specify when you subscribe to the data feed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L33">constructor</a>
</h3>

```typescript
new SpotDatafeedSubscription(name: string, args: SpotDatafeedSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SpotDatafeedSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpotDatafeedSubscriptionState): SpotDatafeedSubscription
```


Get an existing SpotDatafeedSubscription resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L29">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The Amazon S3 bucket in which to store the Spot instance data feed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L33">property prefix</a>
</h3>

```typescript
public prefix: pulumi.Output<string | undefined>;
```


Path of folder inside bucket to place spot pricing data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SpotFleetRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L11">class SpotFleetRequest</a>
</h2>

Provides an EC2 Spot Fleet Request resource. This allows a fleet of Spot
instances to be requested on the Spot market.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L106">constructor</a>
</h3>

```typescript
new SpotFleetRequest(name: string, args: SpotFleetRequestArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SpotFleetRequest resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpotFleetRequestState): SpotFleetRequest
```


Get an existing SpotFleetRequest resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L29">property allocationStrategy</a>
</h3>

```typescript
public allocationStrategy: pulumi.Output<string | undefined>;
```


Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
lowestPrice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L30">property clientToken</a>
</h3>

```typescript
public clientToken: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L36">property excessCapacityTerminationPolicy</a>
</h3>

```typescript
public excessCapacityTerminationPolicy: pulumi.Output<string | undefined>;
```


Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L41">property fleetType</a>
</h3>

```typescript
public fleetType: pulumi.Output<string | undefined>;
```


The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is `maintain`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L48">property iamFleetRole</a>
</h3>

```typescript
public iamFleetRole: pulumi.Output<string>;
```


Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L54">property instanceInterruptionBehaviour</a>
</h3>

```typescript
public instanceInterruptionBehaviour: pulumi.Output<string | undefined>;
```


Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
`terminate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L60">property launchSpecifications</a>
</h3>

```typescript
public launchSpecifications: pulumi.Output<{ ... }[]>;
```


Used to define the launch configuration of the
spot-fleet request. Can be specified multiple times to define different bids
across different markets and instance types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L64">property loadBalancers</a>
</h3>

```typescript
public loadBalancers: pulumi.Output<string[]>;
```


A list of elastic load balancer names to add to the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L68">property replaceUnhealthyInstances</a>
</h3>

```typescript
public replaceUnhealthyInstances: pulumi.Output<boolean | undefined>;
```


Indicates whether Spot fleet should replace unhealthy instances. Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L72">property spotPrice</a>
</h3>

```typescript
public spotPrice: pulumi.Output<string | undefined>;
```


The maximum bid price per unit hour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L76">property spotRequestState</a>
</h3>

```typescript
public spotRequestState: pulumi.Output<string>;
```


The state of the Spot fleet request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L82">property targetCapacity</a>
</h3>

```typescript
public targetCapacity: pulumi.Output<number>;
```


The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L87">property targetGroupArns</a>
</h3>

```typescript
public targetGroupArns: pulumi.Output<string[]>;
```


A list of `aws_alb_target_group` ARNs, for use with
Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L92">property terminateInstancesWithExpiration</a>
</h3>

```typescript
public terminateInstancesWithExpiration: pulumi.Output<boolean | undefined>;
```


Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L96">property validFrom</a>
</h3>

```typescript
public validFrom: pulumi.Output<string | undefined>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L100">property validUntil</a>
</h3>

```typescript
public validUntil: pulumi.Output<string | undefined>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L106">property waitForFulfillment</a>
</h3>

```typescript
public waitForFulfillment: pulumi.Output<boolean | undefined>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="SpotInstanceRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L34">class SpotInstanceRequest</a>
</h2>

Provides an EC2 Spot Instance Request resource. This allows instances to be
requested on the spot market.

By default Terraform creates Spot Instance Requests with a `persistent` type,
which means that for the duration of their lifetime, AWS will launch an
instance with the configured details if and when the spot market will accept
the requested price.

On destruction, Terraform will make an attempt to terminate the associated Spot
Instance if there is one present.

Spot Instances requests with a `one-time` type will close the spot request
when the instance is terminated either by the request being below the current spot
price availability or by a user.

~> **NOTE:** Because their behavior depends on the live status of the spot
market, Spot Instance Requests have a unique lifecycle that makes them behave
differently than other Terraform resources. Most importantly: there is __no
guarantee__ that a Spot Instance exists to fulfill the request at any given
point in time. See the [AWS Spot Instance
documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
for more information.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L257">constructor</a>
</h3>

```typescript
new SpotInstanceRequest(name: string, args: SpotInstanceRequestArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SpotInstanceRequest resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L43">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpotInstanceRequestState): SpotInstanceRequest
```


Get an existing SpotInstanceRequest resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L50">property ami</a>
</h3>

```typescript
public ami: pulumi.Output<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L51">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L55">property associatePublicIpAddress</a>
</h3>

```typescript
public associatePublicIpAddress: pulumi.Output<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L59">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L65">property blockDurationMinutes</a>
</h3>

```typescript
public blockDurationMinutes: pulumi.Output<number | undefined>;
```


The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
Note that you can't specify an Availability Zone group or a launch group if you specify a duration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L71">property cpuCoreCount</a>
</h3>

```typescript
public cpuCoreCount: pulumi.Output<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L75">property cpuThreadsPerCore</a>
</h3>

```typescript
public cpuThreadsPerCore: pulumi.Output<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L79">property creditSpecification</a>
</h3>

```typescript
public creditSpecification: pulumi.Output<{ ... } | undefined>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L84">property disableApiTermination</a>
</h3>

```typescript
public disableApiTermination: pulumi.Output<boolean | undefined>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L89">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L97">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L102">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L106">property getPasswordData</a>
</h3>

```typescript
public getPasswordData: pulumi.Output<boolean | undefined>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L112">property iamInstanceProfile</a>
</h3>

```typescript
public iamInstanceProfile: pulumi.Output<string | undefined>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L119">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
public instanceInitiatedShutdownBehavior: pulumi.Output<string | undefined>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L123">property instanceInterruptionBehaviour</a>
</h3>

```typescript
public instanceInterruptionBehaviour: pulumi.Output<string | undefined>;
```


Indicates whether a Spot instance stops or terminates when it is interrupted. Default is `terminate` as this is the current AWS behaviour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L124">property instanceState</a>
</h3>

```typescript
public instanceState: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L128">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L129">property ipv6AddressCount</a>
</h3>

```typescript
public ipv6AddressCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L133">property ipv6Addresses</a>
</h3>

```typescript
public ipv6Addresses: pulumi.Output<string[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L137">property keyName</a>
</h3>

```typescript
public keyName: pulumi.Output<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L142">property launchGroup</a>
</h3>

```typescript
public launchGroup: pulumi.Output<string | undefined>;
```


A launch group is a group of spot instances that launch together and terminate together.
If left empty instances are launched and terminated individually.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L146">property monitoring</a>
</h3>

```typescript
public monitoring: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L151">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L150">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L152">property passwordData</a>
</h3>

```typescript
public passwordData: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L156">property placementGroup</a>
</h3>

```typescript
public placementGroup: pulumi.Output<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L157">property primaryNetworkInterfaceId</a>
</h3>

```typescript
public primaryNetworkInterfaceId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L163">property privateDns</a>
</h3>

```typescript
public privateDns: pulumi.Output<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L168">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L173">property publicDns</a>
</h3>

```typescript
public publicDns: pulumi.Output<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L177">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L182">property rootBlockDevice</a>
</h3>

```typescript
public rootBlockDevice: pulumi.Output<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L186">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L191">property sourceDestCheck</a>
</h3>

```typescript
public sourceDestCheck: pulumi.Output<boolean | undefined>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L200">property spotBidStatus</a>
</h3>

```typescript
public spotBidStatus: pulumi.Output<string>;
```


The current [bid
status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html)
of the Spot Instance Request.
* `spot_request_state` The current [request
state](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#creating-spot-request-status)
of the Spot Instance Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L205">property spotInstanceId</a>
</h3>

```typescript
public spotInstanceId: pulumi.Output<string>;
```


The Instance ID (if any) that is currently fulfilling
the Spot Instance request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L209">property spotPrice</a>
</h3>

```typescript
public spotPrice: pulumi.Output<string | undefined>;
```


The maximum price to request on the spot market.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L210">property spotRequestState</a>
</h3>

```typescript
public spotRequestState: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L215">property spotType</a>
</h3>

```typescript
public spotType: pulumi.Output<string | undefined>;
```


If set to `one-time`, after
the instance is terminated, the spot request will be closed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L219">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L223">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L227">property tenancy</a>
</h3>

```typescript
public tenancy: pulumi.Output<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L231">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L235">property userDataBase64</a>
</h3>

```typescript
public userDataBase64: pulumi.Output<string | undefined>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L239">property validFrom</a>
</h3>

```typescript
public validFrom: pulumi.Output<string>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L243">property validUntil</a>
</h3>

```typescript
public validUntil: pulumi.Output<string>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. The default end date is 7 days from the current date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L247">property volumeTags</a>
</h3>

```typescript
public volumeTags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L251">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


A list of security group IDs to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L257">property waitForFulfillment</a>
</h3>

```typescript
public waitForFulfillment: pulumi.Output<boolean | undefined>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="Subnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L12">class Subnet</a>
</h2>

Provides an VPC subnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L63">constructor</a>
</h3>

```typescript
new Subnet(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subnet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetState): Subnet
```


Get an existing Subnet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the subnet.
* `availability_zone`- The AZ for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L35">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
public assignIpv6AddressOnCreation: pulumi.Output<boolean | undefined>;
```


Specify true to indicate
that network interfaces created in the specified subnet should be
assigned an IPv6 address. Default is `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L36">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L40">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string>;
```


The CIDR block for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L45">property ipv6CidrBlock</a>
</h3>

```typescript
public ipv6CidrBlock: pulumi.Output<string>;
```


The IPv6 network range for the subnet,
in CIDR notation. The subnet size must use a /64 prefix length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L49">property ipv6CidrBlockAssociationId</a>
</h3>

```typescript
public ipv6CidrBlockAssociationId: pulumi.Output<string>;
```


The association ID for the IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L55">property mapPublicIpOnLaunch</a>
</h3>

```typescript
public mapPublicIpOnLaunch: pulumi.Output<boolean | undefined>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L59">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L63">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="VolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L13">class VolumeAttachment</a>
</h2>

Provides an AWS EBS Volume Attachment as a top level resource, to attach and
detach volumes from AWS Instances.

~> **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L53">constructor</a>
</h3>

```typescript
new VolumeAttachment(name: string, args: VolumeAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeAttachmentState): VolumeAttachment
```


Get an existing VolumeAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L30">property deviceName</a>
</h3>

```typescript
public deviceName: pulumi.Output<string>;
```


The device name to expose to the instance (for
example, `/dev/sdh` or `xvdh`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L37">property forceDetach</a>
</h3>

```typescript
public forceDetach: pulumi.Output<boolean | undefined>;
```


Set to `true` if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in **data loss**. See
[Detaching an Amazon EBS Volume from an Instance][1] for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L41">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


ID of the Instance to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L49">property skipDestroy</a>
</h3>

```typescript
public skipDestroy: pulumi.Output<boolean | undefined>;
```


Set this to true if you do not wish
to detach the volume from the instance to which it is attached at destroy
time, and instead just remove the attachment from Terraform state. This is
useful when destroying an instance which has volumes created by some other
means attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L53">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


ID of the Volume to be attached

<h2 class="pdoc-module-header" id="Vpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L12">class Vpc</a>
</h2>

Provides an VPC resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L92">constructor</a>
</h3>

```typescript
new Vpc(name: string, args: VpcArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vpc resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcState): Vpc
```


Get an existing Vpc resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L34">property assignGeneratedIpv6CidrBlock</a>
</h3>

```typescript
public assignGeneratedIpv6CidrBlock: pulumi.Output<boolean | undefined>;
```


Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L38">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string>;
```


The CIDR block for the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L42">property defaultNetworkAclId</a>
</h3>

```typescript
public defaultNetworkAclId: pulumi.Output<string>;
```


The ID of the network ACL created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L46">property defaultRouteTableId</a>
</h3>

```typescript
public defaultRouteTableId: pulumi.Output<string>;
```


The ID of the route table created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L50">property defaultSecurityGroupId</a>
</h3>

```typescript
public defaultSecurityGroupId: pulumi.Output<string>;
```


The ID of the security group created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L51">property dhcpOptionsId</a>
</h3>

```typescript
public dhcpOptionsId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L57">property enableClassiclink</a>
</h3>

```typescript
public enableClassiclink: pulumi.Output<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L62">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
public enableClassiclinkDnsSupport: pulumi.Output<boolean>;
```


A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L66">property enableDnsHostnames</a>
</h3>

```typescript
public enableDnsHostnames: pulumi.Output<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L70">property enableDnsSupport</a>
</h3>

```typescript
public enableDnsSupport: pulumi.Output<boolean | undefined>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L74">property instanceTenancy</a>
</h3>

```typescript
public instanceTenancy: pulumi.Output<string | undefined>;
```


A tenancy option for instances launched into the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L78">property ipv6AssociationId</a>
</h3>

```typescript
public ipv6AssociationId: pulumi.Output<string>;
```


The association ID for the IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L82">property ipv6CidrBlock</a>
</h3>

```typescript
public ipv6CidrBlock: pulumi.Output<string>;
```


The IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L88">property mainRouteTableId</a>
</h3>

```typescript
public mainRouteTableId: pulumi.Output<string>;
```


The ID of the main route table associated with
this VPC. Note that you can change a VPC's main route table by using an
[`aws_main_route_table_association`](https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L92">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VpcDhcpOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L16">class VpcDhcpOptions</a>
</h2>

Provides a VPC DHCP Options resource.
* `domain_name_servers`, `netbios_name_servers`, `ntp_servers` are limited by AWS to maximum four servers only.
* To actually use the DHCP Options Set you need to associate it to a VPC using [`aws_vpc_dhcp_options_association`](https://www.terraform.io/docs/providers/aws/r/vpc_dhcp_options_association.html).
* If you delete a DHCP Options Set, all VPCs using it will be associated to AWS's `default` DHCP Option Set.
* In most cases unless you're configuring your own DNS you'll want to set `domain_name_servers` to `AmazonProvidedDNS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L52">constructor</a>
</h3>

```typescript
new VpcDhcpOptions(name: string, args?: VpcDhcpOptionsArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcDhcpOptions resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcDhcpOptionsState): VpcDhcpOptions
```


Get an existing VpcDhcpOptions resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L32">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string | undefined>;
```


the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L36">property domainNameServers</a>
</h3>

```typescript
public domainNameServers: pulumi.Output<string[] | undefined>;
```


List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L40">property netbiosNameServers</a>
</h3>

```typescript
public netbiosNameServers: pulumi.Output<string[] | undefined>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L44">property netbiosNodeType</a>
</h3>

```typescript
public netbiosNodeType: pulumi.Output<string | undefined>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L48">property ntpServers</a>
</h3>

```typescript
public ntpServers: pulumi.Output<string[] | undefined>;
```


List of NTP servers to configure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VpcDhcpOptionsAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L11">class VpcDhcpOptionsAssociation</a>
</h2>

Provides a VPC DHCP Options Association resource.
* Removing the DHCP Options Association automatically sets AWS's `default` DHCP Options Set to the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L31">constructor</a>
</h3>

```typescript
new VpcDhcpOptionsAssociation(name: string, args: VpcDhcpOptionsAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcDhcpOptionsAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcDhcpOptionsAssociationState): VpcDhcpOptionsAssociation
```


Get an existing VpcDhcpOptionsAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L27">property dhcpOptionsId</a>
</h3>

```typescript
public dhcpOptionsId: pulumi.Output<string>;
```


The ID of the DHCP Options Set to associate to the VPC.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L31">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the VPC to which we would like to associate a DHCP Options Set.

<h2 class="pdoc-module-header" id="VpcEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L17">class VpcEndpoint</a>
</h2>

Provides a VPC Endpoint resource.

~> **NOTE on VPC Endpoints and VPC Endpoint Associations:** Terraform provides both standalone VPC Endpoint Associations for
Route Tables - (an association between a VPC endpoint and a single `route_table_id`) and
Subnets - (an association between a VPC endpoint and a single `subnet_id`) and
a VPC Endpoint resource with `route_table_ids` and `subnet_ids` attributes.
Do not use the same resource ID in both a VPC Endpoint resource and a VPC Endpoint Association resource.
Doing so will cause a conflict of associations and will overwrite the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L87">constructor</a>
</h3>

```typescript
new VpcEndpoint(name: string, args: VpcEndpointArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpoint resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointState): VpcEndpoint
```


Get an existing VpcEndpoint resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L33">property autoAccept</a>
</h3>

```typescript
public autoAccept: pulumi.Output<boolean | undefined>;
```


Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L37">property cidrBlocks</a>
</h3>

```typescript
public cidrBlocks: pulumi.Output<string[]>;
```


The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L41">property dnsEntries</a>
</h3>

```typescript
public dnsEntries: pulumi.Output<{ ... }[]>;
```


The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L45">property networkInterfaceIds</a>
</h3>

```typescript
public networkInterfaceIds: pulumi.Output<string[]>;
```


One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L50">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


A policy to attach to the endpoint that controls access to the service. Applicable for endpoints of type `Gateway`.
Defaults to full access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L54">property prefixListId</a>
</h3>

```typescript
public prefixListId: pulumi.Output<string>;
```


The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L59">property privateDnsEnabled</a>
</h3>

```typescript
public privateDnsEnabled: pulumi.Output<boolean | undefined>;
```


Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L63">property routeTableIds</a>
</h3>

```typescript
public routeTableIds: pulumi.Output<string[]>;
```


One or more route table IDs. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L67">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L71">property serviceName</a>
</h3>

```typescript
public serviceName: pulumi.Output<string>;
```


The service name, in the form `com.amazonaws.region.service` for AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L75">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L79">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L83">property vpcEndpointType</a>
</h3>

```typescript
public vpcEndpointType: pulumi.Output<string | undefined>;
```


The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L87">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the VPC in which the endpoint will be used.

<h2 class="pdoc-module-header" id="VpcEndpointConnectionNotification">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L11">class VpcEndpointConnectionNotification</a>
</h2>

Provides a VPC Endpoint connection notification resource.
Connection notifications notify subscribers of VPC Endpoint events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L47">constructor</a>
</h3>

```typescript
new VpcEndpointConnectionNotification(name: string, args: VpcEndpointConnectionNotificationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpointConnectionNotification resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointConnectionNotificationState): VpcEndpointConnectionNotification
```


Get an existing VpcEndpointConnectionNotification resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L27">property connectionEvents</a>
</h3>

```typescript
public connectionEvents: pulumi.Output<string[]>;
```


One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L31">property connectionNotificationArn</a>
</h3>

```typescript
public connectionNotificationArn: pulumi.Output<string>;
```


The ARN of the SNS topic for the notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L35">property notificationType</a>
</h3>

```typescript
public notificationType: pulumi.Output<string>;
```


The type of notification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L39">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the notification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L43">property vpcEndpointId</a>
</h3>

```typescript
public vpcEndpointId: pulumi.Output<string | undefined>;
```


The ID of the VPC Endpoint to receive notifications for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L47">property vpcEndpointServiceId</a>
</h3>

```typescript
public vpcEndpointServiceId: pulumi.Output<string | undefined>;
```


The ID of the VPC Endpoint Service to receive notifications for.

<h2 class="pdoc-module-header" id="VpcEndpointRouteTableAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L16">class VpcEndpointRouteTableAssociation</a>
</h2>

Provides a resource to create an association between a VPC endpoint and routing table.

~> **NOTE on VPC Endpoints and VPC Endpoint Route Table Associations:** Terraform provides
both a standalone VPC Endpoint Route Table Association (an association between a VPC endpoint
and a single `route_table_id`) and a VPC Endpoint resource with a `route_table_ids`
attribute. Do not use the same route table ID in both a VPC Endpoint resource and a VPC Endpoint Route
Table Association resource. Doing so will cause a conflict of associations and will overwrite the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L36">constructor</a>
</h3>

```typescript
new VpcEndpointRouteTableAssociation(name: string, args: VpcEndpointRouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpointRouteTableAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointRouteTableAssociationState): VpcEndpointRouteTableAssociation
```


Get an existing VpcEndpointRouteTableAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L32">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The ID of the routing table to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L36">property vpcEndpointId</a>
</h3>

```typescript
public vpcEndpointId: pulumi.Output<string>;
```


The ID of the VPC endpoint with which the routing table will be associated.

<h2 class="pdoc-module-header" id="VpcEndpointService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L17">class VpcEndpointService</a>
</h2>

Provides a VPC Endpoint Service resource.
Service consumers can create an _Interface_ VPC Endpoint to connect to the service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone VPC Endpoint Service Allowed Principal resource
and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L65">constructor</a>
</h3>

```typescript
new VpcEndpointService(name: string, args: VpcEndpointServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpointService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointServiceState): VpcEndpointService
```


Get an existing VpcEndpointService resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L33">property acceptanceRequired</a>
</h3>

```typescript
public acceptanceRequired: pulumi.Output<boolean>;
```


Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L37">property allowedPrincipals</a>
</h3>

```typescript
public allowedPrincipals: pulumi.Output<string[]>;
```


The ARNs of one or more principals allowed to discover the endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L41">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


The Availability Zones in which the service is available.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L45">property baseEndpointDnsNames</a>
</h3>

```typescript
public baseEndpointDnsNames: pulumi.Output<string[]>;
```


The DNS names for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L49">property networkLoadBalancerArns</a>
</h3>

```typescript
public networkLoadBalancerArns: pulumi.Output<string[]>;
```


The ARNs of one or more Network Load Balancers for the endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L53">property privateDnsName</a>
</h3>

```typescript
public privateDnsName: pulumi.Output<string>;
```


The private DNS name for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L57">property serviceName</a>
</h3>

```typescript
public serviceName: pulumi.Output<string>;
```


The service name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L61">property serviceType</a>
</h3>

```typescript
public serviceType: pulumi.Output<string>;
```


The service type, `Gateway` or `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L65">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the VPC endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VpcEndpointServiceAllowedPrinciple">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L16">class VpcEndpointServiceAllowedPrinciple</a>
</h2>

Provides a resource to allow a principal to discover a VPC endpoint service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone VPC Endpoint Service Allowed Principal resource
and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L36">constructor</a>
</h3>

```typescript
new VpcEndpointServiceAllowedPrinciple(name: string, args: VpcEndpointServiceAllowedPrincipleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpointServiceAllowedPrinciple resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointServiceAllowedPrincipleState): VpcEndpointServiceAllowedPrinciple
```


Get an existing VpcEndpointServiceAllowedPrinciple resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L32">property principalArn</a>
</h3>

```typescript
public principalArn: pulumi.Output<string>;
```


The ARN of the principal to allow permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L36">property vpcEndpointServiceId</a>
</h3>

```typescript
public vpcEndpointServiceId: pulumi.Output<string>;
```


The ID of the VPC endpoint service to allow permission.

<h2 class="pdoc-module-header" id="VpcEndpointSubnetAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L16">class VpcEndpointSubnetAssociation</a>
</h2>

Provides a resource to create an association between a VPC endpoint and a subnet.

~> **NOTE on VPC Endpoints and VPC Endpoint Subnet Associations:** Terraform provides
both a standalone VPC Endpoint Subnet Association (an association between a VPC endpoint
and a single `subnet_id`) and a VPC Endpoint resource with a `subnet_ids`
attribute. Do not use the same subnet ID in both a VPC Endpoint resource and a VPC Endpoint Subnet
Association resource. Doing so will cause a conflict of associations and will overwrite the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L36">constructor</a>
</h3>

```typescript
new VpcEndpointSubnetAssociation(name: string, args: VpcEndpointSubnetAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcEndpointSubnetAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointSubnetAssociationState): VpcEndpointSubnetAssociation
```


Get an existing VpcEndpointSubnetAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L32">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The ID of the subnet to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L36">property vpcEndpointId</a>
</h3>

```typescript
public vpcEndpointId: pulumi.Output<string>;
```


The ID of the VPC endpoint with which the subnet will be associated.

<h2 class="pdoc-module-header" id="VpcIpv4CidrBlockAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L13">class VpcIpv4CidrBlockAssociation</a>
</h2>

Provides a resource to associate additional IPv4 CIDR blocks with a VPC.

When a VPC is created, a primary IPv4 CIDR block for the VPC must be specified.
The `aws_vpc_ipv4_cidr_block_association` resource allows further IPv4 CIDR blocks to be added to the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L33">constructor</a>
</h3>

```typescript
new VpcIpv4CidrBlockAssociation(name: string, args: VpcIpv4CidrBlockAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcIpv4CidrBlockAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcIpv4CidrBlockAssociationState): VpcIpv4CidrBlockAssociation
```


Get an existing VpcIpv4CidrBlockAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L29">property cidrBlock</a>
</h3>

```typescript
public cidrBlock: pulumi.Output<string>;
```


The additional IPv4 CIDR block to associate with the VPC.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L33">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the VPC to make the association with.

<h2 class="pdoc-module-header" id="VpcPeeringConnection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L24">class VpcPeeringConnection</a>
</h2>

Provides a resource to manage a VPC peering connection.

~> **NOTE on VPC Peering Connections and VPC Peering Connection Options:** Terraform provides
both a standalone VPC Peering Connection Options and a VPC Peering Connection
resource with `accepter` and `requester` attributes. Do not manage options for the same VPC peering
connection in both a VPC Peering Connection resource and a VPC Peering Connection Options resource.
Doing so will cause a conflict of options and will overwrite the options.
Using a VPC Peering Connection Options resource decouples management of the connection options from
management of the VPC Peering Connection and allows options to be set correctly in cross-account scenarios.

-> **Note:** For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region
VPC Peering Connections use the `aws_vpc_peering_connection` resource to manage the requester's side of the
connection and use the `aws_vpc_peering_connection_accepter` resource to manage the accepter's side of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L78">constructor</a>
</h3>

```typescript
new VpcPeeringConnection(name: string, args: VpcPeeringConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcPeeringConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L33">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcPeeringConnectionState): VpcPeeringConnection
```


Get an existing VpcPeeringConnection resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L40">property acceptStatus</a>
</h3>

```typescript
public acceptStatus: pulumi.Output<string>;
```


The status of the VPC Peering Connection request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L46">property accepter</a>
</h3>

```typescript
public accepter: pulumi.Output<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L50">property autoAccept</a>
</h3>

```typescript
public autoAccept: pulumi.Output<boolean | undefined>;
```


Accept the peering (both VPCs need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L55">property peerOwnerId</a>
</h3>

```typescript
public peerOwnerId: pulumi.Output<string>;
```


The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L60">property peerRegion</a>
</h3>

```typescript
public peerRegion: pulumi.Output<string>;
```


The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws_vpc_peering_connection_accepter` to manage the accepter side.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L64">property peerVpcId</a>
</h3>

```typescript
public peerVpcId: pulumi.Output<string>;
```


The ID of the VPC with which you are creating the VPC Peering Connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L70">property requester</a>
</h3>

```typescript
public requester: pulumi.Output<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L74">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L78">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the requester VPC.

<h2 class="pdoc-module-header" id="VpcPeeringConnectionAccepter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L19">class VpcPeeringConnectionAccepter</a>
</h2>

Provides a resource to manage the accepter's side of a VPC Peering Connection.

When a cross-account (requester's AWS account differs from the accepter's AWS account) or an inter-region
VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter's account.
The requester can use the `aws_vpc_peering_connection` resource to manage its side of the connection
and the accepter can use the `aws_vpc_peering_connection_accepter` resource to "adopt" its side of the
connection into management.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L73">constructor</a>
</h3>

```typescript
new VpcPeeringConnectionAccepter(name: string, args: VpcPeeringConnectionAccepterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcPeeringConnectionAccepter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcPeeringConnectionAccepterState): VpcPeeringConnectionAccepter
```


Get an existing VpcPeeringConnectionAccepter resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L35">property acceptStatus</a>
</h3>

```typescript
public acceptStatus: pulumi.Output<string>;
```


The status of the VPC Peering Connection request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L40">property accepter</a>
</h3>

```typescript
public accepter: pulumi.Output<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L44">property autoAccept</a>
</h3>

```typescript
public autoAccept: pulumi.Output<boolean | undefined>;
```


Whether or not to accept the peering request. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L48">property peerOwnerId</a>
</h3>

```typescript
public peerOwnerId: pulumi.Output<string>;
```


The AWS account ID of the owner of the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L52">property peerRegion</a>
</h3>

```typescript
public peerRegion: pulumi.Output<string>;
```


The region of the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L56">property peerVpcId</a>
</h3>

```typescript
public peerVpcId: pulumi.Output<string>;
```


The ID of the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L61">property requester</a>
</h3>

```typescript
public requester: pulumi.Output<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L65">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L69">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L73">property vpcPeeringConnectionId</a>
</h3>

```typescript
public vpcPeeringConnectionId: pulumi.Output<string>;
```


The VPC Peering Connection ID to manage.

<h2 class="pdoc-module-header" id="VpnConnection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L19">class VpnConnection</a>
</h2>

Provides a VPN connection connected to a VPC. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and the VPC.

~> **Note:** All arguments including `tunnel1_preshared_key` and `tunnel2_preshared_key` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

~> **Note:** The CIDR blocks in the arguments `tunnel1_inside_cidr` and `tunnel2_inside_cidr` must have a prefix of /30 and be a part of a specific range.
[Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L114">constructor</a>
</h3>

```typescript
new VpnConnection(name: string, args: VpnConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpnConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpnConnectionState): VpnConnection
```


Get an existing VpnConnection resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L35">property customerGatewayConfiguration</a>
</h3>

```typescript
public customerGatewayConfiguration: pulumi.Output<string>;
```


The configuration information for the VPN connection's customer gateway (in the native XML format).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L39">property customerGatewayId</a>
</h3>

```typescript
public customerGatewayId: pulumi.Output<string>;
```


The ID of the customer gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L40">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L44">property staticRoutesOnly</a>
</h3>

```typescript
public staticRoutesOnly: pulumi.Output<boolean>;
```


Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L48">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Tags to apply to the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L52">property tunnel1Address</a>
</h3>

```typescript
public tunnel1Address: pulumi.Output<string>;
```


The public IP address of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L56">property tunnel1BgpAsn</a>
</h3>

```typescript
public tunnel1BgpAsn: pulumi.Output<string>;
```


The bgp asn number of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L60">property tunnel1BgpHoldtime</a>
</h3>

```typescript
public tunnel1BgpHoldtime: pulumi.Output<number>;
```


The bgp holdtime of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L64">property tunnel1CgwInsideAddress</a>
</h3>

```typescript
public tunnel1CgwInsideAddress: pulumi.Output<string>;
```


The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L68">property tunnel1InsideCidr</a>
</h3>

```typescript
public tunnel1InsideCidr: pulumi.Output<string>;
```


The CIDR block of the inside IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L72">property tunnel1PresharedKey</a>
</h3>

```typescript
public tunnel1PresharedKey: pulumi.Output<string>;
```


The preshared key of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L76">property tunnel1VgwInsideAddress</a>
</h3>

```typescript
public tunnel1VgwInsideAddress: pulumi.Output<string>;
```


The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L80">property tunnel2Address</a>
</h3>

```typescript
public tunnel2Address: pulumi.Output<string>;
```


The public IP address of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L84">property tunnel2BgpAsn</a>
</h3>

```typescript
public tunnel2BgpAsn: pulumi.Output<string>;
```


The bgp asn number of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L88">property tunnel2BgpHoldtime</a>
</h3>

```typescript
public tunnel2BgpHoldtime: pulumi.Output<number>;
```


The bgp holdtime of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L92">property tunnel2CgwInsideAddress</a>
</h3>

```typescript
public tunnel2CgwInsideAddress: pulumi.Output<string>;
```


The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L96">property tunnel2InsideCidr</a>
</h3>

```typescript
public tunnel2InsideCidr: pulumi.Output<string>;
```


The CIDR block of the second IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L101">property tunnel2PresharedKey</a>
</h3>

```typescript
public tunnel2PresharedKey: pulumi.Output<string>;
```


The preshared key of the second VPN tunnel.
~> **Note:** The preshared key must be between 8 and 64 characters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, periods(.) and underscores(_).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L105">property tunnel2VgwInsideAddress</a>
</h3>

```typescript
public tunnel2VgwInsideAddress: pulumi.Output<string>;
```


The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L109">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L110">property vgwTelemetries</a>
</h3>

```typescript
public vgwTelemetries: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L114">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string>;
```


The ID of the virtual private gateway.

<h2 class="pdoc-module-header" id="VpnConnectionRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L10">class VpnConnectionRoute</a>
</h2>

Provides a static route between a VPN connection and a customer gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L30">constructor</a>
</h3>

```typescript
new VpnConnectionRoute(name: string, args: VpnConnectionRouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpnConnectionRoute resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpnConnectionRouteState): VpnConnectionRoute
```


Get an existing VpnConnectionRoute resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L26">property destinationCidrBlock</a>
</h3>

```typescript
public destinationCidrBlock: pulumi.Output<string>;
```


The CIDR block associated with the local subnet of the customer network.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L30">property vpnConnectionId</a>
</h3>

```typescript
public vpnConnectionId: pulumi.Output<string>;
```


The ID of the VPN connection.

<h2 class="pdoc-module-header" id="VpnGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L12">class VpnGateway</a>
</h2>

Provides a resource to create a VPC VPN Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L40">constructor</a>
</h3>

```typescript
new VpnGateway(name: string, args?: VpnGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpnGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpnGatewayState): VpnGateway
```


Get an existing VpnGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L28">property amazonSideAsn</a>
</h3>

```typescript
public amazonSideAsn: pulumi.Output<string>;
```


The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't specify an ASN, the virtual private gateway is created with the default ASN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L32">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string | undefined>;
```


The Availability Zone for the virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L36">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L40">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="VpnGatewayAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L15">class VpnGatewayAttachment</a>
</h2>

Provides a Virtual Private Gateway attachment resource, allowing for an existing
hardware VPN gateway to be attached and/or detached from a VPC.

-> **Note:** The `aws_vpn_gateway`
resource can also automatically attach the Virtual Private Gateway it creates
to an existing VPC by setting the `vpc_id` attribute accordingly.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L35">constructor</a>
</h3>

```typescript
new VpnGatewayAttachment(name: string, args: VpnGatewayAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpnGatewayAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpnGatewayAttachmentState): VpnGatewayAttachment
```


Get an existing VpnGatewayAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L31">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The ID of the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L35">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string>;
```


The ID of the Virtual Private Gateway.

<h2 class="pdoc-module-header" id="VpnGatewayRoutePropagation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L14">class VpnGatewayRoutePropagation</a>
</h2>

Requests automatic route propagation between a VPN gateway and a route table.

~> **Note:** This resource should not be used with a route table that has
the `propagating_vgws` argument set. If that argument is set, any route
propagation not explicitly listed in its value will be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L34">constructor</a>
</h3>

```typescript
new VpnGatewayRoutePropagation(name: string, args: VpnGatewayRoutePropagationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpnGatewayRoutePropagation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpnGatewayRoutePropagationState): VpnGatewayRoutePropagation
```


Get an existing VpnGatewayRoutePropagation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L30">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The id of the `aws_route_table` to propagate routes into.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L34">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string>;
```


The id of the `aws_vpn_gateway` to propagate routes from.

<h2 class="pdoc-module-header" id="getInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L11">function getInstance</a>
</h2>

```typescript
getInstance(args?: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult>
```


Use this data source to get the ID of an Amazon EC2 Instance for use in other
resources.

<h2 class="pdoc-module-header" id="getInstances">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L21">function getInstances</a>
</h2>

```typescript
getInstances(args?: GetInstancesArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesResult>
```


Use this data source to get IDs or IPs of Amazon EC2 instances to be referenced elsewhere,
e.g. to allow easier migration from another management solution
or to make it easier for an operator to connect through bastion host(s).

-> **Note:** It's a best practice to expose instance details via [outputs](https://www.terraform.io/docs/configuration/outputs.html)
and [remote state](https://www.terraform.io/docs/state/remote.html) and
**use [`terraform_remote_state`](https://www.terraform.io/docs/providers/terraform/d/remote_state.html)
data source instead** if you manage referenced instances via Terraform.

~> **Note:** It's strongly discouraged to use this data source for querying ephemeral
instances (e.g. managed via autoscaling group), as the output may change at any time
and you'd need to re-run `apply` every time an instance comes up or dies.

<h2 class="pdoc-module-header" id="getInternetGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L10">function getInternetGateway</a>
</h2>

```typescript
getInternetGateway(args?: GetInternetGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetInternetGatewayResult>
```


`aws_internet_gateway` provides details about a specific Internet Gateway.

<h2 class="pdoc-module-header" id="getLaunchConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L10">function getLaunchConfiguration</a>
</h2>

```typescript
getLaunchConfiguration(args: GetLaunchConfigurationArgs, opts?: pulumi.InvokeOptions): Promise<GetLaunchConfigurationResult>
```


Provides information about a Launch Configuration.

<h2 class="pdoc-module-header" id="getNatGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L10">function getNatGateway</a>
</h2>

```typescript
getNatGateway(args?: GetNatGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetNatGatewayResult>
```


Provides details about a specific Nat Gateway.

<h2 class="pdoc-module-header" id="getNetworkAcls">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L7">function getNetworkAcls</a>
</h2>

```typescript
getNetworkAcls(args?: GetNetworkAclsArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkAclsResult>
```

<h2 class="pdoc-module-header" id="getNetworkInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L10">function getNetworkInterface</a>
</h2>

```typescript
getNetworkInterface(args?: GetNetworkInterfaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkInterfaceResult>
```


Use this data source to get information about a Network Interface.

<h2 class="pdoc-module-header" id="getNetworkInterfaces">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L7">function getNetworkInterfaces</a>
</h2>

```typescript
getNetworkInterfaces(args?: GetNetworkInterfacesArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkInterfacesResult>
```

<h2 class="pdoc-module-header" id="getRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L14">function getRoute</a>
</h2>

```typescript
getRoute(args: GetRouteArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteResult>
```


`aws_route` provides details about a specific Route.

This resource can prove useful when finding the resource
associated with a CIDR. For example, finding the peering
connection associated with a CIDR value.

<h2 class="pdoc-module-header" id="getRouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L14">function getRouteTable</a>
</h2>

```typescript
getRouteTable(args?: GetRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTableResult>
```


`aws_route_table` provides details about a specific Route Table.

This resource can prove useful when a module accepts a Subnet id as
an input variable and needs to, for example, add a route in
the Route Table.

<h2 class="pdoc-module-header" id="getRouteTables">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L10">function getRouteTables</a>
</h2>

```typescript
getRouteTables(args?: GetRouteTablesArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTablesResult>
```


This resource can be useful for getting back a list of route table ids to be referenced elsewhere.

<h2 class="pdoc-module-header" id="getSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L14">function getSecurityGroup</a>
</h2>

```typescript
getSecurityGroup(args?: GetSecurityGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetSecurityGroupResult>
```


`aws_security_group` provides details about a specific Security Group.

This resource can prove useful when a module accepts a Security Group id as
an input variable and needs to, for example, determine the id of the
VPC that the security group belongs to.

<h2 class="pdoc-module-header" id="getSecurityGroups">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L11">function getSecurityGroups</a>
</h2>

```typescript
getSecurityGroups(args?: GetSecurityGroupsArgs, opts?: pulumi.InvokeOptions): Promise<GetSecurityGroupsResult>
```


Use this data source to get IDs and VPC membership of Security Groups that are created
outside of Terraform.

<h2 class="pdoc-module-header" id="getSubnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L14">function getSubnet</a>
</h2>

```typescript
getSubnet(args?: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult>
```


`aws_subnet` provides details about a specific VPC subnet.

This resource can prove useful when a module accepts a subnet id as
an input variable and needs to, for example, determine the id of the
VPC that the subnet belongs to.

<h2 class="pdoc-module-header" id="getSubnetIds">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L12">function getSubnetIds</a>
</h2>

```typescript
getSubnetIds(args: GetSubnetIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetIdsResult>
```


`aws_subnet_ids` provides a list of ids for a vpc_id

This resource can be useful for getting back a list of subnet ids for a vpc.

<h2 class="pdoc-module-header" id="getVpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L14">function getVpc</a>
</h2>

```typescript
getVpc(args?: GetVpcArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcResult>
```


`aws_vpc` provides details about a specific VPC.

This resource can prove useful when a module accepts a vpc id as
an input variable and needs to, for example, determine the CIDR block of that
VPC.

<h2 class="pdoc-module-header" id="getVpcDhcpOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L10">function getVpcDhcpOptions</a>
</h2>

```typescript
getVpcDhcpOptions(args?: GetVpcDhcpOptionsArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcDhcpOptionsResult>
```


Retrieve information about an EC2 DHCP Options configuration.

<h2 class="pdoc-module-header" id="getVpcEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L11">function getVpcEndpoint</a>
</h2>

```typescript
getVpcEndpoint(args?: GetVpcEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcEndpointResult>
```


The VPC Endpoint data source provides details about
a specific VPC endpoint.

<h2 class="pdoc-module-header" id="getVpcEndpointService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L11">function getVpcEndpointService</a>
</h2>

```typescript
getVpcEndpointService(args?: GetVpcEndpointServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcEndpointServiceResult>
```


The VPC Endpoint Service data source details about a specific service that
can be specified when creating a VPC endpoint within the region configured in the provider.

<h2 class="pdoc-module-header" id="getVpcPeeringConnection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L11">function getVpcPeeringConnection</a>
</h2>

```typescript
getVpcPeeringConnection(args?: GetVpcPeeringConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcPeeringConnectionResult>
```


The VPC Peering Connection data source provides details about
a specific VPC peering connection.

<h2 class="pdoc-module-header" id="getVpcs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L12">function getVpcs</a>
</h2>

```typescript
getVpcs(args?: GetVpcsArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcsResult>
```


This resource can be useful for getting back a list of VPC Ids for a region.

The following example retrieves a list of VPC Ids with a custom tag of `service` set to a value of "production".

<h2 class="pdoc-module-header" id="getVpnGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L11">function getVpnGateway</a>
</h2>

```typescript
getVpnGateway(args?: GetVpnGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetVpnGatewayResult>
```


The VPN Gateway data source provides details about
a specific VPN gateway.

<h2 class="pdoc-module-header" id="AmiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L213">interface AmiArgs</a>
</h2>

The set of arguments for constructing a Ami resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L217">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L221">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L226">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L230">property enaSupport</a>
</h3>

```typescript
enaSupport?: pulumi.Input<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L235">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L240">property imageLocation</a>
</h3>

```typescript
imageLocation?: pulumi.Input<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L245">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L249">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L254">property ramdiskId</a>
</h3>

```typescript
ramdiskId?: pulumi.Input<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L258">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName?: pulumi.Input<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L263">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport?: pulumi.Input<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L264">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L270">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiCopyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L262">interface AmiCopyArgs</a>
</h2>

The set of arguments for constructing a AmiCopy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L266">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L271">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L275">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L280">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L284">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L288">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L293">property sourceAmiId</a>
</h3>

```typescript
sourceAmiId: pulumi.Input<string>;
```


The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L298">property sourceAmiRegion</a>
</h3>

```typescript
sourceAmiRegion: pulumi.Input<string>;
```


The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L299">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```

<h2 class="pdoc-module-header" id="AmiCopyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L179">interface AmiCopyState</a>
</h2>

Input properties used for looking up and filtering AmiCopy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L183">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L187">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L192">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L196">property enaSupport</a>
</h3>

```typescript
enaSupport?: pulumi.Input<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L200">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L205">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L210">property imageLocation</a>
</h3>

```typescript
imageLocation?: pulumi.Input<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L215">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L219">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L220">property manageEbsSnapshots</a>
</h3>

```typescript
manageEbsSnapshots?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L229">property ramdiskId</a>
</h3>

```typescript
ramdiskId?: pulumi.Input<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L233">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName?: pulumi.Input<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L234">property rootSnapshotId</a>
</h3>

```typescript
rootSnapshotId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L239">property sourceAmiId</a>
</h3>

```typescript
sourceAmiId?: pulumi.Input<string>;
```


The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L244">property sourceAmiRegion</a>
</h3>

```typescript
sourceAmiRegion?: pulumi.Input<string>;
```


The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L249">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport?: pulumi.Input<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L250">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiCopy.ts#L256">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiFromInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L245">interface AmiFromInstanceArgs</a>
</h2>

The set of arguments for constructing a AmiFromInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L249">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L254">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L259">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L263">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L270">property snapshotWithoutReboot</a>
</h3>

```typescript
snapshotWithoutReboot?: pulumi.Input<boolean>;
```


Boolean that overrides the behavior of stopping
the instance before snapshotting. This is risky since it may cause a snapshot of an
inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
guarantees that no filesystem writes will be underway at the time of snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L274">property sourceInstanceId</a>
</h3>

```typescript
sourceInstanceId: pulumi.Input<string>;
```


The id of the instance to use as the basis of the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L275">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="AmiFromInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L169">interface AmiFromInstanceState</a>
</h2>

Input properties used for looking up and filtering AmiFromInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L173">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L177">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L182">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L186">property enaSupport</a>
</h3>

```typescript
enaSupport?: pulumi.Input<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L191">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L196">property imageLocation</a>
</h3>

```typescript
imageLocation?: pulumi.Input<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L201">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L202">property manageEbsSnapshots</a>
</h3>

```typescript
manageEbsSnapshots?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L206">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L211">property ramdiskId</a>
</h3>

```typescript
ramdiskId?: pulumi.Input<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L215">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName?: pulumi.Input<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L216">property rootSnapshotId</a>
</h3>

```typescript
rootSnapshotId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L223">property snapshotWithoutReboot</a>
</h3>

```typescript
snapshotWithoutReboot?: pulumi.Input<boolean>;
```


Boolean that overrides the behavior of stopping
the instance before snapshotting. This is risky since it may cause a snapshot of an
inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
guarantees that no filesystem writes will be underway at the time of snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L227">property sourceInstanceId</a>
</h3>

```typescript
sourceInstanceId?: pulumi.Input<string>;
```


The id of the instance to use as the basis of the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L232">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport?: pulumi.Input<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L233">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiFromInstance.ts#L239">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="AmiLaunchPermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L78">interface AmiLaunchPermissionArgs</a>
</h2>

The set of arguments for constructing a AmiLaunchPermission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L82">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


An AWS Account ID to add launch permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L86">property imageId</a>
</h3>

```typescript
imageId: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h2 class="pdoc-module-header" id="AmiLaunchPermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L64">interface AmiLaunchPermissionState</a>
</h2>

Input properties used for looking up and filtering AmiLaunchPermission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L68">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


An AWS Account ID to add launch permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/amiLaunchPermission.ts#L72">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h2 class="pdoc-module-header" id="AmiState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L145">interface AmiState</a>
</h2>

Input properties used for looking up and filtering Ami resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L149">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances. Defaults to "x86_64".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L153">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A longer, human-readable description for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L158">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L162">property enaSupport</a>
</h3>

```typescript
enaSupport?: pulumi.Input<boolean>;
```


Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L167">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L172">property imageLocation</a>
</h3>

```typescript
imageLocation?: pulumi.Input<string>;
```


Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L177">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L178">property manageEbsSnapshots</a>
</h3>

```typescript
manageEbsSnapshots?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A region-unique name for the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L187">property ramdiskId</a>
</h3>

```typescript
ramdiskId?: pulumi.Input<string>;
```


The id of an initrd image (ARI) that will be used when booting the
created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L191">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName?: pulumi.Input<string>;
```


The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L195">property rootSnapshotId</a>
</h3>

```typescript
rootSnapshotId?: pulumi.Input<string>;
```


The Snapshot ID for the root volume (for EBS-backed AMIs)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L200">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport?: pulumi.Input<string>;
```


When set to "simple" (the default), enables enhanced networking
for created instances. No other value is supported at this time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L201">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/ami.ts#L207">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
changes the set of further arguments that are required, as described below.

<h2 class="pdoc-module-header" id="CustomerGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L105">interface CustomerGatewayArgs</a>
</h2>

The set of arguments for constructing a CustomerGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L109">property bgpAsn</a>
</h3>

```typescript
bgpAsn: pulumi.Input<number>;
```


The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L113">property ipAddress</a>
</h3>

```typescript
ipAddress: pulumi.Input<string>;
```


The IP address of the gateway's Internet-routable external interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L117">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Tags to apply to the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L122">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of customer gateway. The only type AWS
supports at this time is "ipsec.1".

<h2 class="pdoc-module-header" id="CustomerGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L82">interface CustomerGatewayState</a>
</h2>

Input properties used for looking up and filtering CustomerGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L86">property bgpAsn</a>
</h3>

```typescript
bgpAsn?: pulumi.Input<number>;
```


The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L90">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the gateway's Internet-routable external interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L94">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Tags to apply to the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/customerGateway.ts#L99">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of customer gateway. The only type AWS
supports at this time is "ipsec.1".

<h2 class="pdoc-module-header" id="DefaultNetworkAclArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L144">interface DefaultNetworkAclArgs</a>
</h2>

The set of arguments for constructing a DefaultNetworkAcl resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L149">property defaultNetworkAclId</a>
</h3>

```typescript
defaultNetworkAclId: pulumi.Input<string>;
```


The Network ACL ID to manage. This
attribute is exported from `aws_vpc`, or manually found via the AWS Console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L153">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L157">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L162">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L166">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultNetworkAclState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L112">interface DefaultNetworkAclState</a>
</h2>

Input properties used for looking up and filtering DefaultNetworkAcl resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L117">property defaultNetworkAclId</a>
</h3>

```typescript
defaultNetworkAclId?: pulumi.Input<string>;
```


The Network ACL ID to manage. This
attribute is exported from `aws_vpc`, or manually found via the AWS Console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L121">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L125">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L130">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultNetworkAcl.ts#L138">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the associated VPC

<h2 class="pdoc-module-header" id="DefaultRouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L131">interface DefaultRouteTableArgs</a>
</h2>

The set of arguments for constructing a DefaultRouteTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L135">property defaultRouteTableId</a>
</h3>

```typescript
defaultRouteTableId: pulumi.Input<string>;
```


The ID of the Default Routing Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L139">property propagatingVgws</a>
</h3>

```typescript
propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L143">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L147">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultRouteTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L108">interface DefaultRouteTableState</a>
</h2>

Input properties used for looking up and filtering DefaultRouteTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L112">property defaultRouteTableId</a>
</h3>

```typescript
defaultRouteTableId?: pulumi.Input<string>;
```


The ID of the Default Routing Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L116">property propagatingVgws</a>
</h3>

```typescript
propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L120">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultRouteTable.ts#L125">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="DefaultSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L154">interface DefaultSecurityGroupArgs</a>
</h2>

The set of arguments for constructing a DefaultSecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L159">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L164">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L165">property revokeRulesOnDelete</a>
</h3>

```typescript
revokeRulesOnDelete?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L169">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L175">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID. **Note that changing
the `vpc_id` will _not_ restore any default security group rules that were
modified, added, or removed.** It will be left in its current state

<h2 class="pdoc-module-header" id="DefaultSecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L118">interface DefaultSecurityGroupState</a>
</h2>

Input properties used for looking up and filtering DefaultSecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L119">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L124">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L129">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L137">property ownerId</a>
</h3>

```typescript
ownerId?: pulumi.Input<string>;
```


The owner ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L138">property revokeRulesOnDelete</a>
</h3>

```typescript
revokeRulesOnDelete?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSecurityGroup.ts#L148">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID. **Note that changing
the `vpc_id` will _not_ restore any default security group rules that were
modified, added, or removed.** It will be left in its current state

<h2 class="pdoc-module-header" id="DefaultSubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L132">interface DefaultSubnetArgs</a>
</h2>

The set of arguments for constructing a DefaultSubnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L133">property availabilityZone</a>
</h3>

```typescript
availabilityZone: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L139">property mapPublicIpOnLaunch</a>
</h3>

```typescript
mapPublicIpOnLaunch?: pulumi.Input<boolean>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L143">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultSubnetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L100">interface DefaultSubnetState</a>
</h2>

Input properties used for looking up and filtering DefaultSubnet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L101">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L102">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
assignIpv6AddressOnCreation?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L103">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L107">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The CIDR block for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L111">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L112">property ipv6CidrBlockAssociationId</a>
</h3>

```typescript
ipv6CidrBlockAssociationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L118">property mapPublicIpOnLaunch</a>
</h3>

```typescript
mapPublicIpOnLaunch?: pulumi.Input<boolean>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultSubnet.ts#L126">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="DefaultVpcArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L221">interface DefaultVpcArgs</a>
</h2>

The set of arguments for constructing a DefaultVpc resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L227">property enableClassiclink</a>
</h3>

```typescript
enableClassiclink?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L228">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
enableClassiclinkDnsSupport?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L232">property enableDnsHostnames</a>
</h3>

```typescript
enableDnsHostnames?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L236">property enableDnsSupport</a>
</h3>

```typescript
enableDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L240">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultVpcDhcpOptionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L105">interface DefaultVpcDhcpOptionsArgs</a>
</h2>

The set of arguments for constructing a DefaultVpcDhcpOptions resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L109">property netbiosNameServers</a>
</h3>

```typescript
netbiosNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L113">property netbiosNodeType</a>
</h3>

```typescript
netbiosNodeType?: pulumi.Input<string>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L117">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultVpcDhcpOptionsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L84">interface DefaultVpcDhcpOptionsState</a>
</h2>

Input properties used for looking up and filtering DefaultVpcDhcpOptions resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L85">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L86">property domainNameServers</a>
</h3>

```typescript
domainNameServers?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L90">property netbiosNameServers</a>
</h3>

```typescript
netbiosNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L94">property netbiosNodeType</a>
</h3>

```typescript
netbiosNodeType?: pulumi.Input<string>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L95">property ntpServers</a>
</h3>

```typescript
ntpServers?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpcDhcpOptions.ts#L99">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DefaultVpcState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L152">interface DefaultVpcState</a>
</h2>

Input properties used for looking up and filtering DefaultVpc resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L156">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L161">property assignGeneratedIpv6CidrBlock</a>
</h3>

```typescript
assignGeneratedIpv6CidrBlock?: pulumi.Input<boolean>;
```


Whether or not an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC was assigned

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L165">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L169">property defaultNetworkAclId</a>
</h3>

```typescript
defaultNetworkAclId?: pulumi.Input<string>;
```


The ID of the network ACL created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L173">property defaultRouteTableId</a>
</h3>

```typescript
defaultRouteTableId?: pulumi.Input<string>;
```


The ID of the route table created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L177">property defaultSecurityGroupId</a>
</h3>

```typescript
defaultSecurityGroupId?: pulumi.Input<string>;
```


The ID of the security group created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L178">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L184">property enableClassiclink</a>
</h3>

```typescript
enableClassiclink?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L185">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
enableClassiclinkDnsSupport?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L189">property enableDnsHostnames</a>
</h3>

```typescript
enableDnsHostnames?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L193">property enableDnsSupport</a>
</h3>

```typescript
enableDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L197">property instanceTenancy</a>
</h3>

```typescript
instanceTenancy?: pulumi.Input<string>;
```


Tenancy of instances spin up within VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L201">property ipv6AssociationId</a>
</h3>

```typescript
ipv6AssociationId?: pulumi.Input<string>;
```


The association ID for the IPv6 CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L205">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 CIDR block of the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L211">property mainRouteTableId</a>
</h3>

```typescript
mainRouteTableId?: pulumi.Input<string>;
```


The ID of the main route table associated with
this VPC. Note that you can change a VPC's main route table by using an
[`aws_main_route_table_association`](https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/defaultVpc.ts#L215">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EgressOnlyInternetGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L68">interface EgressOnlyInternetGatewayArgs</a>
</h2>

The set of arguments for constructing a EgressOnlyInternetGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L72">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="EgressOnlyInternetGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L58">interface EgressOnlyInternetGatewayState</a>
</h2>

Input properties used for looking up and filtering EgressOnlyInternetGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/egressOnlyInternetGateway.ts#L62">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="EipArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L144">interface EipArgs</a>
</h2>

The set of arguments for constructing a Eip resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L150">property associateWithPrivateIp</a>
</h3>

```typescript
associateWithPrivateIp?: pulumi.Input<string>;
```


A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L154">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


EC2 instance ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L158">property networkInterface</a>
</h3>

```typescript
networkInterface?: pulumi.Input<string>;
```


Network interface ID to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L162">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L166">property vpc</a>
</h3>

```typescript
vpc?: pulumi.Input<boolean>;
```


Boolean if the EIP is in a VPC or not.

<h2 class="pdoc-module-header" id="EipAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L136">interface EipAssociationArgs</a>
</h2>

The set of arguments for constructing a EipAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L140">property allocationId</a>
</h3>

```typescript
allocationId?: pulumi.Input<string>;
```


The allocation ID. This is required for EC2-VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L145">property allowReassociation</a>
</h3>

```typescript
allowReassociation?: pulumi.Input<boolean>;
```


Whether to allow an Elastic IP to
be re-associated. Defaults to `true` in VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L152">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L158">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L165">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L169">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The Elastic IP address. This is required for EC2-Classic.

<h2 class="pdoc-module-header" id="EipAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L97">interface EipAssociationState</a>
</h2>

Input properties used for looking up and filtering EipAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L101">property allocationId</a>
</h3>

```typescript
allocationId?: pulumi.Input<string>;
```


The allocation ID. This is required for EC2-VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L106">property allowReassociation</a>
</h3>

```typescript
allowReassociation?: pulumi.Input<boolean>;
```


Whether to allow an Elastic IP to
be re-associated. Defaults to `true` in VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L113">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L119">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L126">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eipAssociation.ts#L130">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The Elastic IP address. This is required for EC2-Classic.

<h2 class="pdoc-module-header" id="EipState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L105">interface EipState</a>
</h2>

Input properties used for looking up and filtering Eip resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L106">property allocationId</a>
</h3>

```typescript
allocationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L112">property associateWithPrivateIp</a>
</h3>

```typescript
associateWithPrivateIp?: pulumi.Input<string>;
```


A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L113">property associationId</a>
</h3>

```typescript
associationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L114">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L118">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


EC2 instance ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L122">property networkInterface</a>
</h3>

```typescript
networkInterface?: pulumi.Input<string>;
```


Network interface ID to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L126">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


Contains the private IP address (if in VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L130">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


Contains the public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/eip.ts#L138">property vpc</a>
</h3>

```typescript
vpc?: pulumi.Input<boolean>;
```


Boolean if the EIP is in a VPC or not.

<h2 class="pdoc-module-header" id="FlowLogArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L126">interface FlowLogArgs</a>
</h2>

The set of arguments for constructing a FlowLog resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L130">property eniId</a>
</h3>

```typescript
eniId?: pulumi.Input<string>;
```


Elastic Network Interface ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L135">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn: pulumi.Input<string>;
```


The ARN for the IAM role that's used to post flow
logs to a CloudWatch Logs log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L139">property logGroupName</a>
</h3>

```typescript
logGroupName: pulumi.Input<string>;
```


The name of the CloudWatch log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L143">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L148">property trafficType</a>
</h3>

```typescript
trafficType: pulumi.Input<string>;
```


The type of traffic to capture. Valid values:
`ACCEPT`,`REJECT`, `ALL`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L152">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


VPC ID to attach to

<h2 class="pdoc-module-header" id="FlowLogState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L94">interface FlowLogState</a>
</h2>

Input properties used for looking up and filtering FlowLog resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L98">property eniId</a>
</h3>

```typescript
eniId?: pulumi.Input<string>;
```


Elastic Network Interface ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L103">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that's used to post flow
logs to a CloudWatch Logs log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L107">property logGroupName</a>
</h3>

```typescript
logGroupName?: pulumi.Input<string>;
```


The name of the CloudWatch log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L111">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L116">property trafficType</a>
</h3>

```typescript
trafficType?: pulumi.Input<string>;
```


The type of traffic to capture. Valid values:
`ACCEPT`,`REJECT`, `ALL`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/flowLog.ts#L120">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


VPC ID to attach to

<h2 class="pdoc-module-header" id="GetInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L25">interface GetInstanceArgs</a>
</h2>

A collection of arguments for invoking getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L31">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to use as filters. There are
several valid keys, for a full reference, check out
[describe-instances in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L35">property getPasswordData</a>
</h3>

```typescript
getPasswordData?: boolean;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L39">property instanceId</a>
</h3>

```typescript
instanceId?: string;
```


Specify the exact Instance ID with which to populate the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L44">property instanceTags</a>
</h3>

```typescript
instanceTags?: { ... };
```


A mapping of tags, each pair of which must
exactly match a pair on the desired Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L45">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetInstanceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L51">interface GetInstanceResult</a>
</h2>

A collection of values returned by getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L55">property ami</a>
</h3>

```typescript
ami: string;
```


The ID of the AMI used to launch the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L59">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L63">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress: boolean;
```


Whether or not the Instance is associated with a public IP address or not (Boolean).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L67">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


The availability zone of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L71">property creditSpecifications</a>
</h3>

```typescript
creditSpecifications: { ... }[];
```


The credit specification of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L72">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L76">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices: { ... }[];
```


The EBS block device mappings of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L80">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized: boolean;
```


Whether the Instance is EBS optimized or not (Boolean).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L84">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices: { ... }[];
```


The ephemeral block device mappings of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L88">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile: string;
```


The name of the instance profile associated with the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L172">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L89">property instanceState</a>
</h3>

```typescript
instanceState: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L90">property instanceTags</a>
</h3>

```typescript
instanceTags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L94">property instanceType</a>
</h3>

```typescript
instanceType: string;
```


The type of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L98">property keyName</a>
</h3>

```typescript
keyName: string;
```


The key name of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L102">property monitoring</a>
</h3>

```typescript
monitoring: boolean;
```


Whether detailed monitoring is enabled or disabled for the Instance (Boolean).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L106">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: string;
```


The ID of the network interface that was created with the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L113">property passwordData</a>
</h3>

```typescript
passwordData: string;
```


Base-64 encoded encrypted password data for the instance.
Useful for getting the administrator password for instances running Microsoft Windows.
This attribute is only exported if `get_password_data` is true.
See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L117">property placementGroup</a>
</h3>

```typescript
placementGroup: string;
```


The placement group of the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L123">property privateDns</a>
</h3>

```typescript
privateDns: string;
```


The private DNS name assigned to the Instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L127">property privateIp</a>
</h3>

```typescript
privateIp: string;
```


The private IP address assigned to the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L132">property publicDns</a>
</h3>

```typescript
publicDns: string;
```


The public DNS name assigned to the Instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L136">property publicIp</a>
</h3>

```typescript
publicIp: string;
```


The public IP address assigned to the Instance, if applicable. **NOTE**: If you are using an [`aws_eip`](https://www.terraform.io/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address directly and not use `public_ip`, as this field will change after the EIP is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L140">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices: { ... }[];
```


The root block device mappings of the Instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L144">property securityGroups</a>
</h3>

```typescript
securityGroups: string[];
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L148">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck: boolean;
```


Whether the network interface performs source/destination checking (Boolean).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L152">property subnetId</a>
</h3>

```typescript
subnetId: string;
```


The VPC subnet ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L156">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L160">property tenancy</a>
</h3>

```typescript
tenancy: string;
```


The tenancy of the instance: `dedicated`, `default`, `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L164">property userData</a>
</h3>

```typescript
userData: string;
```


The User Data supplied to the Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstance.ts#L168">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds: string[];
```


The associated security groups in a non-default VPC.

<h2 class="pdoc-module-header" id="GetInstancesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L33">interface GetInstancesArgs</a>
</h2>

A collection of arguments for invoking getInstances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L39">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to use as filters. There are
several valid keys, for a full reference, check out
[describe-instances in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L43">property instanceStateNames</a>
</h3>

```typescript
instanceStateNames?: string[];
```


A list of instance states that should be applicable to the desired instances. The permitted values are: `pending, running, shutting-down, stopped, stopping, terminated`. The default value is `running`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L48">property instanceTags</a>
</h3>

```typescript
instanceTags?: { ... };
```


A mapping of tags, each pair of which must
exactly match a pair on desired instances.

<h2 class="pdoc-module-header" id="GetInstancesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L54">interface GetInstancesResult</a>
</h2>

A collection of values returned by getInstances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L71">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L58">property ids</a>
</h3>

```typescript
ids: string[];
```


IDs of instances found through the filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L59">property instanceTags</a>
</h3>

```typescript
instanceTags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L63">property privateIps</a>
</h3>

```typescript
privateIps: string[];
```


Private IP addresses of instances found through the filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInstances.ts#L67">property publicIps</a>
</h3>

```typescript
publicIps: string[];
```


Public IP addresses of instances found through the filter

<h2 class="pdoc-module-header" id="GetInternetGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L22">interface GetInternetGatewayArgs</a>
</h2>

A collection of arguments for invoking getInternetGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L30">property internetGatewayId</a>
</h3>

```typescript
internetGatewayId?: string;
```


The id of the specific Internet Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L35">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired Internet Gateway.

<h2 class="pdoc-module-header" id="GetInternetGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L41">interface GetInternetGatewayResult</a>
</h2>

A collection of values returned by getInternetGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L42">property attachments</a>
</h3>

```typescript
attachments: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L48">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L43">property internetGatewayId</a>
</h3>

```typescript
internetGatewayId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getInternetGateway.ts#L44">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetLaunchConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L19">interface GetLaunchConfigurationArgs</a>
</h2>

A collection of arguments for invoking getLaunchConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the launch configuration.

<h2 class="pdoc-module-header" id="GetLaunchConfigurationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L29">interface GetLaunchConfigurationResult</a>
</h2>

A collection of values returned by getLaunchConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L33">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress: boolean;
```


Whether a Public IP address is associated with the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L37">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices: { ... }[];
```


The EBS Block Devices attached to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L41">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized: boolean;
```


Whether the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L45">property enableMonitoring</a>
</h3>

```typescript
enableMonitoring: boolean;
```


Whether Detailed Monitoring is Enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L49">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices: { ... }[];
```


The Ephemeral volumes on the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L53">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile: string;
```


The IAM Instance Profile to associate with launched instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L97">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L57">property imageId</a>
</h3>

```typescript
imageId: string;
```


The EC2 Image ID of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L61">property instanceType</a>
</h3>

```typescript
instanceType: string;
```


The Instance Type of the instance to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L65">property keyName</a>
</h3>

```typescript
keyName: string;
```


The Key Name that should be used for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L69">property placementTenancy</a>
</h3>

```typescript
placementTenancy: string;
```


The Tenancy of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L73">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices: { ... }[];
```


The Root Block Device of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L77">property securityGroups</a>
</h3>

```typescript
securityGroups: string[];
```


A list of associated Security Group IDS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L81">property spotPrice</a>
</h3>

```typescript
spotPrice: string;
```


The Price to use for reserving Spot instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L85">property userData</a>
</h3>

```typescript
userData: string;
```


The User Data of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L89">property vpcClassicLinkId</a>
</h3>

```typescript
vpcClassicLinkId: string;
```


The ID of a ClassicLink-enabled VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getLaunchConfiguration.ts#L93">property vpcClassicLinkSecurityGroups</a>
</h3>

```typescript
vpcClassicLinkSecurityGroups: string[];
```


The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.

<h2 class="pdoc-module-header" id="GetNatGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L25">interface GetNatGatewayArgs</a>
</h2>

A collection of arguments for invoking getNatGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L31">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.
More complex filters can be expressed using one or more `filter` sub-blocks,
which take the following arguments:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L35">property id</a>
</h3>

```typescript
id?: string;
```


The id of the specific Nat Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L39">property state</a>
</h3>

```typescript
state?: string;
```


The state of the NAT gateway (pending | failed | available | deleting | deleted ).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L43">property subnetId</a>
</h3>

```typescript
subnetId?: string;
```


The id of subnet that the Nat Gateway resides in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L44">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L48">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The id of the VPC that the Nat Gateway resides in.

<h2 class="pdoc-module-header" id="GetNatGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L54">interface GetNatGatewayResult</a>
</h2>

A collection of values returned by getNatGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L58">property allocationId</a>
</h3>

```typescript
allocationId: string;
```


The Id of the EIP allocated to the selected Nat Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L59">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L63">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: string;
```


The Id of the ENI allocated to the selected Nat Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L67">property privateIp</a>
</h3>

```typescript
privateIp: string;
```


The private Ip address of the selected Nat Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L71">property publicIp</a>
</h3>

```typescript
publicIp: string;
```


The public Ip (EIP) address of the selected Nat Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L72">property state</a>
</h3>

```typescript
state: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L73">property subnetId</a>
</h3>

```typescript
subnetId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L74">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNatGateway.ts#L75">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetNetworkAclsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L19">interface GetNetworkAclsArgs</a>
</h2>

A collection of arguments for invoking getNetworkAcls.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L23">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L28">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired network ACLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L32">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The VPC ID that you want to filter from.

<h2 class="pdoc-module-header" id="GetNetworkAclsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L38">interface GetNetworkAclsResult</a>
</h2>

A collection of values returned by getNetworkAcls.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L42">property ids</a>
</h3>

```typescript
ids: string[];
```


A list of all the network ACL ids found. This data source will fail if none are found.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkAcls.ts#L43">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetNetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L22">interface GetNetworkInterfaceArgs</a>
</h2>

A collection of arguments for invoking getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to filter off of. There are several valid keys, for a full reference, check out [describe-network-interfaces](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-interfaces.html) in the AWS CLI reference.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L30">property id</a>
</h3>

```typescript
id?: string;
```


The identifier for the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetNetworkInterfaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L37">interface GetNetworkInterfaceResult</a>
</h2>

A collection of values returned by getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L41">property associations</a>
</h3>

```typescript
associations: { ... }[];
```


The association information for an Elastic IP address (IPv4) associated with the network interface. See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L42">property attachments</a>
</h3>

```typescript
attachments: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L46">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


The Availability Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L47">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L48">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L52">property interfaceType</a>
</h3>

```typescript
interfaceType: string;
```


The type of interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L56">property ipv6Addresses</a>
</h3>

```typescript
ipv6Addresses: string[];
```


List of IPv6 addresses to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L60">property macAddress</a>
</h3>

```typescript
macAddress: string;
```


The MAC address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L64">property ownerId</a>
</h3>

```typescript
ownerId: string;
```


The AWS account ID of the owner of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L65">property privateDnsName</a>
</h3>

```typescript
privateDnsName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L66">property privateIp</a>
</h3>

```typescript
privateIp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L67">property privateIps</a>
</h3>

```typescript
privateIps: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L71">property requesterId</a>
</h3>

```typescript
requesterId: string;
```


The ID of the entity that launched the instance on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L72">property securityGroups</a>
</h3>

```typescript
securityGroups: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L73">property subnetId</a>
</h3>

```typescript
subnetId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L74">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterface.ts#L75">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetNetworkInterfacesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L18">interface GetNetworkInterfacesArgs</a>
</h2>

A collection of arguments for invoking getNetworkInterfaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L22">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L27">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired network interfaces.

<h2 class="pdoc-module-header" id="GetNetworkInterfacesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L33">interface GetNetworkInterfacesResult</a>
</h2>

A collection of values returned by getNetworkInterfaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L42">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L37">property ids</a>
</h3>

```typescript
ids: string[];
```


A list of all the network interface ids found. This data source will fail if none are found.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getNetworkInterfaces.ts#L38">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetRouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L31">interface GetRouteArgs</a>
</h2>

A collection of arguments for invoking getRoute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L35">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock?: string;
```


The CIDR block of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L39">property destinationIpv6CidrBlock</a>
</h3>

```typescript
destinationIpv6CidrBlock?: string;
```


The IPv6 CIDR block of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L43">property egressOnlyGatewayId</a>
</h3>

```typescript
egressOnlyGatewayId?: string;
```


The Egress Only Gateway ID of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L47">property gatewayId</a>
</h3>

```typescript
gatewayId?: string;
```


The Gateway ID of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L51">property instanceId</a>
</h3>

```typescript
instanceId?: string;
```


The Instance ID of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L55">property natGatewayId</a>
</h3>

```typescript
natGatewayId?: string;
```


The NAT Gateway ID of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L59">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: string;
```


The Network Interface ID of the Route belonging to the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L63">property routeTableId</a>
</h3>

```typescript
routeTableId: string;
```


The id of the specific Route Table containing the Route entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L67">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId?: string;
```


The VPC Peering Connection ID of the Route belonging to the Route Table.

<h2 class="pdoc-module-header" id="GetRouteResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L73">interface GetRouteResult</a>
</h2>

A collection of values returned by getRoute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L74">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L75">property destinationIpv6CidrBlock</a>
</h3>

```typescript
destinationIpv6CidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L76">property egressOnlyGatewayId</a>
</h3>

```typescript
egressOnlyGatewayId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L77">property gatewayId</a>
</h3>

```typescript
gatewayId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L85">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L78">property instanceId</a>
</h3>

```typescript
instanceId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L79">property natGatewayId</a>
</h3>

```typescript
natGatewayId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L80">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRoute.ts#L81">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId: string;
```

<h2 class="pdoc-module-header" id="GetRouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L28">interface GetRouteTableArgs</a>
</h2>

A collection of arguments for invoking getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L32">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L36">property routeTableId</a>
</h3>

```typescript
routeTableId?: string;
```


The id of the specific Route Table to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L40">property subnetId</a>
</h3>

```typescript
subnetId?: string;
```


The id of a Subnet which is connected to the Route Table (not be exported if not given in parameter).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L45">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L49">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The id of the VPC that the desired Route Table belongs to.

<h2 class="pdoc-module-header" id="GetRouteTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L55">interface GetRouteTableResult</a>
</h2>

A collection of values returned by getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L56">property associations</a>
</h3>

```typescript
associations: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L71">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L60">property routeTableId</a>
</h3>

```typescript
routeTableId: string;
```


The Route Table ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L61">property routes</a>
</h3>

```typescript
routes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L65">property subnetId</a>
</h3>

```typescript
subnetId: string;
```


The Subnet ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L66">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTable.ts#L67">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetRouteTablesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L22">interface GetRouteTablesArgs</a>
</h2>

A collection of arguments for invoking getRouteTables.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired route tables.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L35">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The VPC ID that you want to filter from.

<h2 class="pdoc-module-header" id="GetRouteTablesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L41">interface GetRouteTablesResult</a>
</h2>

A collection of values returned by getRouteTables.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L45">property ids</a>
</h3>

```typescript
ids: string[];
```


A list of all the route table ids found. This data source will fail if none are found.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getRouteTables.ts#L46">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L28">interface GetSecurityGroupArgs</a>
</h2>

A collection of arguments for invoking getSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L32">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L36">property id</a>
</h3>

```typescript
id?: string;
```


The id of the specific security group to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L41">property name</a>
</h3>

```typescript
name?: string;
```


The name of the field to filter by, as defined by
[the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L46">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L50">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The id of the VPC that the desired security group belongs to.

<h2 class="pdoc-module-header" id="GetSecurityGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L56">interface GetSecurityGroupResult</a>
</h2>

A collection of values returned by getSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L60">property arn</a>
</h3>

```typescript
arn: string;
```


The computed ARN of the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L64">property description</a>
</h3>

```typescript
description: string;
```


The description of the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L65">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L66">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L67">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroup.ts#L68">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetSecurityGroupsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L22">interface GetSecurityGroupsArgs</a>
</h2>

A collection of arguments for invoking getSecurityGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L28">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to use as filters. There are
several valid keys, for a full reference, check out
[describe-security-groups in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L33">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match for
desired security groups.

<h2 class="pdoc-module-header" id="GetSecurityGroupsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L39">interface GetSecurityGroupsResult</a>
</h2>

A collection of values returned by getSecurityGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L43">property ids</a>
</h3>

```typescript
ids: string[];
```


IDs of the matches security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L44">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSecurityGroups.ts#L49">property vpcIds</a>
</h3>

```typescript
vpcIds: string[];
```


The VPC IDs of the matched security groups. The data source's tag or filter *will span VPCs*
unless the `vpc-id` filter is also used.

<h2 class="pdoc-module-header" id="GetSubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L32">interface GetSubnetArgs</a>
</h2>

A collection of arguments for invoking getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L37">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: string;
```


The availability zone where the
subnet must reside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L41">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: string;
```


The cidr block of the desired subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L46">property defaultForAz</a>
</h3>

```typescript
defaultForAz?: boolean;
```


Boolean constraint for whether the desired
subnet must be the default subnet for its associated availability zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L50">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L54">property id</a>
</h3>

```typescript
id?: string;
```


The id of the specific subnet to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L58">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: string;
```


The Ipv6 cidr block of the desired subnet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L62">property state</a>
</h3>

```typescript
state?: string;
```


The state that the desired subnet must have.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L67">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L71">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The id of the VPC that the desired subnet belongs to.

<h2 class="pdoc-module-header" id="GetSubnetIdsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L23">interface GetSubnetIdsArgs</a>
</h2>

A collection of arguments for invoking getSubnetIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L24">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L29">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L33">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


The VPC ID that you want to filter from.

<h2 class="pdoc-module-header" id="GetSubnetIdsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L39">interface GetSubnetIdsResult</a>
</h2>

A collection of values returned by getSubnetIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L48">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L43">property ids</a>
</h3>

```typescript
ids: string[];
```


A list of all the subnet ids found. This data source will fail if none are found.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnetIds.ts#L44">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetSubnetResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L77">interface GetSubnetResult</a>
</h2>

A collection of values returned by getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L81">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L82">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
assignIpv6AddressOnCreation: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L83">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L84">property cidrBlock</a>
</h3>

```typescript
cidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L85">property defaultForAz</a>
</h3>

```typescript
defaultForAz: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L86">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L87">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L88">property ipv6CidrBlockAssociationId</a>
</h3>

```typescript
ipv6CidrBlockAssociationId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L89">property mapPublicIpOnLaunch</a>
</h3>

```typescript
mapPublicIpOnLaunch: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L90">property state</a>
</h3>

```typescript
state: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L91">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getSubnet.ts#L92">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetVpcArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L30">interface GetVpcArgs</a>
</h2>

A collection of arguments for invoking getVpc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L34">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: string;
```


The cidr block of the desired VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L39">property default</a>
</h3>

```typescript
default?: boolean;
```


Boolean constraint on whether the desired VPC is
the default VPC for the region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L43">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId?: string;
```


The DHCP options id of the desired VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L47">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L51">property id</a>
</h3>

```typescript
id?: string;
```


The id of the specific VPC to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L56">property state</a>
</h3>

```typescript
state?: string;
```


The current state of the desired VPC.
Can be either `"pending"` or `"available"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L61">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired VPC.

<h2 class="pdoc-module-header" id="GetVpcDhcpOptionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L22">interface GetVpcDhcpOptionsArgs</a>
</h2>

A collection of arguments for invoking getVpcDhcpOptions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L26">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId?: string;
```


The EC2 DHCP Options ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L30">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


List of custom filters as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetVpcDhcpOptionsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L37">interface GetVpcDhcpOptionsResult</a>
</h2>

A collection of values returned by getVpcDhcpOptions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L41">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId: string;
```


EC2 DHCP Options ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L45">property domainName</a>
</h3>

```typescript
domainName: string;
```


The suffix domain name to used when resolving non Fully Qualified Domain Names. e.g. the `search` value in the `/etc/resolv.conf` file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L49">property domainNameServers</a>
</h3>

```typescript
domainNameServers: string[];
```


List of name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L69">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L53">property netbiosNameServers</a>
</h3>

```typescript
netbiosNameServers: string[];
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L57">property netbiosNodeType</a>
</h3>

```typescript
netbiosNodeType: string;
```


The NetBIOS node type (1, 2, 4, or 8). For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L61">property ntpServers</a>
</h3>

```typescript
ntpServers: string[];
```


List of NTP servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcDhcpOptions.ts#L65">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetVpcEndpointArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L24">interface GetVpcEndpointArgs</a>
</h2>

A collection of arguments for invoking getVpcEndpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L28">property id</a>
</h3>

```typescript
id?: string;
```


The ID of the specific VPC Endpoint to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L32">property serviceName</a>
</h3>

```typescript
serviceName?: string;
```


The AWS service name of the specific VPC Endpoint to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L36">property state</a>
</h3>

```typescript
state?: string;
```


The state of the specific VPC Endpoint to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L40">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The ID of the VPC in which the specific VPC Endpoint is used.

<h2 class="pdoc-module-header" id="GetVpcEndpointResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L46">interface GetVpcEndpointResult</a>
</h2>

A collection of values returned by getVpcEndpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L50">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks: string[];
```


The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L54">property dnsEntries</a>
</h3>

```typescript
dnsEntries: { ... }[];
```


The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L55">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L59">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds: string[];
```


One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L63">property policy</a>
</h3>

```typescript
policy: string;
```


The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L67">property prefixListId</a>
</h3>

```typescript
prefixListId: string;
```


The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L71">property privateDnsEnabled</a>
</h3>

```typescript
privateDnsEnabled: boolean;
```


Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L75">property routeTableIds</a>
</h3>

```typescript
routeTableIds: string[];
```


One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L79">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds: string[];
```


One or more security groups associated with the network interfaces. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L80">property serviceName</a>
</h3>

```typescript
serviceName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L81">property state</a>
</h3>

```typescript
state: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L85">property subnetIds</a>
</h3>

```typescript
subnetIds: string[];
```


One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L89">property vpcEndpointType</a>
</h3>

```typescript
vpcEndpointType: string;
```


The VPC Endpoint type, `Gateway` or `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpoint.ts#L90">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetVpcEndpointServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L22">interface GetVpcEndpointServiceArgs</a>
</h2>

A collection of arguments for invoking getVpcEndpointService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L26">property service</a>
</h3>

```typescript
service?: string;
```


The common name of an AWS service (e.g. `s3`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L30">property serviceName</a>
</h3>

```typescript
serviceName?: string;
```


The service name that can be specified when creating a VPC endpoint.

<h2 class="pdoc-module-header" id="GetVpcEndpointServiceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L36">interface GetVpcEndpointServiceResult</a>
</h2>

A collection of values returned by getVpcEndpointService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L40">property acceptanceRequired</a>
</h3>

```typescript
acceptanceRequired: boolean;
```


Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L44">property availabilityZones</a>
</h3>

```typescript
availabilityZones: string[];
```


The Availability Zones in which the service is available.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L48">property baseEndpointDnsNames</a>
</h3>

```typescript
baseEndpointDnsNames: string[];
```


The DNS names for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L69">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L52">property owner</a>
</h3>

```typescript
owner: string;
```


The AWS account ID of the service owner or `amazon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L56">property privateDnsName</a>
</h3>

```typescript
privateDnsName: string;
```


The private DNS name for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L57">property serviceName</a>
</h3>

```typescript
serviceName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L61">property serviceType</a>
</h3>

```typescript
serviceType: string;
```


The service type, `Gateway` or `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcEndpointService.ts#L65">property vpcEndpointPolicySupported</a>
</h3>

```typescript
vpcEndpointPolicySupported: boolean;
```


Whether or not the service supports endpoint policies - `true` or `false`.

<h2 class="pdoc-module-header" id="GetVpcPeeringConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L32">interface GetVpcPeeringConnectionArgs</a>
</h2>

A collection of arguments for invoking getVpcPeeringConnection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L36">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: string;
```


The CIDR block of the requester VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L40">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L44">property id</a>
</h3>

```typescript
id?: string;
```


The ID of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L48">property ownerId</a>
</h3>

```typescript
ownerId?: string;
```


The AWS account ID of the owner of the requester VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L52">property peerCidrBlock</a>
</h3>

```typescript
peerCidrBlock?: string;
```


The CIDR block of the accepter VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L56">property peerOwnerId</a>
</h3>

```typescript
peerOwnerId?: string;
```


The AWS account ID of the owner of the accepter VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L60">property peerRegion</a>
</h3>

```typescript
peerRegion?: string;
```


The region of the accepter VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L64">property peerVpcId</a>
</h3>

```typescript
peerVpcId?: string;
```


The ID of the accepter VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L68">property region</a>
</h3>

```typescript
region?: string;
```


The region of the requester VPC of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L72">property status</a>
</h3>

```typescript
status?: string;
```


The status of the specific VPC Peering Connection to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L77">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired VPC Peering Connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L81">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


The ID of the requester VPC of the specific VPC Peering Connection to retrieve.

<h2 class="pdoc-module-header" id="GetVpcPeeringConnectionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L87">interface GetVpcPeeringConnectionResult</a>
</h2>

A collection of values returned by getVpcPeeringConnection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L92">property accepter</a>
</h3>

```typescript
accepter: { ... };
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L93">property cidrBlock</a>
</h3>

```typescript
cidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L94">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L95">property ownerId</a>
</h3>

```typescript
ownerId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L96">property peerCidrBlock</a>
</h3>

```typescript
peerCidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L97">property peerOwnerId</a>
</h3>

```typescript
peerOwnerId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L98">property peerRegion</a>
</h3>

```typescript
peerRegion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L99">property peerVpcId</a>
</h3>

```typescript
peerVpcId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L100">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L105">property requester</a>
</h3>

```typescript
requester: { ... };
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L106">property status</a>
</h3>

```typescript
status: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L107">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcPeeringConnection.ts#L108">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h2 class="pdoc-module-header" id="GetVpcResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L67">interface GetVpcResult</a>
</h2>

A collection of values returned by getVpc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L71">property arn</a>
</h3>

```typescript
arn: string;
```


Amazon Resource Name (ARN) of VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L75">property cidrBlock</a>
</h3>

```typescript
cidrBlock: string;
```


The CIDR block for the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L76">property cidrBlockAssociations</a>
</h3>

```typescript
cidrBlockAssociations: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L77">property default</a>
</h3>

```typescript
default: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L78">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L82">property enableDnsHostnames</a>
</h3>

```typescript
enableDnsHostnames: boolean;
```


Whether or not the VPC has DNS hostname support

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L86">property enableDnsSupport</a>
</h3>

```typescript
enableDnsSupport: boolean;
```


Whether or not the VPC has DNS support

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L87">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L92">property instanceTenancy</a>
</h3>

```typescript
instanceTenancy: string;
```


The allowed tenancy of instances launched into the
selected VPC. May be any of `"default"`, `"dedicated"`, or `"host"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L96">property ipv6AssociationId</a>
</h3>

```typescript
ipv6AssociationId: string;
```


The association ID for the IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L100">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock: string;
```


The IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L104">property state</a>
</h3>

```typescript
state: string;
```


The State of the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpc.ts#L105">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetVpcsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L23">interface GetVpcsArgs</a>
</h2>

A collection of arguments for invoking getVpcs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L27">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L32">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired vpcs.

<h2 class="pdoc-module-header" id="GetVpcsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L38">interface GetVpcsResult</a>
</h2>

A collection of values returned by getVpcs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L42">property ids</a>
</h3>

```typescript
ids: string[];
```


A list of all the VPC Ids found. This data source will fail if none are found.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpcs.ts#L43">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="GetVpnGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L27">interface GetVpnGatewayArgs</a>
</h2>

A collection of arguments for invoking getVpnGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L31">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: string;
```


The Autonomous System Number (ASN) for the Amazon side of the specific VPN Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L35">property attachedVpcId</a>
</h3>

```typescript
attachedVpcId?: string;
```


The ID of a VPC attached to the specific VPN Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L39">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: string;
```


The Availability Zone of the specific VPN Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L43">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


Custom filter block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L47">property id</a>
</h3>

```typescript
id?: string;
```


The ID of the specific VPN Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L51">property state</a>
</h3>

```typescript
state?: string;
```


The state of the specific VPN Gateway to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L56">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match
a pair on the desired VPN Gateway.

<h2 class="pdoc-module-header" id="GetVpnGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L62">interface GetVpnGatewayResult</a>
</h2>

A collection of values returned by getVpnGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L63">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L64">property attachedVpcId</a>
</h3>

```typescript
attachedVpcId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L65">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L66">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L67">property state</a>
</h3>

```typescript
state: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/getVpnGateway.ts#L68">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L488">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L492">property ami</a>
</h3>

```typescript
ami: pulumi.Input<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L496">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L500">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L506">property cpuCoreCount</a>
</h3>

```typescript
cpuCoreCount?: pulumi.Input<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L510">property cpuThreadsPerCore</a>
</h3>

```typescript
cpuThreadsPerCore?: pulumi.Input<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L514">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L519">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L524">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L532">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L537">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L541">property getPasswordData</a>
</h3>

```typescript
getPasswordData?: pulumi.Input<boolean>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L547">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L554">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L558">property instanceType</a>
</h3>

```typescript
instanceType: pulumi.Input<InstanceType>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L559">property ipv6AddressCount</a>
</h3>

```typescript
ipv6AddressCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L563">property ipv6Addresses</a>
</h3>

```typescript
ipv6Addresses?: pulumi.Input<pulumi.Input<string>[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L567">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L571">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L575">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L579">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L584">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L589">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L593">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L598">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L602">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L606">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L610">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L614">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L618">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L622">property volumeTags</a>
</h3>

```typescript
volumeTags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L626">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L308">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L312">property ami</a>
</h3>

```typescript
ami?: pulumi.Input<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L316">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L320">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L324">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L330">property cpuCoreCount</a>
</h3>

```typescript
cpuCoreCount?: pulumi.Input<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L334">property cpuThreadsPerCore</a>
</h3>

```typescript
cpuThreadsPerCore?: pulumi.Input<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L338">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L343">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L348">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L356">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L361">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L365">property getPasswordData</a>
</h3>

```typescript
getPasswordData?: pulumi.Input<boolean>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L371">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L378">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L379">property instanceState</a>
</h3>

```typescript
instanceState?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L383">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<InstanceType>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L384">property ipv6AddressCount</a>
</h3>

```typescript
ipv6AddressCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L388">property ipv6Addresses</a>
</h3>

```typescript
ipv6Addresses?: pulumi.Input<pulumi.Input<string>[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L392">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L396">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L404">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the network interface that was created with the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L400">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L412">property passwordData</a>
</h3>

```typescript
passwordData?: pulumi.Input<string>;
```


Base-64 encoded encrypted password data for the instance.
Useful for getting the administrator password for instances running Microsoft Windows.
This attribute is only exported if `get_password_data` is true.
Note that this encrypted value will be stored in the state file, as with all exported attributes.
See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L416">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L420">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```


The ID of the instance's primary network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L426">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L431">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L436">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L440">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable. **NOTE**: If you are using an [`aws_eip`](https://www.terraform.io/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address directly and not use `public_ip`, as this field will change after the EIP is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L445">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L449">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L454">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L458">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L462">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L466">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L470">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L474">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L478">property volumeTags</a>
</h3>

```typescript
volumeTags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instance.ts#L482">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="InternetGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L74">interface InternetGatewayArgs</a>
</h2>

The set of arguments for constructing a InternetGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L78">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L82">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="InternetGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L60">interface InternetGatewayState</a>
</h2>

Input properties used for looking up and filtering InternetGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L64">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/internetGateway.ts#L68">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="KeyPairArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L103">interface KeyPairArgs</a>
</h2>

The set of arguments for constructing a KeyPair resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L107">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The name for the key pair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L111">property keyNamePrefix</a>
</h3>

```typescript
keyNamePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L115">property publicKey</a>
</h3>

```typescript
publicKey: pulumi.Input<string>;
```


The public key material.

<h2 class="pdoc-module-header" id="KeyPairState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L81">interface KeyPairState</a>
</h2>

Input properties used for looking up and filtering KeyPair resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L85">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The MD5 public key fingerprint as specified in section 4 of RFC 4716.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L89">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The name for the key pair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L93">property keyNamePrefix</a>
</h3>

```typescript
keyNamePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/keyPair.ts#L97">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


The public key material.

<h2 class="pdoc-module-header" id="LaunchConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L264">interface LaunchConfigurationArgs</a>
</h2>

The set of arguments for constructing a LaunchConfiguration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L268">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L273">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L277">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L281">property enableMonitoring</a>
</h3>

```typescript
enableMonitoring?: pulumi.Input<boolean>;
```


Enables/disables detailed monitoring. This is enabled by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L286">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L291">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM instance profile to associate
with launched instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L295">property imageId</a>
</h3>

```typescript
imageId: pulumi.Input<string>;
```


The EC2 image ID to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L299">property instanceType</a>
</h3>

```typescript
instanceType: pulumi.Input<string>;
```


The size of instance to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L303">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name that should be used for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L308">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the launch configuration. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L313">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L319">property placementTenancy</a>
</h3>

```typescript
placementTenancy?: pulumi.Input<string>;
```


The tenancy of the instance. Valid values are
`"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L324">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L328">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of associated security group IDS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L332">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum price to use for reserving spot instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L336">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L340">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L344">property vpcClassicLinkId</a>
</h3>

```typescript
vpcClassicLinkId?: pulumi.Input<string>;
```


The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L348">property vpcClassicLinkSecurityGroups</a>
</h3>

```typescript
vpcClassicLinkSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).

<h2 class="pdoc-module-header" id="LaunchConfigurationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L174">interface LaunchConfigurationState</a>
</h2>

Input properties used for looking up and filtering LaunchConfiguration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L178">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L183">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L187">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L191">property enableMonitoring</a>
</h3>

```typescript
enableMonitoring?: pulumi.Input<boolean>;
```


Enables/disables detailed monitoring. This is enabled by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L196">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L201">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM instance profile to associate
with launched instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L205">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The EC2 image ID to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L209">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The size of instance to launch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L213">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name that should be used for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L218">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the launch configuration. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L223">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L229">property placementTenancy</a>
</h3>

```typescript
placementTenancy?: pulumi.Input<string>;
```


The tenancy of the instance. Valid values are
`"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L234">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L238">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of associated security group IDS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L242">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum price to use for reserving spot instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L246">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L250">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L254">property vpcClassicLinkId</a>
</h3>

```typescript
vpcClassicLinkId?: pulumi.Input<string>;
```


The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchConfiguration.ts#L258">property vpcClassicLinkSecurityGroups</a>
</h3>

```typescript
vpcClassicLinkSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).

<h2 class="pdoc-module-header" id="LaunchTemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L342">interface LaunchTemplateArgs</a>
</h2>

The set of arguments for constructing a LaunchTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L347">property blockDeviceMappings</a>
</h3>

```typescript
blockDeviceMappings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L352">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit
Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L356">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L361">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L365">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If `true`, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L370">property elasticGpuSpecifications</a>
</h3>

```typescript
elasticGpuSpecifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The elastic GPU to attach to the instance. See Elastic GPU
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L375">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<{ ... }>;
```


The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L379">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The AMI from which to launch the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L384">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L389">property instanceMarketOptions</a>
</h3>

```typescript
instanceMarketOptions?: pulumi.Input<{ ... }>;
```


The market (purchasing) option for the instance. See Market Options
below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L393">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L397">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The kernel ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L401">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L405">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<{ ... }>;
```


The monitoring option for the instance. See Monitoring below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L409">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the launch template. If you leave this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L413">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L418">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L422">property placement</a>
</h3>

```typescript
placement?: pulumi.Input<{ ... }>;
```


The placement of the instance. See Placement below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L426">property ramDiskId</a>
</h3>

```typescript
ramDiskId?: pulumi.Input<string>;
```


The ID of the RAM disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L431">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L435">property tagSpecifications</a>
</h3>

```typescript
tagSpecifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The tags to apply to the resources during launch. See Tags below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L439">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L443">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The Base64-encoded user data to provide when launching the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L447">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="LaunchTemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L219">interface LaunchTemplateState</a>
</h2>

Input properties used for looking up and filtering LaunchTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L223">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L228">property blockDeviceMappings</a>
</h3>

```typescript
blockDeviceMappings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L233">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit
Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L237">property defaultVersion</a>
</h3>

```typescript
defaultVersion?: pulumi.Input<number>;
```


The default version of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L241">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L246">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L250">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If `true`, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L255">property elasticGpuSpecifications</a>
</h3>

```typescript
elasticGpuSpecifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The elastic GPU to attach to the instance. See Elastic GPU
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L260">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<{ ... }>;
```


The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L264">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The AMI from which to launch the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L269">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L274">property instanceMarketOptions</a>
</h3>

```typescript
instanceMarketOptions?: pulumi.Input<{ ... }>;
```


The market (purchasing) option for the instance. See Market Options
below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L278">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L282">property kernelId</a>
</h3>

```typescript
kernelId?: pulumi.Input<string>;
```


The kernel ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L286">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L290">property latestVersion</a>
</h3>

```typescript
latestVersion?: pulumi.Input<number>;
```


The latest version of the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L294">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<{ ... }>;
```


The monitoring option for the instance. See Monitoring below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L298">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the launch template. If you leave this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L302">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L307">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L311">property placement</a>
</h3>

```typescript
placement?: pulumi.Input<{ ... }>;
```


The placement of the instance. See Placement below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L315">property ramDiskId</a>
</h3>

```typescript
ramDiskId?: pulumi.Input<string>;
```


The ID of the RAM disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L320">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L324">property tagSpecifications</a>
</h3>

```typescript
tagSpecifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The tags to apply to the resources during launch. See Tags below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L328">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the launch template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L332">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The Base64-encoded user data to provide when launching the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/launchTemplate.ts#L336">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h2 class="pdoc-module-header" id="MainRouteTableAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L90">interface MainRouteTableAssociationArgs</a>
</h2>

The set of arguments for constructing a MainRouteTableAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L95">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The ID of the Route Table to set as the new
main route table for the target VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L99">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the VPC whose main route table should be set

<h2 class="pdoc-module-header" id="MainRouteTableAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L71">interface MainRouteTableAssociationState</a>
</h2>

Input properties used for looking up and filtering MainRouteTableAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L75">property originalRouteTableId</a>
</h3>

```typescript
originalRouteTableId?: pulumi.Input<string>;
```


Used internally, see __Notes__ below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L80">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table to set as the new
main route table for the target VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/mainRouteTableAssociation.ts#L84">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the VPC whose main route table should be set

<h2 class="pdoc-module-header" id="NatGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L120">interface NatGatewayArgs</a>
</h2>

The set of arguments for constructing a NatGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L124">property allocationId</a>
</h3>

```typescript
allocationId: pulumi.Input<string>;
```


The Allocation ID of the Elastic IP address for the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L128">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ENI ID of the network interface created by the NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L132">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L136">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L140">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The Subnet ID of the subnet in which to place the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L144">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NatGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L90">interface NatGatewayState</a>
</h2>

Input properties used for looking up and filtering NatGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L94">property allocationId</a>
</h3>

```typescript
allocationId?: pulumi.Input<string>;
```


The Allocation ID of the Elastic IP address for the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L98">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ENI ID of the network interface created by the NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L102">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L106">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address of the NAT Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L110">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The Subnet ID of the subnet in which to place the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/natGateway.ts#L114">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkAclArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L126">interface NetworkAclArgs</a>
</h2>

The set of arguments for constructing a NetworkAcl resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L130">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L134">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L139">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the associated Subnet. This
attribute is deprecated, please use the `subnet_ids` attribute instead

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L143">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subnet IDs to apply the ACL to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L147">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L151">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the associated VPC.

<h2 class="pdoc-module-header" id="NetworkAclRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L180">interface NetworkAclRuleArgs</a>
</h2>

The set of arguments for constructing a NetworkAclRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L184">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L188">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<boolean>;
```


Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L192">property fromPort</a>
</h3>

```typescript
fromPort?: pulumi.Input<number>;
```


The from port to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L196">property icmpCode</a>
</h3>

```typescript
icmpCode?: pulumi.Input<string>;
```


ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L200">property icmpType</a>
</h3>

```typescript
icmpType?: pulumi.Input<string>;
```


ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L204">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 CIDR block to allow or deny.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L208">property networkAclId</a>
</h3>

```typescript
networkAclId: pulumi.Input<string>;
```


The ID of the network ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L212">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol. A value of -1 means all protocols.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L216">property ruleAction</a>
</h3>

```typescript
ruleAction: pulumi.Input<string>;
```


Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L220">property ruleNumber</a>
</h3>

```typescript
ruleNumber: pulumi.Input<number>;
```


The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L224">property toPort</a>
</h3>

```typescript
toPort?: pulumi.Input<number>;
```


The to port to match.

<h2 class="pdoc-module-header" id="NetworkAclRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L130">interface NetworkAclRuleState</a>
</h2>

Input properties used for looking up and filtering NetworkAclRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L134">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L138">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<boolean>;
```


Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L142">property fromPort</a>
</h3>

```typescript
fromPort?: pulumi.Input<number>;
```


The from port to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L146">property icmpCode</a>
</h3>

```typescript
icmpCode?: pulumi.Input<string>;
```


ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L150">property icmpType</a>
</h3>

```typescript
icmpType?: pulumi.Input<string>;
```


ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L154">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 CIDR block to allow or deny.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L158">property networkAclId</a>
</h3>

```typescript
networkAclId?: pulumi.Input<string>;
```


The ID of the network ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L162">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol. A value of -1 means all protocols.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L166">property ruleAction</a>
</h3>

```typescript
ruleAction?: pulumi.Input<string>;
```


Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L170">property ruleNumber</a>
</h3>

```typescript
ruleNumber?: pulumi.Input<number>;
```


The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAclRule.ts#L174">property toPort</a>
</h3>

```typescript
toPort?: pulumi.Input<number>;
```


The to port to match.

<h2 class="pdoc-module-header" id="NetworkAclState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L95">interface NetworkAclState</a>
</h2>

Input properties used for looking up and filtering NetworkAcl resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L99">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an egress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L103">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an ingress rule. Parameters defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L108">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the associated Subnet. This
attribute is deprecated, please use the `subnet_ids` attribute instead

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L112">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subnet IDs to apply the ACL to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L116">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkAcl.ts#L120">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the associated VPC.

<h2 class="pdoc-module-header" id="NetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L145">interface NetworkInterfaceArgs</a>
</h2>

The set of arguments for constructing a NetworkInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L149">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Block to define the attachment of the ENI. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L153">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L154">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L158">property privateIps</a>
</h3>

```typescript
privateIps?: pulumi.Input<pulumi.Input<string>[]>;
```


List of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L162">property privateIpsCount</a>
</h3>

```typescript
privateIpsCount?: pulumi.Input<number>;
```


Number of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L166">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of security group IDs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L170">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Whether to enable source destination checking for the ENI. Default true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L174">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


Subnet ID to create the ENI in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkInterfaceAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L111">interface NetworkInterfaceAttachmentArgs</a>
</h2>

The set of arguments for constructing a NetworkInterfaceAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L115">property deviceIndex</a>
</h3>

```typescript
deviceIndex: pulumi.Input<number>;
```


Network interface index (int).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L119">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


Instance ID to attach.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L123">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


ENI ID to attach.

<h2 class="pdoc-module-header" id="NetworkInterfaceAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L85">interface NetworkInterfaceAttachmentState</a>
</h2>

Input properties used for looking up and filtering NetworkInterfaceAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L89">property attachmentId</a>
</h3>

```typescript
attachmentId?: pulumi.Input<string>;
```


The ENI Attachment ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L93">property deviceIndex</a>
</h3>

```typescript
deviceIndex?: pulumi.Input<number>;
```


Network interface index (int).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L97">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


Instance ID to attach.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L101">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


ENI ID to attach.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceAttachment.ts#L105">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status of the Network Interface Attachment.

<h2 class="pdoc-module-header" id="NetworkInterfaceSecurityGroupAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L90">interface NetworkInterfaceSecurityGroupAttachmentArgs</a>
</h2>

The set of arguments for constructing a NetworkInterfaceSecurityGroupAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L94">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


The ID of the network interface to attach to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L98">property securityGroupId</a>
</h3>

```typescript
securityGroupId: pulumi.Input<string>;
```


The ID of the security group.

<h2 class="pdoc-module-header" id="NetworkInterfaceSecurityGroupAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L76">interface NetworkInterfaceSecurityGroupAttachmentState</a>
</h2>

Input properties used for looking up and filtering NetworkInterfaceSecurityGroupAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L80">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the network interface to attach to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterfaceSecurityGroupAttachment.ts#L84">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The ID of the security group.

<h2 class="pdoc-module-header" id="NetworkInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L105">interface NetworkInterfaceState</a>
</h2>

Input properties used for looking up and filtering NetworkInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L109">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Block to define the attachment of the ENI. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L113">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L114">property privateDnsName</a>
</h3>

```typescript
privateDnsName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L115">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L119">property privateIps</a>
</h3>

```typescript
privateIps?: pulumi.Input<pulumi.Input<string>[]>;
```


List of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L123">property privateIpsCount</a>
</h3>

```typescript
privateIpsCount?: pulumi.Input<number>;
```


Number of private IPs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L127">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of security group IDs to assign to the ENI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L131">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Whether to enable source destination checking for the ENI. Default true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L135">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to create the ENI in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/networkInterface.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PeeringConnectionOptionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L169">interface PeeringConnectionOptionsArgs</a>
</h2>

The set of arguments for constructing a PeeringConnectionOptions resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L175">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L181">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L185">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId: pulumi.Input<string>;
```


The ID of the requester VPC peering connection.

<h2 class="pdoc-module-header" id="PeeringConnectionOptionsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L147">interface PeeringConnectionOptionsState</a>
</h2>

Input properties used for looking up and filtering PeeringConnectionOptions resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L153">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L159">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/peeringConnectionOptions.ts#L163">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId?: pulumi.Input<string>;
```


The ID of the requester VPC peering connection.

<h2 class="pdoc-module-header" id="PlacementGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L76">interface PlacementGroupArgs</a>
</h2>

The set of arguments for constructing a PlacementGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the placement group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L84">property strategy</a>
</h3>

```typescript
strategy: pulumi.Input<string>;
```


The placement strategy.

<h2 class="pdoc-module-header" id="PlacementGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L62">interface PlacementGroupState</a>
</h2>

Input properties used for looking up and filtering PlacementGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L66">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the placement group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/placementGroup.ts#L70">property strategy</a>
</h3>

```typescript
strategy?: pulumi.Input<string>;
```


The placement strategy.

<h2 class="pdoc-module-header" id="ProxyProtocolPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L82">interface ProxyProtocolPolicyArgs</a>
</h2>

The set of arguments for constructing a ProxyProtocolPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L87">property instancePorts</a>
</h3>

```typescript
instancePorts: pulumi.Input<pulumi.Input<string>[]>;
```


List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L92">property loadBalancer</a>
</h3>

```typescript
loadBalancer: pulumi.Input<string>;
```


The load balancer to which the policy
should be attached.

<h2 class="pdoc-module-header" id="ProxyProtocolPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L66">interface ProxyProtocolPolicyState</a>
</h2>

Input properties used for looking up and filtering ProxyProtocolPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L71">property instancePorts</a>
</h3>

```typescript
instancePorts?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/proxyProtocolPolicy.ts#L76">property loadBalancer</a>
</h3>

```typescript
loadBalancer?: pulumi.Input<string>;
```


The load balancer to which the policy
should be attached.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L167">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L171">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock?: pulumi.Input<string>;
```


The destination CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L175">property destinationIpv6CidrBlock</a>
</h3>

```typescript
destinationIpv6CidrBlock?: pulumi.Input<string>;
```


The destination IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L179">property egressOnlyGatewayId</a>
</h3>

```typescript
egressOnlyGatewayId?: pulumi.Input<string>;
```


An ID of a VPC Egress Only Internet Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L183">property gatewayId</a>
</h3>

```typescript
gatewayId?: pulumi.Input<string>;
```


An ID of a VPC internet gateway or a virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L187">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


An ID of an EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L191">property natGatewayId</a>
</h3>

```typescript
natGatewayId?: pulumi.Input<string>;
```


An ID of a VPC NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L195">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


An ID of a network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L199">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The ID of the routing table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L203">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId?: pulumi.Input<string>;
```


An ID of a VPC peering connection.

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L121">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L125">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock?: pulumi.Input<string>;
```


The destination CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L129">property destinationIpv6CidrBlock</a>
</h3>

```typescript
destinationIpv6CidrBlock?: pulumi.Input<string>;
```


The destination IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L130">property destinationPrefixListId</a>
</h3>

```typescript
destinationPrefixListId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L134">property egressOnlyGatewayId</a>
</h3>

```typescript
egressOnlyGatewayId?: pulumi.Input<string>;
```


An ID of a VPC Egress Only Internet Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L138">property gatewayId</a>
</h3>

```typescript
gatewayId?: pulumi.Input<string>;
```


An ID of a VPC internet gateway or a virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L142">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


An ID of an EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L143">property instanceOwnerId</a>
</h3>

```typescript
instanceOwnerId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L147">property natGatewayId</a>
</h3>

```typescript
natGatewayId?: pulumi.Input<string>;
```


An ID of a VPC NAT gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L151">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


An ID of a network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L152">property origin</a>
</h3>

```typescript
origin?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L156">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the routing table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L157">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/route.ts#L161">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId?: pulumi.Input<string>;
```


An ID of a VPC peering connection.

<h2 class="pdoc-module-header" id="RouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L116">interface RouteTableArgs</a>
</h2>

The set of arguments for constructing a RouteTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L120">property propagatingVgws</a>
</h3>

```typescript
propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L124">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L132">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="RouteTableAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L78">interface RouteTableAssociationArgs</a>
</h2>

The set of arguments for constructing a RouteTableAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L82">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The ID of the routing table to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L86">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The subnet ID to create an association.

<h2 class="pdoc-module-header" id="RouteTableAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L64">interface RouteTableAssociationState</a>
</h2>

Input properties used for looking up and filtering RouteTableAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L68">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the routing table to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTableAssociation.ts#L72">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet ID to create an association.

<h2 class="pdoc-module-header" id="RouteTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L94">interface RouteTableState</a>
</h2>

Input properties used for looking up and filtering RouteTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L98">property propagatingVgws</a>
</h3>

```typescript
propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual gateways for propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L102">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of route objects. Their keys are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L106">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/routeTable.ts#L110">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="SecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L187">interface SecurityGroupArgs</a>
</h2>

The set of arguments for constructing a SecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L194">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The security group description. Defaults to
"Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you'd like
to classify your security groups in a way that can be updated, use `tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L199">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L204">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L209">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security group. If omitted, Terraform will
assign a random, unique name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L214">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L224">property revokeRulesOnDelete</a>
</h3>

```typescript
revokeRulesOnDelete?: pulumi.Input<boolean>;
```


Instruct Terraform to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L228">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L232">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="SecurityGroupRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L193">interface SecurityGroupRuleArgs</a>
</h2>

The set of arguments for constructing a SecurityGroupRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L197">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of CIDR blocks. Cannot be specified with `source_security_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L205">property fromPort</a>
</h3>

```typescript
fromPort: pulumi.Input<number>;
```


The start port (or ICMP type number if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L209">property ipv6CidrBlocks</a>
</h3>

```typescript
ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L214">property prefixListIds</a>
</h3>

```typescript
prefixListIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of prefix list IDs (for allowing access to VPC endpoints).
Only valid with `egress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L218">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L222">property securityGroupId</a>
</h3>

```typescript
securityGroupId: pulumi.Input<string>;
```


The security group to apply this rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L227">property self</a>
</h3>

```typescript
self?: pulumi.Input<boolean>;
```


If true, the security group itself will be added as
a source to this ingress rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L232">property sourceSecurityGroupId</a>
</h3>

```typescript
sourceSecurityGroupId?: pulumi.Input<string>;
```


The security group id to allow access to/from,
depending on the `type`. Cannot be specified with `cidr_blocks`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L236">property toPort</a>
</h3>

```typescript
toPort: pulumi.Input<number>;
```


The end port (or ICMP code if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L241">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of rule being created. Valid options are `ingress` (inbound)
or `egress` (outbound).

<h2 class="pdoc-module-header" id="SecurityGroupRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L139">interface SecurityGroupRuleState</a>
</h2>

Input properties used for looking up and filtering SecurityGroupRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L143">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of CIDR blocks. Cannot be specified with `source_security_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L147">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L151">property fromPort</a>
</h3>

```typescript
fromPort?: pulumi.Input<number>;
```


The start port (or ICMP type number if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L155">property ipv6CidrBlocks</a>
</h3>

```typescript
ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L160">property prefixListIds</a>
</h3>

```typescript
prefixListIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of prefix list IDs (for allowing access to VPC endpoints).
Only valid with `egress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L164">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L168">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The security group to apply this rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L173">property self</a>
</h3>

```typescript
self?: pulumi.Input<boolean>;
```


If true, the security group itself will be added as
a source to this ingress rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L178">property sourceSecurityGroupId</a>
</h3>

```typescript
sourceSecurityGroupId?: pulumi.Input<string>;
```


The security group id to allow access to/from,
depending on the `type`. Cannot be specified with `cidr_blocks`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L182">property toPort</a>
</h3>

```typescript
toPort?: pulumi.Input<number>;
```


The end port (or ICMP code if protocol is "icmp").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroupRule.ts#L187">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of rule being created. Valid options are `ingress` (inbound)
or `egress` (outbound).

<h2 class="pdoc-module-header" id="SecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L128">interface SecurityGroupState</a>
</h2>

Input properties used for looking up and filtering SecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L132">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the security group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L139">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The security group description. Defaults to
"Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you'd like
to classify your security groups in a way that can be updated, use `tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L144">property egress</a>
</h3>

```typescript
egress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L149">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security group. If omitted, Terraform will
assign a random, unique name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L159">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L163">property ownerId</a>
</h3>

```typescript
ownerId?: pulumi.Input<string>;
```


The owner ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L173">property revokeRulesOnDelete</a>
</h3>

```typescript
revokeRulesOnDelete?: pulumi.Input<boolean>;
```


Instruct Terraform to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L177">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/securityGroup.ts#L181">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="SnapshotCreateVolumePermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L78">interface SnapshotCreateVolumePermissionArgs</a>
</h2>

The set of arguments for constructing a SnapshotCreateVolumePermission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L82">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


An AWS Account ID to add create volume permissions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L86">property snapshotId</a>
</h3>

```typescript
snapshotId: pulumi.Input<string>;
```


A snapshot ID

<h2 class="pdoc-module-header" id="SnapshotCreateVolumePermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L64">interface SnapshotCreateVolumePermissionState</a>
</h2>

Input properties used for looking up and filtering SnapshotCreateVolumePermission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L68">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


An AWS Account ID to add create volume permissions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/snapshotCreateVolumePermission.ts#L72">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


A snapshot ID

<h2 class="pdoc-module-header" id="SpotDatafeedSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L78">interface SpotDatafeedSubscriptionArgs</a>
</h2>

The set of arguments for constructing a SpotDatafeedSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L82">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The Amazon S3 bucket in which to store the Spot instance data feed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L86">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```


Path of folder inside bucket to place spot pricing data.

<h2 class="pdoc-module-header" id="SpotDatafeedSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L64">interface SpotDatafeedSubscriptionState</a>
</h2>

Input properties used for looking up and filtering SpotDatafeedSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L68">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The Amazon S3 bucket in which to store the Spot instance data feed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotDatafeedSubscription.ts#L72">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```


Path of folder inside bucket to place spot pricing data.

<h2 class="pdoc-module-header" id="SpotFleetRequestArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L262">interface SpotFleetRequestArgs</a>
</h2>

The set of arguments for constructing a SpotFleetRequest resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L268">property allocationStrategy</a>
</h3>

```typescript
allocationStrategy?: pulumi.Input<string>;
```


Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
lowestPrice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L274">property excessCapacityTerminationPolicy</a>
</h3>

```typescript
excessCapacityTerminationPolicy?: pulumi.Input<string>;
```


Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L279">property fleetType</a>
</h3>

```typescript
fleetType?: pulumi.Input<string>;
```


The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is `maintain`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L286">property iamFleetRole</a>
</h3>

```typescript
iamFleetRole: pulumi.Input<string>;
```


Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L292">property instanceInterruptionBehaviour</a>
</h3>

```typescript
instanceInterruptionBehaviour?: pulumi.Input<string>;
```


Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
`terminate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L298">property launchSpecifications</a>
</h3>

```typescript
launchSpecifications: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to define the launch configuration of the
spot-fleet request. Can be specified multiple times to define different bids
across different markets and instance types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L302">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of elastic load balancer names to add to the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L306">property replaceUnhealthyInstances</a>
</h3>

```typescript
replaceUnhealthyInstances?: pulumi.Input<boolean>;
```


Indicates whether Spot fleet should replace unhealthy instances. Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L310">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum bid price per unit hour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L316">property targetCapacity</a>
</h3>

```typescript
targetCapacity: pulumi.Input<number>;
```


The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L321">property targetGroupArns</a>
</h3>

```typescript
targetGroupArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of `aws_alb_target_group` ARNs, for use with
Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L326">property terminateInstancesWithExpiration</a>
</h3>

```typescript
terminateInstancesWithExpiration?: pulumi.Input<boolean>;
```


Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L330">property validFrom</a>
</h3>

```typescript
validFrom?: pulumi.Input<string>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L334">property validUntil</a>
</h3>

```typescript
validUntil?: pulumi.Input<string>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L340">property waitForFulfillment</a>
</h3>

```typescript
waitForFulfillment?: pulumi.Input<boolean>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="SpotFleetRequestState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L173">interface SpotFleetRequestState</a>
</h2>

Input properties used for looking up and filtering SpotFleetRequest resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L179">property allocationStrategy</a>
</h3>

```typescript
allocationStrategy?: pulumi.Input<string>;
```


Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
lowestPrice.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L180">property clientToken</a>
</h3>

```typescript
clientToken?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L186">property excessCapacityTerminationPolicy</a>
</h3>

```typescript
excessCapacityTerminationPolicy?: pulumi.Input<string>;
```


Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L191">property fleetType</a>
</h3>

```typescript
fleetType?: pulumi.Input<string>;
```


The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is `maintain`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L198">property iamFleetRole</a>
</h3>

```typescript
iamFleetRole?: pulumi.Input<string>;
```


Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L204">property instanceInterruptionBehaviour</a>
</h3>

```typescript
instanceInterruptionBehaviour?: pulumi.Input<string>;
```


Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
`terminate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L210">property launchSpecifications</a>
</h3>

```typescript
launchSpecifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to define the launch configuration of the
spot-fleet request. Can be specified multiple times to define different bids
across different markets and instance types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L214">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of elastic load balancer names to add to the Spot fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L218">property replaceUnhealthyInstances</a>
</h3>

```typescript
replaceUnhealthyInstances?: pulumi.Input<boolean>;
```


Indicates whether Spot fleet should replace unhealthy instances. Default `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L222">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum bid price per unit hour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L226">property spotRequestState</a>
</h3>

```typescript
spotRequestState?: pulumi.Input<string>;
```


The state of the Spot fleet request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L232">property targetCapacity</a>
</h3>

```typescript
targetCapacity?: pulumi.Input<number>;
```


The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L237">property targetGroupArns</a>
</h3>

```typescript
targetGroupArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of `aws_alb_target_group` ARNs, for use with
Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L242">property terminateInstancesWithExpiration</a>
</h3>

```typescript
terminateInstancesWithExpiration?: pulumi.Input<boolean>;
```


Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L246">property validFrom</a>
</h3>

```typescript
validFrom?: pulumi.Input<string>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L250">property validUntil</a>
</h3>

```typescript
validUntil?: pulumi.Input<string>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotFleetRequest.ts#L256">property waitForFulfillment</a>
</h3>

```typescript
waitForFulfillment?: pulumi.Input<boolean>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="SpotInstanceRequestArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L604">interface SpotInstanceRequestArgs</a>
</h2>

The set of arguments for constructing a SpotInstanceRequest resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L608">property ami</a>
</h3>

```typescript
ami: pulumi.Input<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L612">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L616">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L622">property blockDurationMinutes</a>
</h3>

```typescript
blockDurationMinutes?: pulumi.Input<number>;
```


The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
Note that you can't specify an Availability Zone group or a launch group if you specify a duration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L628">property cpuCoreCount</a>
</h3>

```typescript
cpuCoreCount?: pulumi.Input<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L632">property cpuThreadsPerCore</a>
</h3>

```typescript
cpuThreadsPerCore?: pulumi.Input<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L636">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L641">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L646">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L654">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L659">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L663">property getPasswordData</a>
</h3>

```typescript
getPasswordData?: pulumi.Input<boolean>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L669">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L676">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L680">property instanceInterruptionBehaviour</a>
</h3>

```typescript
instanceInterruptionBehaviour?: pulumi.Input<string>;
```


Indicates whether a Spot instance stops or terminates when it is interrupted. Default is `terminate` as this is the current AWS behaviour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L684">property instanceType</a>
</h3>

```typescript
instanceType: pulumi.Input<string>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L685">property ipv6AddressCount</a>
</h3>

```typescript
ipv6AddressCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L689">property ipv6Addresses</a>
</h3>

```typescript
ipv6Addresses?: pulumi.Input<pulumi.Input<string>[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L693">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L698">property launchGroup</a>
</h3>

```typescript
launchGroup?: pulumi.Input<string>;
```


A launch group is a group of spot instances that launch together and terminate together.
If left empty instances are launched and terminated individually.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L702">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L706">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L710">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L715">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L720">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L724">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L729">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L733">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum price to request on the spot market.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L738">property spotType</a>
</h3>

```typescript
spotType?: pulumi.Input<string>;
```


If set to `one-time`, after
the instance is terminated, the spot request will be closed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L742">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L746">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L750">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L754">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L758">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L762">property validFrom</a>
</h3>

```typescript
validFrom?: pulumi.Input<string>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L766">property validUntil</a>
</h3>

```typescript
validUntil?: pulumi.Input<string>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. The default end date is 7 days from the current date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L770">property volumeTags</a>
</h3>

```typescript
volumeTags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L774">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L780">property waitForFulfillment</a>
</h3>

```typescript
waitForFulfillment?: pulumi.Input<boolean>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="SpotInstanceRequestState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L387">interface SpotInstanceRequestState</a>
</h2>

Input properties used for looking up and filtering SpotInstanceRequest resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L391">property ami</a>
</h3>

```typescript
ami?: pulumi.Input<string>;
```


The AMI to use for the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L392">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L396">property associatePublicIpAddress</a>
</h3>

```typescript
associatePublicIpAddress?: pulumi.Input<boolean>;
```


Associate a public ip address with an instance in a VPC.  Boolean value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L400">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L406">property blockDurationMinutes</a>
</h3>

```typescript
blockDurationMinutes?: pulumi.Input<number>;
```


The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
Note that you can't specify an Availability Zone group or a launch group if you specify a duration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L412">property cpuCoreCount</a>
</h3>

```typescript
cpuCoreCount?: pulumi.Input<number>;
```


Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
[CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L416">property cpuThreadsPerCore</a>
</h3>

```typescript
cpuThreadsPerCore?: pulumi.Input<number>;
```


If set to to 1, hyperthreading is disabled on the launcehd instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L420">property creditSpecification</a>
</h3>

```typescript
creditSpecification?: pulumi.Input<{ ... }>;
```


Customize the credit specification of the instance. See Credit Specification below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L425">property disableApiTermination</a>
</h3>

```typescript
disableApiTermination?: pulumi.Input<boolean>;
```


If true, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L430">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L438">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L443">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L447">property getPasswordData</a>
</h3>

```typescript
getPasswordData?: pulumi.Input<boolean>;
```


If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L453">property iamInstanceProfile</a>
</h3>

```typescript
iamInstanceProfile?: pulumi.Input<string>;
```


The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.
* `ipv6_address_count`- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L460">property instanceInitiatedShutdownBehavior</a>
</h3>

```typescript
instanceInitiatedShutdownBehavior?: pulumi.Input<string>;
```


Shutdown behavior for the
instance. Amazon defaults this to `stop` for EBS-backed instances and
`terminate` for instance-store instances. Cannot be set on instance-store
instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L464">property instanceInterruptionBehaviour</a>
</h3>

```typescript
instanceInterruptionBehaviour?: pulumi.Input<string>;
```


Indicates whether a Spot instance stops or terminates when it is interrupted. Default is `terminate` as this is the current AWS behaviour.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L465">property instanceState</a>
</h3>

```typescript
instanceState?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L469">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L470">property ipv6AddressCount</a>
</h3>

```typescript
ipv6AddressCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L474">property ipv6Addresses</a>
</h3>

```typescript
ipv6Addresses?: pulumi.Input<pulumi.Input<string>[]>;
```


Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L478">property keyName</a>
</h3>

```typescript
keyName?: pulumi.Input<string>;
```


The key name of the Key Pair to use for the instance; which can be managed using the `aws_key_pair` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L483">property launchGroup</a>
</h3>

```typescript
launchGroup?: pulumi.Input<string>;
```


A launch group is a group of spot instances that launch together and terminate together.
If left empty instances are launched and terminated individually.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L487">property monitoring</a>
</h3>

```typescript
monitoring?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L492">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L491">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L493">property passwordData</a>
</h3>

```typescript
passwordData?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L497">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The Placement Group to start the instance in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L498">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L504">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L509">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


Private IP address to associate with the
instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L514">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L518">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L523">property rootBlockDevice</a>
</h3>

```typescript
rootBlockDevice?: pulumi.Input<{ ... }>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L527">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group names to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L532">property sourceDestCheck</a>
</h3>

```typescript
sourceDestCheck?: pulumi.Input<boolean>;
```


Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L541">property spotBidStatus</a>
</h3>

```typescript
spotBidStatus?: pulumi.Input<string>;
```


The current [bid
status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html)
of the Spot Instance Request.
* `spot_request_state` The current [request
state](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#creating-spot-request-status)
of the Spot Instance Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L546">property spotInstanceId</a>
</h3>

```typescript
spotInstanceId?: pulumi.Input<string>;
```


The Instance ID (if any) that is currently fulfilling
the Spot Instance request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L550">property spotPrice</a>
</h3>

```typescript
spotPrice?: pulumi.Input<string>;
```


The maximum price to request on the spot market.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L551">property spotRequestState</a>
</h3>

```typescript
spotRequestState?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L556">property spotType</a>
</h3>

```typescript
spotType?: pulumi.Input<string>;
```


If set to `one-time`, after
the instance is terminated, the spot request will be closed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L560">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The VPC Subnet ID to launch in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L564">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L568">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L572">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L576">property userDataBase64</a>
</h3>

```typescript
userDataBase64?: pulumi.Input<string>;
```


Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L580">property validFrom</a>
</h3>

```typescript
validFrom?: pulumi.Input<string>;
```


The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L584">property validUntil</a>
</h3>

```typescript
validUntil?: pulumi.Input<string>;
```


The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. The default end date is 7 days from the current date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L588">property volumeTags</a>
</h3>

```typescript
volumeTags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the devices created by the instance at launch time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L592">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to associate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/spotInstanceRequest.ts#L598">property waitForFulfillment</a>
</h3>

```typescript
waitForFulfillment?: pulumi.Input<boolean>;
```


If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

<h2 class="pdoc-module-header" id="SubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L156">interface SubnetArgs</a>
</h2>

The set of arguments for constructing a Subnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L162">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
assignIpv6AddressOnCreation?: pulumi.Input<boolean>;
```


Specify true to indicate
that network interfaces created in the specified subnet should be
assigned an IPv6 address. Default is `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L163">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L167">property cidrBlock</a>
</h3>

```typescript
cidrBlock: pulumi.Input<string>;
```


The CIDR block for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L172">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 network range for the subnet,
in CIDR notation. The subnet size must use a /64 prefix length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L178">property mapPublicIpOnLaunch</a>
</h3>

```typescript
mapPublicIpOnLaunch?: pulumi.Input<boolean>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L182">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L186">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="SubnetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L111">interface SubnetState</a>
</h2>

Input properties used for looking up and filtering Subnet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L116">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the subnet.
* `availability_zone`- The AZ for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L122">property assignIpv6AddressOnCreation</a>
</h3>

```typescript
assignIpv6AddressOnCreation?: pulumi.Input<boolean>;
```


Specify true to indicate
that network interfaces created in the specified subnet should be
assigned an IPv6 address. Default is `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L123">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L127">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The CIDR block for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L132">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 network range for the subnet,
in CIDR notation. The subnet size must use a /64 prefix length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L136">property ipv6CidrBlockAssociationId</a>
</h3>

```typescript
ipv6CidrBlockAssociationId?: pulumi.Input<string>;
```


The association ID for the IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L142">property mapPublicIpOnLaunch</a>
</h3>

```typescript
mapPublicIpOnLaunch?: pulumi.Input<boolean>;
```


Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L146">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/subnet.ts#L150">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID.

<h2 class="pdoc-module-header" id="VolumeAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L130">interface VolumeAttachmentArgs</a>
</h2>

The set of arguments for constructing a VolumeAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L135">property deviceName</a>
</h3>

```typescript
deviceName: pulumi.Input<string>;
```


The device name to expose to the instance (for
example, `/dev/sdh` or `xvdh`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L142">property forceDetach</a>
</h3>

```typescript
forceDetach?: pulumi.Input<boolean>;
```


Set to `true` if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in **data loss**. See
[Detaching an Amazon EBS Volume from an Instance][1] for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L146">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


ID of the Instance to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L154">property skipDestroy</a>
</h3>

```typescript
skipDestroy?: pulumi.Input<boolean>;
```


Set this to true if you do not wish
to detach the volume from the instance to which it is attached at destroy
time, and instead just remove the attachment from Terraform state. This is
useful when destroying an instance which has volumes created by some other
means attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L158">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


ID of the Volume to be attached

<h2 class="pdoc-module-header" id="VolumeAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L96">interface VolumeAttachmentState</a>
</h2>

Input properties used for looking up and filtering VolumeAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L101">property deviceName</a>
</h3>

```typescript
deviceName?: pulumi.Input<string>;
```


The device name to expose to the instance (for
example, `/dev/sdh` or `xvdh`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L108">property forceDetach</a>
</h3>

```typescript
forceDetach?: pulumi.Input<boolean>;
```


Set to `true` if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in **data loss**. See
[Detaching an Amazon EBS Volume from an Instance][1] for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L112">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


ID of the Instance to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L120">property skipDestroy</a>
</h3>

```typescript
skipDestroy?: pulumi.Input<boolean>;
```


Set this to true if you do not wish
to detach the volume from the instance to which it is attached at destroy
time, and instead just remove the attachment from Terraform state. This is
useful when destroying an instance which has volumes created by some other
means attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/volumeAttachment.ts#L124">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


ID of the Volume to be attached

<h2 class="pdoc-module-header" id="VpcArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L225">interface VpcArgs</a>
</h2>

The set of arguments for constructing a Vpc resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L231">property assignGeneratedIpv6CidrBlock</a>
</h3>

```typescript
assignGeneratedIpv6CidrBlock?: pulumi.Input<boolean>;
```


Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L235">property cidrBlock</a>
</h3>

```typescript
cidrBlock: pulumi.Input<string>;
```


The CIDR block for the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L241">property enableClassiclink</a>
</h3>

```typescript
enableClassiclink?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L246">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
enableClassiclinkDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L250">property enableDnsHostnames</a>
</h3>

```typescript
enableDnsHostnames?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L254">property enableDnsSupport</a>
</h3>

```typescript
enableDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L258">property instanceTenancy</a>
</h3>

```typescript
instanceTenancy?: pulumi.Input<string>;
```


A tenancy option for instances launched into the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L262">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VpcDhcpOptionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L118">interface VpcDhcpOptionsArgs</a>
</h2>

The set of arguments for constructing a VpcDhcpOptions resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L122">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L126">property domainNameServers</a>
</h3>

```typescript
domainNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L130">property netbiosNameServers</a>
</h3>

```typescript
netbiosNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L134">property netbiosNodeType</a>
</h3>

```typescript
netbiosNodeType?: pulumi.Input<string>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L138">property ntpServers</a>
</h3>

```typescript
ntpServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NTP servers to configure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VpcDhcpOptionsAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L79">interface VpcDhcpOptionsAssociationArgs</a>
</h2>

The set of arguments for constructing a VpcDhcpOptionsAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L83">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId: pulumi.Input<string>;
```


The ID of the DHCP Options Set to associate to the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L87">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the VPC to which we would like to associate a DHCP Options Set.

<h2 class="pdoc-module-header" id="VpcDhcpOptionsAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L65">interface VpcDhcpOptionsAssociationState</a>
</h2>

Input properties used for looking up and filtering VpcDhcpOptionsAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L69">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId?: pulumi.Input<string>;
```


The ID of the DHCP Options Set to associate to the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptionsAssociation.ts#L73">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the VPC to which we would like to associate a DHCP Options Set.

<h2 class="pdoc-module-header" id="VpcDhcpOptionsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L88">interface VpcDhcpOptionsState</a>
</h2>

Input properties used for looking up and filtering VpcDhcpOptions resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L92">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L96">property domainNameServers</a>
</h3>

```typescript
domainNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L100">property netbiosNameServers</a>
</h3>

```typescript
netbiosNameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NETBIOS name servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L104">property netbiosNodeType</a>
</h3>

```typescript
netbiosNodeType?: pulumi.Input<string>;
```


The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L108">property ntpServers</a>
</h3>

```typescript
ntpServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of NTP servers to configure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcDhcpOptions.ts#L112">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VpcEndpointArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L209">interface VpcEndpointArgs</a>
</h2>

The set of arguments for constructing a VpcEndpoint resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L213">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L218">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A policy to attach to the endpoint that controls access to the service. Applicable for endpoints of type `Gateway`.
Defaults to full access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L223">property privateDnsEnabled</a>
</h3>

```typescript
privateDnsEnabled?: pulumi.Input<boolean>;
```


Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L227">property routeTableIds</a>
</h3>

```typescript
routeTableIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more route table IDs. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L231">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L235">property serviceName</a>
</h3>

```typescript
serviceName: pulumi.Input<string>;
```


The service name, in the form `com.amazonaws.region.service` for AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L239">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L243">property vpcEndpointType</a>
</h3>

```typescript
vpcEndpointType?: pulumi.Input<string>;
```


The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L247">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the VPC in which the endpoint will be used.

<h2 class="pdoc-module-header" id="VpcEndpointConnectionNotificationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L119">interface VpcEndpointConnectionNotificationArgs</a>
</h2>

The set of arguments for constructing a VpcEndpointConnectionNotification resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L123">property connectionEvents</a>
</h3>

```typescript
connectionEvents: pulumi.Input<pulumi.Input<string>[]>;
```


One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L127">property connectionNotificationArn</a>
</h3>

```typescript
connectionNotificationArn: pulumi.Input<string>;
```


The ARN of the SNS topic for the notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L131">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId?: pulumi.Input<string>;
```


The ID of the VPC Endpoint to receive notifications for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L135">property vpcEndpointServiceId</a>
</h3>

```typescript
vpcEndpointServiceId?: pulumi.Input<string>;
```


The ID of the VPC Endpoint Service to receive notifications for.

<h2 class="pdoc-module-header" id="VpcEndpointConnectionNotificationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L89">interface VpcEndpointConnectionNotificationState</a>
</h2>

Input properties used for looking up and filtering VpcEndpointConnectionNotification resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L93">property connectionEvents</a>
</h3>

```typescript
connectionEvents?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L97">property connectionNotificationArn</a>
</h3>

```typescript
connectionNotificationArn?: pulumi.Input<string>;
```


The ARN of the SNS topic for the notifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L101">property notificationType</a>
</h3>

```typescript
notificationType?: pulumi.Input<string>;
```


The type of notification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L105">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the notification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L109">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId?: pulumi.Input<string>;
```


The ID of the VPC Endpoint to receive notifications for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointConnectionNotification.ts#L113">property vpcEndpointServiceId</a>
</h3>

```typescript
vpcEndpointServiceId?: pulumi.Input<string>;
```


The ID of the VPC Endpoint Service to receive notifications for.

<h2 class="pdoc-module-header" id="VpcEndpointRouteTableAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L84">interface VpcEndpointRouteTableAssociationArgs</a>
</h2>

The set of arguments for constructing a VpcEndpointRouteTableAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L88">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The ID of the routing table to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L92">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId: pulumi.Input<string>;
```


The ID of the VPC endpoint with which the routing table will be associated.

<h2 class="pdoc-module-header" id="VpcEndpointRouteTableAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L70">interface VpcEndpointRouteTableAssociationState</a>
</h2>

Input properties used for looking up and filtering VpcEndpointRouteTableAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L74">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the routing table to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointRouteTableAssociation.ts#L78">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId?: pulumi.Input<string>;
```


The ID of the VPC endpoint with which the routing table will be associated.

<h2 class="pdoc-module-header" id="VpcEndpointServiceAllowedPrincipleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L84">interface VpcEndpointServiceAllowedPrincipleArgs</a>
</h2>

The set of arguments for constructing a VpcEndpointServiceAllowedPrinciple resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L88">property principalArn</a>
</h3>

```typescript
principalArn: pulumi.Input<string>;
```


The ARN of the principal to allow permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L92">property vpcEndpointServiceId</a>
</h3>

```typescript
vpcEndpointServiceId: pulumi.Input<string>;
```


The ID of the VPC endpoint service to allow permission.

<h2 class="pdoc-module-header" id="VpcEndpointServiceAllowedPrincipleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L70">interface VpcEndpointServiceAllowedPrincipleState</a>
</h2>

Input properties used for looking up and filtering VpcEndpointServiceAllowedPrinciple resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L74">property principalArn</a>
</h3>

```typescript
principalArn?: pulumi.Input<string>;
```


The ARN of the principal to allow permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointServiceAllowedPrinciple.ts#L78">property vpcEndpointServiceId</a>
</h3>

```typescript
vpcEndpointServiceId?: pulumi.Input<string>;
```


The ID of the VPC endpoint service to allow permission.

<h2 class="pdoc-module-header" id="VpcEndpointServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L155">interface VpcEndpointServiceArgs</a>
</h2>

The set of arguments for constructing a VpcEndpointService resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L159">property acceptanceRequired</a>
</h3>

```typescript
acceptanceRequired: pulumi.Input<boolean>;
```


Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L163">property allowedPrincipals</a>
</h3>

```typescript
allowedPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
```


The ARNs of one or more principals allowed to discover the endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L167">property networkLoadBalancerArns</a>
</h3>

```typescript
networkLoadBalancerArns: pulumi.Input<pulumi.Input<string>[]>;
```


The ARNs of one or more Network Load Balancers for the endpoint service.

<h2 class="pdoc-module-header" id="VpcEndpointServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L113">interface VpcEndpointServiceState</a>
</h2>

Input properties used for looking up and filtering VpcEndpointService resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L117">property acceptanceRequired</a>
</h3>

```typescript
acceptanceRequired?: pulumi.Input<boolean>;
```


Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L121">property allowedPrincipals</a>
</h3>

```typescript
allowedPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
```


The ARNs of one or more principals allowed to discover the endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L125">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


The Availability Zones in which the service is available.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L129">property baseEndpointDnsNames</a>
</h3>

```typescript
baseEndpointDnsNames?: pulumi.Input<pulumi.Input<string>[]>;
```


The DNS names for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L133">property networkLoadBalancerArns</a>
</h3>

```typescript
networkLoadBalancerArns?: pulumi.Input<pulumi.Input<string>[]>;
```


The ARNs of one or more Network Load Balancers for the endpoint service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L137">property privateDnsName</a>
</h3>

```typescript
privateDnsName?: pulumi.Input<string>;
```


The private DNS name for the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L141">property serviceName</a>
</h3>

```typescript
serviceName?: pulumi.Input<string>;
```


The service name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L145">property serviceType</a>
</h3>

```typescript
serviceType?: pulumi.Input<string>;
```


The service type, `Gateway` or `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointService.ts#L149">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the VPC endpoint service.

<h2 class="pdoc-module-header" id="VpcEndpointState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L145">interface VpcEndpointState</a>
</h2>

Input properties used for looking up and filtering VpcEndpoint resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L149">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L153">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L157">property dnsEntries</a>
</h3>

```typescript
dnsEntries?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L161">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L166">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A policy to attach to the endpoint that controls access to the service. Applicable for endpoints of type `Gateway`.
Defaults to full access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L170">property prefixListId</a>
</h3>

```typescript
prefixListId?: pulumi.Input<string>;
```


The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L175">property privateDnsEnabled</a>
</h3>

```typescript
privateDnsEnabled?: pulumi.Input<boolean>;
```


Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L179">property routeTableIds</a>
</h3>

```typescript
routeTableIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more route table IDs. Applicable for endpoints of type `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L183">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L187">property serviceName</a>
</h3>

```typescript
serviceName?: pulumi.Input<string>;
```


The service name, in the form `com.amazonaws.region.service` for AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L191">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L195">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L199">property vpcEndpointType</a>
</h3>

```typescript
vpcEndpointType?: pulumi.Input<string>;
```


The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpoint.ts#L203">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the VPC in which the endpoint will be used.

<h2 class="pdoc-module-header" id="VpcEndpointSubnetAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L84">interface VpcEndpointSubnetAssociationArgs</a>
</h2>

The set of arguments for constructing a VpcEndpointSubnetAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L88">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The ID of the subnet to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L92">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId: pulumi.Input<string>;
```


The ID of the VPC endpoint with which the subnet will be associated.

<h2 class="pdoc-module-header" id="VpcEndpointSubnetAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L70">interface VpcEndpointSubnetAssociationState</a>
</h2>

Input properties used for looking up and filtering VpcEndpointSubnetAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L74">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the subnet to be associated with the VPC endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcEndpointSubnetAssociation.ts#L78">property vpcEndpointId</a>
</h3>

```typescript
vpcEndpointId?: pulumi.Input<string>;
```


The ID of the VPC endpoint with which the subnet will be associated.

<h2 class="pdoc-module-header" id="VpcIpv4CidrBlockAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L81">interface VpcIpv4CidrBlockAssociationArgs</a>
</h2>

The set of arguments for constructing a VpcIpv4CidrBlockAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L85">property cidrBlock</a>
</h3>

```typescript
cidrBlock: pulumi.Input<string>;
```


The additional IPv4 CIDR block to associate with the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L89">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the VPC to make the association with.

<h2 class="pdoc-module-header" id="VpcIpv4CidrBlockAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L67">interface VpcIpv4CidrBlockAssociationState</a>
</h2>

Input properties used for looking up and filtering VpcIpv4CidrBlockAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L71">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The additional IPv4 CIDR block to associate with the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcIpv4CidrBlockAssociation.ts#L75">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the VPC to make the association with.

<h2 class="pdoc-module-header" id="VpcPeeringConnectionAccepterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L168">interface VpcPeeringConnectionAccepterArgs</a>
</h2>

The set of arguments for constructing a VpcPeeringConnectionAccepter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L173">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L177">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Whether or not to accept the peering request. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L182">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L186">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L190">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId: pulumi.Input<string>;
```


The VPC Peering Connection ID to manage.

<h2 class="pdoc-module-header" id="VpcPeeringConnectionAccepterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L120">interface VpcPeeringConnectionAccepterState</a>
</h2>

Input properties used for looking up and filtering VpcPeeringConnectionAccepter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L124">property acceptStatus</a>
</h3>

```typescript
acceptStatus?: pulumi.Input<string>;
```


The status of the VPC Peering Connection request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L129">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L133">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Whether or not to accept the peering request. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L137">property peerOwnerId</a>
</h3>

```typescript
peerOwnerId?: pulumi.Input<string>;
```


The AWS account ID of the owner of the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L141">property peerRegion</a>
</h3>

```typescript
peerRegion?: pulumi.Input<string>;
```


The region of the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L145">property peerVpcId</a>
</h3>

```typescript
peerVpcId?: pulumi.Input<string>;
```


The ID of the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L150">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L154">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L158">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the accepter VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnectionAccepter.ts#L162">property vpcPeeringConnectionId</a>
</h3>

```typescript
vpcPeeringConnectionId?: pulumi.Input<string>;
```


The VPC Peering Connection ID to manage.

<h2 class="pdoc-module-header" id="VpcPeeringConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L174">interface VpcPeeringConnectionArgs</a>
</h2>

The set of arguments for constructing a VpcPeeringConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L180">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L184">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Accept the peering (both VPCs need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L189">property peerOwnerId</a>
</h3>

```typescript
peerOwnerId?: pulumi.Input<string>;
```


The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L194">property peerRegion</a>
</h3>

```typescript
peerRegion?: pulumi.Input<string>;
```


The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws_vpc_peering_connection_accepter` to manage the accepter side.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L198">property peerVpcId</a>
</h3>

```typescript
peerVpcId: pulumi.Input<string>;
```


The ID of the VPC with which you are creating the VPC Peering Connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L204">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L208">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L212">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the requester VPC.

<h2 class="pdoc-module-header" id="VpcPeeringConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L126">interface VpcPeeringConnectionState</a>
</h2>

Input properties used for looking up and filtering VpcPeeringConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L130">property acceptStatus</a>
</h3>

```typescript
acceptStatus?: pulumi.Input<string>;
```


The status of the VPC Peering Connection request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L136">property accepter</a>
</h3>

```typescript
accepter?: pulumi.Input<{ ... }>;
```


An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L140">property autoAccept</a>
</h3>

```typescript
autoAccept?: pulumi.Input<boolean>;
```


Accept the peering (both VPCs need to be in the same AWS account).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L145">property peerOwnerId</a>
</h3>

```typescript
peerOwnerId?: pulumi.Input<string>;
```


The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L150">property peerRegion</a>
</h3>

```typescript
peerRegion?: pulumi.Input<string>;
```


The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws_vpc_peering_connection_accepter` to manage the accepter side.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L154">property peerVpcId</a>
</h3>

```typescript
peerVpcId?: pulumi.Input<string>;
```


The ID of the VPC with which you are creating the VPC Peering Connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L160">property requester</a>
</h3>

```typescript
requester?: pulumi.Input<{ ... }>;
```


A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L164">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpcPeeringConnection.ts#L168">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the requester VPC.

<h2 class="pdoc-module-header" id="VpcState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L151">interface VpcState</a>
</h2>

Input properties used for looking up and filtering Vpc resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L155">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L161">property assignGeneratedIpv6CidrBlock</a>
</h3>

```typescript
assignGeneratedIpv6CidrBlock?: pulumi.Input<boolean>;
```


Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L165">property cidrBlock</a>
</h3>

```typescript
cidrBlock?: pulumi.Input<string>;
```


The CIDR block for the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L169">property defaultNetworkAclId</a>
</h3>

```typescript
defaultNetworkAclId?: pulumi.Input<string>;
```


The ID of the network ACL created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L173">property defaultRouteTableId</a>
</h3>

```typescript
defaultRouteTableId?: pulumi.Input<string>;
```


The ID of the route table created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L177">property defaultSecurityGroupId</a>
</h3>

```typescript
defaultSecurityGroupId?: pulumi.Input<string>;
```


The ID of the security group created by default on VPC creation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L178">property dhcpOptionsId</a>
</h3>

```typescript
dhcpOptionsId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L184">property enableClassiclink</a>
</h3>

```typescript
enableClassiclink?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L189">property enableClassiclinkDnsSupport</a>
</h3>

```typescript
enableClassiclinkDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L193">property enableDnsHostnames</a>
</h3>

```typescript
enableDnsHostnames?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L197">property enableDnsSupport</a>
</h3>

```typescript
enableDnsSupport?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable DNS support in the VPC. Defaults true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L201">property instanceTenancy</a>
</h3>

```typescript
instanceTenancy?: pulumi.Input<string>;
```


A tenancy option for instances launched into the VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L205">property ipv6AssociationId</a>
</h3>

```typescript
ipv6AssociationId?: pulumi.Input<string>;
```


The association ID for the IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L209">property ipv6CidrBlock</a>
</h3>

```typescript
ipv6CidrBlock?: pulumi.Input<string>;
```


The IPv6 CIDR block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L215">property mainRouteTableId</a>
</h3>

```typescript
mainRouteTableId?: pulumi.Input<string>;
```


The ID of the main route table associated with
this VPC. Note that you can change a VPC's main route table by using an
[`aws_main_route_table_association`](https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpc.ts#L219">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VpnConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L280">interface VpnConnectionArgs</a>
</h2>

The set of arguments for constructing a VpnConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L284">property customerGatewayConfiguration</a>
</h3>

```typescript
customerGatewayConfiguration?: pulumi.Input<string>;
```


The configuration information for the VPN connection's customer gateway (in the native XML format).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L288">property customerGatewayId</a>
</h3>

```typescript
customerGatewayId: pulumi.Input<string>;
```


The ID of the customer gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L289">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L293">property staticRoutesOnly</a>
</h3>

```typescript
staticRoutesOnly?: pulumi.Input<boolean>;
```


Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L297">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Tags to apply to the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L301">property tunnel1InsideCidr</a>
</h3>

```typescript
tunnel1InsideCidr?: pulumi.Input<string>;
```


The CIDR block of the inside IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L305">property tunnel1PresharedKey</a>
</h3>

```typescript
tunnel1PresharedKey?: pulumi.Input<string>;
```


The preshared key of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L309">property tunnel2InsideCidr</a>
</h3>

```typescript
tunnel2InsideCidr?: pulumi.Input<string>;
```


The CIDR block of the second IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L314">property tunnel2PresharedKey</a>
</h3>

```typescript
tunnel2PresharedKey?: pulumi.Input<string>;
```


The preshared key of the second VPN tunnel.
~> **Note:** The preshared key must be between 8 and 64 characters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, periods(.) and underscores(_).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L318">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L319">property vgwTelemetries</a>
</h3>

```typescript
vgwTelemetries?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L323">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId: pulumi.Input<string>;
```


The ID of the virtual private gateway.

<h2 class="pdoc-module-header" id="VpnConnectionRouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L78">interface VpnConnectionRouteArgs</a>
</h2>

The set of arguments for constructing a VpnConnectionRoute resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L82">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock: pulumi.Input<string>;
```


The CIDR block associated with the local subnet of the customer network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L86">property vpnConnectionId</a>
</h3>

```typescript
vpnConnectionId: pulumi.Input<string>;
```


The ID of the VPN connection.

<h2 class="pdoc-module-header" id="VpnConnectionRouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L64">interface VpnConnectionRouteState</a>
</h2>

Input properties used for looking up and filtering VpnConnectionRoute resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L68">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock?: pulumi.Input<string>;
```


The CIDR block associated with the local subnet of the customer network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnectionRoute.ts#L72">property vpnConnectionId</a>
</h3>

```typescript
vpnConnectionId?: pulumi.Input<string>;
```


The ID of the VPN connection.

<h2 class="pdoc-module-header" id="VpnConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L191">interface VpnConnectionState</a>
</h2>

Input properties used for looking up and filtering VpnConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L195">property customerGatewayConfiguration</a>
</h3>

```typescript
customerGatewayConfiguration?: pulumi.Input<string>;
```


The configuration information for the VPN connection's customer gateway (in the native XML format).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L199">property customerGatewayId</a>
</h3>

```typescript
customerGatewayId?: pulumi.Input<string>;
```


The ID of the customer gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L200">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L204">property staticRoutesOnly</a>
</h3>

```typescript
staticRoutesOnly?: pulumi.Input<boolean>;
```


Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L208">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Tags to apply to the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L212">property tunnel1Address</a>
</h3>

```typescript
tunnel1Address?: pulumi.Input<string>;
```


The public IP address of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L216">property tunnel1BgpAsn</a>
</h3>

```typescript
tunnel1BgpAsn?: pulumi.Input<string>;
```


The bgp asn number of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L220">property tunnel1BgpHoldtime</a>
</h3>

```typescript
tunnel1BgpHoldtime?: pulumi.Input<number>;
```


The bgp holdtime of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L224">property tunnel1CgwInsideAddress</a>
</h3>

```typescript
tunnel1CgwInsideAddress?: pulumi.Input<string>;
```


The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L228">property tunnel1InsideCidr</a>
</h3>

```typescript
tunnel1InsideCidr?: pulumi.Input<string>;
```


The CIDR block of the inside IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L232">property tunnel1PresharedKey</a>
</h3>

```typescript
tunnel1PresharedKey?: pulumi.Input<string>;
```


The preshared key of the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L236">property tunnel1VgwInsideAddress</a>
</h3>

```typescript
tunnel1VgwInsideAddress?: pulumi.Input<string>;
```


The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L240">property tunnel2Address</a>
</h3>

```typescript
tunnel2Address?: pulumi.Input<string>;
```


The public IP address of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L244">property tunnel2BgpAsn</a>
</h3>

```typescript
tunnel2BgpAsn?: pulumi.Input<string>;
```


The bgp asn number of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L248">property tunnel2BgpHoldtime</a>
</h3>

```typescript
tunnel2BgpHoldtime?: pulumi.Input<number>;
```


The bgp holdtime of the second VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L252">property tunnel2CgwInsideAddress</a>
</h3>

```typescript
tunnel2CgwInsideAddress?: pulumi.Input<string>;
```


The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L256">property tunnel2InsideCidr</a>
</h3>

```typescript
tunnel2InsideCidr?: pulumi.Input<string>;
```


The CIDR block of the second IP addresses for the first VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L261">property tunnel2PresharedKey</a>
</h3>

```typescript
tunnel2PresharedKey?: pulumi.Input<string>;
```


The preshared key of the second VPN tunnel.
~> **Note:** The preshared key must be between 8 and 64 characters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, periods(.) and underscores(_).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L265">property tunnel2VgwInsideAddress</a>
</h3>

```typescript
tunnel2VgwInsideAddress?: pulumi.Input<string>;
```


The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L269">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L270">property vgwTelemetries</a>
</h3>

```typescript
vgwTelemetries?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnConnection.ts#L274">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the virtual private gateway.

<h2 class="pdoc-module-header" id="VpnGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L94">interface VpnGatewayArgs</a>
</h2>

The set of arguments for constructing a VpnGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L98">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: pulumi.Input<string>;
```


The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't specify an ASN, the virtual private gateway is created with the default ASN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L102">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The Availability Zone for the virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L106">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L110">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="VpnGatewayAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L83">interface VpnGatewayAttachmentArgs</a>
</h2>

The set of arguments for constructing a VpnGatewayAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L87">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The ID of the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L91">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId: pulumi.Input<string>;
```


The ID of the Virtual Private Gateway.

<h2 class="pdoc-module-header" id="VpnGatewayAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L69">interface VpnGatewayAttachmentState</a>
</h2>

Input properties used for looking up and filtering VpnGatewayAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L73">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The ID of the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayAttachment.ts#L77">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the Virtual Private Gateway.

<h2 class="pdoc-module-header" id="VpnGatewayRoutePropagationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L82">interface VpnGatewayRoutePropagationArgs</a>
</h2>

The set of arguments for constructing a VpnGatewayRoutePropagation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L86">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The id of the `aws_route_table` to propagate routes into.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L90">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId: pulumi.Input<string>;
```


The id of the `aws_vpn_gateway` to propagate routes from.

<h2 class="pdoc-module-header" id="VpnGatewayRoutePropagationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L68">interface VpnGatewayRoutePropagationState</a>
</h2>

Input properties used for looking up and filtering VpnGatewayRoutePropagation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L72">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The id of the `aws_route_table` to propagate routes into.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGatewayRoutePropagation.ts#L76">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The id of the `aws_vpn_gateway` to propagate routes from.

<h2 class="pdoc-module-header" id="VpnGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L72">interface VpnGatewayState</a>
</h2>

Input properties used for looking up and filtering VpnGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L76">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: pulumi.Input<string>;
```


The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't specify an ASN, the virtual private gateway is created with the default ASN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L80">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The Availability Zone for the virtual private gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L84">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/vpnGateway.ts#L88">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID to create in.

<h2 class="pdoc-module-header" id="C3Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L22">let C3Instance2XLarge</a>
</h2>

```typescript
let C3Instance2XLarge: InstanceType = "c3.2xlarge";
```

<h2 class="pdoc-module-header" id="C3Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L23">let C3Instance4XLarge</a>
</h2>

```typescript
let C3Instance4XLarge: InstanceType = "c3.4xlarge";
```

<h2 class="pdoc-module-header" id="C3Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L24">let C3Instance8XLarge</a>
</h2>

```typescript
let C3Instance8XLarge: InstanceType = "c3.8xlarge";
```

<h2 class="pdoc-module-header" id="C3InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L25">let C3InstanceLarge</a>
</h2>

```typescript
let C3InstanceLarge: InstanceType = "c3.large";
```

<h2 class="pdoc-module-header" id="C3InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L26">let C3InstanceXLarge</a>
</h2>

```typescript
let C3InstanceXLarge: InstanceType = "c3.xlarge";
```

<h2 class="pdoc-module-header" id="C4Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L27">let C4Instance2XLarge</a>
</h2>

```typescript
let C4Instance2XLarge: InstanceType = "c4.2xlarge";
```

<h2 class="pdoc-module-header" id="C4Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L28">let C4Instance4XLarge</a>
</h2>

```typescript
let C4Instance4XLarge: InstanceType = "c4.4xlarge";
```

<h2 class="pdoc-module-header" id="C4Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L29">let C4Instance8XLarge</a>
</h2>

```typescript
let C4Instance8XLarge: InstanceType = "c4.8xlarge";
```

<h2 class="pdoc-module-header" id="C4InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L30">let C4InstanceLarge</a>
</h2>

```typescript
let C4InstanceLarge: InstanceType = "c4.large";
```

<h2 class="pdoc-module-header" id="C4InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L31">let C4InstanceXLarge</a>
</h2>

```typescript
let C4InstanceXLarge: InstanceType = "c4.xlarge";
```

<h2 class="pdoc-module-header" id="D2Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L32">let D2Instance2XLarge</a>
</h2>

```typescript
let D2Instance2XLarge: InstanceType = "d2.2xlarge";
```

<h2 class="pdoc-module-header" id="D2Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L33">let D2Instance4XLarge</a>
</h2>

```typescript
let D2Instance4XLarge: InstanceType = "d2.4xlarge";
```

<h2 class="pdoc-module-header" id="D2Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L34">let D2Instance8XLarge</a>
</h2>

```typescript
let D2Instance8XLarge: InstanceType = "d2.8xlarge";
```

<h2 class="pdoc-module-header" id="D2InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L35">let D2InstanceXLarge</a>
</h2>

```typescript
let D2InstanceXLarge: InstanceType = "d2.xlarge";
```

<h2 class="pdoc-module-header" id="F1Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L36">let F1Instance16XLarge</a>
</h2>

```typescript
let F1Instance16XLarge: InstanceType = "f1.16xlarge";
```

<h2 class="pdoc-module-header" id="F1Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L37">let F1Instance2XLarge</a>
</h2>

```typescript
let F1Instance2XLarge: InstanceType = "f1.2xlarge";
```

<h2 class="pdoc-module-header" id="G2Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L38">let G2Instance2XLarge</a>
</h2>

```typescript
let G2Instance2XLarge: InstanceType = "g2.2xlarge";
```

<h2 class="pdoc-module-header" id="G2Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L39">let G2Instance8XLarge</a>
</h2>

```typescript
let G2Instance8XLarge: InstanceType = "g2.8xlarge";
```

<h2 class="pdoc-module-header" id="I3Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L40">let I3Instance16XLarge</a>
</h2>

```typescript
let I3Instance16XLarge: InstanceType = "i3.16xlarge";
```

<h2 class="pdoc-module-header" id="I3Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L41">let I3Instance2XLarge</a>
</h2>

```typescript
let I3Instance2XLarge: InstanceType = "i3.2xlarge";
```

<h2 class="pdoc-module-header" id="I3Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L42">let I3Instance4XLarge</a>
</h2>

```typescript
let I3Instance4XLarge: InstanceType = "i3.4xlarge";
```

<h2 class="pdoc-module-header" id="I3Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L43">let I3Instance8XLarge</a>
</h2>

```typescript
let I3Instance8XLarge: InstanceType = "i3.8xlarge";
```

<h2 class="pdoc-module-header" id="I3InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L44">let I3InstanceLarge</a>
</h2>

```typescript
let I3InstanceLarge: InstanceType = "i3.large";
```

<h2 class="pdoc-module-header" id="I3InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L45">let I3InstanceXLarge</a>
</h2>

```typescript
let I3InstanceXLarge: InstanceType = "i3.xlarge";
```

<h2 class="pdoc-module-header" id="M3Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L46">let M3Instance2XLarge</a>
</h2>

```typescript
let M3Instance2XLarge: InstanceType = "m3.2xlarge";
```

<h2 class="pdoc-module-header" id="M3InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L47">let M3InstanceLarge</a>
</h2>

```typescript
let M3InstanceLarge: InstanceType = "m3.large";
```

<h2 class="pdoc-module-header" id="M3InstanceMedium">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L48">let M3InstanceMedium</a>
</h2>

```typescript
let M3InstanceMedium: InstanceType = "m3.medium";
```

<h2 class="pdoc-module-header" id="M3InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L49">let M3InstanceXLarge</a>
</h2>

```typescript
let M3InstanceXLarge: InstanceType = "m3.xlarge";
```

<h2 class="pdoc-module-header" id="M4Instance10XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L50">let M4Instance10XLarge</a>
</h2>

```typescript
let M4Instance10XLarge: InstanceType = "m4.10xlarge";
```

<h2 class="pdoc-module-header" id="M4Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L51">let M4Instance16XLarge</a>
</h2>

```typescript
let M4Instance16XLarge: InstanceType = "m4.16xlarge";
```

<h2 class="pdoc-module-header" id="M4Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L52">let M4Instance2XLarge</a>
</h2>

```typescript
let M4Instance2XLarge: InstanceType = "m4.2xlarge";
```

<h2 class="pdoc-module-header" id="M4Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L53">let M4Instance4XLarge</a>
</h2>

```typescript
let M4Instance4XLarge: InstanceType = "m4.4xlarge";
```

<h2 class="pdoc-module-header" id="M4InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L54">let M4InstanceLarge</a>
</h2>

```typescript
let M4InstanceLarge: InstanceType = "m4.large";
```

<h2 class="pdoc-module-header" id="M4InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L55">let M4InstanceXLarge</a>
</h2>

```typescript
let M4InstanceXLarge: InstanceType = "m4.xlarge";
```

<h2 class="pdoc-module-header" id="P2Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L56">let P2Instance16XLarge</a>
</h2>

```typescript
let P2Instance16XLarge: InstanceType = "p2.16xlarge";
```

<h2 class="pdoc-module-header" id="P2Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L57">let P2Instance8XLarge</a>
</h2>

```typescript
let P2Instance8XLarge: InstanceType = "p2.8xlarge";
```

<h2 class="pdoc-module-header" id="P2InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L58">let P2InstanceXLarge</a>
</h2>

```typescript
let P2InstanceXLarge: InstanceType = "p2.xlarge";
```

<h2 class="pdoc-module-header" id="R3Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L59">let R3Instance2XLarge</a>
</h2>

```typescript
let R3Instance2XLarge: InstanceType = "r3.2xlarge";
```

<h2 class="pdoc-module-header" id="R3Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L60">let R3Instance4XLarge</a>
</h2>

```typescript
let R3Instance4XLarge: InstanceType = "r3.4xlarge";
```

<h2 class="pdoc-module-header" id="R3Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L61">let R3Instance8XLarge</a>
</h2>

```typescript
let R3Instance8XLarge: InstanceType = "r3.8xlarge";
```

<h2 class="pdoc-module-header" id="R3InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L62">let R3InstanceLarge</a>
</h2>

```typescript
let R3InstanceLarge: InstanceType = "r3.large";
```

<h2 class="pdoc-module-header" id="R3InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L63">let R3InstanceXLarge</a>
</h2>

```typescript
let R3InstanceXLarge: InstanceType = "r3.xlarge";
```

<h2 class="pdoc-module-header" id="R4Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L64">let R4Instance16XLarge</a>
</h2>

```typescript
let R4Instance16XLarge: InstanceType = "r4.16xlarge";
```

<h2 class="pdoc-module-header" id="R4Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L65">let R4Instance2XLarge</a>
</h2>

```typescript
let R4Instance2XLarge: InstanceType = "r4.2xlarge";
```

<h2 class="pdoc-module-header" id="R4Instance4XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L66">let R4Instance4XLarge</a>
</h2>

```typescript
let R4Instance4XLarge: InstanceType = "r4.4xlarge";
```

<h2 class="pdoc-module-header" id="R4Instance8XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L67">let R4Instance8XLarge</a>
</h2>

```typescript
let R4Instance8XLarge: InstanceType = "r4.8xlarge";
```

<h2 class="pdoc-module-header" id="R4InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L68">let R4InstanceLarge</a>
</h2>

```typescript
let R4InstanceLarge: InstanceType = "r4.large";
```

<h2 class="pdoc-module-header" id="R4InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L69">let R4InstanceXLarge</a>
</h2>

```typescript
let R4InstanceXLarge: InstanceType = "r4.xlarge";
```

<h2 class="pdoc-module-header" id="T2Instance2XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L70">let T2Instance2XLarge</a>
</h2>

```typescript
let T2Instance2XLarge: InstanceType = "t2.2xlarge";
```

<h2 class="pdoc-module-header" id="T2InstanceLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L71">let T2InstanceLarge</a>
</h2>

```typescript
let T2InstanceLarge: InstanceType = "t2.large";
```

<h2 class="pdoc-module-header" id="T2InstanceMedium">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L72">let T2InstanceMedium</a>
</h2>

```typescript
let T2InstanceMedium: InstanceType = "t2.medium";
```

<h2 class="pdoc-module-header" id="T2InstanceMicro">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L73">let T2InstanceMicro</a>
</h2>

```typescript
let T2InstanceMicro: InstanceType = "t2.micro";
```

<h2 class="pdoc-module-header" id="T2InstanceNano">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L74">let T2InstanceNano</a>
</h2>

```typescript
let T2InstanceNano: InstanceType = "t2.nano";
```

<h2 class="pdoc-module-header" id="T2InstanceSmall">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L75">let T2InstanceSmall</a>
</h2>

```typescript
let T2InstanceSmall: InstanceType = "t2.small";
```

<h2 class="pdoc-module-header" id="T2InstanceXLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L76">let T2InstanceXLarge</a>
</h2>

```typescript
let T2InstanceXLarge: InstanceType = "t2.xlarge";
```

<h2 class="pdoc-module-header" id="X1Instance16XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L77">let X1Instance16XLarge</a>
</h2>

```typescript
let X1Instance16XLarge: InstanceType = "x1.16xlarge";
```

<h2 class="pdoc-module-header" id="X1Instance32XLarge">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L78">let X1Instance32XLarge</a>
</h2>

```typescript
let X1Instance32XLarge: InstanceType = "x1.32xlarge";
```

<h2 class="pdoc-module-header" id="InstanceType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2/instanceType.ts#L80">type InstanceType</a>
</h2>

```typescript
type InstanceType = c3.2xlarge | c3.4xlarge | c3.8xlarge | c3.large | c3.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c4.large | c4.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge | d2.xlarge | f1.16xlarge | f1.2xlarge | g2.2xlarge | g2.8xlarge | i3.16xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.large | i3.xlarge | m3.2xlarge | m3.large | m3.medium | m3.xlarge | m4.10xlarge | m4.16xlarge | m4.2xlarge | m4.4xlarge | m4.large | m4.xlarge | p2.16xlarge | p2.8xlarge | p2.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r3.large | r3.xlarge | r4.16xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.large | r4.xlarge | t2.2xlarge | t2.large | t2.medium | t2.micro | t2.nano | t2.small | t2.xlarge | x1.16xlarge | x1.32xlarge;
```

