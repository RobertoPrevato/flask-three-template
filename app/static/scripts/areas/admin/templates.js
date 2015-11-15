//
//Knight generated templates file.
//
if (!ko.templates) ko.templates = {};
(function (templates) {
  var o = {
    'dashboard': '<div id="admin-dashboard"> <h1>Admin Dashboard</h1> <p>Implement here your administrative dashboard.</p> </div>',
    'exception-detail': '<h1>TODO</h1>',
    'message-detail': '<h1>TODO</h1>',
    'user-detail': '<!--ko ifnot: data()--> <div data-bind="template: \'empty-view\'"></div> <!--/ko--> <!--ko if: data()--> <div class="detail-view"> <h1>{{ I.t("voc.UserDetails") }}</h1> <dl data-bind="with: data"> <dt>{{ I.t("voc.Email") }}</dt> <dd data-bind="text: email"></dd> <dt>{{ I.t("voc.Roles") }}</dt> <dd> <ul data-bind="foreach: roles"> <li> <span data-bind="text: $data"></span> </li> </ul> </dd> </dl> </div> <!--/ko-->',
    'login': '<div id="login-region" data-bind="dataentry"> <h2>{{ _("voc.Login") }}</h2> <!--ko if: error()--> <p class="error" data-bind="text: error"></p> <!--/ko--> <dl> <dt> <label for="email">{{ _("voc.Email") }}</label> </dt> <dd><input id="email" type="text" name="email" data-bind="value: email" /></dd> <dt> <label for="password">{{ _("voc.Password") }}</label> </dt> <dd><input id="password" type="password" name="password" data-bind="value: password" /></dd> <dt> <label for="remember">{{ _("voc.RememberOnline") }}</label> </dt> <dd><input id="remember" type="checkbox" name="remember" data-bind="checked: remember" /></dd> </dl> <div class="buttons"> <input type="button" value="{{ _("voc.LoginButton") }}" data-bind="click: submit" class="btn btn-primary" /> </div> </div>'
  };
  var x;
  for (x in o) {
    templates[x] = o[x];
  }
})(ko.templates);