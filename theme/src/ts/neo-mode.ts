$(function () {
    let isNeoMode = false;

    // Make functions available globally for onclick handlers
    (window as any).toggleNeoMode = toggleNeoMode;
    (window as any).submitNeoQuery = submitNeoQuery;
    (window as any).populateNeoInput = populateNeoInput;

    function toggleNeoMode() {
        isNeoMode = !isNeoMode;

        if (isNeoMode) {
            // Add neo-active class to body to trigger all styling
            document.body.classList.add('neo-active');
            // Focus the input when opening neo mode
            setTimeout(() => {
                const input = document.getElementById('neo-input') as HTMLInputElement;
                if (input) {
                    input.focus();

                    // Double-check focus worked, retry if needed
                    setTimeout(() => {
                        if (document.activeElement !== input) {
                            input.focus();
                        }
                    }, 100);
                }
            }, 600); // Wait for full animation duration (0.4s + 0.1s delay + buffer)
        } else {
            // Remove neo-active class to restore normal state
            document.body.classList.remove('neo-active');
            // Clear the input when closing neo mode
            const input = document.getElementById('neo-input') as HTMLInputElement;
            if (input) {
                input.value = '';
            }
        }
    }

    function submitNeoQuery() {
        const input = document.getElementById('neo-input') as HTMLInputElement;
        const query = input?.value.trim();

        if (query) {
            // Encode the query for URL safety
            const encodedQuery = encodeURIComponent(query);
            // Redirect to Pulumi Neo app with the query
            window.location.href = `https://app.pulumi.com/neo?prompt=${encodedQuery}&prefer_signup=true`;
        }
    }

    function populateNeoInput(prompt: string) {
        const input = document.getElementById('neo-input') as HTMLInputElement;
        if (input) {
            input.value = prompt;
            input.focus();
        }
    }

    // Allow Enter key to submit
    const neoInput = document.getElementById('neo-input') as HTMLInputElement;
    if (neoInput) {
        neoInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                submitNeoQuery();
            }
        });
    }
});
