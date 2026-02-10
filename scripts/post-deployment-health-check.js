#!/usr/bin/env node

const https = require('https');
const http = require('http');

const targetUrl = process.argv[2] || 'https://www.pulumi.com';
const isProduction = targetUrl.includes('pulumi.com');

const endpoints = [
    { path: '/', expectedStatus: 200, name: 'Homepage' },
    { path: '/docs', expectedStatus: 200, name: 'Docs landing' },
    { path: '/registry', expectedStatus: 200, name: 'Registry landing' },

    { path: '/docs/reference/pkg/nodejs/pulumi/pulumi/', expectedStatus: 200, name: 'Node.js SDK' },
    { path: '/docs/reference/pkg/python/pulumi/', expectedStatus: 200, name: 'Python SDK' },
    { path: '/docs/reference/pkg/dotnet/Pulumi/Pulumi.html', expectedStatus: 200, name: '.NET SDK' },
    { path: '/docs/reference/pkg/java/', expectedStatus: 200, name: 'Java SDK' },

    { path: '/docs/iac/get-started/', expectedStatus: 200, name: 'Getting started' },
    { path: '/docs/cli/commands/', expectedStatus: 200, name: 'CLI reference' },
];

const redirectTests = [
    {
        path: '/docs/intro/cloud-providers/aws/',
        expectedStatus: 301,
        expectedLocation: '/registry/packages/aws/',
        name: 'Cloud provider redirect'
    },
    {
        path: '/docs/reference/pkg/nodejs/pulumi/aws/',
        expectedStatus: 301,
        expectedLocationPattern: /\/docs\/reference\/pkg\/aws\/\?language=nodejs/,
        name: 'Node.js SDK redirect'
    },
];

function makeRequest(url, followRedirects = true) {
    return new Promise((resolve, reject) => {
        const protocol = url.startsWith('https') ? https : http;
        const options = { method: 'GET' };

        const req = protocol.get(url, options, (res) => {
            if (followRedirects && (res.statusCode === 301 || res.statusCode === 302)) {
                const location = res.headers.location;
                const redirectUrl = location.startsWith('http')
                    ? location
                    : new URL(location, url).toString();
                return makeRequest(redirectUrl, true).then(resolve).catch(reject);
            }

            resolve({
                statusCode: res.statusCode,
                headers: res.headers,
                location: res.headers.location
            });
        });

        req.on('error', reject);
        req.setTimeout(10000, () => {
            req.destroy();
            reject(new Error('Request timeout'));
        });
    });
}

async function testEndpoint(baseUrl, endpoint) {
    const url = new URL(endpoint.path, baseUrl).toString();

    try {
        const response = await makeRequest(url, true);

        if (response.statusCode !== endpoint.expectedStatus) {
            console.error(`❌ ${endpoint.name}: Expected ${endpoint.expectedStatus}, got ${response.statusCode}`);
            return false;
        }

        console.log(`✅ ${endpoint.name}: ${response.statusCode}`);
        return true;
    } catch (error) {
        console.error(`❌ ${endpoint.name}: ${error.message}`);
        return false;
    }
}

async function testRedirect(baseUrl, test) {
    const url = new URL(test.path, baseUrl).toString();

    try {
        const response = await makeRequest(url, false);

        if (response.statusCode !== test.expectedStatus) {
            console.error(`❌ ${test.name}: Expected ${test.expectedStatus}, got ${response.statusCode}`);
            return false;
        }

        if (test.expectedLocation && response.location !== test.expectedLocation) {
            console.error(`❌ ${test.name}: Expected location ${test.expectedLocation}, got ${response.location}`);
            return false;
        }

        if (test.expectedLocationPattern && !test.expectedLocationPattern.test(response.location)) {
            console.error(`❌ ${test.name}: Location ${response.location} doesn't match pattern`);
            return false;
        }

        console.log(`✅ ${test.name}: ${response.statusCode} → ${response.location}`);
        return true;
    } catch (error) {
        console.error(`❌ ${test.name}: ${error.message}`);
        return false;
    }
}

async function main() {
    console.log(`\n🏥 Post-Deployment Health Check`);
    console.log(`Target: ${targetUrl}\n`);

    let allPassed = true;

    console.log('Testing endpoints...');
    for (const endpoint of endpoints) {
        const passed = await testEndpoint(targetUrl, endpoint);
        allPassed = allPassed && passed;
    }

    console.log('\nTesting Lambda@Edge redirects...');
    for (const test of redirectTests) {
        const passed = await testRedirect(targetUrl, test);
        allPassed = allPassed && passed;
    }

    console.log('\n' + '='.repeat(50));
    if (allPassed) {
        console.log('✅ All health checks passed!');
        process.exit(0);
    } else {
        console.log('❌ Some health checks failed!');
        process.exit(1);
    }
}

main().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
