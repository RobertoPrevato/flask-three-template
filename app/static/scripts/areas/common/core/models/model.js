//
//  Base model definition
//
R("model", ["extend", "events"], function (Extend, Events) {

  var Model = function (attributes, staticProperties) {
    if (staticProperties) _.extend(this, staticProperties);
    var attrs = attributes || {};
    this.cid = _.uniqueId('c');
    this.disposables = [];
    attrs = _.defaults({}, attrs, _.result(this, 'defaults'));
    var p = "attrsFilter";
    if (this[p])
      this[p](attrs);
    this.set(attrs);
    this.initialize.apply(this, arguments);
  };

  // Attach all inheritable methods to the Model prototype.
  _.extend(Model.prototype, Events, {

    initialize: function () { },

    result: function (name, args) {
      //similar to _.result, but with arguments
      if (this[name])
        return _.isFunction(this[name]) ? this[name](args) : this[name];
      return null;
    },

    set: function (name, value) {
      //sets observable properties in this object
      //passing a plain object as first parameter, will set multiple properties and values
      //if this object already contains a function with the name, calls it passing the value (useful for observables)
      if (typeof name == 'object') {
        _.each(name, function (v, k) {
          this.set(k, v);
        }, this);
        return this;
      }
      //if value is a function; just set it
      if (_.isFunction(value)) {
        this[name] = value;
        return this;
      }
      _.isFunction(this[name]) ? this[name](value) : this[name] = ko.o(value);
      return this;
    },

    //shortcut for defer with binding to model context
    defer: function (fn, a) {
      return this.delay(fn, 0, a);
    },

    delay: function (fn, ms, a) {
      _.delay(_.bind(function () {
        _.isFunction(fn) ? fn.call(this, a) : this[fn](a);
      }, this), ms);
      return this;
    },

    interval: function (name, fn, ms) {
      this.clearInterval(name);
      var id = this[name] = window.setInterval(_.bind(fn, this), ms);
      this.disposables.push({
        dispose: _.partial(function (name, intervalId) {
          window.clearInterval(intervalId);
        }, name, id)
      });
      return this;
    },

    clearInterval: function (name) {
      if (this[name]) window.clearInterval(this[name]), this[name] = null;
      return this;
    },

    //shortcut for Knockout subscribe with binding to model context
    sub: function (name, fn) {
      //support calling passing an object
      if (_.isObject(name)) {
        var x;
        for (x in name) {
          this.sub(x, name[x]);
        }
        return this;
      }
      if (_.isString(fn)) fn = this[fn];//support call with a function name
      this.disposables.push(this[name].subscribe(fn.bind(this)));
      return this;
    },

    //function to dispose of the subscriptions
    dispose: function () {
      //dispose subscriptions (and computed if we start using them)
      var disposables = this.disposables;
      for (var i = 0, l = disposables.length; i < l; i++)
        disposables[i].dispose();
      //call on dispose method
      if (this.onDispose) this.onDispose();
      return this;
    },

    //
    serialize: function () {
      var o = {};
      _.each(_.keys(this.defaults), function (n) {
        o[n] = this[n]();
      }, this);
      return o;
    },

    // shortcut to lodash pick function, unwrapping observables.
    pick: function (arr) {
      if (_.isString(arr))
        arr = _.toArray(arguments);
      var o = {};
      _.each(arr, function (n) {
        o[n] = ko.unwrap(this[n]);
      }, this);
      return o;
    }

  });

  Model.extend = Extend;

  return Model;
});
