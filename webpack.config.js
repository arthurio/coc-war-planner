var path = require("path"),
    BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    // configuration
    context: __dirname,
    entry: './coc_war_planner/static/js/client/index.jsx',
    output: {
        path: './coc_war_planner/static/js/bundles',
        filename: '[name]-[hash].js'
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel?optional[]=runtime'
            }
        ]
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ]
};
