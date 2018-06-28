function Reset(id, on_success, on_failure) {
    const book_link = 'http://www.gigamonkeys.com/book/';

    $(id).submit(function(e) {
        var form = $(this);
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize()
        }).done(function(text) {
            $(id).each(function(){
                this.reset();
            });

            var res = JSON.parse(text);

            notify(res.type, res.message);
            if(res.type === 'success') {
                on_success(res.message);
            }
        }).fail(function() {
            notify('danger', 'Произошла ошибка. Попробуйте обратиться к администратору.' +
                'Если вы не знаете, чем себя занять, рекомендуем почитать эту ' +
                '<a href="'+book_link+'" target="_blank">книгу</a>.');
        });

        // Отмена действия по умолчанию для кнопки submit.
        e.preventDefault();
    });
}

$(function() {
    Reset('#passreset');
    Reset('#dbpasscreate', function () {
        setTimeout(function () {
            location.reload()
        }, 2000)
    });
    Reset('#dbpassreset');
    Reset('#dbcreate', function () {
        setTimeout(function () {
            location.reload()
        }, 2000)
    });
    Reset('#dbdel', function () {
        setTimeout(function () {
            location.reload()
        }, 2000)
    });
});