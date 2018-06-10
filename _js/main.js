(function($) {

//----------------------------------------
// Essentials
//----------------------------------------
var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

// breakpoints
var $screen_xxs = 320;
var $screen_xs = 480;
var $screen_sm = 576;
var $screen_md = 768;
var $screen_lg = 991;
var $screen_xlg = 1200; 


// find out if is touch device
function is_touch_device() {
 return (('ontouchstart' in window)
	  || (navigator.MaxTouchPoints > 0)
	  || (navigator.msMaxTouchPoints > 0));
 //navigator.msMaxTouchPoints for microsoft IE backwards compatibility
}


// Add slideDown animation to Bootstrap dropdown when expanding.
$('.dropdown:not(.main-nav-wrapper-wrapper)').on('show.bs.dropdown', function() {
  $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
});

// Add slideUp animation to Bootstrap dropdown when collapsing.
$('.dropdown:not(.main-nav-wrapper-wrapper)').on('hide.bs.dropdown', function() {
  $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
});

//mobile dropdown
$('.main-header .dropdown').on('show.bs.dropdown', function() {
	var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
	if (windowWidth < $screen_md) {
		$('body').addClass('no-scroll');
	}
	
}).on('hide.bs.dropdown', function() {
	$('body').removeClass('no-scroll');
	
});

//update eqh on hubspot
$('.hbspt-form').bind('DOMSubtreeModified', function(event) {
	if ($().parents('[data-mh]')) {
	  $.fn.matchHeight._maintainScroll = true;
	  $.fn.matchHeight._update();
	}
	
  });
	
$(document).ready(function() {

});

$(window).on('load', function(){
  if ($('[data-mh] [data-mh]').length > 0) {
	$.fn.matchHeight._update();
  }
});

var originalWindowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

$(window).resize(function() {
	
	var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
	
	//prevent functions from recalculating on scroll on mobile. when scrolling on iphone, the bottom appears/disappears and the browser thinks this is resizing
	//execute these functions on width resize only
	if (windowWidth != originalWindowWidth) { //if width resized
	
	}
	
});


$(window).scroll(function () {
	
});

$('[data-slick]').slick();
} (jQuery));
