
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

const white = defaultTheme.colors.white;
const black = defaultTheme.colors.black;
const gray = defaultTheme.colors.gray;
const red = defaultTheme.colors.red;
const yellow = defaultTheme.colors.yellow;
const transparent = defaultTheme.colors.transparent;

const purple = {
    100: "#d7cddc",
    200: "#a48bb3",
    300: "#745687",
    400: "#654276",
    500: brand.purple,
    600: "#421d57",
    700: "#371a47",
    800: "#2a1337",
    900: "#180b1f",
}

const blue = {
    100: "#f5fbff",
    200: "#cae6f7",
    300: "#9dd1f0",
    400: "#73b7e7",
    500: brand.blue,
    600: "#4387c7",
    700: "#3671b0",
    800: "#365881",
    900: "#334866",
}

const orange = {
    100: "#fff7eb",
    200: "#fde6c4",
    300: "#fad49e",
    400: "#f6ba7e",
    500: brand.orange,
    600: "#e17d47",
    700: "#d86131",
    800: "#ba4a2c",
    900: "#993d29",
}

const green = {
    100: "#e0fff2",
    200: "#b2fbe0",
    300: "#81eeca",
    400: "#4ce1b4",
    500: brand.green,
    600: "#25a78b",
    700: "#1d8673",
    800: "#19675b",
    900: "#155148",
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
        },
        colors: {
            white,
            black,
            gray,
            red,
            yellow,
            purple,
            blue,
            orange,
            green,
            transparent,
        },
        maxHeight: {
            '25': '25vh',
            '50': '50vh',
            '75': '75vh',
            '100': '100vh',
        }
    },

    variants: {
        margin: [
            "responsive",
            "hover",
        ],
        padding: [
            "responsive",
            "group-hover",
            "hover",
        ],
    }
}
