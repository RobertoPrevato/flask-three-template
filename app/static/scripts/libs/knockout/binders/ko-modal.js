//
//bootstrap modal dialog view
//
ko.bindingHandlers.modal = {
  init: function(element, valueAccessor, allBindings, model, context) {
    var elem = $(element), options = valueAccessor() || {};
    //use bootstrap modal
    elem.modal(options);
    //on close, trigger event
    elem.on("hidden.bs.modal", function () {
      var onClose = elem.data("onClose");
      if (onClose) onClose(elem);
      if (options.onClose) options.onClose();
    });
    //when opening modal dialog, scroll view to top
    $("body").addClass("modal-open");
    $("html, body").animate({scrollTop: 0}, 300);
    ko.onDispose(element, function () {
      $("body").removeClass("modal-open");
      _.delay(function () {
        $(".modal-backdrop").remove();
      }, 50);
    });
  },
  update: function(element, valueAccessor, allBindings, model, context) {}
};