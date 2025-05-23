/**
 * Adds target="_blank" to all external links to make them open in a new tab.
 * Internal links (links to the same domain) remain unchanged.
 */

(function() {
    // Function to process all links on the page
    function processExternalLinks() {
        // Get the current domain (without protocol, www, or trailing slash)
        const currentDomain = window.location.hostname.replace(/^www\./, '');
        
        // Select all links in the document
        const links = document.querySelectorAll('a[href]');
        
        // Process each link
        links.forEach(link => {
            const href = link.getAttribute('href');
            
            // Skip links without href, anchor links, or javascript: links
            if (!href || href.startsWith('#') || href.startsWith('javascript:')) {
                return;
            }
            
            try {
                // Try to parse the URL (this will throw for relative URLs)
                const url = new URL(href, window.location.origin);
                const linkDomain = url.hostname.replace(/^www\./, '');
                
                // If the domain is different from the current domain, it's external
                if (linkDomain !== currentDomain) {
                    // Add target="_blank" and rel="noopener" (for security)
                    link.setAttribute('target', '_blank');
                    
                    // Add rel="noopener noreferrer" for security
                    const relAttr = link.getAttribute('rel') || '';
                    if (!relAttr.includes('noopener')) {
                        const newRel = relAttr ? `${relAttr} noopener` : 'noopener';
                        link.setAttribute('rel', newRel);
                    }
                }
            } catch (e) {
                // If URL parsing fails, it's likely a relative URL (internal link)
                return;
            }
        });
    }

    // Execute when DOM is fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', processExternalLinks);
    } else {
        processExternalLinks();
    }

    // Also process links after any potential dynamic content updates
    window.addEventListener('load', processExternalLinks);
})();