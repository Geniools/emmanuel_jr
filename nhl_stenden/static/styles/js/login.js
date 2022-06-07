$(function() {
  $("#form_login").on("submit", function () {
    $.ajax({
      url: '/methods/login/',
      method: 'post',
      dataType: 'html',
      data: $(this).serialize(),
      success: function (data) {
        if (data == "true") {
          window.location.href = '/schedule';
        }
      }
    });
    return false;
  });
});