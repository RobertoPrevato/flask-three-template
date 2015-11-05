## `/dal.mongo` Data access layer to MongoDB

This folder contains data access code for a main application database using MongoDB.
If your application needs more than one MongoDB database, add the settings to the configuration file as appropriate. 

The code should be abstracted from the Flask application, in such a way that it could be reused in 
different applications (e.g. a  desktop application written using PyQt).

The DAL should be referenced only by the BLL.