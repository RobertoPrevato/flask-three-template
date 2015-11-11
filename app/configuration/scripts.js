/**
 * Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
 * https://github.com/RobertoPrevato/Flask-three-template
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
 *
 * Configuration file for JavaScript resources.
 * This file is read both by Grunt, to generate built and minified javascript,
 * and by the Python application, to generate <script> tags.
 */
module.exports = {

  "bundling": false,
  "minification": false,

  "sets": {

    "libs": [
      "/scripts/libs/lodash.js",
      "/scripts/libs/jquery.js",
      "/scripts/libs/simrou.js",
      "/scripts/libs/bootstrap.js",
      "/scripts/libs/r.js",
      "/scripts/libs/i.js",
      "/scripts/libs/knockout.js",
      "/scripts/libs/knockout/ko-shortcuts.js",
      "/scripts/libs/knockout/ko-template-engine.js",
      "/scripts/libs/knockout/binders/ko-href.js",
      "/scripts/libs/knockout/binders/ko-src.js",
      "/scripts/libs/knockout/binders/ko-data.js",
      "/scripts/libs/knockout/binders/ko-modal.js",
      "/scripts/libs/plugins/jquery-dataentry.js",
      "/scripts/libs/plugins/jquery-dataentry-knockout.js",
      "/scripts/shared/components/extend.js",
      "/scripts/shared/components/events.js",
      "/scripts/shared/browser/browser.js",
      "/scripts/areas/common/templates.js",
      "/scripts/areas/common/core/models/model.js",
      "/scripts/areas/common/setup.js",
      "/scripts/areas/common/app.js",
      "/scripts/areas/common/routes.js"
    ],

    "admin": [
      "/scripts/libs/plugins/jquery.kingtable.min.js",
      "/scripts/areas/admin/templates.js",
      "/scripts/areas/admin/locale/en.js",
      "/scripts/areas/admin/dashboard/services.js",
      "/scripts/areas/admin/dashboard/models/dashboard.js",
      "/scripts/areas/admin/dashboard/routes.js",
      "/scripts/areas/admin/start.js"
    ],

    "admin-login": [
      "/scripts/areas/common/validation/email.js",
      "/scripts/areas/admin/templates.js",
      "/scripts/areas/admin/locale/en.js",
      "/scripts/areas/admin/login/services.js",
      "/scripts/areas/admin/login/models/panel.js",
      "/scripts/areas/admin/login/routes.js",
      "/scripts/areas/admin/start.js"
    ],

    "public": [
      "/scripts/areas/public/templates.js",
      "/scripts/areas/public/locale/en.js",
      "/scripts/areas/public/dashboard/models/panel.js",
      "/scripts/areas/public/dashboard/services.js",
      "/scripts/areas/public/dashboard/routes.js",
      "/scripts/areas/public/help/models/panel.js",
      "/scripts/areas/public/help/routes.js",
      "/scripts/areas/public/start.js"
    ]
  }
};