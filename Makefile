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
	$(MAKE) build-assets

.PHONY: update-repos
update-repos:
	./scripts/update_repos.sh

.PHONY: serve
serve:
	./scripts/serve.sh

.PHONY: serve-static
serve-static:
	yarn run http-server public

.PHONY: recent-posts
recent-posts:
	@echo -e "\033[0;32mRecent blog posts:\033[0m"
	cd scripts/python && pipenv install && pipenv run python list_recent_posts.py --format full

.PHONY: generate-related-tags
generate-related-tags:
	@echo -e "\033[0;32mGenerating tag-based related posts...\033[0m"
	cd scripts/python && pipenv install && pipenv run python generate_tag_related.py
	@echo -e "\033[0;32mDone! Updated data/related.yaml\033[0m"

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	NOBUILD=true ./scripts/run_typedoc.sh
	./scripts/generate_python_docs.sh
	PULUMI_EXPERIMENTAL=true pulumi gen-markdown ./content/docs/cli/commands

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD:\033[0m"
	$(MAKE) build-assets
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

.PHONY: copy_static_prebuilt
copy_static_prebuilt:
	mkdir -p public && cp -R static-prebuilt/* public/

.PHONY: ci_push
ci_push::
	$(MAKE) banner
	$(MAKE) ensure
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

.PHONY: ci_bucket_cleanup
ci_bucket_cleanup:
	$(MAKE) banner
	./scripts/ci-bucket-cleanup.sh

.PHONY: ci_update_search_index
ci_update_search_index:
	echo "Updating search index: ${DEPLOYMENT_ENVIRONMENT}..."
	./scripts/ci-update-search-index.sh "${DEPLOYMENT_ENVIRONMENT}"

.PHONY: serve-all
serve-all:
	./node_modules/.bin/concurrently --kill-others -r "./scripts/serve.sh" "yarn --cwd ./theme run start"

.PHONY: build-assets
build-assets:
	yarn --cwd ./theme run build

.PHONY: test
test:
	$(MAKE) test-programs

.PHONY: test-programs
test-programs:
	./scripts/programs/test.sh preview

.PHONY: upgrade-programs
upgrade-programs:
	./scripts/programs/upgrade.sh

.PHONY: new-tutorial-module
new-tutorial-module:
	./scripts/content/new-tutorial-module.sh

.PHONY: new-tutorial-topic
new-tutorial-topic:
	./scripts/content/new-tutorial-topic.sh

.PHONY: new-tutorial
new-tutorial:
	./scripts/content/new-tutorial.sh

.PHONY: new-template
new-template:
	./scripts/content/new-template.sh

.PHONY: new-example-program
new-example-program:
	./scripts/content/new-example-program.sh

.PHONY: new-blog-post
new-blog-post:
	hugo new --kind blog-post --contentDir content \
	"blog/$(shell bash -c 'read -p "Slug (e.g., 'my-new-post'): " slug; echo $$slug')"

.PHONY: lint
lint:
	./scripts/lint.sh

.PHONY: format
format:
	./scripts/format.sh

.PHONY: new-dev-stack
new-dev-stack:
	./scripts/create-dev-stack.sh

.PHONY: deploy-dev-stack
deploy-dev-stack:
	./scripts/deploy-dev-stack.sh

.PHONY: destroy-dev-stack
destroy-dev-stack:
	./scripts/destroy-dev-stack.sh

.PHONY: generate-compliance-pages
generate-compliance-pages:
	node scripts/aws-compliance-scraper/scrape.js
	./scripts/content/generate-compliance-pages.sh