// Adapted from https://lunrjs.com/guides/index_prebuilding.html

const lunr = require("../static/js/lunr.min.js");
const stdin = process.stdin;
const stdout = process.stdout;

let buffer = [];

stdin.resume();
stdin.setEncoding("utf8");

stdin.on("data", data => buffer.push(data));

stdin.on("end", () => {
    const data = JSON.parse(buffer.join(""));

    const index = lunr(function () {
        this.ref("ref");
        this.field("title", { boost: 10 });

        for (var url in data) {
            const page = data[url];
            if (page.title || page.content) {
                // We use '|' to separate the URL and title in the ref, so
                // ensure we haven't inadvertently introduced a page that
                // contains a '|' in its URL.
                if (url.indexOf("|") !== -1) {
                    throw new Error(`unexpected '|' in url: ${url}`);
                }

                this.add({
                    ref: url + "|" + page.title,
                    title: page.title,
                });
            }
        }
    })

    stdout.write(JSON.stringify(index));
});
