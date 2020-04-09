module github.com/pulumi/docs/tools/resourcedocsgen

go 1.13

require (
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/pkg v1.14.0
	github.com/pulumi/pulumi/sdk v1.14.0
)

replace (
	github.com/pulumi/pulumi/pkg => ../../../pulumi/pkg
	github.com/pulumi/pulumi/sdk => ../../../pulumi/sdk
)
