seajs.config({
    base:'/static/js/',
    comboSyntax: ['??', ','],

    alias: {
        '$': 'jquery/jquery.1.11.1.min',
        'jquery': 'jquery/jquery.1.11.1.min',
        'jquery_base': 'jquery/jquery.base64',
        //'combo': 'seajs_combo',
        //'flush': 'seajs_flush',
        'fancybox_css':'fancybox/jquery.fancybox.1.3.4.css',
        'fancybox':'fancybox/jquery.fancybox.1.3.4.pack',
        'bootstrap': 'bootstrap.min',
        'sea_combo_flush': 'sea_combo_flush.js',
        's_css':'seajs_css',
        'messenger_css': 'messager/css/messenger.css',
        'messenger_css2': 'messager/css/messenger-theme-flat.css',
        'messenger': 'messager/js/messenger.min',
        'cookie':'jquery_cookie',
        'jq_tmpl':'jquery.tmpl.min',
        'baidujs':'http://cbjs.baidu.com/js/m.js',
        'png_min':'png_min'
    },
    charset: 'utf-8'
});
seajs.use(['$','init']);