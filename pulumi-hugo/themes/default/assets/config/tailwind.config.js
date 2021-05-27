
// Tailwind configuration. Changes to this file require a dev-server restart.
//
// Configuration docs:
// https://tailwindcss.com/docs/configuration
//
// Default configuration:
// https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js

const defaultTheme = require('tailwindcss/defaultTheme');

const brand = {
    yellow: "#f7bf2a",
    salmon: "#f26e7e",
    fuchsia: "#bd4c85",
    purple: "#8a3391",
    violet: "#805ac3",
    blue: "#4d5bd9",
};

const white = defaultTheme.colors.white;
const black = defaultTheme.colors.black;
const transparent = defaultTheme.colors.transparent;

const red = {
    100: "#fff5f5",
    200: "#fed7d7",
    300: "#feb2b2",
    400: "#fc8181",
    500: "#f56565",
    600: "#e53e3e",
    700: "#c53030",
    800: "#9b2c2c",
    900: "#742a2a",
};

const gray = {
    100: "#f9f9fa",
    200: "#f2f2f4",
    300: "#e5e5e9",
    400: "#d8d9df",
    500: "#bebfc9",
    600: "#8e8f97",
    700: "#5f6065",
    800: "#2f3032",
    900: "#131314",
};

const yellow = {
    100: "#fef9ea",
    200: "#fdf2d4",
    300: "#fce5aa",
    400: "#fad97f",
    500: "#f9cc55",
    600: brand.yellow,
    700: "#c69922",
    800: "#947319",
    900: "#634c11",
};

const salmon = {
    100: "#fef1f2",
    200: "#fce2e5",
    300: "#fac5cb",
    400: "#f7a8b2",
    500: "#f58b98",
    600: brand.salmon,
    700: "#c25865",
    800: "#91424c",
    900: "#612c32",
};

const fuchsia = {
    100: "#f8edf3",
    200: "#f2dbe7",
    300: "#e5b7ce",
    400: "#d794b6",
    500: "#ca709d",
    600: brand.fuchsia,
    700: "#973d6a",
    800: "#712e50",
    900: "#4c1e35",
};

const purple = {
    100: "#f3ebf4",
    200: "#e8d6e9",
    300: "#d0add3",
    400: "#b985bd",
    500: "#a15ca7",
    600: brand.purple,
    700: "#6e2974",
    800: "#531f57",
    900: "#37143a",
}

const violet = {
    100: "#f2eff9",
    200: "#e6def3",
    300: "#ccbde7",
    400: "#b39cdb",
    500: "#997bcf",
    600: brand.violet,
    700: "#66489c",
    800: "#4d3675",
    900: "#33244e",
};

const blue = {
    100: "#edeffb",
    200: "#dbdef7",
    300: "#b8bdf0",
    400: "#949de8",
    500: "#717ce1",
    600: brand.blue,
    700: "#3e49ae",
    800: "#2e3782",
    900: "#1f2457",
}

const orange = {
    100: "#fff7eb",
    200: "#fde6c4",
    300: "#fad49e",
    400: "#f6ba7e",
    500: "#ee975c",
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
    500: "#2fc89f",
    600: "#25a78b",
    700: "#1d8673",
    800: "#19675b",
    900: "#155148",
}

module.exports = {
    purge: false,
    theme: {
        extend: {
            fontFamily: {
                display: [
                    "Gilroy",
                    ...defaultTheme.fontFamily.sans,
                ],
                body: [
                    "Inter",
                    ...defaultTheme.fontFamily.sans,
                ],
                mono: [
                    "Roboto Mono",
                    ...defaultTheme.fontFamily.mono,
                ]
            },
        },
        colors: {
            white,
            black,
            gray,
            transparent,
            yellow,
            salmon,
            fuchsia,
            purple,
            blue,
            red,
            orange,
            green,
            violet,
        },
        maxHeight: {
            "25": "25vh",
            "50": "50vh",
            "75": "75vh",
            "100": "100vh",
        },
        screens: {
            sm: "640px",
            md: "768px",
            lg: "1024px",
            xl: "1280px",
        },
    },
};
