$(function() {
    var book_link = 'http://www.gigamonkeys.com/book/';

    $('#passreset').submit(function(e) {
        var form = $(this);
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize()
        }).done(function(text) {
            $('#passreset').each(function(){
                this.reset();
            });

            var res = JSON.parse(text);

            if(res.success) {
                notify('success', 'Пароль успешно обновлён!');
            } else {
                notify('danger', res.message)
            }
        }).fail(function() {
            notify('danger', 'Произошла ошибка. Попробуйте позже.\n' +
                'Если вы не знаете, чем себя занять, рекомендуем почитать эту ' +
                '<a href="'+book_link+'" target="_blank">книгу</a>.')
        });

        // Отмена действия по умолчанию для кнопки submit.
        e.preventDefault();
    });
});
