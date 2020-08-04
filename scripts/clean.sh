#!/bin/bash

yarn cache clean
rm -rf node_modules
rm -rf components/node_modules
rm -rf infrastructure/node_modules
rm -rf public
rm -rf cypress/screenshots
rm -rf cypress/videos
rm -f origin-bucket-metadata.json
rm -f redirects.txt
