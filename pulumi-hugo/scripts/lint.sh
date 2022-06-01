#!/bin/bash

node ./scripts/lint/lint-markdown.js
yarn prettier --check .
