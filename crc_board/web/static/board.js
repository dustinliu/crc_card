$( function() {
    $( '.sortable' ).sortable();
    $( '.sortable' ).disableSelection();
    $('.popup').dialog({
        autoOpen: false,
        width: 600,
        modal: true,
        title: 'Create Board'
        // buttons: [
        //     {
        //         text: "Create",
        //         click: create_board()
        //
        //         // Uncommenting the following line would hide the text,
        //         // resulting in the label being used as a tooltip
        //         //showText: false
        //     }
        // ]
    });
} );


function show_create() {
    $('.popup').dialog('open');
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

    window.location.replace("/");
}

function create_card(id) {
    var name = $('#card_name').val();
    $.ajax({
        type: 'POST',
        url: '/api/cards',
        dataType: 'json',
        data: { name: name, board_id: id},
        success: function () {
        },
        error: function (error) {
            console.log(error.status);
            console.log(error.responseJSON.message);
        }
    });

    window.location.reload();
}
