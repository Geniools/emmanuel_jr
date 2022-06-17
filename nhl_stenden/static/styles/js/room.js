$(function() {

  $("#get_room").on("submit", function () {
    current_id = $("#room_input").val();

    $.ajax({
      url: '/methods/getroom/',
      method: 'post',
      dataType: 'html',
      data: $(this).serialize(),
      success: function (data) {
        if (data === "true") {
          $("#room_placeholder").attr("placeholder", "TRUE: " + current_id);
        } else {
          $("#room_placeholder").attr("placeholder", "FALSE!");
        }
      }
    });
    return false;
  });

});