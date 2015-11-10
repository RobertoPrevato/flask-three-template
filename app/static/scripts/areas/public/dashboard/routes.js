//
//  Router configuration for dashboard
//
R("dashboard.routes", ["app", "routes", "models.dashboard"], function (app, Routes, Dashboard) {

  _.extend(Routes, {
    '/': {
      get: function (e, params) {
        app.go(Dashboard, params);
      }
    }
  });

});
