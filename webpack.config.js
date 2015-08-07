var path = require("path"),
    webpack = require('webpack'),
    BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: [
        'webpack-dev-server/client?http://localhost:8080',
        'webpack/hot/only-dev-server',
        './coc_war_planner/static/js/client/index.jsx'
    ],

    output: {
        path: path.resolve('./coc_war_planner/static/js/bundles/'),
        filename: "[name]-[hash].js",
        publicPath: 'http://localhost:8080/static/js/bundles/' // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    module: {
        loaders: [{
            // we pass the output from babel loader to react-hot loader
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loaders: ['react-hot', 'babel']
        }]
    },
    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    }
}
