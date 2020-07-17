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
	rm -rf node_modules
	rm -rf components/node_modules
	rm -rf public

.PHONY: ensure
ensure:
	./scripts/ensure.sh

.PHONY: ensure_tools
ensure_tools:
	echo "Restoring resourcedocsgen deps..."
	cd tools/resourcedocsgen && go mod tidy && go mod download

.PHONY: lint_markdown
lint_markdown:
	yarn lint-markdown

.PHONY: serve
serve:
	@echo -e "\033[0;32mSERVE:\033[0m"
	yarn lint-markdown --no-error
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
	yarn lint-markdown
	./scripts/build-site.sh

.PHONY: bucketize
bucketize:
	@echo -e "\033[0;32mBUCKETIZE:\033[0m"
	./scripts/bucketize.sh

.PHONY: pulumify
pulumify:
	@echo -e "\033[0;32mBUILD PULUMIFY:\033[0m"
	$(MAKE) ensure
	./scripts/build-site.sh preview

.PHONY: test
test:
	$(MAKE) check_links_local

.PHONY: check_links_local
check_links_local::
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/check-links.sh local

.PHONY: ci_push
ci_push::
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) build
	$(MAKE) bucketize
	./scripts/run-pulumi.sh update

.PHONY: ci_pull_request
ci_pull_request::
	$(MAKE) banner
	$(MAKE) ensure
	$(MAKE) build
	$(MAKE) test
	./scripts/run-pulumi.sh preview

.PHONY: ci_schedule
ci_schedule::
	$(MAKE) banner
	$(MAKE) ensure
	./scripts/check-links.sh www
