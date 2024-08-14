import pulumi

# Import the configuration values
config = pulumi.Config()

# Retrieve the values of "myEnvironment" and "myPassword"
environment = config.get("myEnvironment")
password = config.get_secret("myPassword")

# Export the values as an output
pulumi.export('Environment', environment)
pulumi.export("Password", password)