# Flask-three-template
Project template for Python Flask three-tier web applications, using [Aurelia web framework](http://aurelia.io/).
<img src="http://ugrose.com/ug.png" width="300" height="300" alt="UgRoslein" title="UgRoslein - ugrose.com" align="right" />

## Features
* Integration with [Aurelia](http://aurelia.io/) web framework.
* Project skeleton ready to use, to start a three tier web application using Flask for its presentation layer.
* Localization strategy, using Flask-Babel.
* Authentication and authorization strategies, including anonymous authentication.
* Login mechanism protected against brute forcing (stores login attempts in DB).
* DB based sessions strategy.
* MongoDB collections for accounts, sessions, login attempts.
* Example files for production deployment using Nginx and uWSGI servers.
* Skeleton for data access layers for MongoDB.
* Skeleton for unit testing.
* Custom error pages.
* Application db logger, to store and retrieve messages and exceptions logs in database

<img src="http://ugrose.com/content/demos/flask/Flask-Aurelia.png" title="Flask-Aurelia" />

## Branches
* [empty-project](https://github.com/RobertoPrevato/flask-three-template/tree/empty-project): empty template without any authentication strategy.
* [master](https://github.com/RobertoPrevato/flask-three-template/tree/master): template with custom authentication and authorization strategy.
* [spa-humbular](https://github.com/RobertoPrevato/flask-three-template/tree/spa-humbular): template with Humbular Single Page Application strategy.
* [spa-aurelia](https://github.com/RobertoPrevato/flask-three-template/tree/spa-aurelia): Single Page Application template using Aurelia framework.

## How to prepare the environment
Refer to the [dedicated wiki page](https://github.com/RobertoPrevato/flask-three-template/wiki/Preparing-the-environment), for instructions about how to prepare the server side environment.

In order to use the Flask-Aurelia template, it`s necessary to install the software required by Aurelia (e.g. NodeJs, gulp; jspm).
Refer to the [dedicated wiki page](https://github.com/RobertoPrevato/flask-three-template/wiki/Using-Aurelia)
and to the official [Aurelia getting started guide](http://aurelia.io/docs.html#/aurelia/framework/latest/doc/article/getting-started) for more information.
> Note: since the jspm packages need to be accessible to the client, the npm install command must be executed directly from the app/static folder, where the package.json file resides

## Servers setup
* Basic settings file for Nginx.
* Settings file for uWSGI.
* Development server ready to use: Flask itself.

