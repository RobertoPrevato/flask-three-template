"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
from bll.reports.reportsmanager import ReportsManager

def register_dblogger(app):
    """
     Initialize an application global db logger, to store and retrieve application
     messages and exceptions in database.
    """
    DAL_PROJECT = app.config["DAL_PROJECT"]

    log_store = None
    if DAL_PROJECT == "dalmongo":
        from dalmongo.reports.reportsstore import ReportsStore
        log_store = ReportsStore()
    else:
        raise Exception("ReportsStore for `{}` implemented".format(DAL_PROJECT))

    # instantiate the membership provider
    log_manager = ReportsManager({ "store": log_store })

    # attach to the application a dblogger;
    # but without overriding the Flask logger property.
    setattr(app, "reports", log_manager)
