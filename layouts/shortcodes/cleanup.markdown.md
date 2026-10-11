Before moving on, tear down the resources that are part of your stack to avoid incurring any charges.

1. Run `pulumi destroy` to tear down all resources. You'll be prompted to make sure you really want to delete these resources. A destroy operation may take some time, since Pulumi waits for the resources to finish shutting down before it considers the destroy operation to be complete.
1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.
