R("browser", [], function () {
  return {
    getNavigatorInfo: function () {
      return _.pick(navigator, "platform", "userAgent", "appVersion", "language", "product", "appName", "vendor");
    }
  };
});