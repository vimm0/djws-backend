const webpack = require('webpack')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const AssetsPlugin = require('assets-webpack-plugin')

const outputPath = __dirname + '/djwebshiksha/static/dist/'

// the path(s) that should be cleaned
let pathsToClean = [outputPath]

let extractTextPlugin = new ExtractTextPlugin({filename: 'css/[name]-[hash].css', allChunks: true})

let assetsPluginInstance = new AssetsPlugin({
   filename: 'assets.json',
   path: __dirname
 })

module.exports = {
  entry: {
    app: './djwebshiksha/src/index.js'
  },
  output: {
    path: outputPath,
    publicPath: 'dist/',
    filename: 'js/[name].bundle-[hash].js'
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js$/, // files ending with .js
        exclude: /node_modules/, // exclude the node_modules directory
        loader: 'babel-loader' // use this (babel-core) loader
      },
      {
        test: /\.s?css$/,
        use: extractTextPlugin.extract({
          use: [{
            loader: 'css-loader', options: {
              sourceMap: true,
              minimize: true
            }
          }, {
            loader: 'sass-loader', options: {
              sourceMap: false,
              minimize: true
            }
          }],
          fallback: 'style-loader'
        })
      },
      {test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'url-loader?limit=10000&mimetype=application/font-woff'},
      {test: /\.(png|gif|ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader', query: { outputPath: 'images/', publicPath: '../',} }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(pathsToClean),
    extractTextPlugin,
    assetsPluginInstance
  ]
}