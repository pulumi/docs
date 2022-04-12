module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220412185656-e66127e08308 // indirect
	github.com/pulumi/theme v0.0.0-20220408190516-8a57775e2cfc // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
