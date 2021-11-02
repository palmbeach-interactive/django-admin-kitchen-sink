const merge = require('webpack-merge');
const path = require('path');
const common = require('./common');

const CopyWebpackPlugin = require('copy-webpack-plugin');

const BUILD = path.resolve(__dirname, '../', 'build');
const RELEASE = path.resolve(__dirname, '../', 'app/django_slick_admin/static/django_slick_admin');


module.exports = merge(common, {
  mode: 'production',
  output: {
    path: BUILD,
    filename: '[name].js',
  },
  plugins: [
    new CopyWebpackPlugin([
      {
        from: BUILD,
        to: RELEASE,
      }
    ])
  ],
});
