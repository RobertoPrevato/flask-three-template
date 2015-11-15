//
//  Users admin panel.
//
R("users-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    id: "users-panel",
    listUrl: "#/users",
    template: "generic-panel",
    detailview: "user-detail",

    defaults: {
      data: void(0),
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    table: {
      url: "/admin/getusers",
      detailRoute: "#/user/",
      columns: {
        email: I.t("voc.Email"),
        roles: I.t("voc.Roles"),
        data: {
          hidden: true,
          secret: true
        }
      }
    },

    initialize: function (params) {
      this.handleParams(params);
    },

    handleParams: function (params) {
      if (!params) params = { view: "list" };
      //function to use to handle url changes;
      var self = this;
      switch (params.view)
      {
        case "list":
          //display the list view
          self.subtemplate("tableview");
          break;
        case "details":
          //display the detail view
          self
            .loading(true)
            .subtemplate(self.detailview)
            .loadDetails(params.id);
          break;
        default:
          throw "View type `" + params.view + "` is not handled.";
      }
    },

    loadDetails: function (id) {
      var self = this;

      Services.getUserDetails({
        id: id
      }).done(function (data) {
        self
          .data(data)
          .loading(false);
      }).fail(function () {
        self.error({
          title: I.t("errors.LoadingData"),
          retry: function () {
            self.loading(true).delay(function () {
              self.loadDetails(id);
            }, 300);
          }
        }).loading(false);
      });
    }
  });
});