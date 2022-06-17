$(function() {
	$("#form_rates i").click(function() {
		$("#form_rates i").removeClass("active");
		$("#form_rates i").slice(0, Number($(this).attr("rate_id"))).addClass("active");
		$("#form .input_rates").val($(this).attr("rate_id"));
	});

	$("#form_mobile_rates i").click(function() {
		$("#form_mobile_rates i").removeClass("active");
		$("#form_mobile_rates i").slice(0, Number($(this).attr("rate_id"))).addClass("active");
		$("#form_mobile .input_rates").val($(this).attr("rate_id"));
	});
});