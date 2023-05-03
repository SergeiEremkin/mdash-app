$(document).ready(function() {
    $('#id_need_call').on('change', (function (e) {
    if($(this).prop('checked')){
       $('#id_date_next_call').attr('disabled', false);
    } else {
        $('#id_date_next_call').attr('disabled', true);
    }
    }));
});











