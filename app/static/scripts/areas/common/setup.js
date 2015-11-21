//common libraries setup
(function () {
  //lodash template settings
  _.extend(_.templateSettings, {
    escape: /\{\{(.+?)\}\}/g,
    evaluate: /\{%(.+?)%\}/g,
    interpolate: /\{#(.+?)#\}/g
  });
  R.debug = true;

  var aft = document.getElementById("meta-aft").content;
  var loc = document.getElementById("meta-loc").content;

  $.ajaxPrefilter(function (options, originalOptions, xhr) {
    //set antiforgery token and application based request culture for each AJAX request.
    _.each({
      "X-AFT": aft,
      "X-Request-Culture": loc
    }, function (v, k) {
      xhr.setRequestHeader(k, v);
    });
  });

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

  //modify Simrou to force a default hash
  Simrou.prototype.resolveHash = function (event) {
    var hash, url;
    if (this.observeHash) {
      if (this.eventSupported) {
        url = event.originalEvent.newURL;
      }
      hash = this.getHash(url);
      var re = this.resolve(hash, "get");
      if (!re) {
        //redirect to /
        location.hash = "#/";
        return false;
      }
      return true;
    }
  };

})();
