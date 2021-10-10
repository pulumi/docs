module github.com/pulumi/pulumi-docs

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211010051412-66896d757138 // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20211010051406-c0e202967a98 // indirect
	github.com/pulumi/theme v0.0.0-20211010000958-6bd881e4195f // indirect
)

// The override is needed because this repo is currently private and module at themes/default
// will be considered a private Go module as well. We could configure an SSH key to get around
// that but this is simpler for the time being.

replace github.com/pulumi/registry/themes/default => ../registry/themes/default
