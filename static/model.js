/*jslint node: true */
'use strict';


// function getBrand() {
    // var menu = $('#menu').get(0);
    // var ac = 'УАЗ';
    // var brand = $("li").find("a");
    // // console.log($(this).attr('id'));
    // // console.log(brand[10]);
    // for (var i = 10; i < brand.length; i += 1) {
        // var name = $(brand[i]).get(0).innerHTML;
        // // console.log(name);
    // }
// };


$(document).ready(function(){
    $('.brand').click(function(){
        var name = $(this.innerHTML).get(0).innerText;
        // var name = $('#name').get(0).innerHTML;
        $.post('/getBrand', {name: name}, function (answer) {
            $('#brandButton').get(0).innerHTML = answer + '<span class="caret">';
        });
        $.post('/getModel', {name: name}, function(answer) {
            $('#model').html('');

            // $('#model').html(answer.models);
            console.log(answer.models);

            for (var i = 0; i < answer.models.length; i += 1) {
                $('#model').append('<li class="model"><a href="#">' + answer.models[i] + '</a></li>');
            };
            $('.model').click(function(){
                var model = $(this.innerHTML).get(0).innerText;
                $.post('/changeModel', {name: model}, function (answer) {
                    $('#modelButton').get(0).innerHTML = answer + '<span class="caret">';
                });
                console.log(model);
            });
        });
    });
})
