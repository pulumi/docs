const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");

const app = express();

app.use((req, res, next) => {
    console.log(req.url);
    next();
});

app.use(
    "/cloud-ai",
    createProxyMiddleware({
        target: "http://localhost:3002/cloud-ai",
        logger: console,
        changeOrigin: true,
    })
);

app.use(
    createProxyMiddleware({
        target: "http://127.0.0.1:1313",
        logger: console,
        changeOrigin: true,
    })
);

app.use((req, res, next) => {
    console.log(req.url);
    next();
});

// Use a number for port, not a string
app.listen(1312, () => {
    console.log("Listening! http://127.0.0.1:1312");
});