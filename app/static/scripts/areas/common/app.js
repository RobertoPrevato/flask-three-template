//
//  Main object for a whole area. This file is abstracted from specific implementations: it is meant to be used
// in any kind of area (e.g. public, admin, etc.).
//
R("app", [], function () {

  return {

    routes: {},
    dialog: ko.o(""),
    template: ko.o(""),
    panel: ko.o(""),

    /**
     * Sets the current panel as an instance of the given type; or updates the current one with the given parameters.
     * @param model type of panel that must be displayed
     * @param params route parameters
     * @returns {*}
     */
    go: function (model, params) {
      var cp = this.panel();
      if (cp && cp instanceof model && cp.handleParams) {
        cp.handleParams(params);
        return this;
      }
      return this.setPanel(new model(params));
    },

    /**
     * Sets the given panel as model for the main view, using the panel template.
     * @param instance of panel to set in the main view
     */
    setPanel: function (instance) {
      this.template("").disposePanel();
      return this.template(instance.template).panel(instance);
    },

    /**
     * Disposes and removes the current panel;
     * @returns {*}
     */
    disposePanel: function () {
      var currentPanel = this.panel();
      if (currentPanel) {
        if (currentPanel.dispose)
          currentPanel.dispose();
        this.panel(void(0));
      }
      return this;
    },

    /**
     * Displays a message dialog.
     * @param title of the message dialog
     * @param message of the message dialog
     * @returns {*}
     */
    message: function (title, message) {
      return this.dialog({
        title: title,
        content: message,
        type: "generic-dialog"
      });
    },

    /**
     * Displays an error dialog.
     * @param title of the error dialog
     * @param message of the error dialog
     * @returns {*}
     */
    error: function (title, message) {
      return this.dialog({
        title: title || I.t("errors.TechnicalError"),
        content: message || I.t("errors.PerformingOperation"),
        type: "generic-dialog"
      });
    },

    /**
     * Starts the application.
     */
    start: function () {
      return this
        .startRouter()
        .initializeLocale()
        .bind();
    },

    /**
     * Initializes the current locale in the object used for client side localization.
     */
    initializeLocale: function () {
      //TODO: integrate here your localization logic;
      I.setLocale("en");
      return this;
    },

    /**
     * Starts the client side routing.
     */
    startRouter: function () {
      var router = new Simrou(this.routes);
      this.router = router;
      // Start the engine!
      router.start("/");
      return this;
    },

    /**
     * Binds the application to the view.
     */
    bind: function () {
      var el = document.getElementById("content");
      el.setAttribute("data-bind", "template: 'view'");
      ko.bind(this, el);
      return this;
    }
  };

});
