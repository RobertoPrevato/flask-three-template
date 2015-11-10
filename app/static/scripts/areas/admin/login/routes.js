//
//  Router configuration for admin login
//
R("adminlogin.routes", ["app", "routes", "admin-login-panel"], function (app, Routes, Panel) {

  _.extend(Routes, {
    "/": {
      get: function (e, params) {
        app.go(Panel, params);
      }
    }
  });

});
