const path = require('path');
const webpack = require('webpack');
var config = require('../config');

const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
// const AssetsPlugin = require('assets-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


function resolve(dir) {
    return path.join(__dirname, '..', dir);
}

// Custom
let outputPath = resolve("/static/");

// the path(s) that should be cleaned
let pathsToClean = [outputPath];

let extractTextPlugin = new ExtractTextPlugin({filename: 'css/[name]-[hash].css', allChunks: true});

module.exports = {
    // changed part is from http://owaislone.org/blog/webpack-plus-reactjs-and-django/
    entry: [
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        './djwebshiksha/src/index.js',
    ],
    output: {
        path: outputPath,
        publicPath: 'http://localhost:3000/assets/bundles/',
        filename: 'js/[name].bundle-[hash].js'
    },
    devtool: '#eval-source-map',
    resolve: {
        // extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue': 'vue/dist/vue.common.js',
            // 'components': resolve('src/components')
        }
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                // options: vueLoaderConfig
            },
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
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'url-loader?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.(png|gif|ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'file-loader',
                query: {outputPath: 'images/',
                    publicPath: 'http://localhost:3000/assets/bundles/',
                }
            }
        ]
    },
    // devServer: {
    //     // contentBase: "/static/",
    //     // compress: true,
    //     publicPath: 'http://localhost:8000/static/',
    //     hot:true,
    //     // open:true,
    //     inline:true,
    //     // host: '0.0.0.0',
    //     // port: 8080,
    // },
    plugins: [
        // new CleanWebpackPlugin(pathsToClean),
        extractTextPlugin,
        new HtmlWebpackPlugin({
        template: config.index.constantTemplate,
        filename: config.base.templateName,
        hash: true
        },),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NamedModulesPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),

    ]
};