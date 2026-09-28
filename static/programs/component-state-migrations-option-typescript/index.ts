import * as pulumi from "@pulumi/pulumi";

// Shape of pulumi.StateMigrationArgs, shown here for reference.
type StateMigrationArgs = {
    urn: pulumi.URN;
    oldState: Record<string, any>[];
};

// Shape of pulumi.StateMigrationResult, shown here for reference.
type StateMigrationResult = {
    newState: Record<string, any>[];
    successors?: Record<pulumi.URN, pulumi.URN>;
};

function migrate(args: pulumi.StateMigrationArgs): pulumi.StateMigrationResult | undefined {
    // args.urn identifies the component being registered.
    // args.oldState contains the component's prior state and its descendants.
    // Return { newState, successors } when the state needs migration.
    return undefined;
}

const component = new MyComponent("example", {}, {
    stateMigrations: [migrate],
});
