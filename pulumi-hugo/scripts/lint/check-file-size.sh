#! /bin/bash

# list files staged for commit
git diff --staged --name-only | \
while read line; do
    # ignore the generated bundles
    if [[ $line == "themes/default/assets/css/bundle.css" || $line == "themes/default/assets/css/marketing.css" || $line == "themes/default/assets/js/bundle.js" || $line == "themes/default/assets/js/marketing.js" ]]; then
        continue
    fi

    echo $line

    # get size in bytes
    size=$(wc -c "$line" | awk '{print $1}');
    # verify staged files less than 3MB
    if [ $((size)) -gt 3000000 ]; then
        echo -e "\033[93m WARNING: $line greater than 3MB in size. \033[0m"
        exit 1
    fi
done
