//
//  Knockout KingTable binder.
//
(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor, model) {
    var v = ko.unwrap(valueAccessor());
    $(element).kingtable(v);
    ko.onDispose(element, function (element) {
      //dispose the kingtable
      var kingtable = $(element).data("kingtable");
      if (kingtable) kingtable.dispose();
    });
  };

  ko.bindingHandlers.kingtable = {
    init: setter
  };

})();
