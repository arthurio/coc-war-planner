var path = require("path"),
    webpack = require('webpack'),
    BundleTracker = require('webpack-bundle-tracker'),
    Clean = require('clean-webpack-plugin');

module.exports = {
    context: __dirname,
    entry: [
        'es7-autobinder',
        './coc_war_planner/static/js/client/index.jsx'
    ],

    output: {
        path: path.resolve('./coc_war_planner/static/js/bundles/'),
        filename: "[name]-[hash].js",
        publicPath: '/static/js/bundles/'
    },

    plugins: [
        new Clean(['coc_war_planner/static/js/dist', 'coc_war_planner/static/js/bundles']),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    module: {
        loaders: [{
            // we pass the output from babel loader to react-hot loader
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loaders: ['babel?stage=1']
        }]
    },
    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    }
}
