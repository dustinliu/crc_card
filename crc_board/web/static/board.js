$( function() {
    $( '.sortable' ).sortable();
    $( '.sortable' ).disableSelection();
} );


function show_create() {
    $('.form').css({'display': 'inline-block'})
}


function create_board() {
    var name = $('#board_name').val();
    var desc = $('#board_desc').val();
    $.ajax({
        type: 'POST',
        url: '/api/boards',
        dataType: 'json',
        data: { name: name, description: desc},
        success: function () {
            console.log('success')
        },
        error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
        }
    });
    window.location.replace("{{ url_for('.index') }}");
}
