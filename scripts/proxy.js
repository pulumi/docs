
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use((req, res, next) => {
  console.log(req.url);

  next();
})


app.use(
  createProxyMiddleware({
      pathFilter: '/cloud-ai',
    target: 'http://localhost:3002',
  logger: console,
  }),
);

app.use(createProxyMiddleware({
  target: 'http://localhost:1313',
logger: console,
}),)


app.use((req, res, next) => {
  console.log(req.url);

  next();
})



app.listen('8009');
console.log('Listening!');
