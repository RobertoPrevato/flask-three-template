//
//  Sessions admin panel.
//
R("sessions-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    id: "sessions-panel",
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    table: {
      url: "/admin/getsessions",
      orderBy: "expiration",
      sortOrder: "desc",
      columns: {
        email: I.t("voc.Email"),
        client_ip: I.t("voc.ClientIp"),
        anonymous: I.t("voc.Anonymous"),
        expiration: I.t("voc.Expiration"),
        user_agent: I.t("voc.UserAgent")
      }
    },

    initialize: function () {

    }
  });
});