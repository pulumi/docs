
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
    blue: "#52a6da",
}

const purple = {
    100: "#ddcae8",
    200: "#9c76b3",
    300: "#83549c",
    400: "#6c348a",
    500: brand.purple,
    600: "#421d57",
    700: "#371a47",
    800: "#2a1337",
    900: "#180b1f",
}

// TBD: Orange and green scales. (Using defaults for now.)

const blue = {
    100: "#c4eeff",
    200: "#abe7ff",
    300: "#94e1ff",
    400: "#63d0ff",
    500: brand.blue,
    600: "#3182ce",
    700: "#1873bd",
    800: "#0a4970",
    900: "#0f2e3b",
}

const orange = defaultTheme.colors.orange;
const green = defaultTheme.colors.green;
const gray = defaultTheme.colors.gray;

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
                purple,
                blue,
                orange,
                green,
                gray,
            },
        },
    },

    variants: {
        margin: [
            "responsive",
            "hover",
        ]
    }
}
