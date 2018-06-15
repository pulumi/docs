(function($) {
	var innerType = $('.type-inner');
	var innerTypeStep = $('.type-step');
	var textBlock = $('.type-block');
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
				randInt += parseInt(randomIntFromInterval(40,70));
				var typing = setTimeout(function(y){
					currElTyped.append(text.charAt(y));
				},randInt, i);
			};

			setTimeout(function(){
				textBlockCurr++;
				if(textBlockCurr <= textBlockLength) {
					console.log('run if true');
					currElTyped.removeClass('cursor');
					textAnim();
				}
			},randInt+800);

		},400);
	}

	function initType() {
		textBlockCurr = 1;
		textBlockLength = textBlock.length;
		// console.log(textBlockLength);
		typeWrite('type-block-' + textBlockCurr);
	}

	function textAnim() {
		console.log('run textAnim()');
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