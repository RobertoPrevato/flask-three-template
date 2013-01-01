//
//  Router configuration for users admin
//
R("users.admin.routes", [
  "app",
  "routes",
  "users-panel",
  "messages-panel",
  "exceptions-panel"], function (app, Routes, UsersPanel, MessagesPanel, ExceptionsPanel) {

  _.extend(Routes, {
    "/users": {
      get: function (e, params) {
        app.go(UsersPanel, params);
      }
    },
    "/exceptions": {
      get: function (e, params) {
        app.go(ExceptionsPanel, params);
      }
    },
    "/messages": {
      get: function (e, params) {
        app.go(MessagesPanel, params);
      }
    }
  });

});