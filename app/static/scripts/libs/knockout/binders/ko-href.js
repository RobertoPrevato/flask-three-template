(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor) {
    var v = valueAccessor();
    element.setAttribute("href", v);
  };

  ko.bindingHandlers.href = {
    init: setter,
    update: setter
  };

})();
