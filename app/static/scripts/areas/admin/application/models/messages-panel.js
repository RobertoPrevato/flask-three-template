//
//  App messages admin panel.
//
R("messages-panel", ["model"], function (Model) {

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
      orderBy: "timestamp",
      sortOrder: "desc",
      columns: {
        kind: I.t("voc.Kind"),
        message: I.t("voc.Message"),
        timestamp: I.t("voc.Timestamp")
      }
    }
  });
});