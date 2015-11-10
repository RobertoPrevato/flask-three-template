//
//  Model for bootstrap dropdown/up menus
//
R("dropmenu", ["model"], function (Model) {
  return Model.extend({
    defaults: {
      text: "",
      css: "",
      context: null,
      items: [],
      selected: null,
      autoname: true
    },

    initialize: function () {
      var self = this;
      if (!self.context())
        self.context(self);
      self.setProperties().setListeners();
    },

    attrsFilter: function (data) {
      if (data.items) {
        data.items = _.map(data.items, function (o) {
          return _.isString(o) ? {
            text: o
          } : o;
        });
      }
    },

    setProperties: function () {
      if (!this.selected()) {
        var items = this.items();
        this.text(items && items.length ? items[0].text : "");
      }
      return this;
    },

    setListeners: function () {
      return this.setItemListener();
    },

    setitem: function (item) {
      this.selected(item);
    },

    setItemListener: function () {
      if (this.autoname()) {
        this.sub({
          selected: function (newVal) {
            this.text(newVal.text);
            this.trigger("item-changed", newVal);
          }
        });
      }
    }
  });
});
