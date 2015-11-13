//
//  Services for the application admin
//
R("app-services", [], function () {
  return {
    getMessages: function (params) {
      return $.ajax({
        url: "/admin/getmessages"
      });
    },
    getExceptions: function (params) {
      return $.ajax({
        url: "/admin/getexceptions"
      });
    },
    getUsers: function (params) {
      return $.ajax({
        url: "/admin/getusers"
      });
    }
  };
});
