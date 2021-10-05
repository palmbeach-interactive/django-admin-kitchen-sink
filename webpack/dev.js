const webpack = require('webpack');
const merge = require('webpack-merge');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const path = require('path');
// eslint-disable-next-line import/no-extraneous-dependencies
const StyleLintPlugin = require('stylelint-webpack-plugin');
const common = require('./common');

// must be the same as WEBPACK_DEVSERVER_HEADER
const DEVSERVER_HEADER = 'X-WEBPACK-DEVSERVER';

// points to STATICFILES_DIRS configured in django
const BUILD = path.resolve(__dirname, '../', 'build');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'source-map',
  output: {
    path: BUILD,
    filename: '[name].js',
    publicPath: 'http://localhost:3000/static/',
  },
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js',
    },
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new CopyWebpackPlugin([
      {
        from: './src/asset',
        to: path.resolve(BUILD, 'asset'),
      },
    ], { debug: 'debug' }),
    new StyleLintPlugin({
      fix: true,
      files: [
        './src/**/*.vue',
        './src/**/*.scss',
      ],
    }),
  ],
  devServer: {
    hot: true,
    inline: true,
    host: '0.0.0.0',
    port: 3000,
    compress: true,
    disableHostCheck: true,
    watchOptions: {
      poll: true,
    },
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    proxy: {
      '/': {
        target: 'http://127.0.0.1:8080',
        onProxyReq: (proxyReq) => {
          // add header to let django know about getting a devserver request
          proxyReq.setHeader(DEVSERVER_HEADER, 'on');
        },
      },

    },
  },
});
