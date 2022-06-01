$(function() {
	$("#slider_image img").each(function(index) {
		$("#slider_dots").append(`<div class="dot"></div>`);
		$("#slider_dots .dot").eq(1).addClass("active");
	});

	$("#slider_dots .dot").click(function() {
		let i = ($(this).index());

		$("#slider_image img").css({"opacity":"0"});
		$("#slider_image img").eq(i).css({"opacity":"1"});
		$("#slider_dots .dot").removeClass('active');
		$("#slider_dots .dot").eq(i).addClass('active');
	});
});