const login = () => {
  $('div.card-content').empty();

  async function verify() {
    $.get('/status', (response) => {
      if (!response.status) {
        $('location').attr('href', '/login');
      }
    });
  }

  verify().then(() => {
    $.get('/login', (data) => {
      $('div.card-content').append(`<p>${data.g_url}</p>`);
      $('button.loginout').text('Logout');
      $('button.loginout').attr('id', 'logout');
      $('p.card-header-title').text(`${data.g_login}`);
      $('h5#sentence').text('Look at you, you polyglot! 🎏');
    });
  });
};

const logout = () => {
  $('div.card-content').empty();

  $.get('/logout', () => {});

  $('div.card-content').empty();
  $('button.loginout').text('Login');
  $('button.loginout').attr('id', 'login');
  $('p.card-header-title').text('spadefish');
  $('h5#sentence').text("Let's get swimming. 🐟🐟🐟");
};

$('document').ready(() => {
  $('button.loginout').click(function transition() {
    if ($(this).attr('id') === 'login') {
      login();
    } else {
      logout();
    }
  });
});
