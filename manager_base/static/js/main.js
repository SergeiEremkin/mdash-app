$(document).ready(function() {
    $('#need_call').on('change', (function (e) {
    if($(this).prop('checked')){
       $('#date_next_call').attr('disabled', null);
    } else {
        $('#date_next_call').attr('disabled', true);
    }
    }));
});











