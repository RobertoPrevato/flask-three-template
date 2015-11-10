//
//  Services for the admin area login
//
R("adminlogin-services", [], function () {
  return {
    login: function (params) {
      return $.ajax({
        url: "/admin/login",
        method: "POST",
        data: {
          username: params.username,
          password: params.password
        },
        context: params.context
      }).promise();
    }
  };
});
