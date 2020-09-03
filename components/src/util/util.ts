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

// chunkArray splits up an array into chunks.
export function chunkArray<T>(array: T[], amount: number): T[][] {
    const result: T[][] = [[]];
    for (let i = 0; i < array.length; i++) {
        const item = array[i];
        const resultLastItem = result[result.length - 1];

        if (resultLastItem.length === amount) {
            result.push([item]);
            continue;
        }

        result[result.length - 1] = resultLastItem.concat([item]);
    }

    return result;
}

// classNames builds the class name of an HTML Element based on the true/false values
// in the options.
//
// Ex. const class = classNames("base-class", { "hidden": someVar });
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
