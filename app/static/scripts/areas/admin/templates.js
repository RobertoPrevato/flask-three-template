//
//Knight generated templates file.
//
if (!ko.templates) ko.templates = {};
(function (templates) {
  var o = {
    'dashboard': '<div id="admin-dashboard"> <h1>Admin Dashboard</h1> <p>Implement here your administrative dashboard.</p> </div>',
    'exception-detail': '<h1>TODO</h1>',
    'message-detail': '<h1>TODO</h1>',
    'user-detail': '<h1>TODO</h1>',
    'login': '<div id="login-region" data-bind="dataentry"> <h2>{{ _("voc.Login") }}</h2> <!--ko if: error()--> <p class="error" data-bind="text: error"></p> <!--/ko--> <dl> <dt> <label for="email">{{ _("voc.Email") }}</label> </dt> <dd><input id="email" type="text" name="email" data-bind="value: email" /></dd> <dt> <label for="password">{{ _("voc.Password") }}</label> </dt> <dd><input id="password" type="password" name="password" data-bind="value: password" /></dd> <dt> <label for="remember">{{ _("voc.RememberOnline") }}</label> </dt> <dd><input id="remember" type="checkbox" name="remember" data-bind="checked: remember" /></dd> </dl> <div class="buttons"> <input type="button" value="{{ _("voc.LoginButton") }}" data-bind="click: submit" class="btn btn-primary" /> </div> </div>'
  };
  var x;
  for (x in o) {
    templates[x] = o[x];
  }
})(ko.templates);