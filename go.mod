module github.com/pulumi/pulumi-docs

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20210921220917-4cd003f8b3fa // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20210827215118-ba028ca54298 // indirect
	github.com/pulumi/theme v0.0.0-20210916192005-a7b8b129e78c // indirect
)

// The override is needed because this repo is currently private and module at themes/default
// will be considered a private Go module as well. We could configure an SSH key to get around
// that but this is simpler for the time being.
replace github.com/pulumi/registry/themes/default => /Users/dgrove/go/src/github.com/pulumi/registry/themes/default
