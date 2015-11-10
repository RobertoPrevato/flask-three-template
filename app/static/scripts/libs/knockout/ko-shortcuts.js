(function (k) {

  //define shortcuts for knockout; some properties are too long and they don't get minified
  k.o = function (a) {
    return a instanceof Array
      ? this.observableArray(a)
      : this.observable(a);
  };
  k.bind = ko.applyBindings;

  //knockout is ridiculously verbose
  k.onDispose = ko.utils.domNodeDisposal.addDisposeCallback;
})(ko);