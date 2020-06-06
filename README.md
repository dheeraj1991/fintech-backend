Fintech Backend
===================

- - - - 
# Project Details #
The project is intended to make use of two apis to insert data to SQLite database. This is developed in Django 3.0 based project, which needs python3.6>= to run.

## APIs ##
### Create User ###
API end point  : {base_url}/api/v1/create_customer/  
Request Method : POST  
Content-Type : application/json  
Example Request Body :  
```javascript
{
    "first_name": "John",
    "last_name": "Vang",
    "dob": "10-10-2005"
}
```

### Create Policy ###
API end point  : {base_url}/api/v1/create_policy/  
Request Method : POST  
Content-Type : application/json  
Example Request Body :  
```javascript
{
    "type": "accident-claim",
    "premium": 1000,
    "cover": 1000000
}
```


Steps to setup the project : 
1. Clone the repo to your local
2. Create a virtual env with python version set as python3.6 or above
3. Activate the environment and from the root of the folder run `pip install -r requirements.txt` this will install all the required python dependecies
4. Since migration files are not included in the code base, we need to run the following commands to create the respective tables in the data base.
    1. `python manage.py makemigrations`
    2. `python manage.py migrate`
5. After the migrations are done you will see a new sqlite database created with the name db.sqlite3
6. Now you can start the server by running `python manage.py runserver`

The server by default runs on prot 8000, hence your base URL would be http://localhost:8000.