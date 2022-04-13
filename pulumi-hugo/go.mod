module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220413105207-4b1d8817cf18 // indirect
	github.com/pulumi/theme v0.0.0-20220413161117-81acd4117c85 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
