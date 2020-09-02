import * as uuid from "uuid";

// Extracts a query string variable from the browser's location.
export function getQueryVariable(paramKey) :string {
    const query = window.location.search.substring(1);
    const vars = query.split("&");

    let paramVal = null
    vars.forEach( v => {
        const pair = v.split("=");
        if (pair[0] === paramKey) {
            paramVal = decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    })
    return paramVal;
}

export function getUUID() {
    return uuid.v4();
}

interface ClassNamesOptions {
    [key: string]: boolean;
}

export function classNames(baseClass: string, opts: ClassNamesOptions): string {
    const classes = [ baseClass ];
    const classesToCheck = Object.keys(opts);

    for (let i = 0; i < classesToCheck.length; i++) {
        const classToCheck = classesToCheck[i];

        if (opts[classToCheck]) {
            classes.push(classToCheck);
        }
    }

    return classes.join(" ");
}
