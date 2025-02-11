<center> <h1>HBNB - MySQL</h1> </center>

This repository contains the second stage of a student project to build a clone of the AirBnB website. The original can be found [here](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS). This stage implements a backend interface using a sql database to manage program data through a console. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using either communication with a sql database or a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8/Unit Testing | [/tests](https://github.com/JakeFC/AirBnB_clone_v2/tree/master/tests) | All code is pep8 compliant and modules are unittested|
| 2: Console create | [console.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/console.py) | Add a kwargs-like method for creating objects |
| 3. MySQL setup dev | [setup_mysql_dev.sql](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Create a database and user for db storage |
| 4. MySQL setup test | [setup_mysql_test.sql](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Create a database and user for db storage testing (no info is saved after console exit) |
| 5. Delete object | [/models/engine/file_storage.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update file_storage with a method to delete objects and updated all() to accept class argument |
| 6. DBStorage States and Cities | [/models/engine/db_storage.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) [/models/_ _init_ _.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/__init__.py) [/models/base_model.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/base_model.py) [/models/city.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/city.py) [/models/state.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/state.py) | Implement sql database storage functionality to the console, using city and state |
| 7. DB User | [/models/user.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/user.py) | Update user class for db storage |
| 8. DB Place | [/models/place.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/place.py) | Update place class for db storage |
| 9. DB Review | [/models/review.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/review.py) | Update review class for db storage |
| 10. DBStorage Amenity | [/models/amenity.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/place.py](https://github.com/JakeFC/AirBnB_clone_v2/blob/master/models/place.py) | Update amenity class for db storage and implement a many to many relationship between place and amenity |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

2. Run setup for mysql if using sql database storage (otherwise skip to 3)
```
/AirBnB_clone_v2$ ./setup_mysql_dev.sql
```
3. Once the repository is cloned locate the "console.py" file and run it as follows:
(using file storage method)
```
/AirBnB_clone_v2$ ./console.py
```
(using database storage method)
```
/AirBnB_clone_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create <classname> - Creates an instance based on given class

    * create <classname> <args> - Creates an instance of given class with each arg used as a key-pair (attr=value) to set the given attribute names to the given values

    * destroy <classname> <id> - Destroys an object based on class and UUID

    * show <classname> <id> - Shows an object based on class and UUID

    * all [<classname>] - Shows all objects the program has access to, or all objects of a given class

    * update <classname> <id> <attribute name> <value> - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
Updated 6/11/2021
<br>