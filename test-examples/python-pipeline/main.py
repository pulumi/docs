# Python example for data engineering team
import pulumi
import pulumi_aws as aws
import pulumi_azure_native as azure
import pandas as pd
from typing import List, Dict

class DataPipeline(pulumi.ComponentResource):
    """Multi-cloud data pipeline infrastructure."""
    
    def __init__(self, name: str, config: Dict, opts=None):
        super().__init__('custom:DataPipeline', name, None, opts)
        
        # Use pandas to analyze configuration and optimize deployment
        regions_df = pd.DataFrame(config['regions'])
        regions_df['cost_score'] = regions_df.apply(self._calculate_cost, axis=1)
        regions_df['latency_score'] = regions_df.apply(self._calculate_latency, axis=1)
        
        # Deploy to optimal regions based on analysis
        optimal_regions = regions_df.nsmallest(3, 'cost_score')
        
        for _, region in optimal_regions.iterrows():
            if region['provider'] == 'aws':
                self._create_aws_pipeline(name, region)
            elif region['provider'] == 'azure':
                self._create_azure_pipeline(name, region)
    
    def _calculate_cost(self, region: pd.Series) -> float:
        """Calculate cost score for a region (lower is better)."""
        base_costs = {'us-east-1': 1.0, 'us-west-2': 1.1, 'eu-west-1': 1.2}
        return base_costs.get(region['name'], 1.5)
    
    def _calculate_latency(self, region: pd.Series) -> float:
        """Calculate latency score for a region (lower is better)."""
        base_latency = {'us-east-1': 10, 'us-west-2': 50, 'eu-west-1': 100}
        return base_latency.get(region['name'], 200)
    
    def _create_aws_pipeline(self, name: str, region: pd.Series):
        # Create data lake
        data_lake = aws.s3.Bucket(
            f"{name}-{region['name']}-lake",
            versioning=aws.s3.BucketVersioningArgs(enabled=True),
            opts=pulumi.ResourceOptions(parent=self)
        )
        
        # Create processing Lambda
        processor = aws.lambda_.Function(
            f"{name}-processor",
            runtime="python3.9",
            handler="process.handler",
            code=pulumi.AssetArchive({'.': pulumi.FileArchive('./processor')}),
            environment=aws.lambda_.FunctionEnvironmentArgs(
                variables={'DATA_LAKE': data_lake.id}
            ),
            opts=pulumi.ResourceOptions(parent=self)
        )
        
        # Set up event triggers
        aws.s3.BucketNotification(
            f"{name}-trigger",
            bucket=data_lake.id,
            lambda_functions=[aws.s3.BucketNotificationLambdaFunctionArgs(
                lambda_function_arn=processor.arn,
                events=['s3:ObjectCreated:*'],
                filter_prefix='raw/',
            )],
            opts=pulumi.ResourceOptions(parent=self)
        )
    
    def _create_azure_pipeline(self, name: str, region: pd.Series):
        # Azure implementation would go here
        pass

# Usage example
if __name__ == "__main__":
    config_data = {
        'regions': [
            {'name': 'us-east-1', 'provider': 'aws'},
            {'name': 'us-west-2', 'provider': 'aws'},
            {'name': 'eu-west-1', 'provider': 'aws'},
        ]
    }
    
    pipeline = DataPipeline("data-pipeline", config_data)
    pulumi.export("pipeline_created", "success")