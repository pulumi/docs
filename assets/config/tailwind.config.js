
// Tailwind configuration. Changes to this file require a dev-server restart.
//
// Configuration docs:
// https://tailwindcss.com/docs/configuration
//
// Default configuration:
// https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js

const defaultTheme = require('tailwindcss/defaultTheme');

const brand = {
    purple: "#512668",
    orange: "#ee975c",
    green: "#2fc89f",
    blue: "#3ec2f8",
    gray: "#f1f1f1",
}

const purple = {
    100: "#ddcae8",
    300: "#83549c",
    500: brand.purple,
    700: "#371a47",
    900: "#180b1f",
}

const blue = {
    100: "#C4EEFF",
    300: "#94E1FF",
    500: brand.blue,
    700: "#238FBA",
    900: "#0F2E3B",
}

module.exports = {
    theme: {

        extend: {

            fontFamily: {
                display: [
                    "Ubuntu",
                    ...defaultTheme.fontFamily.sans,
                ],
                body: [
                    "Open Sans",
                    ...defaultTheme.fontFamily.sans,
                ],
            },

            colors: {
                purple: {
                    100: purple["100"],
                    300: purple["300"],
                    500: purple["500"],
                    default: purple["500"],
                    700: purple["700"],
                    900: purple["900"],
                },
                blue: {
                    100: blue["100"],
                    300: blue["300"],
                    500: blue["500"],
                    default: blue["500"],
                    700: blue["700"],
                    900: blue["900"],
                },
                green: {
                    default: brand.green,
                    ...defaultTheme.colors.green,
                },
                orange: {
                    default: brand.orange,
                    ...defaultTheme.colors.orange,
                },
                gray: {
                    default: brand.gray,
                    ...defaultTheme.colors.gray,
                },
            },
        },
    },
}
