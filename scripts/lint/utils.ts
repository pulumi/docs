/**
 * Debug logging helper
 */
export function debug(...args: any[]) {
    if (process.env.DEBUG === '1') {
        console.log('[DEBUG]', ...args);
    }
}
