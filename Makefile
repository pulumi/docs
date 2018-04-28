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
	bundle install
	npm install -g broken-link-checker

.PHONY: serve
serve: 
	@echo -e "\033[0;32mSERVE:\033[0m"
	bundler exec jekyll serve --strict_front_matter

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh
	pulumi gen-markdown ./reference/cli

.PHONY: build
build: 
	@echo -e "\033[0;32mBUILD:\033[0m"
	bundle install
	bundler exec jekyll build

.PHONY: test
test:
	blc http://localhost:4000 -r --exclude-external --exclude '*/packages/*' --exclude '*/releases/pulumi*' --exclude '*/examples/*'

.PHONY: deploy
deploy:
	@echo -e "\033[0;32mDEPLOY:\033[0m"
ifeq ($(TRAVIS_BRANCH),master)
	./scripts/deploy.sh staging
endif
ifeq ($(TRAVIS_BRANCH),production)
	./scripts/deploy.sh production
endif

.PHONY: travis_push
travis_push:: banner ensure build deploy

.PHONY: travis_pull_request
travis_pull_request:: banner ensure build

.PHONY: travis_cron
travis_cron:: banner ensure build

.PHONY: travis_api
travis_api:: banner ensure build
