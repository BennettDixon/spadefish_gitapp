async function request() {
  $('div.card-content').empty();
}

async function clear() {
  $('div.card-content').empty();
}

$('document').ready(() => {
  $('button.loginout').click(function transition() {
    if ($(this).attr('id') === 'login') {
      request().then(() => {
        $('div.card-content').append('<svg />');
        $('button.loginout').text('Logout');
        $('button.loginout').attr('id', 'logout');
      });
    } else {
      clear().then(() => {
        $('div.card-content').append('<svg /></svg>');
        $('button.loginout').text('Login');
        $('button.loginout').attr('id', 'login');
      });
    }
  });
});
