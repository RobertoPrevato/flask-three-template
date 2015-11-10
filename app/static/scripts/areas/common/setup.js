//common libraries setup
R("setup", [], function () {
  
  //lodash template settings
  _.extend(_.templateSettings, {
    escape: /\{\{(.+?)\}\}/g,
    evaluate: /\{%(.+?)%\}/g,
    interpolate: /\{#(.+?)#\}/g
  });

  R.debug = true;
});