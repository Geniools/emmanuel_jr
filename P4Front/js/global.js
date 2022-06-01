$(function() {

	function scroll(value) {
		if (value) {
			$("body").removeClass("fixed");
		} else {
			$("body").addClass("fixed");
		}
	}

	let MENU = false;

	$("#burger").click(function() {
		MENU = !MENU;

		if (MENU) {
			scroll(false);
			$("#popup").css({"opacity":"1", "z-index":"777"});
			setTimeout(function() {
				$("#popup .wrapper").css({"left":"0px"});
			}, 300);
		} else {
			scroll(true);
			$("#popup .wrapper").css({"left":"-300px"});
			setTimeout(function() {
				$("#popup").css({"opacity":"0", "z-index":"-1"});
			}, 300);
		}
	});
});