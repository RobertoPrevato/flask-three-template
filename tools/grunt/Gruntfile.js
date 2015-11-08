var path = require("path");

module.exports = function (grunt) {

  var rel = "../../app/static";

  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    less: {
      shared: {
        options: {
          cleancss: true
        },
        files: {
          "../../app/static/styles/styles.css": "../../app/static/styles/styles.less",
          "../../app/static/styles/areas/admin/styles.css": "../../app/static/styles/areas/admin/styles.less"
        }
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
