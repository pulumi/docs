// Shape of pulumi.StateMigrationArgs, shown here for reference.
type StateMigrationArgs struct {
    URN      pulumi.URN
    OldState []map[string]any
}

// Shape of pulumi.StateMigrationResult, shown here for reference.
type StateMigrationResult struct {
    NewState   []map[string]any
    Successors map[string]string
}

migrate := func(_ context.Context, args *pulumi.StateMigrationArgs) (*pulumi.StateMigrationResult, error) {
    // args.URN identifies the component being registered.
    // args.OldState contains the component's prior state and its descendants.
    // Return &pulumi.StateMigrationResult{NewState: ..., Successors: ...}, nil when needed.
    return nil, nil
}

component, err := NewMyComponent(ctx, "example",
    pulumi.StateMigrations([]pulumi.StateMigration{migrate}),
)
if err != nil {
    return err
}
