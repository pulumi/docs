import pulumi

# Import the configuration values
config = pulumi.Config()

# Retrieve the values of "region" and "apiKey"
region = config.get("region")
api_key = config.get_secret("apiKey")

# Export the values as an output
pulumi.export('Region', region)
pulumi.export("ApiKey", api_key)