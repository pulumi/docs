"use strict";
const pulumi = require("@pulumi/pulumi");

const sqlServer = pulumi.output({
    name: "myDbServer",
    ipAddress: "10.0.0.0/24",
});

const database = pulumi.output({
    name: "myExampleDatabase",
    engine: "sql-db",
});

exports.sqlServerName = sqlServer.name;
exports.databaseName = database.name;
