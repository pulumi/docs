#!/bin/bash

clean_gomods() {
    local requires=0
    local i=0

    for file in $(find ./static/programs/* -name 'go.mod' -not -path "**/node_modules/**" )
    do
        new_file="$(cat $file)"
        split_at="$(awk '/require/{i++; if (i==2) { print NR-1; exit }}' $file)"

        if [[ "$split_at" != "" ]]; then
            new_file="$(cat $file | head -n $split_at)"
        fi

        echo "$new_file" > "$file"
    done
}
