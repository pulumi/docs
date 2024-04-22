import pulumi

# Import the configuration values
config = pulumi.Config()

# Retrieve the value of "myEnvironment"
myValue = config.get("myEnvironment")

# Export the value as an output
pulumi.export('Value', myValue)