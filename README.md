Table of contents
=================

* [CARTOON Backend](#cartoon-backend)
* [Table of contents](#table-of-contents)
* [Requirements](#requirements)
* [Installation](#installation)

# CARTOON Backend
A simple REST API that handles a list of camera that has the ability to return the data based on geographical coordinates, used by https://github.com/AdrianoDiDio/CARTOON application.

Requirements
============
This guide assumes that a Linux distribution is used, commands for Windows are similar but requires some steps to get the required files.
In order to setup this package we need to install python3,pip,mysql using a simple bash command (Note that sudo may be required in order to install it):
```bash
$ apt-install python3,pip,mysql-server
```
After installing the required packages the installation can proceed.

Installation
============
After cloning the repository, we need to create a new virtual enviroment.
Virtual Enviroment let us create a separate enviroment from the system to install local dependencies required by this package.
In order to create a new enviroment, open up the shell in the folder where the project was unzipped and run:
```bash
$ python3 -m venv env
```
This will create an hidden folder called .env that will contains all the required files to run the project.
Next, we need to activate it by running:
```bash
$ source .env/bin/activate
```
Now, we need to download all the required files by running:
```bash
$ pip install -r requirements.txt
```
After pip is done installing, we need to setup our database using django utilities.
Before running the commands, modify the section DATABASES inside the file PyAuthBackend/settings.py by inserting the
MySQL Username,Password,DBName and Host.
If any of the parameters is wrong or missing DJango will display an error asking to fix it.
**Make sure to create the database before applying any migration**
Next, we need to prepare our query needed to create the Database structure by running the command:
```bash
$ python manage.py makemigrations
```
and then:
```bash
$ python manage.py migrate
```
If all the commands completed without error, we can now start the local development server by running:
```bash
$ python manage.py runserver <OptionalIPAddress:Port>
```
If IP address is not specified, server will be available at localhost:8000, API can be reached at localhost:8000/api.
By opening localhost:8000 in a browser user should see the API documentation made using swagger.

Finally, after checking that everything is working, we can create a SuperUser that will manage the User's registration
by running the command:

```bash
$ python manage.py createsuperuser
```
This user can now login at localhost:8000/admin (or a custom IP address) to manage all the registered users.
An SQL script is provided within the repository containing a list of test camera that can be used to test the API.
E.G:
```bash
$ mysql -D DBName -u Username -p < CameraTable.sql
```
