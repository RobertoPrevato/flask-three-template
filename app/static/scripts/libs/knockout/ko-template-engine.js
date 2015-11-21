//Roberto Prevato
//custom template engine for knockout js, to support cached templates
(function (ko, _) {

  //NB: in newer versions of lodash, the template function returns a compiler function;
  //in older versions it returns directly a string
  var templateMode = typeof _.template("") == "string" ? 0 : 1;
  function getTemplate(data, context, key) {
    switch (templateMode) {
      case 0:
        //legacy mode: _.template returns a string
        return _.template(data, context);
      case 1:
        //newer mode: _.template returns a compiler function
        //was the template already cached? (i.e. is it already a function, instead of html?)
        if (typeof data == "function")
          return data(context);
        //store in cache and return compiled template
        var compiler = ko.templates[key] = _.template(data);
        return compiler(context);
    }
  }

  //utility for localization strategy
  var I;
  //if I.js is defined; use it.
  //https://github.com/RobertoPrevato/I.js
  if (window["I"]) I = window.I;
  //if i18n is defined; use it.
  //https://github.com/fnando/i18n-js
  else if (window["I18n"]) I = window.I18n;
  else throw "Missing implementation of i18n. Please refer to https://github.com/RobertoPrevato/jQuery-KingTable/wiki/Implementing-localization";

  //override base templateEngine makeTemplateSource to extend it, to load cached templates
  ko.templateEngine.prototype.makeTemplateSource = function (template, templateDocument) {
    // Named template
    if (typeof template == "string") {
      templateDocument = templateDocument || document;
      var elem = templateDocument.getElementById(template);
      //if the element is not a script, we don't care about it
      if (elem && !/script/i.test(elem.tagName)) elem = null;
      if (!elem) {
        //check if the template is defined inside templates object
        if (!ko.templates || !ko.templates[template]) throw new Error("Cannot find template with ID " + template);
        //take template from cache object
        var s = document.createElement('script');
        s.setAttribute('type', 'text/html');
        s.setAttribute('id', template);
        //compile for translations
        console.log(I);
        var t = getTemplate(ko.templates[template], {}, template);
        s.text = t;
        //set reference to s
        elem = s;
      } else {
        //check if the template id is used in two different places
        if (ko.templates && ko.templates[template]) throw new Error("Two templates with the same ID " + template + " exist in the document and in the templates definition.");
      }
      return new ko.templateSources.domElement(elem);
    } else if ((template.nodeType == 1) || (template.nodeType == 8)) {
      // Anonymous template
      return new ko.templateSources.anonymousTemplate(template);
    } else
      throw new Error("Unknown template type: " + template);
  };
})(ko, _);