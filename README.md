# runit
## Controller

Controller will allow execution of Python scripts from a remote location by checking
 for an authorization from a database. This allows execution on the server from Django
 PHP or any other means of updating a SQL database.

************
* Database Setup 
************
The only database set up required is as follows:
  1. Create Table called "programs"
  2. Create Three Columns:
    -program(varchar(25))
    -runorkill(boolean)
    -changed(boolean)
    
************
* Django Setup 
************
 Updating this section soon.
