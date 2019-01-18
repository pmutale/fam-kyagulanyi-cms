const webpack = require("webpack");
const WebpackDevServer = require("webpack-dev-server");
const config = require("./webpack/webpack.config");

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  inline: true,
  // host: "mwebaza.localhost", // In hosts files create a passage for this endpoint => (localhost   mwebaza.localhost)
  proxy: {
    "**": "http://mwebaza.localhost:9000",
    "secure": false,
  },
  historyApiFallback: true
}).listen(9000, "mwebaza.localhost", function (err, result) {
  if (err) {
    console.error(err)
  }

  console.log("Listening at 0.0.0.0:9000")
});
