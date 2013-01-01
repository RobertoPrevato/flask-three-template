//
//  App messages admin panel.
//
R("messages-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    id: "messages-panel",
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    initialize: function () {

    },

    table: {
      url: "/admin/getmessages",
      useQueryString: false,
      columns: {
        kind: I.t("voc.Kind"),
        message: I.t("voc.Message"),
        timestamp: I.t("voc.Timestamp"),
        data: {
          hidden: true,
          secret: true
        }
      }
    }
  });
});