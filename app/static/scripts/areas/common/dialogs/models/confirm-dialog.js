//
//  Confirm dialog model
//
R("models.confirm-dialog", ["model"], function (Model) {

  return Model.extend({
    defaults: {
      id: "",
      title: "",
      content: ""
    }
  }, {
    type: "confirm-dialog"
  });
});
