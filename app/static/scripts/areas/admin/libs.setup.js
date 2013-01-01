//
// admin area specific libraries settings
//
(function () {
  //disable the query string usage in KingTable:
  $.KingTable.prototype.defaults.useQueryString = false;

  //boolean default template
  // modifies the default schemas
  _.extend($.KingTable.Schemas.DefaultByType, {
    boolean: function (columnSchema) {
      return {
        sortable: true,
        template: '{% if(' + columnSchema.name + ') {%}' + I.t("voc.Yes") + '{% } else { %}' + I.t("voc.No") + '{% } %}'
      };
    }
  });
})();

