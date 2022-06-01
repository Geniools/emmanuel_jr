(function($){

    $.fn.extend({ 

        addTemporaryClass: function(className, duration) {
            var elements = this;
            setTimeout(function() {
                elements.removeClass(className);
            }, duration);

            return this.each(function() {
                $(this).addClass(className);
            });
        }
    });

})(jQuery);

$(function() {

	$("#items .item").click(function() {
		$(this).addTemporaryClass("active", 800);
		$(".click", this).addTemporaryClass("active", 800);
	});
});