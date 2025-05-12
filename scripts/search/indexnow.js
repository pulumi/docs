/**
 * IndexNow API implementation for Pulumi docs
 * 
 * This script submits new or updated URLs to the IndexNow API
 * to trigger immediate crawling by search engines.
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const Sitemapper = require('sitemapper');
const sitemap = new Sitemapper();

// IndexNow API settings
const INDEXNOW_ENDPOINT = 'https://www.bing.com/indexnow';
const INDEXNOW_API_KEY = process.env.INDEXNOW_API_KEY || '33134703c43349ddb227d769745f33cc';
const INDEXNOW_KEY_LOCATION = 'indexnow.txt';
// Cache file to store previously submitted URLs
const CACHE_FILE = path.join(__dirname, '../../public/indexnow-submitted-urls.json');
const BATCH_SIZE = 10000; // Maximum number of URLs per batch (IndexNow allows up to 10,000)
const SITE_URL = 'https://www.pulumi.com';

// Get environment
const isTestMode = process.env.INDEXNOW_TEST_MODE === 'true';

/**
 * Get URLs from sitemap
 */
async function getSitemapUrls() {
    console.log('Fetching sitemap URLs...');
    try {
        const result = await sitemap.fetch(`${SITE_URL}/sitemap.xml`);
        return result.sites
            // Filter out any excluded patterns if needed
            // For example: .filter(url => !url.match(/\/api-docs\//))
            .map(url => url.trim())
            .sort();
    } catch (error) {
        console.error('Error fetching sitemap:', error);
        return [];
    }
}

/**
 * Load previously submitted URLs from cache file
 */
function loadSubmittedUrls() {
    try {
        if (fs.existsSync(CACHE_FILE)) {
            const data = fs.readFileSync(CACHE_FILE, 'utf8');
            return JSON.parse(data);
        }
    } catch (error) {
        console.warn('Error loading submitted URLs cache, starting fresh:', error.message);
    }
    return {
        lastSubmission: null,
        urls: {}
    };
}

/**
 * Save submitted URLs to cache file
 */
function saveSubmittedUrls(cache) {
    try {
        // Ensure the directory exists
        const dir = path.dirname(CACHE_FILE);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
        fs.writeFileSync(CACHE_FILE, JSON.stringify(cache, null, 2));
    } catch (error) {
        console.error('Error saving submitted URLs cache:', error);
    }
}

/**
 * Submit URLs to IndexNow API
 */
async function submitToIndexNow(urls) {
    if (urls.length === 0) {
        console.log('No URLs to submit.');
        return;
    }

    // Split URLs into batches (IndexNow allows up to 10,000 URLs per submission)
    for (let i = 0; i < urls.length; i += BATCH_SIZE) {
        const batch = urls.slice(i, Math.min(i + BATCH_SIZE, urls.length));
        
        console.log(`Submitting batch of ${batch.length} URLs to IndexNow...`);
        
        // Prepare data for IndexNow API
        const data = JSON.stringify({
            host: new URL(SITE_URL).hostname,
            key: INDEXNOW_API_KEY,
            keyLocation: `${SITE_URL}/${INDEXNOW_KEY_LOCATION}`,
            urlList: batch
        });

        if (isTestMode) {
            console.log('TEST MODE - would submit:');
            console.log(`Endpoint: ${INDEXNOW_ENDPOINT}`);
            console.log(`Data: ${data}`);
            continue;
        }

        // Submit to IndexNow API
        try {
            await new Promise((resolve, reject) => {
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Content-Length': data.length
                    }
                };

                const req = https.request(INDEXNOW_ENDPOINT, options, (res) => {
                    let responseData = '';
                    
                    res.on('data', (chunk) => {
                        responseData += chunk;
                    });
                    
                    res.on('end', () => {
                        if (res.statusCode >= 200 && res.statusCode < 300) {
                            console.log(`Successfully submitted ${batch.length} URLs to IndexNow.`);
                            resolve();
                        } else {
                            console.error(`IndexNow API error (${res.statusCode}): ${responseData}`);
                            reject(new Error(`IndexNow API returned status ${res.statusCode}: ${responseData}`));
                        }
                    });
                });

                req.on('error', (error) => {
                    console.error('Error submitting to IndexNow:', error);
                    reject(error);
                });

                req.write(data);
                req.end();
            });
        } catch (error) {
            console.error('Failed to submit batch to IndexNow:', error);
            // Continue with the next batch even if this one failed
        }
    }
}

/**
 * Generate the IndexNow API key verification file
 */
function generateKeyFile() {
    console.log('Generating IndexNow key verification file...');
    const keyFilePath = path.join(__dirname, '../../public', INDEXNOW_KEY_LOCATION);
    
    try {
        fs.writeFileSync(keyFilePath, INDEXNOW_API_KEY);
        console.log(`Key file generated at: ${keyFilePath}`);
    } catch (error) {
        console.error('Error generating key file:', error);
    }
}

/**
 * Main function
 */
async function main() {
    console.log('Starting IndexNow URL submission...');
    
    // Generate the key verification file
    generateKeyFile();
    
    // Get URLs from sitemap
    const sitemapUrls = await getSitemapUrls();
    console.log(`Found ${sitemapUrls.length} URLs in sitemap.`);
    
    // Load previously submitted URLs
    const cache = loadSubmittedUrls();
    cache.lastSubmission = new Date().toISOString();
    
    // Find URLs to submit (new or updated)
    const urlsToSubmit = [];
    
    for (const url of sitemapUrls) {
        // Add URL if it wasn't submitted before, or force submission 
        // if INDEXNOW_FORCE_SUBMIT is set to true
        if (!cache.urls[url] || process.env.INDEXNOW_FORCE_SUBMIT === 'true') {
            urlsToSubmit.push(url);
            cache.urls[url] = { lastSubmitted: cache.lastSubmission };
        }
    }
    
    console.log(`Found ${urlsToSubmit.length} new or updated URLs to submit.`);
    
    // Submit URLs to IndexNow
    await submitToIndexNow(urlsToSubmit);
    
    // Save updated cache
    saveSubmittedUrls(cache);
    
    console.log('IndexNow URL submission completed.');
}

// Run the main function
main().catch(error => {
    console.error('IndexNow script failed:', error);
    process.exit(1);
});