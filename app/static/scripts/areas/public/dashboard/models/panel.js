//
// Model of the dashboard view
//
R("models.dashboard", ["model"], function (Model) {

  return Model.extend({

    template: "dashboard",

    //defaults are merged with constructor options and set as Knockout observables in the model
    defaults: {},

    initialize: function () {

    }

  });
});

