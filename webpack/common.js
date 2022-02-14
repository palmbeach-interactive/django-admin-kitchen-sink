require('babel-polyfill');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const path = require('path');

const DEV_MODE = process.env.NODE_ENV !== 'production';

// pints to source to be built by webpack
const SRC = path.resolve(__dirname, '../', 'src');

// points to STATICFILES_DIRS configured in django
const BUILD = path.resolve(__dirname, '../', 'build');

module.exports = {
  entry: {
    bundle: ['babel-polyfill', './src/bundle.js'],
    'cms-styles': ['babel-polyfill', './src/cms-styles-bundle.js'],
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
            ],
          },
        },
      },
      {
        test: /\.scss$/,
        use: [
          DEV_MODE ? 'style-loader' : MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
          },
          {
            loader: 'sass-loader',
          },
          {
            loader: `postcss-loader`,
            options: {
              options: {},
            },
          },
        ],
      },
      {
        test: /\.css$/,
        use: [
          'css-loader',
        ],
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[contenthash]',
          outputPath: 'asset/img',
          publicPath: '../asset/img',
        },
      },
    ],
  },
  plugins: [
    // new webpack.HotModuleReplacementPlugin(),
    new MiniCssExtractPlugin({
      // this is relative to output.path
      filename: './css/[name].css',
      chunkFilename: './css/[name].css',
    }),
    new CopyWebpackPlugin([
      {
        from: path.resolve(SRC, 'asset'),
        to: path.resolve(BUILD, 'asset'),
      },
    ], {debug: 'warning'}),
  ],
};
