.PHONY: clean
clean:
	./scripts/clean.sh

.PHONY: ensure
ensure:
	./scripts/ensure.sh

.PHONY: lint
lint:
	./scripts/lint.sh

.PHONY: test
test:
	./scripts/test.sh

.PHONY: build
build:
	./scripts/build.sh

.PHONY: serve
serve:
	./scripts/serve.sh

.PHONY: serve-all
serve-all:
	./scripts/serve.sh all

.PHONY: ci-pull-request
ci-pull-request: ensure lint test
	./scripts/ci/pull-request.sh

.PHONY: ci-pull-request-closed
ci-pull-request-closed:
	./scripts/ci/pull-request-closed.sh

.PHONY: ci-scheduled
ci-scheduled:
	./scripts/ci/scheduled.sh

.PHONY: new-blog-post
new-blog-post:
	hugo new --kind blog-post \
		"themes/default/content/blog/$(shell bash -c 'read -p "Slug (e.g., 'my-new-post'): " slug; echo $$slug')"

.PHONY: new-learn-module
new-learn-module:
	./scripts/content/new-learn-module.sh

.PHONY: new-learn-topic
new-learn-topic:
	./scripts/content/new-learn-topic.sh
