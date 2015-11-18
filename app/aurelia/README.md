# app/aurelia

The source code, in EcmaScript6, is contained inside this folder /src/.
The Flask server will serve only files under /static/ folder; this is where the Gulp watcher deploys the transpiled JavaScript code.

During development, a gulp watch task is running from this folder; monitoring changes to source files;
and automatically generating JavaScript code for the /static/scripts folder.