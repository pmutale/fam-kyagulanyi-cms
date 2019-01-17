const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: "",
  context: __dirname,

  entry: 'frontend/src/react/app',

  output: {
      path: path.resolve('./static/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
  ], // add all common plugins here

  module: {
    rules: [] // add all common loaders here
  },

  resolve: {
    // modulesDirectories: ['node_modules', 'bower_components'],
    extensions: [".js", ".jsx"]
  },
}
