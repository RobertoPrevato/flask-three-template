//
//  App exceptions admin panel.
//
R("exceptions-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "exception-detail"
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
    }
  });
});