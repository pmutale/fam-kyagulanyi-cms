const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractText = require('extract-text-webpack-plugin');
const config = require('./webpack.base.config.js');

config.mode = 'development';
// Use webpack dev server
config.entry = [
  'webpack-dev-server/client?http://mwebaza.localhost:9000',
  'webpack/hot/only-dev-server',
];

// override django's STATIC_URL for webpack bundles
config.output.publicPath = 'http://mwebaza.localhost:9000/static/bundles/';

// Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  // new webpack.NoErrorsPlugin(),
  new BundleTracker({filename: './webpack-stats.json'}),
])

// Add a loader for JSX files with react-hot enabled
config.module.rules.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot', 'babel'] },
  { test: /\.css$/, exclude: /node_modules/, loaders: ['style-loader', 'css-loader'] },
  { test: /\.scss$/, use: ExtractText.extract({
          fallback: 'style-loader',
          use: ['css-loader', 'sass-loader']
        })}
)

module.exports = config
