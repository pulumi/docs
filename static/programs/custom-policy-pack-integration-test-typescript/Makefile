ensure: 
	make -C ../custom-policy-pack-typescript ensure

test: ensure

	PULUMI_CONFIG_PASSPHRASE="foo" pulumi login --local
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi install
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi cancel --stack organization/custom-policy-pack-integration-test/dev --yes
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi destroy --stack organization/custom-policy-pack-integration-test/dev --yes --refresh --remove
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi stack init organization/custom-policy-pack-integration-test/dev --non-interactive
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi stack select organization/custom-policy-pack-integration-test/dev
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi config set aws:region us-west-2
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi preview --policy-pack ../custom-policy-pack-typescript

.PHONY: test ensure