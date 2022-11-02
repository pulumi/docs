module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20221101232100-4cb4fc2c9ec4 // indirect
	github.com/pulumi/theme v0.0.0-20221102140116-a8c5cff57f9e // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
