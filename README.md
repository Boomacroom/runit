# runit
## Controller

Controller will allow execution of Python scripts from a remote location behind a VPN by checking
 for an authorization from the database. This allows execution on the server from Django
 PHP or any other means of updating a SQL database.

************
* Database Setup 
************
The only database set up required is as follows:
  1. Create Table called "programs"
  2. Create Three Columns:
  
| program | runorkill | changed |
| --- | --- | --- |
| test.py | True | True |

program is set up as a varchar(25)

runorkill is set up as a boolean

changed is set up as a boolean

************
* Django Setup 
************
 Updating this section soon.
