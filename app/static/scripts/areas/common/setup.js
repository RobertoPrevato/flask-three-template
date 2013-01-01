//common libraries setup
R("setup", [], function () {
  
  //lodash template settings
  _.extend(_.templateSettings, {
    escape: /\{\{(.+?)\}\}/g,
    evaluate: /\{%(.+?)%\}/g,
    interpolate: /\{#(.+?)#\}/g
  });

  R.debug = true;

  //support query string after the hash in routes (ignores it!)
  Simrou.prototype.RegExpCache.searchHash = /(\?.+)$/;
  Simrou.prototype.getHash = function (url) {
    if (url == null) {
      url = location.hash;
    }
    //update the hash in a global observable
    url = url.replace(this.RegExpCache.searchHash, "");
    return String(url).replace(this.RegExpCache.extractHash, '$1');
  };
});