$(document).ready(function() {
  $('#chat-form').submit(function(event) {
    event.preventDefault();
    var message = $('#chat-input').val();
    $.ajax({
      type: 'POST',
      url: '/chatbot/',
      data: {
        'message': message,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(response) {
        var message = response['message'];
        $('.messages').append('<div class="message sent"><p>' + message + '</p></div>');
        $('#chat-input').val('');
        $('.chat-window').scrollTop($('.chat-window')[0].scrollHeight);
      },
      error: function(response) {
        alert('Error: ' + response.responseText);
      }
    });
  });

  $('#close-chat').click(function() {
    $('.chat-window').fadeOut();
  });
});
