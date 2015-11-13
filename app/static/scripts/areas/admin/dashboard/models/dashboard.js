//
//  Admin dashboard panel
//
R("admin-dashboard", ["app", "model", "admin-services"], function (app, Model, Services) {

  return Model.extend({

    template: "generic-panel",
    subtemplate: "dashboard",

    defaults: {
      loading: !true,
      error: void(0)
    },

    initialize: function () {

    },

    load: function () {
      Services.getDashboardData({
        context: this
      }).done(function (data) {


        this.loading(false);

      }).fail(app.errorDialog)
    }

  });
});
