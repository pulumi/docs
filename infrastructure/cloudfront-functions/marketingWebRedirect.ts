// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Facet regex matches marketing-web's infra/www/viewer-request.ts; each \ is doubled to survive this literal.
export const marketingWebRedirectCode = `
function redirect(request, location) {
    var query = request.rawQueryString();
    return {
        statusCode: 301,
        statusDescription: 'Moved Permanently',
        headers: {
            'location': { value: query ? location + '?' + query : location },
            'cache-control': { value: 'max-age=604800' },
        },
    };
}

function isBarePath(uri) {
    return !uri.endsWith('/') && uri.indexOf('.', uri.lastIndexOf('/')) === -1;
}

function handler(event) {
    var request = event.request;
    var uri = request.uri;

    var legacyFacet = uri.match(/^\\/dev\\/browse\\/(cloud|language|tag|collection)\\/(.*)$/);
    if (legacyFacet) {
        var facet = '/dev/' + legacyFacet[1] + '/' + legacyFacet[2];
        return redirect(request, isBarePath(facet) ? facet + '/' : facet);
    }

    if (!isBarePath(uri)) {
        return request;
    }

    // marketing-web rewrites /dev/foo to /dev/foo.md for these, so a redirect would only add a hop.
    var accept = request.headers['accept'] ? request.headers['accept'].value : '';
    if (accept.indexOf('text/markdown') !== -1) {
        return request;
    }

    return redirect(request, uri + '/');
}
`;
