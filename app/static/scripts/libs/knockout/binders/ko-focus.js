//focus custom binders
_.extend(ko.bindingHandlers, {

  focus: {
    init: function (element) {
      var elem = $(element);
      _.delay(function () {
        if (/input|select|button/i.test(element.tagName))
          elem.trigger('focus');
        else
          elem.find(":input:not(:disabled):not([readonly]):first").trigger('focus');
      }, 50);
    }
  },

  scroll: {
    init: function (element) {
      //var elem = $(element);
      _.delay(function () {
        //when opening modal dialog, scroll view to top
        $('html, body').animate({ scrollTop: 0 }, 300);
      }, 50);
    }
  }

});
