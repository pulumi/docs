module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220302010909-d03f7ae43bb6 // indirect
	github.com/pulumi/theme v0.0.0-20220303003800-4efaa926a4d0 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
