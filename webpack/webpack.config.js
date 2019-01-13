// const path = require('path');
// const webpack = require('webpack');
// const BundleTracker = require('webpack-bundle-tracker');
// const ExtractText = require('extract-text-webpack-plugin');
//
// module.exports = {
//   context: __dirname,
//   entry:  [
//     'webpack-dev-server/client?http://localhost:3000',
//     'webpack/hot/only-dev-server',
//     'frontend/src/react/app',
//   ],
//   output: {
//     path: path.resolve('assets/dist'),
//     filename: '[name]-[hash].js',
//     publicPath: 'http://mwebaza.localhost:9000/assets/bundles/'
//
//   },
//   plugins: [
//     new BundleTracker({
//       path: __dirname,
//       filename: 'webpack-stats.json',
//     }),
//     new webpack.HotModuleReplacementPlugin(),
//     new webpack.NoErrorsPlugin(), // don't reload if there is an error
//   ],
//
//   module: {
//     rules: [
//       {
//         test: /\.jsx?$/,
//         loaders: ['react-hot', 'babel'],
//         exclude: /node_modules/,
//       },
//       {
//         test: /\.css$/,
//         loader: ['style-loader', 'css-loader'],
//       },
//       {
//         test: /\.scss$/,
//         use: ExtractText.extract({
//           fallback: 'style-loader',
//           use: ['css-loader', 'sass-loader']
//         })
//       },
//     ],
//   },
//   resolve: {
//     modulesDirectories: ['node_modules', 'bower_components'],
//     extensions: ['', '.js', '.jsx']
//   }
// }
