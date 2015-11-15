//
//  Knockout KingTable binder.
//
(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor, model) {
    var v = ko.unwrap(valueAccessor());
    v.$el = $(element);
    var table = new $.KingTable(v, { context: model });
    if (v.onRender) v.onRender.call(model, table);

    //register event handlers
    if (model.loading)
      table.on("fetch:end", function () {
        model.loading(false);
      });

    if (model.error)
      table.on("fetch:error", function () {
        model.error({
          title: I.t("errors.LoadingData"),
          retry: function () {
            model.loading(true).delay(function () {
              table.refresh();
            }, 300);
          }
        });
      });

    //render the table
    table.render();
    ko.onDispose(element, function (element) {
      //dispose the kingtable
      //var kingtable = $(element).data("kingtable");
      delete table.context;
      table.dispose();
    });
  };

  ko.bindingHandlers.kingtable = {
    init: setter
  };
})();
