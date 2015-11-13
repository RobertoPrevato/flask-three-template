//
// Knockout menu and menustrip binders.
//
R("ko-menu", ["menu-builder"], function (MenuBuilder) {

  var setter = function(element, valueAccessor, allBindingsAccessor, model) {
    var options = ko.unwrap(valueAccessor());
    var schema = options ? options.schema || model.menu : model.menu;
    if (!schema) throw "missing `schema`";
    var html = MenuBuilder(schema);
    var el = $(element);
    el.html(html);
  };

  ko.bindingHandlers.menu = {
    init: setter,
    update: setter
  };

  var menustrip = function(element, valueAccessor, allBindingsAccessor, model) {
    var options = ko.unwrap(valueAccessor());
    var menus = options ? options.schema || model.menus : model.menus;
    if (!menus) throw "missing `menus`";
    var a = [];
    a.push("<div class=\"ug-menu-strip\">");
    for (var i = 0, j = menus.length; i < j; i++) {
      var menu = menus[i];
      if (!menu) continue;
      a.push("<div class=\"ug-menu-wrapper\" data-bind=\"with: menus[" + i + "]\">");
      a.push("<span tabindex=\"0\" class=\"ug-expander\" data-bind=\"text: name\"></span>");
      a.push(MenuBuilder(menu));
      a.push("</div>");
    }
    a.push("</div>");
    var el = $(element);
    el.html(a.join(""));
  };

  ko.bindingHandlers.menustrip = {
    init: menustrip,
    update: menustrip
  };
});

