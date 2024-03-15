## ¡WELCOME TO THE AIRBNB CLONE PROJECT!

<img src="https://i.pinimg.com/originals/87/10/23/871023fca810e57347eab0ae811ccfdf.png" title="AirBnB clone project" />


## DESCRIPTION
It is a simple command interpreter to manage the objects used in the AirBnB clone project by:
 - Allowing for the creation of new objects.
 - Allows retrieval of an object from a file, a database, etc.
 - Allows operations to be performed on objects
 - Allows object attributes to be updated.
 - Allows objects to be destroyed.


## The project contains:
 - A parent class (called BaseModel) used for initialization, serialization, and deserialization of instances.
 - Creates a simple flow of serialization/deserialization, as follows: Instance <-> Dictionary <-> JSON string <-> file
 - Creation of all subclasses ```User``` , ```State```, ```City```, ```Amenity```, ```Place```, ```Review```
 - Creation of a the first abstracted storage engine of the project: File storage.
 - Unittests to validate all classes as well as the storage engine.


## Command Interpreter 💻:
The command interpreter allows you to interact with the application to create, update, delete, and display instances of the different models in the database.

## How to Start
To start the command interpreter, follow these steps:
 - Clone the repository from ```git@github.com:marialegl/holbertonschool-AirBnB_clone.git```
 - Open a terminal and navigate to the directory where you cloned the repository.</li>
 - Run the following command:
```bash
./console.py
```

## How to Use
Once you've started the command interpreter, you can use the following commands:

 - ```create <model_name>```: Create a new instance of the specified model.
 - ```show <model_name> <id>```: Show the details of a specific instance of the model.
 - ```update <model_name> <id> <attribute> <value>```: Update a specific attribute of an instance of the model.
 - ```destroy <model_name> <id>```: Delete a specific instance of the model.
 - ```all <model_name>```: Show all instances of the specified model.
 - ```quit```: Exit the command interpreter.

## Examples

To create a new user:
```bash
(hbnb) create User
```

To list all users:
```bash
(hbnb) all User
```

To exit the command interpreter:
```bash
(hbnb) quit
```

### Have fun exploring the functionalities of the AirBnB Clone command interpreter!

# Developed by

<p>Maria Alejandra Gonzalez</p>
<a href="https://www.linkedin.com/in/maria-alejandra-gonzalez-londo%C3%B1o-a5084a208/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">
  <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50">
</a>

<a href="https://github.com/marialegl">
 <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo.png" width="100">
</a>

------------

<p>David Vasquez</p>
<a href="https://www.linkedin.com/in/foultrip//">
  <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50">
</a>

<a href="https://github.com/FoulTrip">
 <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo.png" width="100">
</a>
