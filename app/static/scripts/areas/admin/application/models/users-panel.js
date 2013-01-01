//
//  Users admin panel.
//
R("users-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    id: "users-panel",
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    table: {
      url: "/admin/getusers",
      columns: {
        email: I.t("voc.Email"),
        roles: I.t("voc.Roles"),
        data: {
          hidden: true,
          secret: true
        }
      }
    },

    initialize: function () {

    }
  });
});