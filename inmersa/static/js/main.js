var array = new Array()
var listado_carrito = [];
var codes = new Array()

$(document).ready(function(){
  get_items_to_localstorage();
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
 
    });
    //search filter
    $("#busqueda").keyup(function(){
 
        var filter = $(this).val(), count = 0;
 
        $(".card-columns .card").each(function(){
 
            if ($(this).find('.card-title').text().search(new RegExp(filter, "i")) < 0) {
                $(this).fadeOut();
 
            } else {
                $(this).show();
                count++;
            }
        });
 
    });
});

function get_items_to_localstorage(){
    var items = JSON.parse(localStorage.getItem("cart"));
    if (items != null){
        listado_carrito = items
        for (var i=0; i < items.length; i++){
            array.push(items[i])
        }
        add_to_cart();
        if(listado_carrito.length > 0){
          $('#carrito_top').css('display', 'block');
          cout_items_cart(listado_carrito.length);
        }
    }else{
        listado_carrito.length = 0;
        add_to_cart();
    }

}


function callback_cart(item){
    $.ajax({
        url: '/api/platos/',
        data: {
            'codigo':item
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#carrito_top').html('<p>An error has occurred</p>');
            alert(jqXHR.status);
            alert(textStatus);
            alert(errorThrown);
        },
        dataType : 'json',
        success: function(data) {
            array.push(data[0]) 
            listado_carrito = unique(array)
            cout_items_cart(listado_carrito.length);
            add_to_cart();
            $('#carrito_top').css('display', 'block');
        }
    })
}


function add_to_cart(){
    $('#carrito_top .dropdown-menu').empty();
    for(var i = 0; i < listado_carrito.length; i++){
      json = JSON.stringify(listado_carrito[i])
      json = json.replace(/"/g, "'");
        var item = `<a class="dropdown-item `+listado_carrito[i]['codigo'] +`" href="javascript:void(0)" onClick="delete_to_cart(`+json +`,'`+listado_carrito[i]['codigo'] +`')">`+listado_carrito[i]['nombre'] + `-` +listado_carrito[i]['valor'] +`</a>`
        $('#carrito_top .dropdown-menu').append(item);
        codes.push(listado_carrito[i]['codigo'])
    }
    button_shop(codes)
}

function cout_items_cart(items){
    if (items == 0){
        $('.counter').css('display', 'none');
    }else{
        $('.counter').css('display', 'initial').text(items);  
    }
}

function button_shop(codes){
  $('#carrito_top .comprar').remove()
  var button = '<div class="dropdown-divider"></div><button class="comprar btn btn-primary" onClick="comprar()" data-codes="'+codes+'">Finalizar compra</button>'
  $('#carrito_top .dropdown-menu').append(button);

}


function unique(obj){
    var uniques=[];
    var stringify={};
    for(var i=0;i<obj.length;i++){
       var keys=Object.keys(obj[i]);
       keys.sort(function(a,b) {return a-b});
       var str='';
        for(var j=0;j<keys.length;j++){
           str+= JSON.stringify(keys[j]);
           str+= JSON.stringify(obj[i][keys[j]]);
        }
        if(!stringify.hasOwnProperty(str)){
            uniques.push(obj[i]);
            stringify[str]=true;
        }
    }
    localStorage.setItem('cart', JSON.stringify(uniques));
    return uniques;
}


function delete_to_cart(json, item){
    var index  = arrayObjectIndexOf(array, json, "codigo")
    removeByIndex(array, index); 
    removeByIndex(codes, index);   
    listado_carrito = unique(array)
    button_shop(codes)
    cout_items_cart(listado_carrito.length);
    if(listado_carrito.length == 0){
        $('#carrito_top').css('display', 'none');
    }
    $('#carrito_top').find(".dropdown-menu ."+item+"").remove()
}

function arrayObjectIndexOf(myArray, searchTerm, property) {
    for(var i = 0, len = myArray.length; i < len; i++) {
        if (myArray[i][property] === searchTerm[property]) {
          return i
        };
    }
    return -1;
}

function removeByIndex(arr, index) {
  arr.splice(index, 1);
}

function logout(){
  localStorage.clear();
  window.location.href = "/logout/"
}

function comprar(){
  var codes = $('.comprar').data('codes')
  data = {'datos':codes}
  $.post( "/api/comprar/", data)
      .done(function( data, statusText, xhr ) {
        console.log(statusText )
        if(statusText == "success"){
            setTimeout(function(){
                localStorage.clear();
                window.location.href = "/"
              ;},1000
            );
        }else{
          alert('ups algo salio mal')
        }
        
    });


}


