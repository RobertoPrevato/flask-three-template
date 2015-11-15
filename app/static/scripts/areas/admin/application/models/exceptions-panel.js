//
//  App exceptions admin panel.
//
R("exceptions-panel", ["model"], function (Model) {

  return Model.extend({
    id: "exceptions-panel",
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "tableview"
    },

    initialize: function () {

    },

    table: {
      url: "/admin/getexceptions",
      orderBy: "timestamp",
      sortOrder: "desc",
      columns: {
        type: I.t("voc.Type"),
        message: I.t("voc.Message"),
        callstack: I.t("voc.Callstack"),
        timestamp: I.t("voc.Timestamp")
      }
    }
  });
});