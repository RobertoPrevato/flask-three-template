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
      "/scripts/libs/knockout/binders/ko-id.js",
      "/scripts/libs/knockout/binders/ko-data.js",
      "/scripts/libs/knockout/binders/ko-modal.js",
      "/scripts/libs/knockout/binders/ko-menu.js",
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
      "/scripts/areas/admin/locale/en.js",
      "/scripts/shared/components/extend.js",
      "/scripts/shared/components/events.js",
      "/scripts/shared/components/string.js",
      "/scripts/shared/components/regex.js",
      "/scripts/shared/components/date.js",
      "/scripts/shared/components/reflection.js",
      "/scripts/shared/components/array-search.js",
      "/scripts/shared/data/object-analyzer.js",
      "/scripts/shared/data/sanitizer.js",
      "/scripts/shared/data/query.js",
      "/scripts/shared/data/file.js",
      "/scripts/shared/data/csv.js",
      "/scripts/shared/data/xml.js",
      "/scripts/shared/data/i18n.js",
      "/scripts/shared/menus/menu-builder.js",
      "/scripts/shared/menus/menu-functions.js",
      "/scripts/shared/menus/menu.js",
      "/scripts/shared/filters/filters-manager.js",
      "/scripts/libs/plugins/kingtable/kingtable-core.js",
      "/scripts/libs/plugins/kingtable/jquery.kingtable.js",
      "/scripts/libs/plugins/kingtable/lodash/jquery.kingtable-lodash.js",
      "/scripts/libs/plugins/kingtable/lodash/templates.js",
      "/scripts/libs/knockout/binders/ko-kingtable.js",
      "/scripts/areas/admin/templates.js",
      "/scripts/areas/admin/dashboard/services.js",
      "/scripts/areas/admin/dashboard/models/dashboard.js",
      "/scripts/areas/admin/dashboard/routes.js",
      "/scripts/areas/admin/application/services.js",
      "/scripts/areas/admin/application/models/users-panel.js",
      "/scripts/areas/admin/application/models/messages-panel.js",
      "/scripts/areas/admin/application/models/exceptions-panel.js",
      "/scripts/areas/admin/application/routes.js",
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