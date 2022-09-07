$(function () {
    var loadForm = function () {
        var btn = $(this);
        var _url = btn.attr("data-url");
        $.ajax({
            url: _url,
            type: 'get',
            beforeSend: function () {
                $("#crudModal .modal-content").html("");
                $("#crudModal").modal("show");
            },
            success: function (data) {
                $("#crudModal .modal-content").html(data);
                setTimeout(function (){
                    $('#crudModal input:enabled:visible:first').focus();
                    $("#crudModal input:enabled:visible:first").select();
                }, 500);
            }
        });
    };
    $("#bodybase").on("click", ".button_create", loadForm);
    $("#bodybase").on("click", ".button_detail", loadForm);
    $("#bodybase").on("click", ".button_update", loadForm);
    $("#bodybase").on("click", ".button_delete", loadForm);

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            type: form.attr("method"),
            data: form.serialize(),
            headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
            success: function (data, status, xhr) {
                if (data.indexOf("</form>") > 0) {
                    $("#crudModal .modal-content").html(data);
                    setTimeout(function (){
                        $("#crudModal input:visible:first").select();
                    }, 100);
                } else {
                    $("#object_list").html(data);
                    $("#crudModal").modal("hide");
                }
            },
            error: function (jqXhr, textStatus, errorMessage) {
                alert(errorMessage);
            }
        });
        return false;
    };
    $("#crudModal").on("submit", ".CreateForm", saveForm);
    $("#crudModal").on("submit", ".UpdateForm", saveForm);
    $("#crudModal").on("submit", ".DeleteForm", saveForm);
});