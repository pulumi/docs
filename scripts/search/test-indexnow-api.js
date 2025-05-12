/**
 * Test script for verifying IndexNow API functionality
 * 
 * This script makes a real API call with a single test URL to validate
 * that the IndexNow API works correctly with our implementation.
 */

const https = require('https');

// IndexNow API settings
const INDEXNOW_ENDPOINT = 'https://www.bing.com/indexnow';
const INDEXNOW_API_KEY = process.env.INDEXNOW_API_KEY || '33134703c43349ddb227d769745f33cc';
const TEST_URL = 'https://www.pulumi.com/';

// Function to test IndexNow API
async function testIndexNowApi() {
    console.log('Testing IndexNow API with a single URL submission...');
    console.log(`API Key: ${INDEXNOW_API_KEY}`);
    console.log(`Test URL: ${TEST_URL}`);
    
    // Prepare data for IndexNow API
    const data = JSON.stringify({
        host: new URL(TEST_URL).hostname,
        key: INDEXNOW_API_KEY,
        keyLocation: `${TEST_URL}indexnow.txt`,
        urlList: [TEST_URL]
    });
    
    // Log the request
    console.log('\nRequest data:');
    console.log(data);
    
    try {
        const response = await new Promise((resolve, reject) => {
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
                    resolve({
                        statusCode: res.statusCode,
                        headers: res.headers,
                        body: responseData
                    });
                });
            });
            
            req.on('error', (error) => {
                reject(error);
            });
            
            req.write(data);
            req.end();
        });
        
        // Log the response
        console.log('\nResponse:');
        console.log(`Status code: ${response.statusCode}`);
        console.log('Headers:', JSON.stringify(response.headers, null, 2));
        console.log('Body:', response.body);
        
        // Check if successful
        if (response.statusCode >= 200 && response.statusCode < 300) {
            console.log('\n✅ SUCCESS: IndexNow API test completed successfully!');
        } else {
            console.log('\n❌ ERROR: IndexNow API test failed with status code', response.statusCode);
        }
    } catch (error) {
        console.error('\n❌ ERROR: Failed to test IndexNow API:', error);
    }
}

// Run the test
testIndexNowApi();