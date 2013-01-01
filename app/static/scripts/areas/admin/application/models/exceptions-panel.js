//
//  App exceptions admin panel.
//
R("exceptions-panel", ["model", "app-services"], function (Model, Services) {

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
        useQueryString: false,
        orderBy: "timestamp",
        sortOrder: "desc",
        columns: {
          type: I.t("voc.Type"),
          message: I.t("voc.Message"),
          callstack: I.t("voc.Callstack"),
          timestamp: I.t("voc.Timestamp"),
          data: {
            hidden: true,
            secret: true
          }
        }
      }
  });
});