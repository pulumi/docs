.PHONY: default
default: banner generate build

.PHONY: all
all: banner generate build

.PHONY: banner
banner: 
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Documentation Site\033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

.PHONY: docker
docker:
	docker build . -t docs
	docker run -it -p 4000:4000 docs

.PHONY: configure
configure:
	@echo -e "\033[0;32mCONFIGURE:\033[0m"
	gem install jekyll bundler

.PHONY: ensure
ensure:
	bundle install --path=./vendor
	npm install broken-link-checker typedoc

.PHONY: serve
serve: 
	@echo -e "\033[0;32mSERVE:\033[0m"
	@bundle exec jekyll serve --strict_front_matter --host 0.0.0.0 --incremental

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	pulumi gen-markdown ./reference/cli

.PHONY: build
build: 
	@echo -e "\033[0;32mBUILD:\033[0m"
	bundle install --path=./vendor
	bundler exec jekyll build
	node ./scripts/build-search-index.js < ./_site/search-data.json > ./_site/search-index.json
	rm ./_site/search-data.json

.PHONY: test
test:
	# We exclude a few links:
	#     - Our generated API docs have lots of broken links
	#     - Our changelog includes links to private repos
	#     - GitHub Edit Links may be broken, because the page might not yet exist!
	#     - Our LinkedIn page, for some reason, returns an HTTP error (despite being valid)
	# Fixes for the former two are tracked by https://github.com/pulumi/docs/issues/568.
	./node_modules/.bin/blc http://localhost:4000 -r \
		--exclude "/reference/pkg" \
		--exclude "/reference/changelog.html" \
		--exclude "https://github.com/pulumi/docs/edit/master" \
		--exclude "https://www.linkedin.com/company/pulumi/"

.PHONY: validate
validate:
	bundle exec jekyll serve --strict_front_matter --host 0.0.0.0 --incremental --detach >/dev/null 2>&1
	$(MAKE) test
	pkill -f jekyll

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
travis_push:: banner ensure build deploy

.PHONY: travis_pull_request
travis_pull_request:: banner ensure build validate preview

.PHONY: travis_cron
travis_cron:: banner ensure build

.PHONY: travis_api
travis_api:: banner ensure build
