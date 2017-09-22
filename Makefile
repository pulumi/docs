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

.PHONY: serve
serve: 
	@echo -e "\033[0;32mSERVE:\033[0m"
	bundler exec jekyll serve --strict_front_matter

.PHONY: generate
generate:
	@echo -e "\033[0;32mGENERATE:\033[0m"
	./scripts/run_typedoc.sh

.PHONY: build
build: 
	@echo -e "\033[0;32mBUILD:\033[0m"
	bundle install
	bundler exec jekyll build
