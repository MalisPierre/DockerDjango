const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: [
      'localhost',
      'https://frontend-0aaz.onrender.com/',
      '192.168.1.1',
    ],
    disableHostCheck: true
    }
})