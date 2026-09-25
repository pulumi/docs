from typing import Any

import pulumi


# Fields of pulumi.StateMigrationArgs, shown here for reference.
class StateMigrationArgs:
    urn: str
    old_state: list[dict[str, Any]]


# Fields of pulumi.StateMigrationResult, shown here for reference.
class StateMigrationResult:
    new_state: list[dict[str, Any]]
    successors: dict[str, str] | None


def migrate(args: pulumi.StateMigrationArgs) -> pulumi.StateMigrationResult | None:
    # args.urn identifies the component being registered.
    # args.old_state contains the component's prior state and its descendants.
    # Return pulumi.StateMigrationResult(new_state=..., successors=...) when needed.
    return None


component = MyComponent(
    "example",
    opts=pulumi.ResourceOptions(state_migrations=[migrate]),
)
