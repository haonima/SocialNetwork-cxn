﻿jQuery.cookie=function(name,value,options){if("undefined"==typeof value){var cookieValue=null;if(document.cookie&&""!=document.cookie)for(var cookies=document.cookie.split(";"),i=0;i<cookies.length;i++){var cookie=jQuery.trim(cookies[i]);if(cookie.substring(0,name.length+1)==name+"="){cookieValue=decodeURIComponent(cookie.substring(name.length+1));break}}return cookieValue}options=options||{},null===value&&(value="",options.expires=-1);var expires="";if(options.expires&&("number"==typeof options.expires||options.expires.toUTCString)){var date;"number"==typeof options.expires?(date=new Date,date.setTime(date.getTime()+24*options.expires*60*60*1e3)):date=options.expires,expires="; expires="+date.toUTCString()}var path=options.path?"; path="+options.path:"",domain=options.domain?"; domain="+options.domain:"",secure=options.secure?"; secure":"";document.cookie=[name,"=",encodeURIComponent(value),expires,path,domain,secure].join("")};