module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20230117210514-69d958e4ac83 // indirect
	github.com/pulumi/theme v0.0.0-20230104232221-88239bb01cba // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
