//
//  Users admin panel.
//
R("users-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    table: {
      url: "/admin/getusers",
      useQueryString: false,
      columns: {
        email: "Email",
        roles: "Roles",
        data: {
          hidden: true,
          secret: true
        }
      }
    },

    initialize: function () {

    },

    loadList: function () {
      Services.getUsers({
        context: this
      }).done(function (data) {

      }).fail(function () {
        this.error({
          title: I.t("errors.LoadingContents")

        });
      });
    },

    loadDetails: function () {
      console.log("TODO");
    }
  });
});