//
//email validation rules
//
(function () {

  var getError = $.Forms.Validation.GetError;

  _.extend($.Forms.Validation.Rules, {

    newPassword: {
      fn: function (field, value, forced, options) {
        var defaults = {
          //default regular expressions for new passwords,
          //checks for text string to have at least one Numeric and one Character and the length of text string to be
          //at least 6 characters long
          enforceRx: /^(?=.*\d)(?=.*[a-zA-Z\.\,\;\@\$\!\?\#\*\-\_\%\&]).{9,}$/,
          allowedCharsRx: /^[0-9a-zA-Z\.\,\;\@\$\!\?\#\*\-\_\%\&]+$/,
          twinField: field.attr("name") == "password-one" ? "input[name=\"password-two\"]" : "input[name=\"password-one\"]",
          messages: {
            weak: I.t("errors.passwordTooWeak"),
            notAllowedChars: I.t("errors.illegalCharsInPassword")
          }
        };
        var o = $.extend(true, {}, defaults, options || {}), twinField;
        if (o.twinField) {
          twinField = field.closest("div").find(o.twinField);
          if (!forced && twinField.val()) {
            //if validation is not forced, trigger validation on the twinField
            twinField.trigger("blur.validation", [true]);
          }
        }
        //if (!value.match(o.allowedCharsRx)) {
        //  return getError(o.messages.notAllowedChars, arguments);
        //}
        if (o.enforceRx && !value.match(o.enforceRx)) {
          return getError(o.messages.weak, arguments);
        }
        if (twinField) {
          //compare values
          var twinFieldValue = twinField.val();
          if (twinFieldValue && twinFieldValue != value) {
            return getError(I.t("errors.passwordsDontMatch"), arguments);
          }
        }
        return true;
      }
    }

  });
})();
