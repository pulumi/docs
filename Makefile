.PHONY: default
default: banner generate build

.PHONY: all
all: banner generate build

.PHONY: banner
banner:
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Documentation Site\033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

.PHONY: ensure
ensure:
	yarn install

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	hugo server -D

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/reference/cli

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD:\033[0m"
	hugo
	node ./scripts/build-search-index.js < ./public/search-data/index.json > ./public/search-index.json
	rm -rf ./public/search-data

.PHONY: test
test:
	# We exclude a few links:
	#     - Our generated API docs have lots of broken links
	#     - Our changelog includes links to private repos
	#     - GitHub Edit Links may be broken, because the page might not yet exist!
	#     - Our LinkedIn page, for some reason, returns an HTTP error (despite being valid)
	#     - Our Visual Studio Marketplace link for the Azure Pipelines task extension,
	#       although valid and publicly available, is reported as a broken link.
	# Fixes for the former two are tracked by https://github.com/pulumi/docs/issues/568.
	./node_modules/.bin/blc http://localhost:1313 -r \
		--exclude "/reference/pkg" \
		--exclude "/reference/changelog" \
		--exclude "https://github.com/pulumi/docs/edit/master" \
		--exclude "https://www.linkedin.com/company/pulumi/" \
		--exclude "https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task"

.PHONY: validate
validate:
	hugo server -D --disableBrowserError --disableLiveReload &>/dev/null &
	while ! nc -z localhost 1313; do sleep 0.1; done
	$(MAKE) test
	pkill -f hugo

.PHONY: preview
preview:
	@echo -e "\033[0;32mPREVIEW:\033[0m"
ifeq ($(TRAVIS_BRANCH),master)
	./scripts/preview.sh staging
endif
ifeq ($(TRAVIS_BRANCH),production)
	./scripts/preview.sh production
endif

.PHONY: deploy
deploy:
	@echo -e "\033[0;32mDEPLOY:\033[0m"
ifeq ($(TRAVIS_BRANCH),master)
	./scripts/update.sh staging
endif
ifeq ($(TRAVIS_BRANCH),production)
	./scripts/update.sh production
endif

.PHONY: travis_push
travis_push::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),master)
	HUGO_BASEURL=https://staging.pulumi.io/ $(MAKE) build
else
	$(MAKE) build
endif
	$(MAKE) deploy

.PHONY: travis_pull_request
travis_pull_request::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),master)
	HUGO_BASEURL=https://staging.pulumi.io/ $(MAKE) build
else
	$(MAKE) build
endif
	$(MAKE) validate
	$(MAKE) preview

.PHONY: travis_cron
travis_cron::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),master)
	HUGO_BASEURL=https://staging.pulumi.io/ $(MAKE) build
else
	$(MAKE) build
endif

.PHONY: travis_api
travis_api::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),master)
	HUGO_BASEURL=https://staging.pulumi.io/ $(MAKE) build
else
	$(MAKE) build
endif
