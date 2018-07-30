$(function() {

    $("#thresholdModal").on("show.bs.modal", function(e) {

        const button = $(e.relatedTarget);
        const field = button.attr("data-field");

        $.ajax({
            url: '/data-pre_processing/ajax/get_values',
            type: "POST",
            data: { 'field': field },
            success: function(data) {
                console.log(data);
            },
            error: function(e) {
                console.log(e.responseText);
            }
        });
    });
});






















function getCookie(name) {

    var cookieValue = null;

    if (document.cookie && document.cookie != '') {

        var cookies = document.cookie.split(';');

        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});