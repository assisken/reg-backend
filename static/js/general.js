function notify(type, text) {
    var notification = $('<div/>', {
        class: 'alert alert-' + type
    });
    notification.prependTo('#notify-container');
    notification.append(text);
    notification.fadeIn('slow');
    notification.click(function() {
        notification.fadeOut('slow', function () {this.remove();});
    });
    setTimeout(function () {
        notification.fadeOut('slow', function () {this.remove();})
    }, 10000)
}

$('#alert-success').click(function(){
    var notification = $('#alert-' + type);
    notification.fadeOut('slow', function () {this.remove();});
});