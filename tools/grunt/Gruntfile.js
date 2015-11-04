var path = require("path");

module.exports = function (grunt) {

  var rel = "../../app/static";
  var lessFiles = {};
  lessFiles[rel + "/styles/shared.css"] = rel + "/styles/shared.less";

  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    less: {
      shared: {
        options: {
          paths: [rel + "/styles/shared/styles"],
          cleancss: true
        },
        files: lessFiles
      }
    },

    concat: {},

    uglify: {}
  });
  //grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-less");
  //grunt.loadNpmTasks("grunt-contrib-uglify");

  grunt.registerTask("default", ["less"]);
};
