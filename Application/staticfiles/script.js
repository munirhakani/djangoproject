$(function () {
    var buttonAction_click = function () {
        var _this = $(this);
        $.ajax({
            url: _this.attr("data-url"),
            type: 'get',
            success: function (data) {
                $("#object_list").html(data);
                $("#objectModal").modal("hide");
            }
        });
    };
    $("#bodybase").on("click", ".button_action", buttonAction_click);
    
    var loadForm = function () {
        var _this = $(this);
        var _thisModal = _this.attr("data-bs-target");
        $.ajax({
            url: _this.attr("data-url"),
            type: 'get',
            beforeSend: function () {
                $(_thisModal + " .modal-content").html("");
            },
            success: function (data) {
                $(_thisModal + " .modal-content").html(data);
                $(_thisModal).modal("show");
                setTimeout(function () {
                    $(_thisModal + " input:visible:first").select();
                }, 100);
            },
        });
    };
    $("#bodybase").on("click", ".button_create", loadForm);
    $("#bodybase").on("click", ".button_find", loadForm);
    $("#bodybase").on("click", ".button_detail", loadForm);
    $("#bodybase").on("click", ".button_update", loadForm);
    $("#bodybase").on("click", ".button_delete", loadForm);

    var saveForm = function () {
        var _this = $(this);
        $.ajax({
            url: _this.attr("action"),
            type: _this.attr("method"),
            data: _this.serialize(),
            headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
            success: function (data, status, xhr) {
                if (data.indexOf("</form>") > 0) {
                    $("#objectModal .modal-content").html(data);
                    setTimeout(function (){
                        $("#objectModal input:visible:first").select();
                    }, 100);
                } else {
                    $("#object_list").html(data);
                    $("#objectModal").modal("hide");
                }
            },
            error: function (jqXhr, textStatus, errorMessage) {
                alert(errorMessage);
            },
        });
        return false;
    };
    $("#objectModal").on("submit", ".CreateForm", saveForm);
    $("#objectModal").on("submit", ".FindForm", saveForm);
    $("#objectModal").on("submit", ".UpdateForm", saveForm);
    $("#objectModal").on("submit", ".DeleteForm", saveForm); 
});