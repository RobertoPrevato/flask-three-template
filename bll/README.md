## `/bll` Business logic layer

All business logic related to the application should be contained in this folder.
The code should be abstracted from the Flask application, in such a way that it could be reused in 
different applications (i.e. a  desktop application written using PyQt).

The business logic layer should be referenced only by the application using it;
and it should reference one or more data access layers; depending on the data that it needs to manipulate.
