//
//Knight generated templates file.
//
if (!ko.templates) ko.templates = {};
(function (templates) {
  var o = {
    'login': '<div id="login-region" data-bind="dataentry"> <h2>{{ _("voc.Login") }}</h2> <!--ko if: error()--> <p class="error" data-bind="text: error"></p> <!--/ko--> <form id="login-form" action="/admin/auth" method="post"> <dl> <dt> <label for="username">{{ _("voc.Username") }}</label> </dt> <dd><input id="username" type="text" name="username" data-bind="value: username" /></dd> <dt> <label for="password">{{ _("voc.Password") }}</label> </dt> <dd><input id="password" type="password" name="password" data-bind="value: password" /></dd> </dl> <div class="buttons"> <input type="submit" value="{{ _("voc.Login") }}" /> </div> </form> </div>'
  };
  var x;
  for (x in o) {
    templates[x] = o[x];
  }
})(ko.templates);