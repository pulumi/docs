.PHONY: default
default: banner generate build

.PHONY: all
all: banner generate build

.PHONY: banner
banner:
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Website           \033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

.PHONY: clean
clean:
	./scripts/clean.sh

.PHONY: ensure
ensure: clean
	./scripts/ensure.sh

.PHONY: ensure_tools
ensure_tools:
	echo "Restoring resourcedocsgen deps..."
	cd tools/resourcedocsgen && go mod download

.PHONY: serve
serve:
	./scripts/serve.sh

.PHONY: serve-static
serve-static:
	yarn run http-server public

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/docs/cli/commands
	./scripts/mktutorial.sh

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD:\033[0m"
	./scripts/build-site.sh

.PHONY: check_links
check_links:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/link-checker/check-links.sh "https://www.pulumi.com"

.PHONY: check_search_urls
check_search_urls:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/search/check-urls.sh production "https://www.pulumi.com"

.PHONY: new_learn_module
new_learn_module:
	./scripts/new-learn-module.sh

.PHONY: copy_static_prebuilt
copy_static_prebuilt:
	mkdir -p public && cp -R static-prebuilt/* public/

.PHONY: new_learn_topic
new_learn_topic:
	./scripts/new-learn-topic.sh

.PHONY: ci_push
ci_push::
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/ci-push.sh

.PHONY: ci_pull_request
ci_pull_request:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/ci-pull-request.sh

.PHONY: ci_pull_request_closed
ci_pull_request_closed:
	$(MAKE) banner
	./scripts/ci-pull-request-closed.sh

.PHONY: ci_bucket_cleanup
ci_bucket_cleanup:
	$(MAKE) banner
	./scripts/ci-bucket-cleanup.sh

.PHONY: ci_update_search_index
ci_update_search_index:
	$(MAKE) ensure
	echo "Updating search index in ${DEPLOYMENT_ENVIRONMENT}..."
	./scripts/ci-update-search-index.sh "${DEPLOYMENT_ENVIRONMENT}"
