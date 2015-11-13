//
//  App messages admin panel.
//
R("messages-panel", ["model", "app-services"], function (Model, Services) {

  return Model.extend({
    template: "generic-panel",

    defaults: {
      error: void(0),
      loading: false,
      subtemplate: "message-detail"
    },

    initialize: function () {

    },

    loadList: function () {
      Services.getMessages({
        context: this
      }).done(function (data) {

      }).fail(function () {
        this.error({
          title: I.t("errors.LoadingContents")

        });
      });
    },

    loadDetails: function () {

    }
  });
});