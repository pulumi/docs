document.addEventListener("DOMContentLoaded", function () {
    let isNeoMode = false;

    (window as any).toggleNeoMode = toggleNeoMode;
    (window as any).submitNeoQuery = submitNeoQuery;
    (window as any).populateNeoInput = populateNeoInput;

    function toggleNeoMode() {
        isNeoMode = !isNeoMode;

        if (isNeoMode) {
            document.body.classList.add('neo-active');
            setTimeout(() => {
                const input = document.getElementById('neo-input') as HTMLInputElement;
                if (input) {
                    input.focus();
                    setTimeout(() => {
                        if (document.activeElement !== input) {
                            input.focus();
                        }
                    }, 100);
                }
            }, 600);
        } else {
            document.body.classList.remove('neo-active');
            const input = document.getElementById('neo-input') as HTMLInputElement;
            if (input) {
                input.value = '';
            }
        }

        const analytics = (window as any).analytics;
        const analyticsAvailable = analytics && analytics.track && typeof analytics.track === "function";

        if (analyticsAvailable) {
            const trackData = {
                neoModeActive: isNeoMode ? "true" : "false",
            };
            analytics.track("neo-mode-toggle", trackData);
        }
    }

    function submitNeoQuery() {
        const input = document.getElementById('neo-input') as HTMLInputElement;
        const query = input?.value.trim();

        if (query) {
            const encodedQuery = encodeURIComponent(query);
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

    const neoInput = document.getElementById('neo-input') as HTMLInputElement;
    if (neoInput) {
        neoInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                submitNeoQuery();
            }
        });
    }
});
