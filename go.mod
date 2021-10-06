module github.com/pulumi/pulumi-docs

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211006183715-8bfe690c3b3f // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20210929002709-940e5a1d2c43 // indirect
	github.com/pulumi/theme v0.0.0-20211001214832-2c758d993730 // indirect
)

// The override is needed because this repo is currently private and module at themes/default
// will be considered a private Go module as well. We could configure an SSH key to get around
// that but this is simpler for the time being.
replace github.com/pulumi/registry/themes/default => ../registry/themes/default
