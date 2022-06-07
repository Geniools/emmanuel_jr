$(function () {
  $("#form_registration").on("submit", function () {
    if ($("#password").val() != $("#check_password").val()) {
      alert("Passwords don't match!");
      return false;
    }

    $.ajax({
      url: '/methods/registration/',
      method: 'post',
      dataType: 'html',
      data: $(this).serialize(),
      success: function (data) {
        if (data == "true") {
          window.location.href = '/schedule';
        } else {
          alert("This account may already exist or the data is incorrect.");
        }
      }
    });
    return false;
  });
});