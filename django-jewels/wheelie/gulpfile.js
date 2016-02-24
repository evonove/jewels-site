require('gulp');

// importing Wheelie instance and the base Wheelie recipe
var wheelie = require('wheelie');
var recipe = require('wheelie-recipe');

// adding the base recipe to Wheelie
wheelie.add(recipe);
wheelie.setDefault('watch');

// build customizations
var vendors = [
    'jquery/dist/jquery.min.js',
    'svg-injector/dist/svg-injector.min.js'
];

var scripts = [
    'compatibility/modernizr-custom.js',
    'layers-animation.js',
    'gems-animation.js',
    'svg-injections.js'
];

wheelie.update('uglify', {
    scripts: scripts,
    vendors: vendors
});

// the production and the live building, output processed files
// in the `wheelie/static/` folder
wheelie.setBuild('static/');
wheelie.setDist('static/');
wheelie.build();
