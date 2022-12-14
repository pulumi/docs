module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20221214013438-c3182fd14fb3 // indirect
	github.com/pulumi/theme v0.0.0-20221212233240-164b90446d56 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
