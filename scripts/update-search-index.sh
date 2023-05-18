#!/bin/bash

node --max-old-space-size=8192 ./scripts/search/main.js "$1"
