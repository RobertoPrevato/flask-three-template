(function () {

  var setter = function(element, valueAccessor, allBindingsAccessor) {
    var v = valueAccessor();
    element.setAttribute("src", v);
  };

  ko.bindingHandlers.src = {
    init: setter,
    update: setter
  };

})();
