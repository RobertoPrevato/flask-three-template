//
//email validation rules
//
(function () {

  var getError = $.Forms.Validation.GetError;

  _.extend($.Forms.Validation.Rules, {

    email: {
      fn: function (field, value, forced) {
        if (!value) return true;
        var name = field.attr("name"), twinField;
        if (_.contains(["email-one", "email-two"], name)) {
          twinField = name == "email-one" ? "input[name=\"email-two\"]" : "input[name=\"email-one\"]";
          twinField = field.closest("div").find(twinField);
        }
        //validate trimmed value
        value = $.trim(value);
        var limit = 40;
        var rx = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (twinField && !forced) {
          //if validation is not forced, trigger validation on the twinField
          if (twinField.val()) twinField.trigger("blur.validation", [true]);
        }
        if (!value.match(rx) || value.length > limit) {
          return getError(I.t("errors.email"), arguments);
        }
        if (twinField) {
          //compare values
          var twinFieldValue = $.trim(twinField.val());
          if (twinFieldValue && twinFieldValue != value) {
            return getError(I.t("errors.emailsDontMatch"), arguments);
          }
        }
        return true;
      }
    }
  });
})();
