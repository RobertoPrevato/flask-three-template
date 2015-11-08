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

## Dependencies
* Python.
* [Flask](http://flask.pocoo.org/).
* [Flask-Babel](https://pythonhosted.org/Flask-Babel/).
```bash
$ sudo pip install Flask
$ sudo pip install Flask-Babel
```

## Servers setup
* Basic settings file for Nginx.
* Settings file for uWSGI.
* Development server ready to use: Flask itself.

## Grunt integration
* JavaScript bundling and minification strategy.
* LESS compilation.