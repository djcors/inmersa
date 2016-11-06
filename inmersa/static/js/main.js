$(document).ready(function(){
    $('.fav').click(function(){
        $.botton = $(this)
        user = $(this).data('user');
        plato = $(this).data('pk');
        liked = $(this).data('liked');
        data = {
            'user':user,
            'plato':plato,
            'liked':liked
        }
       $.post( "/api/fav/", data)
          .done(function( data ) {
            if(liked == "True"){
                console.log($.botton)
               $.botton.data('liked',"")
               $.botton.attr('data-liked',"False");
               $.botton.removeClass('liked');
            }else{
               $.botton.data('liked',"True");
               $.botton.attr('data-liked',"True");
               $.botton.addClass('liked');    
            }
            $.botton.next().text(data['fav'])
            
        });
 
    })
    
});
