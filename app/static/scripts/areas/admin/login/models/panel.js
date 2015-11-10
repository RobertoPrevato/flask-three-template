//
//  Admin login panel
//
R("admin-login-panel", ["model", "adminlogin-services"], function (Model, Services) {

  return Model.extend({

    template: "login",

    defaults: {

    },

    initialize: function () {

    },

    // validation schema
    schema: {
      username: {
        validation: ["required"]
      },

      password: {
        validation: ["required"]
      }
    },

    submit: function () {
      if (this.submitting) return false;
      this.submitting = true;

      this.validate().done(function () {
        //try login
        Services.tryLogin({
          context: this
        }).done(function (data) {


        }).fail(function () {

        });
      });
    }

  });
});
