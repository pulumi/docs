.PHONY: default
default: banner build

.PHONY: all
all: banner build

.PHONY: banner
banner: 
	@echo -e "\033[1;37m=========================\033[0m"
	@echo -e "\033[1;37mPulumi Documentation Site\033[0m"
	@echo -e "\033[1;37m=========================\033[0m"

.PHONY: serve
serve: 
	@echo -e "\033[0;32mSERVE:\033[0m"
	bundler exec jekyll serve

.PHONY: build
build: 
	@echo -e "\033[0;32mBUILD:\033[0m"
	bundler exec jekyll build
