module github.com/pulumi/docs/tools/resourcedocsgen

go 1.15

require (
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/pkg/v2 v2.12.2
	github.com/pulumi/pulumi/sdk/v2 v2.12.2
)

replace (
	github.com/pulumi/pulumi/pkg/v2 => ../../../pulumi/pkg
	github.com/pulumi/pulumi/sdk/v2 => ../../../pulumi/sdk
	github.com/Sirupsen/logrus => github.com/sirupsen/logrus v1.5.0
)
