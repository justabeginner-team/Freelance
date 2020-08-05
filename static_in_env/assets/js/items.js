$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-item").modal("show");
      },
      success: function (data) {
        $("#modal-item .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#item-table tbody").html(data.html_item_list);
          $("#modal-item").modal("hide");
        }
        else {
          $("#modal-item .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-item").click(loadForm);
  $("#modal-item").on("submit", ".js-item-create-form", saveForm);

  // Update book
  $("#item-table").on("click", ".js-update-item", loadForm);
  $("#modal-item").on("submit", ".js-item-update-form", saveForm);

    // Delete book
    $("#item-table").on("click", ".js-delete-item", loadForm);
    $("#modal-item").on("submit", ".js-item-delete-form", saveForm);
});