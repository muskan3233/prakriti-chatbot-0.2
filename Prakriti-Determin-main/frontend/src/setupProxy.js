const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    '.\api.js',  // Specify the API endpoint you want to proxy
    createProxyMiddleware({
      target: 'http://127.0.0.1:8000',  // Specify the backend server URL
      changeOrigin: true,
    })
  );
};
