.PHONY: default
default: banner generate build

.PHONY: all
all: banner generate build

.PHONY: banner
banner: 
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Documentation Site\033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

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
	bundler exec jekyll serve --strict_front_matter --host 0.0.0.0 --incremental

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
	@# Verify dashboard.json is valid JSON (e.g. doesn't have any trailing commas).
	jq -e . dashboard.json >/dev/null 2>&1

.PHONY: test
test:
	./node_modules/.bin/blc http://localhost:4000 -r --exclude-external  --exclude '*/releases/pulumi*' --exclude '*/examples/*' --exclude '*/reference/pkg/*'

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
travis_pull_request:: banner ensure build

.PHONY: travis_cron
travis_cron:: banner ensure build

.PHONY: travis_api
travis_api:: banner ensure build
