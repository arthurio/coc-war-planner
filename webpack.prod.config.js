var config = require('./webpack.config.js'),
    path = require('path'),
    webpack = require('webpack'),
    BundleTracker = require('webpack-bundle-tracker');

config.output.path = path.resolve('./coc_war_planner/static/js/dist/');
config.output.publicPath = '/static/js/dist/';

config.plugins = [
    new BundleTracker({filename: './webpack-stats-prod.json'}),

    // removes a lot of debugging code in React
    new webpack.DefinePlugin({
        'process.env': {
            'NODE_ENV': JSON.stringify('production')
        }
    }),

    // keeps hashes consistent between compilations
    new webpack.optimize.OccurenceOrderPlugin(),

    // minifies your code
    new webpack.optimize.UglifyJsPlugin({
        compressor: {
            warnings: false
        }
    })
];

module.exports = config;
