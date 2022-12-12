module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20221212191356-8d3cf7df29f5 // indirect
	github.com/pulumi/theme v0.0.0-20221212191246-d8c9ccd48bc9 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
