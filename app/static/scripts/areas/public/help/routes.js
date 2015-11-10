//
//  Router configuration for help
//
R("help.routes", ["app", "routes", "models.gettingstarted"], function (app, Routes, GettingStarted) {

  _.extend(Routes, {
    '/getting-started': {
      get: function (e, params) {
        app.go(GettingStarted, params);
      }
    }
  });

});
