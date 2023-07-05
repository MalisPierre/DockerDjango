const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: [
      'localhost',
      'https://frontend-0aaz.onrender.com/',
      '3.134.238.10',
      '3.129.111.220',
      '52.15.118.168',
      '192.168.1.1',
    ],
    }
})