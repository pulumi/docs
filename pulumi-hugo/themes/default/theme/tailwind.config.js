// Tailwind configuration. Changes to this file require a dev-server restart.
//
// Configuration docs:
// https://tailwindcss.com/docs/configuration
//
// Default configuration:
// https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js

const { global } = require("./tokens.json");
const defaultTheme = require("tailwindcss/defaultTheme");

const hexToRGB = (hexString) => {
    let color = hexString.replace(/#/g, "");
    var r = parseInt(color.substr(0, 2), 16);
    var g = parseInt(color.substr(2, 2), 16);
    var b = parseInt(color.substr(4, 2), 16);
    return [ r, g, b];
};

const colorFamilyToRGB = (tailwindColorObject) => {
    return Object.keys(tailwindColorObject)
        .reduce((o, key) => {
            o[key] = hexToRGB(tailwindColorObject[key]).join(",");
            return o;
        }, {});
};

const brand = {
    yellow: global.colors.brand.yellow.value,
    salmon: global.colors.brand.salmon.value,
    fuchsia: global.colors.brand.fuchsia.value,
    purple: global.colors.brand.purple.value,
    violet: global.colors.brand.violet.value,
    blue: global.colors.brand.blue.value,
};

const white = defaultTheme.colors.white;
const black = defaultTheme.colors.black;
const transparent = defaultTheme.colors.transparent;

const red = {
    100: global.colors.red["100"].value,
    200: global.colors.red["200"].value,
    300: global.colors.red["300"].value,
    400: global.colors.red["400"].value,
    500: global.colors.red["500"].value,
    600: global.colors.red["600"].value,
    700: global.colors.red["700"].value,
    800: global.colors.red["800"].value,
    900: global.colors.red["900"].value,
};

const gray = {
    100: global.colors.gray["100"].value,
    200: global.colors.gray["200"].value,
    300: global.colors.gray["300"].value,
    400: global.colors.gray["400"].value,
    500: global.colors.gray["500"].value,
    600: global.colors.gray["600"].value,
    700: global.colors.gray["700"].value,
    800: global.colors.gray["800"].value,
    850: global.colors.gray["850"].value,
    900: global.colors.gray["900"].value,
};

const yellow = {
    100: global.colors.yellow["100"].value,
    200: global.colors.yellow["200"].value,
    300: global.colors.yellow["300"].value,
    400: global.colors.yellow["400"].value,
    500: global.colors.yellow["500"].value,
    600: brand.yellow,
    700: global.colors.yellow["700"].value,
    800: global.colors.yellow["800"].value,
    900: global.colors.yellow["900"].value,
};

const salmon = {
    100: global.colors.salmon["100"].value,
    200: global.colors.salmon["200"].value,
    300: global.colors.salmon["300"].value,
    400: global.colors.salmon["400"].value,
    500: global.colors.salmon["500"].value,
    600: brand.salmon,
    700: global.colors.salmon["700"].value,
    800: global.colors.salmon["800"].value,
    900: global.colors.salmon["900"].value,
};

const fuchsia = {
    100: global.colors.fuchsia["100"].value,
    200: global.colors.fuchsia["200"].value,
    300: global.colors.fuchsia["300"].value,
    400: global.colors.fuchsia["400"].value,
    500: global.colors.fuchsia["500"].value,
    600: brand.fuchsia,
    700: global.colors.fuchsia["700"].value,
    800: global.colors.fuchsia["800"].value,
    900: global.colors.fuchsia["900"].value,
};

const purple = {
    100: global.colors.purple["100"].value,
    200: global.colors.purple["200"].value,
    300: global.colors.purple["300"].value,
    400: global.colors.purple["400"].value,
    500: global.colors.purple["500"].value,
    600: brand.purple,
    700: global.colors.purple["700"].value,
    800: global.colors.purple["800"].value,
    900: global.colors.purple["900"].value,
};

const violet = {
    100: global.colors.violet["100"].value,
    200: global.colors.violet["200"].value,
    300: global.colors.violet["300"].value,
    400: global.colors.violet["400"].value,
    500: global.colors.violet["500"].value,
    600: brand.violet,
    700: global.colors.violet["700"].value,
    800: global.colors.violet["800"].value,
    900: global.colors.violet["900"].value,
};

const blue = {
    100: global.colors.blue["100"].value,
    200: global.colors.blue["200"].value,
    300: global.colors.blue["300"].value,
    400: global.colors.blue["400"].value,
    500: global.colors.blue["500"].value,
    600: brand.blue,
    700: global.colors.blue["700"].value,
    800: global.colors.blue["800"].value,
    900: global.colors.blue["900"].value,
};

const orange = {
    100: global.colors.orange["100"].value,
    200: global.colors.orange["200"].value,
    300: global.colors.orange["300"].value,
    400: global.colors.orange["400"].value,
    500: global.colors.orange["500"].value,
    600: global.colors.orange["600"].value,
    700: global.colors.orange["700"].value,
    800: global.colors.orange["800"].value,
    900: global.colors.orange["900"].value,
};

const green = {
    100: global.colors.green["100"].value,
    200: global.colors.green["200"].value,
    300: global.colors.green["300"].value,
    400: global.colors.green["400"].value,
    500: global.colors.green["500"].value,
    600: global.colors.green["600"].value,
    700: global.colors.green["700"].value,
    800: global.colors.green["800"].value,
    900: global.colors.green["900"].value,
};

module.exports = {
    purge: false,
    theme: {
        extend: {
            fontFamily: {
                display: [global.typography.fontFamilies.display.value, ...defaultTheme.fontFamily.sans],
                body: [global.typography.fontFamilies.body.value, ...defaultTheme.fontFamily.sans],
                mono: [global.typography.fontFamilies.mono.value, ...defaultTheme.fontFamily.mono],
            },
            boxShadow: {
                "3xl": "0 35px 70px -20px rgba(0, 0, 0, 0.5)",
            },
        },
        rgbColors: {
            gray: colorFamilyToRGB(gray),
            blue: colorFamilyToRGB(blue),
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
            25: "25vh",
            50: "50vh",
            75: "75vh",
            100: "100vh",
        },
        screens: {
            sm: "640px",
            md: "768px",
            lg: "1024px",
            xl: "1280px",
            xxl: "1536px",
        },
    },
};
