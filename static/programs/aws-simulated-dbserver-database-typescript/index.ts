import * as pulumi from "@pulumi/pulumi";

const sqlServer = pulumi.output({
    name: "myDbServer",
    ipAddress: "10.0.0.0/24",
});

const database = pulumi.output({
    name: "myExampleDatabase",
    engine: "sql-db",
});

export const sqlServerName = sqlServer.name;
export const databaseName = database.name;
