﻿define("list",function(require,exports){function changeImg(btn){var idx=btn.index();$(".js-fi-tab .js-fi").removeClass("fi-now").fadeTo(200,.5),btn.fadeTo(200,1),$(".js-fi-ct").find(".js-fi").removeClass("show").hide(),$(".js-fi-ct").find(".js-fi").eq(idx).fadeIn("slow")}function changeImgBg(){$(".js-fi-ct").find(".js-fi").find("a img").addClass("imgAnimation")}require("moder_fav_collect"),require("moder_share_box"),require("moder_sub_tag"),$(".js-fi-tab").length>0&&$(".js-fi-tab .js-fi").mouseover(function(){changeImg($(this)),changeImgBg($(this))}),$(".js-yarcrontab").length>0&&$.get("http://www.huxiu.com/yarcrontab.html",function(data){})});