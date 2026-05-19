# If mise (https://mise.jdx.dev) is installed locally, route tool
# invocations through `mise exec --` so the versions pinned in mise.toml
# resolve whether or not the dev has activated mise in their shell.
# If mise isn't present (e.g. in CI, which installs tools via dedicated
# actions), $(MISE) expands to nothing and the system PATH is used.
MISE := $(shell command -v mise > /dev/null 2>&1 && echo "mise exec --")

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
	$(MAKE) sync-icons
	./scripts/fetch-openapi-spec.sh
	$(MISE) node scripts/fetch-github-stars.js
	$(MAKE) build-assets

.PHONY: sync-icons
sync-icons:
	$(MISE) node scripts/sync-icons.js
	$(MISE) node scripts/normalize-custom-icons.js
	$(MISE) node scripts/build-icon-sprite.js

.PHONY: update-repos
update-repos:
	./scripts/update_repos.sh

.PHONY: update-versions
update-versions:
	$(MISE) node scripts/get-cli-versions.js

.PHONY: serve
serve:
	$(MISE) ./scripts/serve.sh

.PHONY: serve-static
serve-static:
	$(MISE) yarn run http-server public

.PHONY: recent-posts
recent-posts:
	@echo -e "\033[0;32mRecent blog posts:\033[0m"
	cd scripts/python && pipenv install && pipenv run python list_recent_posts.py --format full

.PHONY: generate-related-tags
generate-related-tags:
	@echo -e "\033[0;32mGenerating tag-based related posts...\033[0m"
	cd scripts/python && pipenv install && pipenv run python generate_tag_related.py
	@echo -e "\033[0;32mDone! Updated data/related.yaml\033[0m"

.PHONY: build
build:
	@echo -e "\033[0;32mBUILD:\033[0m"
	$(MAKE) build-assets
	$(MISE) ./scripts/build-site.sh

.PHONY: lint-markdown
lint-markdown:
	@echo -e "\033[0;32mLINT MARKDOWN OUTPUT:\033[0m"
	$(MISE) node scripts/join-markdown-lines.js
	cp .markdownlint-cli2-markdown-output.jsonc public/.markdownlint-cli2.jsonc
	# --fix pass may exit non-zero after applying fixes; the unfixed lint run below is the real gate
	cd public && $(MISE) npx markdownlint-cli2 --fix "docs/**/index.md" || true
	cd public && $(MISE) npx markdownlint-cli2 "docs/**/index.md"

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
	./node_modules/.bin/concurrently --kill-others -r "$(MISE) ./scripts/serve.sh" "$(MISE) yarn --cwd ./theme run start"

.PHONY: build-assets
build-assets:
	$(MISE) yarn --cwd ./theme run build

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
	@echo "⚠️  DEPRECATED: This command is no longer maintained."
	@echo ""
	@echo "Please use the Claude Code slash command instead:"
	@echo "  /new-blog-post"
	@echo ""
	@echo "The slash command provides:"
	@echo "  • Automatic author detection from git config"
	@echo "  • Smart author onboarding for new contributors"
	@echo "  • Pre-populated fields to reduce manual work"
	@echo "  • Consistent structure matching latest standards"
	@echo ""
	@echo "If you don't have Claude Code, see: https://claude.com/claude-code"
	@echo ""
	@echo "Running the old command anyway... (Ctrl+C to cancel)"
	@bash -c 'read -p "Slug (e.g., \"my-new-post\"): " slug; hugo new --kind blog-post --contentDir content "blog/$$slug"'

.PHONY: lint
lint:
	$(MISE) ./scripts/lint.sh

.PHONY: lint-prose
lint-prose:
	@echo -e "\033[0;32mLINT PROSE (Vale):\033[0m"
	$(MISE) ./scripts/lint-prose.sh $(ARGS)

.PHONY: format
format:
	$(MISE) ./scripts/format.sh

.PHONY: new-dev-stack
new-dev-stack:
	./scripts/create-dev-stack.sh

.PHONY: deploy-dev-stack
deploy-dev-stack:
	./scripts/deploy-dev-stack.sh

.PHONY: destroy-dev-stack
destroy-dev-stack:
	./scripts/destroy-dev-stack.sh
