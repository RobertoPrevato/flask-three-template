//
//  Router configuration for admin dashboard
//
R("admin.routes", ["app", "routes", "admin-dashboard"], function (app, Routes, Panel) {

  _.extend(Routes, {
    "/": {
      get: function (e, params) {
        app.go(Panel, params);
      }
    }
  });

});
