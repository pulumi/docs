
// Tailwind configuration. Changes to this file require a dev-server restart.
// https://tailwindcss.com/docs/configuration
module.exports = {
    theme: {

        extend: {

            fontFamily: {
                display: ["Ubuntu"],
                body: ["Open Sans"],
            },

            colors: {
                purple: {
                    darkest: "#1a111f",
                    dark: "#371847",
                    default: "#512668",
                    light: "#f6e5ff",
                },
                blue: {
                    darker: "#0079AB",
                    default: "#00acf2",
                    light: "#e1f6ff",
                    bright: "#3EC2F8",
                },
                green: {
                    default: "#2fc89f",
                },
                orange: {
                    default: "#ee975c",
                    light: "#fbe5d7",
                },
                gray: {
                    dark: "#222",
                    default: "#555555",
                    light: "#cccccc",
                    lighter: "#d3d3d3",
                    lightest: "#f1f1f1",
                }
            },
        },
    },
}
