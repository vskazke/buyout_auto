/*jslint node: true */
'use strict';


$(document).ready(function(){
    $('.form-group').focus(function() {
        $(this).get(0).placeholder = '';
        $(this).append('<div>dffff</div>');
    });
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
    $('.year').click(function(){
        var year = $(this.innerHTML).get(0).innerText;
        // var name = $('#name').get(0).innerHTML;
        $.post('/getYear', {name: year}, function (answer) {
            $('#yearButton').get(0).innerHTML = answer + '<span class="caret">';
        });
    });
    $( "#phone" ).focus(function() {
        var num = $(this).get(0).value = '+7 --- --- -- --';
        $('#phone').click(function() {
            $(this).get(0).setSelectionRange(2, 2);
            console.log(this.value);
        });
        var n = this.value;
        $('#phone').keypress(function(event) {
            var num = $(this).get(0).selectionStart;
            var element = String.fromCharCode(event);
            // if ($(this).get(0).selectionStart == 1 || $(this).get(0).selectionStart == 0) {
                // $(this).attr("id", "disabled");
            // };
            // $("#disabled").attr("disabled", "disabled");
            if (num ==2 || num==6 || num == 10 || num == 13) {
                this.value = this.value.substring(0, num) + ' ';
            }
            // if (num == 0 || num == 1 ) {
                // return false;
            // };
            if (event.which >= 48 && event.which <= 57 || event.which == 32) {
                return;
            } else { return false };

        });
    });
    $( "#phoneCall" ).focus(function() {
        var num = $(this).get(0).value = '+7 --- --- -- --';
        $('#phoneCall').click(function() {
            $(this).get(0).setSelectionRange(2, 2);
            console.log(this.value);
        });
        var n = this.value;
        $('#phoneCall').keypress(function(event) {
            var num = $(this).get(0).selectionStart;
            var element = String.fromCharCode(event);
            // if ($(this).get(0).selectionStart == 1 || $(this).get(0).selectionStart == 0) {
                // $(this).attr("id", "disabled");
            // };
            // $("#disabled").attr("disabled", "disabled");
            if (num ==2 || num==6 || num == 10 || num == 13) {
                this.value = this.value.substring(0, num) + ' ';
            }
            // if (num == 0 || num == 1 ) {
                // return false;
            // };
            if (event.which >= 48 && event.which <= 57 || event.which == 32) {
                return;
            } else { return false };

        });
    });
    $("#send").click(function() {
        // about auto
        var brand = $("#brandButton").get(0).innerText;
        var model = $("#modelButton").get(0).innerText;
        var year = $("#yearButton").get(0).innerText;
        // about person
        var name = $("#name").get(0).value;
        var phone = $("#phone").get(0).value;
        if (phone.length != 0 && name.length != 0 && phone != '+7 --- --- -- --' && phone.length == 16) {
            $.post('/short_result',
                {'brand': brand,
                    'model': model,
                    'year': year,
                    'name': name,
                    'phone': phone},
                function (answer) {
                    $('#answer').html(answer);
            $('#callBack').modal('hide');
            });
        }else {
            $("#name").css('background', 'red');
            $("#name").get(0).placeholder = 'укажите ваше имя';
            $("#phone").css('background', 'red');
            $("#phone").get(0).placeholder = 'укажите номер телефона';
        };
    });
    $("#sendCallBack").click(function() {
        var name = $("#nameCall").get(0).value;
        var phone = $("#phoneCall").get(0).value;
        if (phone.length != 0 && name.length != 0 && phone != '+7 --- --- -- --' && phone.length == 16) {
            $.post('/callBack',
                {'name': name,
                 'phone': phone},
                function (answer) {
                    $('#answer').html(answer);
            $('#callBack').modal('hide');
            });
        }else {
            $("#nameCall").css('background', 'red');
            $("#nameCall").get(0).placeholder = 'укажите ваше имя';
            $("#phoneCall").css('background', 'red');
            $("#phoneCall").get(0).placeholder = 'укажите номер телефона';
        };
    });
})
