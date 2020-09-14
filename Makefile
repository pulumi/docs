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
ensure:
	./scripts/ensure.sh

.PHONY: ensure_tools
ensure_tools:
	echo "Restoring resourcedocsgen deps..."
	cd tools/resourcedocsgen && go mod tidy && go mod download

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	$(MAKE) lint
	./scripts/serve.sh

.PHONY: serve_components
serve_components:
	@echo -e "\033[0;32mSERVE COMPONENTS:\033[0m"
	yarn --cwd components run start

.PHONY: build_components
build_components:
	@echo -e "\033[0;32mBUILD COMPONENTS:\033[0m"
	yarn --cwd components run build

.PHONY: build_search_index
build_search_index:
	@echo -e "\033[0;32mBUILD SEARCH INDEX:\033[0m"
	node ./scripts/build-search-index.js < ./public/docs/search-data/index.json > ./public/docs/search-index.json
	rm -rf ./public/docs/search-data

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	pulumi gen-markdown ./content/docs/reference/cli
	./scripts/mktutorial.sh

.PHONY: copy_static_prebuilt
copy_static_prebuilt:
	mkdir -p public && cp -R static-prebuilt/* public/

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD:\033[0m"
	$(MAKE) lint
	./scripts/build-site.sh

.PHONY: lint
lint:
	yarn run lint-markdown

.PHONY: test
test:
	$(MAKE) check_links_local

.PHONY: check_links_local
check_links_local:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/check-links.sh local

.PHONY: check_links
check_links:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/check-links.sh www

.PHONY: remove_buckets
remove_buckets:
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/remove-recent-buckets.sh push
	./scripts/remove-recent-buckets.sh pr

.PHONY: ci_push
ci_push::
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) lint
	./scripts/ci-push.sh

.PHONY: ci_pull_request
ci_pull_request:
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) lint
	./scripts/ci-pull-request.sh

.PHONY: ci_pull_request_closed
ci_pull_request_closed:
	$(MAKE) banner
	./scripts/ci-pull-request-closed.sh
