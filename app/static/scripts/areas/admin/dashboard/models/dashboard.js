//
//  Admin dashboard panel
//
R("admin-dashboard", ["app", "model", "admin-services"], function (app, Model, Services) {

  return Model.extend({

    template: "dashboard",

    defaults: {
      error: void(0)
    },

    initialize: function () {

    }

  });
});
