(function($) {
	var anchorBar = $('.anchor-container');
	var anchorBarCont = $('.content-block-anchors');
	var targetOffset;

	if($("#anchor-point").length) { // does anchor-point even exist?
		targetOffset = $("#anchor-point").offset().top;
	}

	function anchorAdj() {
		anchorBarH = anchorBar.outerHeight();
		anchorBarCont.css({
			"min-height": anchorBarH + "px"
		});

		if($("#anchor-point").length) { // does anchor-point even exist?
			targetOffset = $(".content-block-anchors").offset().top;
		}
	}

	function scrollPos() {
		if ( $(window).scrollTop() > targetOffset ) {
			$("#anchor-point").css( {
				"position": "fixed",
				"top": 0,
				"left": 0
			});
		} else {
			$("#anchor-point").css( {
				"position": "relative"
			});
		}
	};

	// smooth scroll anchor links
	$('a[href*="#"]')
	// Remove links that don't actually link to anything
	.not('[href="#"]')
	.not('[href="#0"]')
	.click(function(event) {

		// On-page links
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
			|| location.hostname == this.hostname) {

			// Figure out element to scroll to
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			 // Does a scroll target exist?
			 if (target.length) {
				// Only prevent default if animation is actually gonna happen
				event.preventDefault();
				
				var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
				
				if (windowWidth < 768) {
					$('html,body').animate({
						scrollTop: target.offset().top - $('.main-header').height() //minus the sticky mobile nav
					}, 700);
				}
				else {
					$('html,body').animate({
						scrollTop: target.offset().top
					}, 700);
				}
				
				return false;
			}
		}
	});


	$(document).ready(function(){
		anchorAdj();
	});

	$(window).on('load', function(){

	});

	$(window).resize(function() {
		anchorAdj();

	});

	$(window).scroll(function(){
		scrollPos();
	});
} (jQuery));