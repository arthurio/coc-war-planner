config = require('./webpack.config.js');

config.output.path = require('path').resolve('./coc_war_planner/static/js/dist');

config.plugins = [
    new BundleTracker({filename: './webpack-stats-prod.json'})
]

module.exports = config;
