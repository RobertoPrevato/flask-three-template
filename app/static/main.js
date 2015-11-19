//
// main, application starter
//
System.register([], function (_export) {
  'use strict';
  _export('configure', configure);

  function configure(aurelia) {
    aurelia.use.standardConfiguration().developmentLogging();

    aurelia.start().then(function (a) {
      return a.setRoot();
    });
  }

  return {
    setters: [function (_bootstrap) {}],
    execute: function execute() {}
  };
});