// ***********************************************************
// This example support/index.js is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'

// Alternatively you can use CommonJS syntax:
// require('./commands')

// Tolerate the opaque cross-origin "Script error." the browser reports for a
// third-party script loaded from another origin (e.g. the OneTrust CMP, which
// runs only on the OneTrust-registered public domains and throws when loaded on
// an S3 origin or preview host). Cypress fails the active test on ANY uncaught
// exception, which would otherwise make our page smoke tests hostage to a
// third-party script we don't control. Ignore only that opaque cross-origin
// case — it carries no stack and the message is exactly "Script error." — so
// genuine same-origin application errors still fail the test.
Cypress.on('uncaught:exception', (err) => {
    if (err && typeof err.message === 'string' && /^Script error\.?$/.test(err.message)) {
        return false
    }
    return undefined
})
