//
//Knight generated templates file.
//
if (!ko.templates) ko.templates = {};
(function (templates) {
  var o = {
    'dashboard': '<div id="admin-dashboard"> <h1>Admin Dashboard</h1> <p>Implement here your administrative dashboard.</p> </div>',
    'user-form': '<div class="form-view"> <div data-bind="dataentry"> <h2 data-bind="text: formtitle"></h2> <dl> <dt><label for="email">{{ I.t("voc.Email") }}</label></dt> <dd> <input id="email" name="email" type="text" data-bind="value: data().email" /> </dd> <!--ko if: data().id--> <dt><label for="banned">{{ I.t("voc.Banned") }}</label></dt> <dd> <input id="banned" name="banned" type="checkbox" data-bind="checked: data().banned" /> </dd> <!--/ko--> <!--ko ifnot: data().id--> <dt><label for="password-one">{{ I.t("voc.Password") }}</label></dt> <dd> <input id="password-one" name="password-one" type="password" data-bind="value: data().passwordone" /> </dd> <dt><label for="password-two">{{ I.t("voc.ConfirmPassword") }}</label></dt> <dd> <input id="password-two" name="password-two" type="password" data-bind="value: data().passwordtwo" /> </dd> <!--/ko--> <dt><label for="roles">{{ I.t("voc.Roles") }}</label></dt> <dd> <select data-bind="options: form().roles, selectedOptions: data().roles" multiple="multiple"></select> </dd> </dl> </div> <div class="buttons"> <button type="button" class="btn" data-bind="click: save">{{ I.t("voc.Save") }}</button> <button type="button" class="btn" data-bind="click: cancel">{{ I.t("voc.Cancel") }}</button> </div> </div>',
    'login': '<div id="login-region" data-bind="dataentry"> <h2>{{ I.t("voc.Login") }}</h2> <!--ko if: error()--> <p class="error" data-bind="text: error"></p> <!--/ko--> <dl> <dt> <label for="email">{{ I.t("voc.Email") }}</label> </dt> <dd><input id="email" type="text" name="email" data-bind="value: email" /></dd> <dt> <label for="password">{{ I.t("voc.Password") }}</label> </dt> <dd><input id="password" type="password" name="password" data-bind="value: password" /></dd> <dt> <label for="remember">{{ I.t("voc.RememberOnline") }}</label> </dt> <dd><input id="remember" type="checkbox" name="remember" data-bind="checked: remember" /></dd> </dl> <div class="buttons"> <input type="button" value="{{ I.t("voc.LoginButton") }}" data-bind="click: submit" class="btn btn-primary" /> </div> </div>'
  };
  var x;
  for (x in o) {
    templates[x] = o[x];
  }
})(ko.templates);