//
// Model of the getting started view
//
R("models.gettingstarted", ["model"], function (Model) {

  return Model.extend({

    template: "gettingstarted",

    //defaults are merged with constructor options and set as Knockout observables in the model
    defaults: {
      dialog: void(0)
    },

    initialize: function () {

    },

    open_dialog: function () {
      this.dialog({
        title: "Example dialog",
        content: "See in the code how Knockout and Bootstrap interact."
      });
    }

  });
});

