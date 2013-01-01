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
    }
  };
});
