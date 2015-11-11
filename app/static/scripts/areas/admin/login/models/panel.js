//
//  Admin login panel
//
R("admin-login-panel", ["app", "browser", "model", "adminlogin-services"], function (app, Browser, Model, Services) {

  return Model.extend({

    template: "login",

    defaults: {
      email: "",
      password: "",
      remember: false,
      error: void(0)
    },

    initialize: function () {

    },

    // validation schema
    schema: {
      email: {
        validation: ["required", "email"]
      },

      password: {
        validation: ["required"]
      }
    },

    submit: function () {
      var self = this;
      if (self.submitting) return false;
      self.submitting = true;

      self.validate().done(function (data) {
        //try login
        Services.login({
          context: self,
          email: data.email,
          password: data.password,
          remember: self.remember(),
          navigator: Browser.getNavigatorInfo()
        }).done(function (data) {
          if (data.success) {
            //redirect to admin dashboard
            location.replace("/admin");
          } else {
            //display an error message
            self.error(I.t("errors.LoginFailed"));
            self.submitting = false;
          }
        }).fail(function () {
          app.errorDialog();
          self.submitting = false;
        });
      }).fail(function () {
        self.submitting = false;
      });
    }
  });
});
