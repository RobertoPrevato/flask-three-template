(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor) {
    var v = valueAccessor();

    element.setAttribute("id", v);
  };

  ko.bindingHandlers.id = {
    init: setter,
    update: setter
  };

})();
