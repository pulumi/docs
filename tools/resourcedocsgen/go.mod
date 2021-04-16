module github.com/pulumi/docs/tools/resourcedocsgen

go 1.16

require (
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/pkg/v3 v3.0.0-rc.1.0.20210416174742-3cc917164c0b
	github.com/pulumi/pulumi/sdk/v3 v3.0.0-rc.1.0.20210416174742-3cc917164c0b
)

replace (
	github.com/Sirupsen/logrus => github.com/sirupsen/logrus v1.5.0
	github.com/pulumi/pulumi/pkg/v3 => ../../../pulumi/pkg
	github.com/pulumi/pulumi/sdk/v3 => ../../../pulumi/sdk
)
