$(function () {
    var select_parent = function() {
        var _this = $(this);
        if (_this.find(":selected").val()) {
            $.ajax({
                url: '/_account/get_accounttype_pk__account_id/',
                type: 'get',
                data: {'id': _this.find(":selected").val()},
                success: function (data) {
                    $("#id_accounttype").val(data);
                }
            });
        }
    };
    $("#objectModal").on("change", ".select_parent", select_parent);

    var select_accounttype = function() {
        var _this = $(this);
        if (_this.find(":selected").val()) {
            $.ajax({
                url: '/_account/get_account_list__accounttype_id/',
                type: 'get',
                data: {'id': _this.find(":selected").val()},
                success: function (data) {
                    $("#id_parent").html(data);
                }
            });
        } else {
            $.ajax({
                url: '/_account/get_account_list/',
                type: 'get',
                success: function (data) {
                    $("#id_parent").html(data);
                }
            });
        }
    };
    $("#objectModal").on("change", ".select_accounttype", select_accounttype);
});