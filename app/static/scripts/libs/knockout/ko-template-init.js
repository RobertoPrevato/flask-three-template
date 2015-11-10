(function (ko) {
  var templateInit = ko.bindingHandlers.template.init;

  //overrides base template.init to hide the element during processing
  ko.bindingHandlers.template.init = function (element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {

    var el = $(element);
    //make element not visible while working on it
    el.css({ visibility: 'hidden' });
    _.defer(function () {
      //make visible
      el.css({ visibility: 'visible' });
    });

    return templateInit(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext);
  };
})(ko);