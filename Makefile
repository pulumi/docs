# The HUGO_ENVIRONMENT environment variable determines which Hugo environment
# to build/serve.
HUGO_ENVIRONMENT ?= development

.PHONY: default
default: banner generate build

.PHONY: all
all: banner generate build

.PHONY: banner
banner:
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Website           \033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

.PHONY: ensure
ensure:
	yarn install

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	hugo server --buildDrafts --buildFuture

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/docs/reference/cli

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD ($(HUGO_ENVIRONMENT)):\033[0m"
	hugo
	node ./scripts/build-search-index.js < ./public/docs/search-data/index.json > ./public/docs/search-index.json
	rm -rf ./public/docs/search-data

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
		--exclude "/docs/reference/pkg" \
		--exclude "/docs/reference/changelog" \
		--exclude "https://github.com/pulumi/docs/edit/master" \
		--exclude "https://www.linkedin.com/" \
		--exclude "https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task" \
		--exclude "https://blog.mapbox.com/" \
		--exclude "https://github.com/pulls?"

.PHONY: validate
validate:
	hugo server \
	    --buildDrafts --disableBrowserError --disableLiveReload \
	    &>/dev/null &
	while ! nc -z localhost 1313; do sleep 0.1; done
	$(MAKE) test
	pkill -f hugo

.PHONY: travis_push
travis_push::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),staging)
	HUGO_ENVIRONMENT=staging $(MAKE) build
	$(MAKE) validate
	./scripts/run-pulumi.sh update staging
else ifeq ($(TRAVIS_BRANCH),master)
	HUGO_ENVIRONMENT=production $(MAKE) build
	$(MAKE) validate
	./scripts/run-pulumi.sh update production
else
	$(MAKE) build
	$(MAKE) validate
endif

.PHONY: travis_pull_request
travis_pull_request::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),staging)
	HUGO_ENVIRONMENT=staging $(MAKE) build
	$(MAKE) validate
	./scripts/run-pulumi.sh preview staging
else ifeq ($(TRAVIS_BRANCH),master)
	HUGO_ENVIRONMENT=production $(MAKE) build
	$(MAKE) validate
	./scripts/run-pulumi.sh preview production
else
	$(MAKE) build
	$(MAKE) validate
endif

.PHONY: travis_cron
travis_cron::
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) build
	$(MAKE) validate
