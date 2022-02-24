module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220223224643-3b1717eef395 // indirect
	github.com/pulumi/theme v0.0.0-20220222233350-49bbdb42cc1c // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
