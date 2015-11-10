//
//  Base dialog model
//
R("models.dialog", ["model"], function (Model) {

  return Model.extend({
    defaults: {
      title: "",
      content: ""
    }
  }, {
    type: "generic-dialog"
  });
});
