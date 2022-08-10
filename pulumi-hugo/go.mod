module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220802121037-df31798f61b8 // indirect
	github.com/pulumi/theme v0.0.0-20220810160555-fcce60a17add // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
