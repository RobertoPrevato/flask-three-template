var gulp = require("gulp");
var paths = require("../paths");

gulp.task("start", function() {
  return gulp.src([paths.output]);
});
