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

.PHONY: lint_markdown
lint_markdown:
	yarn lint-markdown

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	yarn lint-markdown --no-error
	hugo server --buildDrafts --buildFuture

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/docs/reference/cli
	./scripts/mktutorial.sh

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD ($(HUGO_ENVIRONMENT)):\033[0m"
	yarn lint-markdown
	NODE_ENV=production hugo --minify
	node ./scripts/build-search-index.js < ./public/docs/search-data/index.json > ./public/docs/search-index.json
	rm -rf ./public/docs/search-data

.PHONY: test
test:
	./scripts/check-links.sh

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
ifeq ($(TRAVIS_BRANCH),master)
	$(MAKE) build
	./scripts/run-pulumi.sh update production
else
	$(MAKE) build
endif

.PHONY: travis_pull_request
travis_pull_request::
	$(MAKE) banner
	$(MAKE) ensure
ifeq ($(TRAVIS_BRANCH),master)
	$(MAKE) build
	./scripts/run-pulumi.sh preview production
else
	$(MAKE) build
endif

.PHONY: travis_cron
travis_cron::
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) build
	$(MAKE) validate
