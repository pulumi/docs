/**
 * AI Bot Detection and Tracking for llms.txt experiment
 * Tracks AI/LLM bot access to pulumi.com to measure llms.txt effectiveness
 */

(function() {
    'use strict';

    /**
     * Detects if the current user agent is an AI/LLM bot
     * Based on actual bot traffic data from pulumi.com analytics
     * @returns {boolean} true if AI bot detected
     */
    function detectAIBot() {
        const ua = navigator.userAgent.toLowerCase();

        // Known AI bot patterns from actual traffic data
        const aiPatterns = [
            /claudebot\/\d+\.\d+/i,           // ClaudeBot/1.0
            /amazonbot\/\d+\.\d+/i,           // Amazonbot/0.1
            /chatgpt-user\/\d+\.\d+/i,        // ChatGPT-User/1.0
            /oai-searchbot\/\d+\.\d+/i,       // OAI-SearchBot/1.0, 1.3
            /perplexitybot\/\d+\.\d+/i,       // PerplexityBot/1.0
            /gptbot/i,                         // GPTBot (general)
            /anthropic/i,                      // Anthropic bots
            /bingbot/i,                        // Bing (may use AI)
            /baiduspider/i,                    // Baidu (has AI features)
            /\bbot\b.*\/(ai|llm|gpt|claude)/i // Future-proofing pattern
        ];

        return aiPatterns.some(pattern => pattern.test(ua));
    }

    /**
     * Sends tracking event to analytics
     * @param {string} eventName - Name of the event
     * @param {object} eventData - Additional event data
     */
    function trackEvent(eventName, eventData) {
        // Use Segment analytics if available
        if (typeof window.analytics !== 'undefined' && window.analytics.track) {
            window.analytics.track(eventName, eventData);
        }

        // Also send to Google Analytics if available
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, {
                'event_category': 'llms_txt',
                ...eventData
            });
        }

        // Log to console in development
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            console.log('[AI Bot Tracking]', eventName, eventData);
        }
    }

    /**
     * Initialize AI bot tracking
     */
    function initAIBotTracking() {
        // Check if current visitor is an AI bot
        const isAIBot = detectAIBot();

        if (isAIBot) {
            // Track AI bot page access
            trackEvent('ai_bot_access', {
                user_agent: navigator.userAgent,
                page_path: window.location.pathname,
                page_url: window.location.href,
                referrer: document.referrer,
                timestamp: new Date().toISOString()
            });

            // Add data attribute to body for debugging
            document.body.setAttribute('data-ai-bot', 'true');
        }

        // Track llms.txt file access specifically
        if (window.location.pathname === '/llms.txt') {
            trackEvent('llms_txt_fetch', {
                user_agent: navigator.userAgent,
                is_ai_bot: isAIBot,
                referrer: document.referrer,
                timestamp: new Date().toISOString()
            });
        }

        // Track .md version requests (future enhancement)
        if (window.location.pathname.endsWith('.md')) {
            trackEvent('markdown_version_request', {
                user_agent: navigator.userAgent,
                is_ai_bot: isAIBot,
                page_path: window.location.pathname,
                referrer: document.referrer,
                timestamp: new Date().toISOString()
            });
        }
    }

    // Wait for DOM and analytics to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAIBotTracking);
    } else {
        // DOM already loaded, initialize immediately
        // Give analytics libraries a moment to load
        setTimeout(initAIBotTracking, 100);
    }

    // Export functions for testing/debugging
    window.pulumiAITracking = {
        detectAIBot: detectAIBot,
        trackEvent: trackEvent,
        initAIBotTracking: initAIBotTracking
    };
})();