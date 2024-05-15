import pulumi

sql_server = pulumi.Output.from_input({
    "name": "myDbServer",
    "ipAddress": "10.0.0.0/24",
});

database = pulumi.Output.from_input({
    "name": "myExampleDatabase",
    "engine": "sql-db",
});