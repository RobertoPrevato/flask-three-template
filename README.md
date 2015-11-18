# Flask-three-template
Project template for Python Flask three-tier web applications.

## Features
* Project skeleton ready to use, to start developing a three tier web application using Flask for its presentation layer.
* Localization strategy, using Flask-Babel.
* Example files for production deployment using Nginx and uWSGI servers.
* Skeleton for data access layers for MongoDB.
* Skeleton for unit testing.
* Custom error pages.

## Branches
* [empty-project](https://github.com/RobertoPrevato/flask-three-template/tree/empty-project): empty template without any authentication strategy.
* [master](https://github.com/RobertoPrevato/flask-three-template/tree/master): template with custom authentication and authorization strategy.
* [spa-humbular](https://github.com/RobertoPrevato/flask-three-template/tree/spa-humbular): template with Humbular Single Page Application strategy.
* [spa-aurelia](https://github.com/RobertoPrevato/flask-three-template/tree/spa-aurelia): Single Page Application template using Aurelia framework.

## How to prepare the environment
* [Flask](http://flask.pocoo.org/).
* [Flask-Babel](https://pythonhosted.org/Flask-Babel/).

Refer to the [dedicated wiki page](https://github.com/RobertoPrevato/flask-three-template/wiki/Preparing-the-environment), for instructions about how to prepare the environment and install the dependencies.

## Servers setup
* Basic settings file for Nginx.
* Settings file for uWSGI.
* Development server ready to use: Flask itself.

## Grunt integration
* JavaScript bundling and minification strategy.
* LESS compilation.
