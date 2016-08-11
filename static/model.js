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
        $.post('/hello', {name: name}, function (answer) {
            $('#sayHello').get(0).innerHTML = answer + '<span class="caret">';
        });
    });
})
