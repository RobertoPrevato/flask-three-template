//
//  Services for the admin area login
//
R("adminlogin-services", [], function () {
  return {
    login: function (params) {
      return $.ajax({
        url: "/admin/auth",
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
          email: params.email,
          password: params.password,
          remember: params.remember,
          navigator: params.navigator
        }),
        context: params.context
      }).promise();
    }
  };
});
