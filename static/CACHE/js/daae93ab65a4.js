$(function(){var $explorer=$('#explorer');$('.nav-main .submenu-trigger').on('click',function(){if($(this).closest('li').find('.nav-submenu').length){if($explorer.data('dlmenu')&&$explorer.dlmenu('isOpen')){$explorer.dlmenu('closeMenu');}
if($('.nav-wrapper.submenu-active').length&&!$(this).closest('li').hasClass('submenu-active')){$('.nav-main .submenu-active, .nav-wrapper').removeClass('submenu-active');}
$(this).closest('li').toggleClass('submenu-active');$('.nav-wrapper').toggleClass('submenu-active');return false}});$(document).on('keydown click',function(e){if($('.nav-wrapper.submenu-active').length&&(e.keyCode==27||!e.keyCode)){$('.nav-main .submenu-active, .nav-wrapper').removeClass('submenu-active');}});});