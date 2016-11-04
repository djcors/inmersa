$(document).ready(function(){
    $( "#fecha" ).datepicker({
        dateFormat: "dd/mm/yy",
        minDate: new Date
    });
    $('#timepicker1').timepicker();
    $('#simple-menu').sidr({
        name: 'sidr-main',
        source: '.nav-pills',
        side: 'right'
    });
    $('.carousel').carousel({
        pause: true,
        interval: false
    })

});
