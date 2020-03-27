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
	yarn --cwd components install

.PHONY: lint_markdown
lint_markdown:
	yarn lint-markdown

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	yarn lint-markdown --no-error
	yarn --cwd components run build
	hugo server --buildDrafts --buildFuture

.PHONY: serve-components
serve-components:
	@echo -e "\033[0;32mSERVE COMPONENTS:\033[0m"
	yarn --cwd components run start

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/docs/reference/cli
	./scripts/mktutorial.sh

.PHONY: resource_docs
resource_docs::
	./scripts/gen_resource_docs.sh

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD ($(HUGO_ENVIRONMENT)):\033[0m"
	yarn lint-markdown
	NODE_ENV=production yarn --cwd components run build
	./scripts/run-hugo-build.sh
	node ./scripts/build-search-index.js < ./public/docs/search-data/index.json > ./public/docs/search-index.json
	rm -rf ./public/docs/search-data

.PHONY: test
test:
	./scripts/check-links.sh

.PHONY: ci_push
ci_push::
	$(MAKE) banner
	$(MAKE) ensure
# GITHUB_HEAD_REF will be set only for forked repos,
# so it is safe to check it and only run Pulumi if it is empty.
ifeq ($(GITHUB_HEAD_REF),)
	$(MAKE) build
	./scripts/run-pulumi.sh update production
else
	$(MAKE) build
endif

.PHONY: ci_pull_request
ci_pull_request::
	$(MAKE) banner
	$(MAKE) ensure
# GITHUB_HEAD_REF will be set only for forked repos,
# so it is safe to check it and only run Pulumi if it is empty.
ifeq ($(GITHUB_HEAD_REF),)
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
	$(MAKE) test
