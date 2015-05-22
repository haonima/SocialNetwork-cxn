define('init',function(require, exports){

    window.console = window.console || (function(){
        var c = {}; c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile
            = c.clear = c.exception = c.trace = c.assert = function(){};
        return c;
    })();


    
  
    //require.async(['jquery.lazyload.min','lazyload'], function(){});
    //require('seajs_combo');
    require('jquery');
    require('sea_combo_flush');

    require.async(['bootstrap','public','jquery.lazyload.min','lazyload'], function(){
//        seajs.flush();
    });


   
    if($('.jobAds-1').length > 0) {
        require.async('jobAds/jobs.css');
        require.async('jobAds/setup', function(jobDisplayer) {
            jobDisplayer.add_jobAds1();
        })
    }

  
    if($('.jobAds-2').length > 0) {
        require.async('jobAds/jobs.css');
        require.async('jobAds/setup', function(jobDisplayer) {
            jobDisplayer.add_jobAds2();
        })
    }

    if($('.jobAds-3').length > 0) {
        require.async('jobAds/jobs.css');
        require.async('jobAds/setup', function(jobDisplayer) {
            jobDisplayer.add_jobAds3();
        })
    }

    if($('.jobAds-4').length > 0) {
        require.async('jobAds/jobs.css');
        require.async('jobAds/setup', function(jobDisplayer) {
            jobDisplayer.add_jobAds4();
        })
    }
    
    if($('.ad-fixed-right').length > 0){
        var offsetTop = $('.ad-fixed-right').offset().top;
        $(window).on("scroll", function() {

            if(!$('.js-xiu-cmt-list').hasClass('hidden') && !$('.js-xiu-cmt-list').hasClass('js-ad-flag')){
                offsetTop += $('.js-xiu-cmt-list').height();
                $('.js-xiu-cmt-list').addClass('js-ad-flag');
            }
            if(!$('.js-hot-author-list').hasClass('hidden') && !$('.js-hot-author-list').hasClass('js-ad-flag')){
                offsetTop += $('.js-hot-author-list').height();
                $('.js-hot-author-list').addClass('js-ad-flag');
            }

            if ($(window).scrollTop() > offsetTop) {
                $('.ad-fixed-right').css({'position': 'fixed', 'top': '10px', 'z-index': '80'});
            } else {
                $('.ad-fixed-right').css({'position': 'relative', 'top': 'auto'});
            }
        });
    }



   
    if($('#page_tg').length > 0) {
        require.async('page_tg', function(page_tg) {})
    }


    if($('#page_article').length > 0) {
        require.async('page_article', function(page_article) {})

        if($('.page-article-about').length > 0){
            require.async('page_article_about', function(page_article_about) {})
        }
    }

    
    if($('.js-moder-reg').length > 0) {
        require.async('moder_moder_reg', function(moder_moder_reg) {})
    }

  
    if($('#page_idx').length > 0) {
        require.async('idx', function(idx) {})
    }

   
    if($('#page_list').length > 0) {
        require.async('list', function(list) {})

        
        if($('.list-read').length > 0) {
            require.async('list_read', function(list_read) {
                list_read.on();
            })
        }
    }


    
    if($('#page_ctt').length > 0) {
        require.async('ctt', function(ctt) {
            ctt.on();
        })


        
        if($('.ctt-read').length > 0) {
            require.async('ctt_read', function(ctt_read) {
                ctt_read.on();
            })
        }

    }

   
    if($('#page_per_center').length > 0) {
        require.async('per_center', function(per_center) {})

     
        if($('.per-center-fragment').length > 0) {
            require.async('per_center_fragment', function(per_center_fragment) {})
        }
    }

   
    if($('#page_use').length > 0) {
        require.async('page_use', function(page_use) {})


    }


 
    if($('#page_wenji').length > 0) {
        require.async('page_wenji', function(page_wenji) {})


    }


    if($('#page_tag').length > 0) {
        require.async('page_tag', function(page_tag) {})
    }

    if($('#page_author').length > 0) {
        require.async('page_author', function(page_tag) {})
    }


  
    if($('#page_active').length > 0) {
        require.async('page_active', function(page_active) {})
    }

    if($('#page_group').length > 0) {
        require.async('page_group', function(page_active) {})
    }

 
    if($('#page_blank').length > 0) {
        require.async('page_blank', function(page_blank) {})

    }
   
    if($('#page_404').length > 0) {
        require.async('page_404', function(page_404) {})

    }

 
    if($('#page_rss').length > 0) {
        require.async('page_rss', function(page_rss) {})
    }




    require('s_css');

    require.async(['cookie','messenger','messenger_css','messenger_css2'],function(){
        Messenger.options = {
            extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-right',
            theme: 'flat'
        };
    })


});