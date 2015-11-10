//data custom binder
ko.bindingHandlers.data = {
  init: function(element, valueAccessor, allBindingsAccessor) {
    $(element).data(valueAccessor());
  },
  update: function(element, valueAccessor, allBindingsAccessor) {
    $(element).data(valueAccessor());
  }
};
