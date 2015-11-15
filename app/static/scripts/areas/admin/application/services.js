//
//  Services for the application admin
//
R("app-services", [], function () {
  return {
    getList: function (params) {
      return $.ajax({
        url: params.url,
        context: params.context
      }).promise();
    },
    getUserDetails: function (params) {
      return $.ajax({
        url: "/admin/getuserdetails",
        type: "POST",
        data: {
          id: params.id
        },
        dataType: "json",
        context: params.context
      }).promise();
    }
  };
});
