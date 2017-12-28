module.exports = {
    index:{
        devTool:'source-map',
        publicPath: '/static/',
        imageOutput: '/images/',
        sourceToClean: ['css', 'js'],
        cssFilename: 'css/[name]-[hash].css',
        jsFilename: 'js/[name].bundle-[hash].js',
        constantTemplate:'djwebshiksha/templates/variable.html',

    },
    base: {
        templateName: '../djwebshiksha/templates/base.html',
    },
    loader: {
        css: 'css-loader',
        sass: 'sass-loader',
        style: 'style-loader',
    }

};