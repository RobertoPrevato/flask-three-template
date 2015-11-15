//
//  Users admin panel.
//
R("users-panel", ["admin-panel", "user-services"], function (AdminPanel, Services) {

  return AdminPanel.extend({
    id: "users-panel",
    listUrl: "#/users",
    formView: "user-form",
    editItemTitle: I.t("voc.EditUser"),
    createItemTitle: I.t("voc.CreateNewUser"),
    services: Services,

    defaults: {
      data: {}, //stores the object data (for edit views; or create new)
      error: void(0),
      loading: false,
      subtemplate: "tableview",
      formtitle: ""
    },

    schema: {
      email: {
        validation: ["required", "email"]
      },
      "password-one": {
        validation: ["required", "newPassword"]
      },
      "password-two": {
        validation: ["required", "newPassword"]
      }
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

    initialize: function () {

    }
  });
});