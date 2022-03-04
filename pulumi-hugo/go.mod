module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220304184422-38a11542fa36 // indirect
	github.com/pulumi/theme v0.0.0-20220303225500-a190487e91b9 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
