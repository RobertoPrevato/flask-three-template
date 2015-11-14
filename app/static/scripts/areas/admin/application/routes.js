//
//  Router configuration for users admin
//
R("users.admin.routes", [
  "app",
  "routes",
  "users-panel",
  "messages-panel",
  "exceptions-panel",
  "sessions-panel"], function (app, Routes, UsersPanel, MessagesPanel, ExceptionsPanel, SessionsPanel) {

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
    },
    "/sessions": {
      get: function (e, params) {
        app.go(SessionsPanel, params);
      }
    }
  });

});
