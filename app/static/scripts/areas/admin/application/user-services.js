//
//  Services for the users admin
//
R("user-services", [], function () {
  return {
    save: function (params) {
      return $.ajax({
        url: "/admin/saveuser",
        type: "POST",
        data: JSON.stringify(params.data),
        dataType: "json",
        contentType: "application/json",
        context: params.context
      }).promise();
    },
    getDetails: function (params) {
      return $.ajax({
        url: "/admin/getuserdetails",
        type: "POST",
        data: {
          id: params.id
        },
        dataType: "json",
        context: params.context
      }).promise();
    },
    getFormData: function (params) {
      return $.ajax({
        url: "/admin/getuserformdata",
        type: "POST",
        dataType: "json",
        context: params.context
      }).promise();
    }
  };
});
