(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor) {
    var v = ko.unwrap(valueAccessor());
    element.setAttribute("id", v);
  };

  ko.bindingHandlers.id = {
    init: setter,
    update: setter
  };

})();
