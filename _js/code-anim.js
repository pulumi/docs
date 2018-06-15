(function($) {
	var innerType = $('.type-inner');
	var innerTypeStep = $('.type-step');
	var textBlock = $('.type-block');
	var animContainer = $('.anim_container');
	var animTextBox = $('.anim_textbox');
	var animHeadBar = $('.anim_headbar');
	var contHeight;
	var text;
	var currEl;
	var currElTyped;
	var textBlockLength;
	var textBlockCurr;

	function randomIntFromInterval(min,max) {
		return Math.floor(Math.random()*(max-min+1)+min);
	}

	function typeWrite(el) {
		var randInt = 0;
		currEl = $('#'+el);
		currElTyped = currEl.find('.type-text');
		currElTyped.addClass('cursor');
		text = currElTyped.text();
		
		currEl.css({
			"opacity": 1
		});
		currEl.find(innerType).remove();
		
		setTimeout(function(){ // leave gap between instruction and typed out answer

			for (var i = 0; i < text.length; i++) {
				randInt += parseInt(randomIntFromInterval(40,50));
				var typing = setTimeout(function(y){
					currElTyped.append(text.charAt(y));
				},randInt, i);
			};

			setTimeout(function(){ // how long until it starts the next line
				textBlockCurr++;
				if(textBlockCurr <= textBlockLength) {
					currElTyped.removeClass('cursor');
					textAnim();
				}
			},randInt+400);

		},600);
	}

	function initType() {
		textBlockCurr = 1;
		var idCurr = textBlockCurr;
		textBlockLength = textBlock.length;
		contHeight = animTextBox.outerHeight();

		textBlock.each(function(){
			// dynamically add ids to blocks
			$(this).attr("id", "type-block-" + idCurr);
			idCurr++;
		});

		$('.anim_textbox').css({
			"min-height": contHeight + 'px'
		});
		typeWrite('type-block-' + textBlockCurr);
	}

	function textAnim() {
		typeWrite('type-block-' + textBlockCurr);
	}

	$(document).ready(function(){
		initType();
	});

	$(window).on('load', function(){

	});

	$(window).resize(function() {
		
	});


	$(window).scroll(function () {
		
	});

} (jQuery));