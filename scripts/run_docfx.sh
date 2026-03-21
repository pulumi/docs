#!/bin/bash
# Usage: run_docfx

set -o nounset -o errexit -o pipefail

# Build the .NET projects first so that protobuf-generated types (Pulumirpc) are
# present in the obj/ directories before docfx tries to compile them.
dotnet build ../pulumi-dotnet/sdk/Pulumi/Pulumi.csproj
dotnet build ../pulumi-dotnet/sdk/Pulumi.Automation/Pulumi.Automation.csproj

cd docfx
docfx
